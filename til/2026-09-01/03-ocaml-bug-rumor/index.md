---
date: 2026-09-01
topic: "Слуха о баге хватает, чтобы найти эксплойт"
source: https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/
lang: [ru, en]
generated: true
---

## RU

Саймон Уиллисон [пересказывает пост](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) Анила Мадхавапедди — профессора Кембриджа и одного из core-мейнтейнеров компилятора OCaml. Тот сообщает, что в OCaml-проектах уязвимости стали находить по одному лишь слуху о баге — без деталей, без PoC, просто по факту упоминания. Что здесь важно понять: LLM-инструменты для поиска уязвимостей достаточно хороши, чтобы взять расплывчатую наводку («где-то тут может быть баг») и довести её до рабочего эксплойта самостоятельно, перебирая код систематичнее человека. Это смещает баланс между тем, кто первым патчит уязвимость, и тем, кто первым её эксплуатирует, — раскрытие информации даже без технических подробностей больше не безопасно по умолчанию.

## EN

Simon Willison [relays a post](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) by Anil Madhavapeddy, a Cambridge professor and core maintainer of the OCaml compiler. He reports that security issues in OCaml projects are now being found off nothing more than a rumour of a bug — no details, no PoC, just the fact that one was mentioned. What matters here: LLM-based vulnerability-hunting tools are now good enough to take a vague hint ("there might be a bug around here") and turn it into a working exploit on their own, combing through code more systematically than a human would. That shifts the balance between who patches a vulnerability first and who exploits it first — disclosure without technical detail is no longer safe by default.
