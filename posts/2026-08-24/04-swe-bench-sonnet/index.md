---
date: 2026-08-24
topic: "SWE-bench Verified и Claude 3.5 Sonnet: что на самом деле измеряет «лучший в кодинге»"
source: https://www.anthropic.com/engineering/swe-bench-sonnet
image: https://cdn.sanity.io/images/4zrzovbb/website/e4468f749aa715a8cdc4c270686927e1e8c3ea29-2400x1260.png
lang: [ru, en]
generated: true
---

![SWE-bench Verified](https://cdn.sanity.io/images/4zrzovbb/website/e4468f749aa715a8cdc4c270686927e1e8c3ea29-2400x1260.png)

## Русская версия

# SWE-bench Verified и Claude 3.5 Sonnet: что на самом деле измеряет «лучший в кодинге»

Третий инженерный пост Anthropic, всплывший в сегодняшней подборке — [«Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet»](https://www.anthropic.com/engineering/swe-bench-sonnet) — стоит того, чтобы разобрать не только результат, но и сам бенчмарк. SWE-bench Verified — это подмножество реальных issue из открытых GitHub-репозиториев, отфильтрованное и проверенное вручную так, чтобы задачи были однозначно решаемы и корректно проверяемы автоматическими тестами. Модель получает описание бага или фичи из настоящего issue и должна сгенерировать патч, который проходит скрытые тесты репозитория — это заметно ближе к реальной работе разработчика, чем LeetCode-подобные задачи.

Пост описывает не только сам результат модели, но и «scaffolding» — обвязку вокруг модели, которая даёт ей доступ к файловой системе репозитория, возможность запускать команды и итеративно проверять свой патч перед финальной сдачей. Это важный методологический момент: результат на SWE-bench — это не «чистая» способность модели решать задачи одним проходом, а способность модели в паре с конкретной агентной обвязкой, написанной конкретной командой. Смените обвязку — и число на лидерборде изменится, даже если веса модели останутся теми же.

Именно поэтому к любым заявлениям в духе «модель X — новый номер один по кодингу» стоит подходить с долей здорового скепсиса. SWE-bench, при всех своих сильных сторонах, — это набор задач из открытого Python-кода на GitHub, со своей спецификой: определённый стиль кодовой базы, определённый тип issue, определённый размер патча. Хорошая производительность здесь не гарантирует такую же производительность на закрытом энтерпрайз-коде на Java, C++ или легаси-системах с совершенно другой архитектурой и стилем. Бенчмарки — полезный сигнал направления, но не универсальная метрика «качества кодинга» как таковой.

Есть и более прозаичный риск — насыщение и «утечка» бенчмарка: чем популярнее становится SWE-bench как ориентир, тем больше вероятность, что примеры, похожие на его задачи, попадают в обучающие данные последующих моделей, что искусственно завышает результат без реального роста способностей за пределами бенчмарка.

### Почему вам это важно

Если вы выбираете модель для агентного кодинга по лидерборду SWE-bench, [этот пост](https://www.anthropic.com/engineering/swe-bench-sonnet) стоит прочитать целиком, а не только ради итоговой цифры — там описана именно обвязка, которая довела результат до заявленного уровня. Перед покупкой решения проверьте его на своей кодовой базе и своём стеке: цифра из чужого пресс-релиза, полученная на open-source Python-репозиториях, может не иметь никакого отношения к тому, как модель справится с вашим легаси-кодом.

## English version

# SWE-bench Verified and Claude 3.5 Sonnet: what "best at coding" actually measures

The third Anthropic engineering post to surface in today's roundup — [«Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet»](https://www.anthropic.com/engineering/swe-bench-sonnet) — is worth unpacking not just for the result, but for the benchmark itself. SWE-bench Verified is a subset of real issues from open-source GitHub repositories, filtered and manually verified so that each task is unambiguously solvable and correctly checkable by automated tests. The model gets a bug or feature description from a real issue and has to produce a patch that passes the repository's hidden tests — noticeably closer to actual developer work than LeetCode-style puzzles.

The post describes not just the model's result but the "scaffolding" — the harness around the model that gives it access to the repository's filesystem, lets it run commands, and lets it iteratively check its own patch before final submission. That's an important methodological point: a SWE-bench score isn't a "pure" measure of a model's one-shot problem-solving ability — it's a measure of the model paired with a specific agentic harness built by a specific team. Swap the harness and the leaderboard number changes, even if the model weights stay the same.

That's exactly why any claim along the lines of "model X is now the new number one at coding" deserves a healthy dose of skepticism. SWE-bench, for all its strengths, is a set of tasks drawn from open-source Python code on GitHub, with its own particular flavor: a specific codebase style, a specific type of issue, a specific patch size. Strong performance here doesn't guarantee the same performance on closed-source enterprise code in Java, C++, or legacy systems with an entirely different architecture and style. Benchmarks are a useful directional signal, not a universal measure of "coding quality" as such.

There's also a more mundane risk — saturation and benchmark leakage: the more popular SWE-bench becomes as a reference point, the more likely examples resembling its tasks end up in later models' training data, artificially inflating the score without a real gain in capability outside the benchmark.

### Why it matters

If you're picking a model for agentic coding based on the SWE-bench leaderboard, [this post](https://www.anthropic.com/engineering/swe-bench-sonnet) is worth reading in full rather than just for the headline number — it specifically describes the harness that got the result to the claimed level. Before adopting a solution, test it against your own codebase and stack: a number from someone else's press release, obtained on open-source Python repos, may have little relation to how the model handles your legacy code.
