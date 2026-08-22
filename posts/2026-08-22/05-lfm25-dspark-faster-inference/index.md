---
date: 2026-08-22
topic: "LFM2.5-DSpark от Liquid AI: до 3.2x ускорения инференса"
source: https://huggingface.co/blog/LiquidAI/lfm25-dspark
image: https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/ZMoThfdqzAz8cbxweVQfO.gif
lang: [ru, en]
generated: true
---

![LFM2.5-DSpark inference demo](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/ZMoThfdqzAz8cbxweVQfO.gif)

## Русская версия

# LFM2.5-DSpark от Liquid AI: до 3.2x ускорения инференса

Liquid AI опубликовала на Hugging Face пост под заголовком [«Up to 3.2x Faster Inference with LFM2.5-DSpark»](https://huggingface.co/blog/LiquidAI/lfm25-dspark) — «до 3.2 раз быстрее инференс с LFM2.5-DSpark». Liquid AI — компания-спин-офф из MIT, известная своей линейкой Liquid Foundation Models (LFM), которую она с самого начала позиционирует не как конкурента гигантским моделям по бенчмаркам, а как модели, заточенные под работу на edge-устройствах и в условиях ограниченных вычислительных ресурсов — там, где важнее не абсолютное качество, а скорость и объём памяти.

Именно в этом контексте и стоит читать заявленный прирост в 3.2 раза: речь не о том, что модель стала «умнее», а о том, что тот же (или сопоставимый) уровень качества теперь можно получить заметно быстрее — а значит, дешевле в расчёте на запрос, и практичнее для устройств, где каждая миллисекунда и каждый ватт на счету. Для инференс-инженеров это ровно тот тип новости, который двигает реальные архитектурные решения: не «новый рекорд на лидерборде», а конкретное число «X раз быстрее», которое можно напрямую заложить в расчёт стоимости обслуживания трафика.

Такие анонсы стоит воспринимать не изолированно, а как часть общей гонки за эффективность инференса, которая идёт параллельно с гонкой за качество моделей: квантизация, спекулятивное декодирование, оптимизированные ядра для конкретного железа — у каждого вендора свой набор трюков, и «DSpark» здесь, судя по всему, обозначение конкретной техники или конфигурации именно от Liquid AI.

### Почему вам это важно

Если вы считаете unit-экономику инференса — стоимость запроса, задержку под нагрузкой, требования к памяти на edge-устройстве, — [пост Liquid AI про LFM2.5-DSpark](https://huggingface.co/blog/LiquidAI/lfm25-dspark) стоит добавить в список кандидатов для замера на собственной задаче, прежде чем принимать заявленное ускорение на веру: цифры вендора почти всегда получены на конкретном железе и конкретной нагрузке, и разница на вашем стеке может оказаться другой.

## English version

# LFM2.5-DSpark from Liquid AI: up to 3.2x faster inference

Liquid AI published a Hugging Face post titled ["Up to 3.2x Faster Inference with LFM2.5-DSpark"](https://huggingface.co/blog/LiquidAI/lfm25-dspark). Liquid AI is an MIT spin-off known for its Liquid Foundation Models (LFM) line, which the company has positioned from the start not as a leaderboard competitor to the largest models, but as models built to run on edge devices and under tight compute budgets — where speed and memory footprint matter more than raw benchmark scores.

That's the right context for reading the claimed 3.2x figure: this isn't about the model getting "smarter," it's about reaching the same (or comparable) quality level noticeably faster — which translates directly into lower cost per request and more practical deployment on devices where every millisecond and every watt counts. For inference engineers, this is exactly the kind of announcement that drives real architecture decisions: not "a new leaderboard record," but a concrete "X times faster" number you can plug straight into a cost-per-request calculation.

Announcements like this are best read as part of the broader efficiency race running alongside the quality race: quantization, speculative decoding, hardware-specific kernels — every vendor has its own bag of tricks, and "DSpark" here appears to be Liquid AI's name for a specific technique or configuration.

### Why it matters

If you're doing inference unit economics — cost per request, latency under load, memory budget on an edge device — [Liquid AI's LFM2.5-DSpark post](https://huggingface.co/blog/LiquidAI/lfm25-dspark) belongs on your shortlist to benchmark against your own workload before taking the claimed speedup at face value: vendor numbers are almost always measured on specific hardware under a specific load, and the gap on your own stack can look different.
