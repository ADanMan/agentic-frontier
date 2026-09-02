---
date: 2026-09-02
topic: "Multi-Vector embeddings: один документ — не один вектор"
source: https://huggingface.co/blog/multi-vector-encoder
lang: [ru, en]
generated: true
---

## RU

Hugging Face выпустил разбор [Multi-Vector (Late Interaction) Embedding моделей в Sentence Transformers](https://huggingface.co/blog/multi-vector-encoder) за авторством Tom Aarsen, Antoine Chaffin и Raphael Sourty. Что здесь важно понять: классический подход к эмбеддингам сжимает весь документ или запрос в один вектор, а сравнение при поиске — это одно скалярное произведение. Late interaction (в духе ColBERT) вместо этого хранит по вектору на каждый токен и сравнивает запрос с документом «токен к токену», выбирая для каждого токена запроса максимально похожий токен документа и суммируя эти максимумы. Это дороже по памяти и вычислениям, чем один вектор на документ, но точнее ловит частичные совпадения — когда важен конкретный термин в длинном тексте, а не общий смысл целиком. Раз Sentence Transformers, самая массовая библиотека эмбеддингов в экосистеме, добавляет такую поддержку — это сигнал, что multi-vector-поиск переходит из области нишевых исследовательских реализаций в стандартный инструментарий.

## EN

Hugging Face published a breakdown of [Multi-Vector (Late Interaction) Embedding models in Sentence Transformers](https://huggingface.co/blog/multi-vector-encoder), by Tom Aarsen, Antoine Chaffin, and Raphael Sourty. What matters here: the classic embedding approach compresses an entire document or query into a single vector, and search comparison boils down to one dot product. Late interaction (in the ColBERT tradition) instead keeps one vector per token and compares query to document token-by-token, taking each query token's best-matching document token and summing those maxima. That's more expensive in memory and compute than a single vector per document, but it catches partial matches more precisely — when a specific term matters in a long text rather than the overall gist. The fact that Sentence Transformers, the most widely used embedding library in the ecosystem, is adding support for this is a signal that multi-vector search is moving from niche research implementations into standard tooling.
