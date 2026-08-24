---
date: 2026-08-24
topic: "«Building Effective Agents»: почему Anthropic предлагает НЕ строить агента"
source: https://www.anthropic.com/engineering/building-effective-agents
image: https://cdn.sanity.io/images/4zrzovbb/website/76b5733c669f0dfb9c7aa7fc512a495867cf12e6-2400x1260.png
lang: [ru, en]
generated: true
---

![Building effective agents](https://cdn.sanity.io/images/4zrzovbb/website/76b5733c669f0dfb9c7aa7fc512a495867cf12e6-2400x1260.png)

## Русская версия

# «Building Effective Agents»: почему Anthropic предлагает НЕ строить агента

Инженерный блог Anthropic регулярно всплывает в лентах как один из самых часто цитируемых источников по агентной архитектуре, и пост [«Building Effective Agents»](https://www.anthropic.com/engineering/building-effective-agents) — ровно тот случай. Его центральная мысль звучит почти провокационно на фоне всеобщей агентной эйфории: в большинстве случаев вам не нужен агент. Вам нужен «workflow» — заранее спроектированная последовательность вызовов LLM с чётко прописанной логикой ветвления, где модель отвечает за отдельные шаги, но не управляет процессом целиком.

Anthropic вводит различие, которое стоит запомнить и повторять на каждом дизайн-ревью: workflow — это система, где пути выполнения кода заданы заранее программистом; агент — это система, где LLM сама, динамически, решает, какие шаги предпринять и какими инструментами воспользоваться, опираясь на обратную связь от среды. Это не про «хуже/лучше» — это про предсказуемость против гибкости. Workflow проще тестировать, дешевле в вызовах модели и почти не подвержены случаям, когда модель «зацикливается» или уходит не в ту сторону. Агент дороже и менее предсказуем, зато справляется с задачами, которые заранее нельзя разложить на фиксированный граф шагов.

В посте описан набор конкретных паттернов workflow — цепочка промптов (prompt chaining), маршрутизация (routing), параллелизация, оркестратор с подчинёнными воркерами, и цикл evaluator-optimizer, где одна LLM генерирует, а другая критикует и просит доработать. Каждый паттерн — ответ на конкретную инженерную задачу: разбить сложную задачу на шаги, направить запрос в нужную ветку обработки, распараллелить независимые подзадачи, или добавить цикл самопроверки там, где качество первого прохода недостаточно.

Скептический момент, который стоит держать в голове: этот пост — не нейтральный академический разбор, а материал от вендора, который продаёт API для построения именно таких систем. Рекомендация «начинайте с простого, добавляйте агентность только когда она реально нужна» звучит разумно и, что важно, полезна независимо от того, чьи модели вы используете — но не стоит забывать, что она же снижает планку жалоб на то, что «агент от Anthropic» не всегда справляется: если у вас всё сломалось, возможно, вам вообще не нужен был агент.

### Почему вам это важно

Если вы проектируете систему на LLM и первый инстинкт — «сделаем агента», [этот пост](https://www.anthropic.com/engineering/building-effective-agents) — хороший чек-лист для паузы. Начните с вопроса, можно ли описать процесс заранее фиксированным графом шагов. Если да — возьмите workflow, он предсказуемее и дешевле в эксплуатации. Агентность стоит вводить только там, где заранее неизвестно, сколько шагов потребуется и какие инструменты понадобятся — а не потому, что это модное слово в питче для инвесторов.

## English version

# "Building Effective Agents": why Anthropic tells you NOT to build an agent

Anthropic's engineering blog keeps surfacing as one of the most frequently cited sources on agent architecture, and [«Building Effective Agents»](https://www.anthropic.com/engineering/building-effective-agents) is exactly that kind of post. Its central claim sounds almost provocative against the backdrop of general agent euphoria: in most cases, you don't need an agent. You need a "workflow" — a pre-designed sequence of LLM calls with explicit branching logic, where the model handles individual steps but doesn't drive the process as a whole.

Anthropic draws a distinction worth memorizing and repeating at every design review: a workflow is a system where the code paths are set in advance by the engineer; an agent is a system where the LLM itself dynamically decides which steps to take and which tools to use, based on feedback from the environment. This isn't about "better vs. worse" — it's about predictability vs. flexibility. Workflows are easier to test, cheaper in model calls, and rarely fall into the trap of the model looping or wandering off course. An agent is more expensive and less predictable, but it handles tasks that can't be laid out in advance as a fixed graph of steps.

The post describes a specific set of workflow patterns — prompt chaining, routing, parallelization, an orchestrator with worker sub-agents, and an evaluator-optimizer loop where one LLM generates and another critiques and asks for revisions. Each pattern answers a specific engineering problem: breaking a complex task into steps, routing a request to the right processing branch, parallelizing independent subtasks, or adding a self-check loop where the quality of a first pass isn't good enough.

One skeptical point worth keeping in mind: this post isn't a neutral academic survey — it's vendor content from a company selling the API for building exactly these kinds of systems. The advice "start simple, add agency only when you actually need it" is sound and, importantly, useful regardless of whose models you use — but it also conveniently lowers the bar for complaints that "an Anthropic-powered agent" doesn't always work: if things broke, maybe you didn't need an agent in the first place.

### Why it matters

If you're designing an LLM-based system and your first instinct is "let's build an agent," [this post](https://www.anthropic.com/engineering/building-effective-agents) is a good checklist to pause on. Start by asking whether the process can be described upfront as a fixed graph of steps. If yes, use a workflow — it's more predictable and cheaper to run. Reach for agency only where the number of steps and tools needed genuinely can't be known in advance — not because "agent" is the trendy word in your pitch deck.
