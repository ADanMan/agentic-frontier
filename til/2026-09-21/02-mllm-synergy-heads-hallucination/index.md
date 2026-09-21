---
date: 2026-09-21
topic: "Галлюцинации MLLM привязали не к вниманию вообще, а к конкретным 'synergy heads'"
source: https://huggingface.co/papers/2609.09206
lang: [ru, en]
generated: true
---

## RU

Статья [«MLLMs Hallucinate when Information Distribution Drifts in Synergy Heads»](https://huggingface.co/papers/2609.09206) (Meng'en Qin, Junye Chen, Jucheng Liu, Youlu Xing, Song Wang и соавторы) сужает привычную формулировку «мультимодальные модели галлюцинируют из-за внимания» до конкретного механизма: дело не во внимании вообще, а в дрейфе распределения информации именно в «synergy heads» — головах, отвечающих за совмещение сигналов из разных модальностей.

Что здесь важно понять: авторы прямо называют слабость существующих attention-based методов борьбы с галлюцинациями — они опираются на «косвенные сигналы» (дальше фрагмент абстракта в дайджесте обрывается, какие именно методы предлагаются взамен — не сказано). Даже без деталей решения сама диагностика полезна: если проблема действительно локализована в конкретном подмножестве голов, а не размазана по всей attention-матрице, это меняет, где искать причину галлюцинации при отладке своей MLLM.

## EN

The paper [«MLLMs Hallucinate when Information Distribution Drifts in Synergy Heads»](https://huggingface.co/papers/2609.09206) (Meng'en Qin, Junye Chen, Jucheng Liu, Youlu Xing, Song Wang, and co-authors) narrows the usual "multimodal models hallucinate because of attention" claim down to a specific mechanism: it's not attention broadly, but a drift in information distribution specifically inside "synergy heads" — the heads responsible for combining signals across modalities.

What's worth understanding: the authors explicitly call out a weakness in existing attention-based hallucination-mitigation methods — they rely on "indirect signals" (the abstract excerpt in the digest cuts off right after that, so what the paper proposes instead isn't stated here). Even without the fix's details, the diagnosis itself is useful: if the problem really is localized to a specific subset of heads rather than spread across the whole attention matrix, that changes where you'd look first when debugging hallucinations in your own MLLM.
