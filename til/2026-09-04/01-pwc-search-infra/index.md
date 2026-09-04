---
date: 2026-09-04
topic: "Поиск на Papers with Code — это не одна фича, а три инфраструктурных примитива HF"
source: https://huggingface.co/blog/pwc-search
lang: [ru, en]
generated: true
---

## RU

В блоге Hugging Face вышел пост Нильса Рогге [«How Hugging Face Inference Endpoints, Jobs, and Buckets Power Search on Papers with Code»](https://huggingface.co/blog/pwc-search) — о том, как поиск на Papers with Code собран из трёх отдельных примитивов платформы: Inference Endpoints (обслуживание модели, которая считает эмбеддинги запроса и документов), Jobs (пакетовая обработка — прогнать эмбеддинги по всему корпусу статей заранее, а не на лету) и Buckets (хранилище для результатов). Что здесь важно понять: «фича поиска» на витрине выглядит единым продуктом, но под капотом это три разные инженерные задачи с разными требованиями — обслуживание модели с низкой задержкой, массовая batch-обработка без ограничения по времени ответа и просто хранение. Собирать поисковую фичу как один монолит, а не как связку специализированных примитивов, обычно оказывается лишней инженерной работой именно там, где платформа уже даёт готовый кусок под конкретную часть задачи.

## EN

Hugging Face's blog has a post by Niels Rogge, [«How Hugging Face Inference Endpoints, Jobs, and Buckets Power Search on Papers with Code»](https://huggingface.co/blog/pwc-search), on how Papers with Code's search is built from three separate platform primitives: Inference Endpoints (serving the model that computes query and document embeddings), Jobs (batch processing — embedding the whole corpus of papers ahead of time rather than on the fly), and Buckets (storage for the results). What matters here: a "search feature" looks like one product on the surface, but under the hood it's three distinct engineering problems with different requirements — low-latency model serving, unbounded-time batch processing, and plain storage. Building a search feature as one monolith instead of a set of specialized primitives is usually extra engineering work exactly where the platform already ships a ready piece for that specific part of the job.
