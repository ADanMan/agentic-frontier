---
date: 2026-09-22
topic: "Skill Synthesis from Code: вчера был известен только первый лимит существующих методов, сегодня всплыл и второй"
source: https://huggingface.co/papers/2609.05571
lang: [ru, en]
generated: true
---

## RU

Вчера в блоге разбиралась статья [«Grounded Skill Synthesis from Code at Scale for Agentic Intelligence»](https://huggingface.co/papers/2609.05571), и доступный тогда фрагмент абстракта обрывался ровно на фразе «existing methods face two limitations», не называя ни одного из них. Сегодня в том же RSS-источнике попался чуть более длинный фрагмент, и оба лимита теперь видны: первый — trajectory-based synthesis требует взаимодействия с конкретным окружением (то есть нужно реально прогонять агента в среде, чтобы получить траектории). Второй — skills, полученные из документации («document-derived»), судя по всему «may lac[k]» что-то — и вот здесь фрагмент обрывается уже во второй раз, буквально на середине слова «lack». Что именно им не хватает, не сказано.

Что здесь важно понять: даже одно это уточнение сужает картину — конкурирующий метод не просто «хуже», он терпит неудачу по двум разным причинам (нужна живая среда vs. нужна полнота документации), и статья, судя по названию, обещает третий путь — учиться прямо из кода.

## EN

Yesterday's post covered [«Grounded Skill Synthesis from Code at Scale for Agentic Intelligence»](https://huggingface.co/papers/2609.05571), and the abstract excerpt available then cut off right at "existing methods face two limitations," without naming either one. Today the same RSS source yielded a slightly longer excerpt, and both limitations are now visible: the first is that trajectory-based synthesis requires interactions with specific environments — you actually have to run the agent in that environment to get trajectories. The second is that document-derived skills apparently "may lac[k]" something — and the excerpt cuts off a second time, mid-word, right at "lack." What exactly they lack isn't stated.

What's worth understanding: even this much narrows the picture — the competing approach doesn't just underperform, it fails for two distinct reasons (needs a live environment vs. needs documentation completeness), and per the title, the paper promises a third path: learning directly from code.
