---
date: 2026-09-01
topic: "OpenAI разрывает контракт с Cursor после сделки со SpaceX"
source: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex
lang: [ru, en]
generated: true
---

![OpenAI decision on Cursor](https://images.ctfassets.net/kftzwdyauwt9/6RFKP8tysuxOLxVaiCRlu/ac31b03c2aeb6e3da620f2db89c7b6e9/index-our-decision-on-cursor-following-its-acquisition-by-spacex.png?w=1600&h=900&fit=fill)

## Русская версия

# OpenAI разрывает контракт с Cursor после сделки со SpaceX

OpenAI [опубликовала короткое заявление](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex): компания сворачивает контракт, по которому предоставляла свои модели редактору кода Cursor, — и делает это сразу после того, как Cursor был куплен SpaceX. Формулировка в посте предельно сухая, конкретных цифр или деталей контракта там нет — только сам факт решения и его привязка к смене владельца.

Дальше начинается зона, где стоит быть честным: сама OpenAI не объясняет мотивы подробно, а значит любые рассуждения о причинах — это уже наша интерпретация, а не цитата. Но контекст напрашивается сам: SpaceX принадлежит Илону Маску, а Маск — совладелец xAI, прямого конкурента OpenAI на рынке моделей. Продолжать поставлять свою модель продукту, который теперь фактически находится под крышей конкурирующей экосистемы, — стратегически странно даже без всякой публичной вражды. Это не история про технические ограничения, а история про то, где проходят границы «кто с кем дружит» в индустрии, где модели — это инфраструктура, а не просто API-вызов.

Для рынка AI-редакторов кода это тоже сигнал. Cursor построен поверх сторонних моделей — это была и остаётся его архитектурная особенность: продукт-обёртка, а не собственная модель. Такая позиция даёт гибкость (можно переключаться между провайдерами), но она же делает продукт уязвимым именно к таким разрывам: если один из ключевых поставщиков модели уходит по причинам, не связанным с качеством продукта, а связанным с корпоративной политикой, — это риск, который принимающие решение о смене владельца, видимо, либо недооценили, либо сознательно приняли.

Стоит быть осторожным с драматизацией: один пост на официальном блоге — это не подтверждение того, что Cursor остаётся без моделей вообще, а лишь то, что один конкретный контракт с одним конкретным поставщиком закрывается. У Cursor наверняка есть и другие модели-провайдеры в стеке.

### Почему вам это важно

Если вы строите продукт поверх чужих LLM-API, этот кейс — практическое напоминание: зависимость от одного поставщика — это не только вопрос цены или лимитов, но и корпоративной политики, которая может измениться в один день без предупреждения. [Решение OpenAI](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex) стоит читать не как разовую новость, а как аргумент в пользу мультивендорной архитектуры для любого AI-продукта, который не хочет зависеть от чужих M&A-решений.

## English version

# OpenAI cuts its Cursor contract after the SpaceX acquisition

OpenAI [posted a short statement](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex) announcing it is winding down the contract that supplied its models to the code editor Cursor — right after Cursor was acquired by SpaceX. The wording is deliberately terse: no numbers, no contract details, just the fact of the decision and its explicit link to the change of ownership.

From here it's worth being upfront: OpenAI doesn't spell out its reasoning in detail, so anything beyond that is our own reading, not a quote. But the context is hard to ignore: SpaceX is Elon Musk's company, and Musk co-owns xAI, a direct competitor to OpenAI in the model market. Continuing to supply your model to a product that now effectively sits inside a rival ecosystem is strategically awkward even without any public feud. This isn't a story about technical limitations — it's a story about where the "who works with whom" lines get drawn in an industry where models are infrastructure, not just an API call away.

It's also a signal for the AI code-editor market more broadly. Cursor is built on top of third-party models — that's been its architectural identity from the start: a wrapper product, not an in-house model. That stance buys flexibility (you can swap providers) but it also makes the product exposed to exactly this kind of cutoff — when a key model supplier walks away for reasons unrelated to product quality and entirely about corporate politics, that's a risk whoever approved the ownership change either underweighted or knowingly accepted.

Worth resisting the urge to overdramatize: one blog post doesn't confirm Cursor is left without any models at all — only that one specific contract with one specific vendor is closing. Cursor almost certainly has other model providers in its stack already.

### Why it matters

If you're building a product on top of someone else's LLM API, this case is a concrete reminder: single-vendor dependency isn't just a pricing or rate-limit question — it's a corporate-politics question that can change overnight without warning. [OpenAI's decision](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex) is worth reading not as a one-off news item but as an argument for multi-vendor architecture in any AI product that doesn't want to depend on someone else's M&A calls.
