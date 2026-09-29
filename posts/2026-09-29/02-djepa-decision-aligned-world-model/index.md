---
date: 2026-09-29
topic: World models / decision-making
source: https://huggingface.co/papers/2609.24749
lang: [ru, en]
generated: true
---

## Русская версия

# D-JEPA: когда «модель мира» предсказывает будущее правильно, но всё равно выбирает не то действие

Latent world models — это модели, которые учатся предсказывать последствия действий не в пикселях или токенах, а в сжатом латентном пространстве: взял действие, получил вектор, вектор описывает «примерно что произойдёт». Звучит эффективно, и обычно так и есть — предсказывать в латентном пространстве дешевле, чем генерировать полное будущее состояние целиком.

Но у этого подхода есть скрытое допущение, которое разбирает новая работа [D-JEPA: A Decision-Aligned Latent World Model](https://huggingface.co/papers/2609.24749) (Shuaijun Liu, Chengyu Wu, Qifu Wen, Feiyang You, Chenglong Zhang и соавторы): точное предсказание не гарантирует, что расстояние между латентными векторами кандидатов правильно отражает, какое действие реально сработает. Иными словами, модель может отлично «угадывать будущее» — и при этом сравнение кандидатов в её латентном пространстве может вести к неправильному выбору. Авторы называют это «decision-local problem» — проблема локальна не к точности предсказания вообще, а конкретно к моменту принятия решения между альтернативами.

Представьте: у вас два варианта действия. World model честно предсказывает, что латентный вектор варианта A ближе к «желаемому» результату, чем вектор варианта B. Вы выбираете A. А на практике B срабатывает, а A — нет, просто потому что метрика близости в латентном пространстве не была откалибрована под то, что реально имеет значение для исполнения. Точность предсказания (что случится) и полезность для принятия решения (что выбрать) — это, оказывается, разные вещи, и одно не следует автоматически из другого.

Это довольно неприятный вывод для всей области reinforcement learning и планирования через world models: если ваш алгоритм выбирает действие по расстоянию в латентном пространстве, стоит спросить — а это расстояние вообще про то, про что вы думаете?

### Почему вам это важно

Если вы работаете с любым агентом, который планирует через симуляцию/предсказание в латентном пространстве (робототехника, RL-агенты, даже LLM-агенты, оценивающие варианты действий по эмбеддингам), это прямое предупреждение: точность world model — не то же самое, что её пригодность для выбора между конкретными альтернативами. Проверяйте decision-alignment отдельно от prediction accuracy.

## English version

# D-JEPA: When a World Model Predicts the Future Correctly and Still Picks the Wrong Action

Latent world models predict the consequences of actions not in pixels or tokens, but in a compressed latent space: take an action, get a vector, the vector roughly encodes "what happens." It's efficient, and usually it works — predicting in latent space is cheaper than generating a full future state outright.

But there's a hidden assumption baked into that approach, and a new paper, [D-JEPA: A Decision-Aligned Latent World Model](https://huggingface.co/papers/2609.24749) (Shuaijun Liu, Chengyu Wu, Qifu Wen, Feiyang You, Chenglong Zhang, and collaborators), calls it out: accurate prediction doesn't guarantee that latent distance actually reflects which candidate action will execute successfully. The model can be great at "guessing the future" while its latent-space comparison between candidates still points at the wrong one. The authors frame this as a "decision-local problem" — not about prediction accuracy in general, but specifically about the moment you're comparing alternatives to pick one.

Picture it concretely: two candidate actions. The world model correctly predicts that action A's latent vector sits closer to the "desired" outcome than action B's. You pick A. In practice, B works and A doesn't — simply because the latent-space distance metric was never calibrated against what actually matters for execution. Prediction accuracy (what will happen) and decision usefulness (what to pick) turn out to be different properties, and one doesn't automatically follow from the other.

That's an uncomfortable finding for planning-via-world-models and RL more broadly: if your algorithm selects actions by latent-space distance, it's worth asking whether that distance is actually measuring what you think it is.

### Why it matters

If you work with any agent that plans through latent-space prediction — robotics, RL agents, even LLM agents scoring action candidates by embeddings — this is a direct warning: a world model's prediction accuracy is not the same thing as its fitness for choosing between specific alternatives. Test decision-alignment separately from prediction accuracy.
