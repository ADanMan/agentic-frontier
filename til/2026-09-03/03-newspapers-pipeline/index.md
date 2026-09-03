---
date: 2026-09-03
topic: "Миллиарды токенов из газетных архивов — и почему это не просто OCR"
source: https://huggingface.co/papers/2608.18972
lang: [ru, en]
generated: true
---

## RU

Работа [Institutional Newspapers Pipeline](https://huggingface.co/papers/2608.18972) авторства Matteo Cargnelutti, Catherine Brobston, Eben English, Jake Sadow, Kacie Bailey и соавторов ставит проблему прямо: «исторические газеты — обширная летопись общественной жизни, но их плотная, нерегулярная и порой зашумлённая вёрстка делает вычислительный доступ к этим материалам сложным и ограниченным». Что здесь важно понять: газетная полоса — это не линейный текст, а несколько колонок, заголовков и врезок вперемешку на одной странице, поэтому простой OCR без понимания макета склеивает соседние колонки в бессмысленную кашу. Пайплайн, судя по названию, решает именно задачу «извлечь из такого материала миллиарды качественных токенов», а не просто распознать буквы — то есть сначала разобрать структуру страницы, и только потом читать текст в правильном порядке.

## EN

[Institutional Newspapers Pipeline](https://huggingface.co/papers/2608.18972), by Matteo Cargnelutti, Catherine Brobston, Eben English, Jake Sadow, Kacie Bailey and co-authors, states the problem directly: "historical newspapers are an abundant record of public life, but their dense, irregular and sometimes noisy layouts make computational access to these materials both challenging and limited." What matters here: a newspaper page isn't linear text — it's several columns, headlines, and sidebars packed together on one page, so plain OCR without layout awareness merges adjacent columns into nonsense. Judging by its name, the pipeline is built to solve "extract billions of quality tokens from this kind of material," not just recognize letters — meaning it has to parse the page's structure first, and only then read the text in the correct order.
