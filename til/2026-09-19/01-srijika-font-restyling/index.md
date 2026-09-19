---
date: 2026-09-19
topic: "Srijika: новый стиль шрифта для 9 индийских письменностей без пересборки OpenType-логики"
source: https://huggingface.co/papers/2609.05661
lang: [ru, en]
generated: true
---

## RU

В дайджесте — статья [«Srijika: OpenType-Layout-Reusing Font Restyling for Nine Indic Scripts»](https://huggingface.co/papers/2609.05661) (Anil Pai). Сохранившаяся часть аннотации: система создаёт устанавливаемые OpenType-шрифты для девяти брахмийских письменностей (деванагари, тамильский, бенгальский, телугу, каннада, малаялам, гуджарати, гурмукхи, ория), но вместо генерации шрифта с нуля переиспользует уже существующую разметку OpenType-layout, меняя только контуры глифов («restyles glyph outlines from shapin…» — обрыв на слове, вероятно «shaping-aware»).

Что здесь важно понять: для индийских письменностей самое дорогое в создании шрифта — не рисование букв, а правила сложного шейпинга (лигатуры, составные знаки, перестановки), закодированные в таблицах OpenType. Если Srijika действительно переиспользует эту логику и меняет только визуальный стиль глифов, это резко снижает стоимость создания новых стилей для языков, для которых шрифтов и так немного. Точный механизм — в [полной статье](https://huggingface.co/papers/2609.05661).

## EN

Today's digest includes [«Srijika: OpenType-Layout-Reusing Font Restyling for Nine Indic Scripts»](https://huggingface.co/papers/2609.05661) (Anil Pai). The surviving abstract: the system produces installable OpenType fonts for nine Brahmic scripts (Devanagari, Tamil, Bengali, Telugu, Kannada, Malayalam, Gujarati, Gurmukhi, Odia), but instead of generating a font from scratch, it reuses existing OpenType layout rules and only restyles the glyph outlines ("restyles glyph outlines from shapin…" — cut off, likely "shaping-aware").

What's worth understanding: for Indic scripts, the expensive part of font-making isn't drawing letterforms, it's the complex shaping rules (ligatures, conjuncts, reordering) encoded in OpenType tables. If Srijika genuinely reuses that logic and only swaps the visual style, that sharply cuts the cost of producing new styles for languages that already have few font choices. The exact mechanism is in [the full paper](https://huggingface.co/papers/2609.05661).
