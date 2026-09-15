---
date: 2026-09-15
topic: "Sentence Transformers обещает разбор: как дообучать multi-vector эмбеддинги"
source: https://huggingface.co/blog/train-multi-vector-encoder
lang: [ru, en]
generated: true
---

## RU

В дайджесте — только заголовок и автор поста в блоге Hugging Face: [«Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers»](https://huggingface.co/blog/train-multi-vector-encoder), автор — Tom Aarsen, без текста аннотации. Что можно понять из самого заголовка, не додумывая остального: речь про multi-vector эмбеддинги — модели, которые представляют текст не одним вектором на весь документ, а набором векторов (по одному на токен или чанк), как это устроено в подходах вроде ColBERT для позднего взаимодействия (late interaction) в поиске. Заголовок обещает практическое руководство по дообучению именно такого типа моделей средствами библиотеки Sentence Transformers, а не только теорию. Какие конкретно техники дообучения и датасеты разбираются — аннотация не говорит; за деталями — [сам пост](https://huggingface.co/blog/train-multi-vector-encoder).

## EN

The digest carries only the title and author of a Hugging Face blog post: [«Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers»](https://huggingface.co/blog/train-multi-vector-encoder), by Tom Aarsen, with no summary text. What's worth noting from the title alone, without inventing the rest: this is about multi-vector embeddings — models that represent text not as a single vector per document but as a set of vectors (one per token or chunk), the way late-interaction approaches like ColBERT work in search. The title promises a practical finetuning guide for exactly this kind of model using the Sentence Transformers library, not just theory. Which specific finetuning techniques and datasets are covered isn't stated; for details, see [the post itself](https://huggingface.co/blog/train-multi-vector-encoder).
