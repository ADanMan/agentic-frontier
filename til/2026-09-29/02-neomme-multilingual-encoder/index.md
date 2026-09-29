---
date: 2026-09-29
topic: "NeoMME: H Company анонсирует энкодер, 'нативно' мультимодальный и мультиязычный"
source: https://huggingface.co/blog/Hcompany/neomme
lang: [ru, en]
generated: true
---

## RU

В блоге Hugging Face вышел короткий анонс от H Company — [NeoMME: an efficient Multimodal-native and Multilingual Encoder](https://huggingface.co/blog/Hcompany/neomme). Что здесь важно понять: это энкодер, а не генеративная LLM — то есть модель, задача которой превращать вход (текст, изображение) в единое представление для последующих задач (поиск, классификация, ретрив), а не генерировать текст. Ключевое слово в названии — «native»: авторы позиционируют мультимодальность и мультиязычность не как надстройку поверх текстовой модели, а как то, что заложено в архитектуру с нуля. Само название «эффективный» намекает на компромисс в сторону меньшего размера/латентности ради практичного деплоя. К сожалению, в самом дайджесте нет конкретных цифр по бенчмаркам или размеру модели — только заголовок и авторство, так что судить о реальных результатах пока рано, стоит дождаться полного поста.

## EN

Hugging Face's blog carries a short announcement from H Company — [NeoMME: an efficient Multimodal-native and Multilingual Encoder](https://huggingface.co/blog/Hcompany/neomme). Worth understanding: this is an encoder, not a generative LLM — a model whose job is turning input (text, images) into a shared representation for downstream tasks like search, classification, or retrieval, not generating text. The key word in the name is "native": the authors are positioning multimodality and multilinguality as baked into the architecture from the start, not bolted onto a text-only model afterward. "Efficient" in the title hints at a size/latency tradeoff aimed at practical deployment. Unfortunately, today's digest snippet carries no concrete benchmark numbers or model size — just the title and byline — so it's too early to judge actual results; the full post is worth checking directly.
