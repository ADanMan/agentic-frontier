---
date: 2026-09-29
topic: "Prefill и decode: почему один и тот же запрос к LLM на самом деле проходит две разные фазы обслуживания"
source: https://huggingface.co/papers/2609.26333
lang: [ru, en]
generated: true
---

```mermaid
flowchart LR
    U["Пользовательский запрос"] --> P["Prefill<br/>обработка всего промпта сразу<br/>compute-bound"]
    P -->|"KV-кэш"| D["Decode<br/>генерация токенов по одному<br/>memory-bound"]
    D --> O["Ответ пользователю"]
```

## Русская версия

# Prefill и decode: две разные фазы одного запроса к LLM

В сегодняшнем посте про [Disaggregated Quantization](https://huggingface.co/papers/2609.26333) мелькают два термина — prefill и decode, — которые стоит разобрать отдельно, потому что понимание этой разницы объясняет добрую половину решений, которые инженеры принимают при обслуживании LLM в продакшене.

Когда вы отправляете запрос модели, происходит не один процесс, а два, устроенных совершенно по-разному. Сначала — **prefill**: модель принимает весь ваш промпт целиком (системный промпт, историю диалога, вопрос) и за один проход вычисляет представления (KV-кэш) для каждого токена входа. Это чисто параллельная задача — все токены известны заранее, их можно обработать одновременно, большой матричным умножением. Узкое место здесь — вычислительная мощность (FLOPS): чем больше у вас GPU и чем быстрее они считают, тем быстрее закончится prefill. Отсюда термин compute-bound.

Дальше начинается **decode**: модель генерирует ответ токен за токеном, и каждый новый токен зависит от всех предыдущих (включая только что сгенерированные). Это принципиально последовательный процесс — нельзя посчитать токен номер 10, не зная токен номер 9. На каждом шаге модели нужно прочитать из памяти веса и весь накопленный KV-кэш, чтобы посчитать всего один новый токен. Из-за этого GPU большую часть времени не считает, а ждёт, пока данные приедут из памяти. Узкое место — не FLOPS, а пропускная способность памяти (memory bandwidth). Отсюда термин memory-bound.

Разница между «упираемся в вычисления» и «упираемся в память» — это не абстрактная деталь для инженеров чипов, а причина, по которой современные системы обслуживания LLM (vLLM, SGLang и подобные) физически разносят prefill и decode на разные GPU или даже разные кластеры: под каждую фазу выгодно подбирать своё железо и свои оптимизации, а держать их вместе — значит постоянно идти на компромисс. Именно в эту логику встраивается идея из сегодняшнего поста: если фазы уже разделены по железу, почему бы не разделить и схему квантования — низкую точность туда, где упор в вычисления (prefill), и компактные веса туда, где упор в память (decode).

### Почему вам это важно

Если вы когда-нибудь задавались вопросом, почему время до первого токена (time-to-first-token) и скорость генерации последующих токенов (tokens per second) — это две разные метрики, которые надо оптимизировать по отдельности, теперь у этого есть объяснение: это буквально две разные фазы с разным узким местом. Оптимизация одной не обязательно улучшает другую.

## English version

# Prefill and Decode: The Two Different Phases Inside One LLM Request

Today's post on [Disaggregated Quantization](https://huggingface.co/papers/2609.26333) uses two terms — prefill and decode — that are worth unpacking on their own, because understanding the split explains a good chunk of the engineering decisions behind serving LLMs in production.

When you send a request to a model, it's not one process but two, and they behave very differently. First comes **prefill**: the model ingests your entire prompt at once (system prompt, conversation history, the question) and computes representations (the KV cache) for every input token in a single pass. This is an embarrassingly parallel task — every token is known upfront, so they can all be processed together as one large matrix multiplication. The bottleneck here is raw compute (FLOPS): the more GPUs you have and the faster they crunch numbers, the faster prefill finishes. Hence "compute-bound."

Then comes **decode**: the model generates the response one token at a time, and each new token depends on every previous one (including ones just generated). This is inherently sequential — you can't compute token 10 without knowing token 9. At every step, the model has to read the weights and the entire accumulated KV cache from memory just to produce a single new token. As a result, the GPU spends most of its time waiting for data to arrive from memory rather than computing. The bottleneck isn't FLOPS — it's memory bandwidth. Hence "memory-bound."

The difference between "compute-bound" and "memory-bound" isn't an abstract detail for chip engineers — it's the reason modern LLM serving stacks (vLLM, SGLang, and similar) physically split prefill and decode across separate GPUs or even separate clusters: each phase benefits from different hardware choices and optimizations, and keeping them together means constantly compromising between the two. That's exactly the logic behind today's post: if the phases are already split by hardware, why not split the quantization scheme too — low precision where you're compute-bound (prefill), compact weights where you're memory-bound (decode).

### Why it matters

If you've ever wondered why time-to-first-token and tokens-per-second are two separate metrics that get optimized independently, now you know why: they're literally two different phases with two different bottlenecks. Optimizing one doesn't automatically improve the other.
