---
date: 2026-09-29
topic: Efficient fine-tuning / LoRA merging
source: https://huggingface.co/papers/2609.22237
lang: [ru, en]
generated: true
---

## Русская версия

# Не все ранги одинаково полезны: как экономить бюджет при слиянии LoRA-адаптеров

Идея LoRA (low-rank adapters) звучит красиво: вместо того чтобы держать в памяти отдельную копию модели под каждую задачу, вы храните маленькие «довески» — адаптеры — и подключаете нужный на лету. Но у этой красоты есть цена: если у вас десятки задач, десятки адаптеров нужно где-то хранить и между ними переключаться, и это тоже накладные расходы на инференсе.

Логичный следующий шаг — слияние (merging): взять несколько LoRA-адаптеров и склеить их в один, чтобы не тратить время на подгрузку под каждый запрос. Именно с этим и разбирается новая работа [«Not All Ranks Are Equal: Budget-Aware LoRA Merging Across Tasks»](https://huggingface.co/papers/2609.22237) (Avinash Amballa, Yashas Malur Saidutta, Wenbo Li, Lazar Valkov, Srinivas Chappidi). Авторы указывают на проблему, которую обычно замалчивают: существующие методы слияния молчаливо предполагают, что каждому слою нужен один и тот же ранг адаптера. А это, конечно же, не так — простая задача (скажем, классификация тональности) прекрасно обходится рангом 8, а что-то более «мозговыносящее» требует ранга 32 и выше.

Если вы всё равно усредняете (или иначе комбинируете) адаптеры с одинаковым «весом ранга» на каждый слой, вы либо тратите память впустую на простых задачах, либо режете по живому сложные. Авторы предлагают распределять ранг по бюджету — то есть решать не «какой ранг взять для всех», а «куда именно в сети стоит вложить ограниченный суммарный бюджет ранга», задача-специфично.

Здесь нет сенсационных цифр, которые можно было бы процитировать (в дайджесте абстракт обрывается до конкретных результатов), но сама постановка вопроса симптоматична для всей темы адаптации моделей: индустрия долго решала задачу «как обучить дёшево», а сейчас настала очередь задачи «как обслуживать дёшево много адаптеров одновременно». Слияние — это не бесплатная операция, у неё есть свои компромиссы, и работа честно называет один из них по имени.

### Почему вам это важно

Если вы держите в проде больше одной LoRA-адаптированной задачи — на что угодно, от чат-ботов до классификаторов, — вопрос «как слить адаптеры без потери качества» рано или поздно встанет перед вами. Знать, что «одинаковый ранг для всех» — это скрытое упрощение, а не нейтральный дефолт, стоит держать в голове ещё до того, как вы напишете код мёржа.

## English version

# Not All Ranks Are Equal: Budgeting LoRA Merges Across Tasks

LoRA (low-rank adapters) sold everyone on a neat promise: instead of a full model copy per task, you keep small "adapter" deltas and swap them in at inference time. The catch is that once you have dozens of tasks, you also have dozens of adapters to store and route between — which is its own overhead.

The obvious next move is merging: combine several LoRA adapters into one so you're not juggling per-request loads. That's exactly what a new paper, [«Not All Ranks Are Equal: Budget-Aware LoRA Merging Across Tasks»](https://huggingface.co/papers/2609.22237) (Avinash Amballa, Yashas Malur Saidutta, Wenbo Li, Lazar Valkov, Srinivas Chappidi), digs into. The authors call out an assumption most merging methods quietly make: that every layer deserves the same adapter rank. Obviously not true — a simple task (say, sentiment classification) does fine at rank 8, while something gnarlier needs rank 32 or more.

If you merge adapters as though they all carried the same "rank weight" per layer, you either waste capacity on easy tasks or starve the hard ones. The paper's proposal is to allocate rank against a fixed total budget — deciding not "what rank for everyone" but "where in the network a limited shared rank budget should actually go," task by task.

There are no headline numbers to quote here — the digest excerpt cuts off before results — but the framing itself is a useful signal about where adapter-based fine-tuning is heading. The field spent a long stretch answering "how do we train cheaply"; the next question is "how do we serve many adapters cheaply, together." Merging isn't a free operation, and this paper is at least honest about naming one of its hidden costs.

### Why it matters

If you're running more than one LoRA-adapted task in production — chatbots, classifiers, whatever — the "how do we merge without losing quality" question will land on your desk eventually. Worth internalizing now, before you write the merge code, that "same rank for everyone" is a hidden simplification, not a neutral default.
