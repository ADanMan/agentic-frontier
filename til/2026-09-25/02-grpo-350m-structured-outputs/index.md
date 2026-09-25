---
date: 2026-09-25
topic: "350M-модель + 100 шагов GRPO = заявка на лучшие структурированные выводы — заголовок без тела статьи"
source: https://huggingface.co/blog/grpo-with-trl-ifstruct
lang: [ru, en]
generated: true
---

## RU

Дайджест принёс только заголовок и авторов — [«Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps»](https://huggingface.co/blog/grpo-with-trl-ifstruct), Leonie Monigatti, ben burtenshaw, Sergio Paniego — без текста самого поста. Что здесь важно понять из заголовка: GRPO (Group Relative Policy Optimization) — метод RL-дообучения, где для одного и того же промпта модель генерирует группу ответов, и награда каждого считается относительно остальных в группе, а не по отдельной value-модели — это дешевле по вычислениям, чем классический PPO с отдельным критиком. «Структурированные выводы» обычно означает JSON, следование заданной схеме или формату, который парсер должен суметь прочитать без ошибок. Заявка «100 шагов» звучит как аргумент в пользу дешевизны и скорости подхода на маленькой (350M параметров) модели — но конкретных метрик до/после в дайджесте нет, это домысел по заголовку, а не пересказ найденного в статье.

## EN

The digest surfaced only a title and authors — [«Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps»](https://huggingface.co/blog/grpo-with-trl-ifstruct), Leonie Monigatti, ben burtenshaw, Sergio Paniego — with no post body. What's worth knowing from the title alone: GRPO (Group Relative Policy Optimization) is an RL fine-tuning method where, for the same prompt, the model generates a group of responses and each one's reward is computed relative to the rest of the group rather than through a separate value model — cheaper computationally than classic PPO with a dedicated critic. "Structured outputs" typically means JSON or conformance to a given schema/format a parser needs to read without errors. The "100 steps" framing reads as an argument for how cheap and fast the approach is on a small (350M-parameter) model — but there are no concrete before/after metrics in the digest; that's an inference from the title, not a recap of anything found in the post.
