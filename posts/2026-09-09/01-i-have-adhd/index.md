---
date: 2026-09-09
topic: "i-have-adhd: скилл, который запрещает агенту хоронить ответ в стене текста"
source: https://github.com/ayghri/i-have-adhd
lang: [ru, en]
generated: true
---

```mermaid
flowchart LR
    Q["Вопрос пользователя"] --> A["Агент думает"]
    A --> L["Длинный разбор,<br/>отступления, преамбулы"]
    A --> S["i-have-adhd:<br/>ответ сначала"]
    L -.ответ погребён<br/>в конце.-> U1["Пользователь листает"]
    S --> U2["Пользователь видит<br/>суть сразу"]
```

![diagram](fig-1.svg)

## Русская версия

# i-have-adhd: скилл, который запрещает агенту хоронить ответ в стене текста

Сегодня в топе GitHub trending — репозиторий с названием, которое сложно не заметить: [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd), 30,337 → 31,156 звёзд (+819 за окно, 656 «today»), Python, #1 в рейтинге. Описание короткое и предельно конкретное: «A skill to stop your coding agent from burying the answer. ADHD-friendly output».

Идея бьёт точно в знакомую всем, кто работает с агентами вроде Claude Code или Codex, боль: модель получает вопрос, честно разворачивает цепочку рассуждений, перечисляет варианты, объясняет контекст — и только в последнем абзаце, тремя строчками, даёт собственно ответ. Если вы спрашивали что-то простое («какой командой откатить коммит»), а получили пять абзацев про философию git, это она, «похороненная под текстом» суть. Название скилла — не шутка про диагноз ради шутки, а точное описание паттерна: вниманию нужен ответ сразу, а не в конце пути через рассуждения агента.

Технически это, судя по всему, именно skill в смысле Claude Code/Codex-скиллов — небольшой набор инструкций, который меняет поведение агента на уровне формата вывода, а не архитектуру модели. То есть ничего не «чинится» в модели — просто явно предписывается: сначала главное, потом обоснование, если оно вообще нужно. Это тот же класс инструментов, что и десятки других «skills»-репозиториев в трендах последних недель: не новая способность модели, а тонкая настройка того, что именно долетает до пользователя.

Здесь стоит быть скептичным ровно в одном месте: 819 новых звёзд за день — это признание того, что боль реальна и узнаваема, а не доказательство, что решение работает надёжно на любом промпте. «ADHD-friendly output» — формулировка из README, а не результат теста на живых пользователях с разными стилями мышления. Сам факт, что такой скилл нужен и разбирают его нарасхват, говорит больше о культуре агентных инструментов в целом (слишком много «рассуждений вслух» без фильтра), чем о том, что именно этот репозиторий — окончательное решение.

### Почему вам это важно

Если вы замечаете, что ваш агент отвечает на простые вопросы длинными портянками, а суть находится где-то в третьем абзаце — это управляемая проблема на уровне промпта или системной инструкции, а не неизбежность. [i-have-adhd](https://github.com/ayghri/i-have-adhd) — конкретный, проверяемый на своих задачах пример такого фикса; посмотрите, воспроизводится ли эффект на ваших собственных запросах, прежде чем тащить его в прод.

## English version

# i-have-adhd: a skill that bans your agent from burying the answer

Today's #1 on GitHub trending has a name hard to miss: [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd), 30,337 → 31,156 stars (+819 over the window, 656 "today"), Python. The description is short and to the point: "A skill to stop your coding agent from burying the answer. ADHD-friendly output."

The idea lands squarely on a pain anyone who works with agents like Claude Code or Codex will recognize: the model gets a question, dutifully unrolls a chain of reasoning, lists options, explains context — and only in the last paragraph, in three lines, gives the actual answer. Ask something simple ("what command reverts a commit?") and get five paragraphs on git philosophy back, and that's exactly it — the answer buried under text. The skill's name isn't a joke for its own sake; it's an accurate description of the pattern: attention needs the answer up front, not at the end of a walk through the agent's reasoning.

Technically this looks like a "skill" in the Claude Code/Codex sense — a small set of instructions that changes the agent's output format rather than the model's architecture. Nothing gets "fixed" inside the model itself; it's simply told, explicitly: lead with the answer, justify after, if justification is even needed. That puts it in the same class as dozens of other "skills" repos that have trended in recent weeks — not a new model capability, but a fine-tuning of what actually reaches the user.

Worth exactly one note of skepticism: 819 new stars in a day is a sign the pain is real and widely recognized, not proof the fix holds up reliably across every prompt. "ADHD-friendly output" is a phrase from the README, not a result from testing across different thinking styles. The fact that a skill like this is even needed — and is being snapped up this fast — says more about agentic-tooling culture in general (too much unfiltered "thinking out loud") than about this specific repo being the definitive answer.

### Why it matters

If you notice your agent answering simple questions with long walls of text, where the actual point is buried in paragraph three, that's a fixable prompt- or system-instruction-level problem, not an inevitability. [i-have-adhd](https://github.com/ayghri/i-have-adhd) is a concrete, testable example of such a fix — check whether the effect reproduces on your own queries before shipping it to production.
