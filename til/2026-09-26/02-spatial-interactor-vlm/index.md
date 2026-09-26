---
date: 2026-09-26
topic: "Spatial-Interactor: пространственное рассуждение через локальные переходы состояния, а не статичную сцену"
source: https://huggingface.co/papers/2609.23038
lang: [ru, en]
generated: true
---

## RU

В дайджесте — препринт [«Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World»](https://huggingface.co/papers/2609.23038) за авторством Kaixiang Yao, Xu Wang, Miao Pan, Hu Xiyue, Weishi Wang и соавторов. Аннотация обрывается на «Reasoning in dynamic environments requires VLMs to perceive local state transitions caused by object mot…» — обрыв на слове «motion». Что здесь важно понять из уцелевшего текста: авторы разделяют «пространственное рассуждение вообще» (понять, где что находится на одном статичном кадре) и рассуждение в динамических средах — где модели нужно отслеживать «локальные переходы состояния», вызванные движением объектов, то есть не просто зафиксировать расположение объектов один раз, а следить, как оно меняется от кадра к кадру из-за движения. Название метода — «через взаимодействие с наблюдаемым физическим миром» — намекает, что предлагаемый подход учит эту способность не на статичных размеченных сценах, а через какую-то форму активного взаимодействия со средой, но конкретный механизм обучения (симуляция? реальные роботы? синтетические траектории?) в дайджест не попал.

## EN

Today's digest carries the preprint [«Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World»](https://huggingface.co/papers/2609.23038) by Kaixiang Yao, Xu Wang, Miao Pan, Hu Xiyue, Weishi Wang, and co-authors. The abstract cuts off at "Reasoning in dynamic environments requires VLMs to perceive local state transitions caused by object mot…" — breaking off mid-word at "motion." What's worth understanding from the surviving text: the authors distinguish "spatial reasoning in general" (figuring out where things are in one static frame) from reasoning in dynamic environments, where a model needs to track "local state transitions" caused by object motion — not just fixing object positions once, but following how they change frame to frame because things move. The method's name — "through interaction with the observable physical world" — hints that the proposed approach trains this capability not on static labeled scenes but through some form of active interaction with the environment, though the specific training mechanism (simulation? real robots? synthetic trajectories?) didn't make it into the digest.
