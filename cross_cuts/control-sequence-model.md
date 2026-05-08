---
title: control-sequence-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-sequence-model`

**5 corpus entries disclose this subsystem.**

Earliest disclosure: 1997-11

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Long Short-Term Memory (LSTM) (1997-11)

- **id**: `lstm-hochreiter-schmidhuber-1997`
- **corpus**: academic
- **creator**: TU München + IDSIA Lugano; Sepp Hochreiter, Jürgen Schmidhuber
- **disclosure**: Hochreiter, S., Schmidhuber, J. 'Long Short-Term Memory'. Neural Computation 9(8) 1997. Technische Universität München + IDSIA Lugano.
- **ip status**: public-domain
- **prior art notes**: LSTM (Hochreiter + Schmidhuber 1997) is the foundational recurrent neural network architecture. 28-year-deep public-domain prior art. >85,000 citations. The pre-Transformer-era sequence-modeling standard, still used in modern robotic policy architectures (RoboFlamingo round-29 uses LSTM action decoder). Direct shielding for any commercial humanoid claim using recurrent neural network architectures.

## Sequence to Sequence Learning (2014-09)

- **id**: `sutskever-seq2seq-nips-2014`
- **corpus**: academic
- **creator**: Google; Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **disclosure**: Sutskever, I., Vinyals, O., Le, Q. V. 'Sequence to Sequence Learning with Neural Networks'. NeurIPS 2014. arXiv:1409.3215. Google.
- **ip status**: public-domain
- **prior art notes**: Seq2Seq (Sutskever-Vinyals-Le NeurIPS 2014) is the foundational encoder-decoder neural network paper. 11-year-deep public-domain prior art. The architectural pattern underlying every encoder-decoder system in the corpus, including every VLA's action-decoder pattern. Together with LSTM (round-30) + Transformer (round-29), establishes the sequence-modeling chain underlying every modern AI system.

## Transformer (Attention Is All You Need) (2017-06)

- **id**: `transformer-vaswani-neurips-2017`
- **corpus**: academic
- **creator**: Google Brain + Google Research; Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin
- **disclosure**: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., Polosukhin, I. 'Attention Is All You Need'. NeurIPS 2017. arXiv:1706.03762. Google Brain + Google Research.
- **ip status**: public-domain
- **prior art notes**: The Transformer (Vaswani et al. NeurIPS 2017) is **the single most-cited prior-art-everything-in-the-corpus reference**. 8-year-deep public-domain prior art. Direct architectural ancestor of every modern foundation model + every VLA. This entry resolves ~50 prior_art_notes references that previously cited 'Transformer architecture' or 'Vaswani 2017' informally. **Direct shielding for any commercial humanoid claim that uses transformer architectures**, which is essentially every modern humanoid VLA + perception system.

## Retentive Network (RetNet) (2023-07)

- **id**: `retentive-network-microsoft-2023`
- **corpus**: academic
- **creator**: Microsoft Research + Tsinghua University; Yutao Sun, Furu Wei et al.
- **disclosure**: Sun, Y., Dong, L., Huang, S., Ma, S., Xia, Y., Xue, J., Wang, J., Wei, F. 'Retentive Network: A Successor to Transformer for Large Language Models'. arXiv:2307.08621, July 2023. Microsoft Research + Tsinghua University.
- **ip status**: public-domain
- **prior art notes**: RetNet (Sun et al. Microsoft + Tsinghua 2023) is one of the canonical post-Transformer architecture explorations. 2-year-deep public-domain prior art. Together with Mamba (round-34), establishes the alternative-architecture prior-art chain that challenges Transformer dominance in long-context sequence modeling.

## Mamba (Selective State-Space Model) (2023-12)

- **id**: `mamba-state-space-model-gu-dao-2023`
- **corpus**: academic
- **creator**: CMU + Princeton + Together AI; Albert Gu, Tri Dao
- **disclosure**: Gu, A., Dao, T. 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces'. COLM 2024. arXiv:2312.00752. CMU + Princeton + Together AI. Antecedent: S4 / S4D / S5 (Gu 2022).
- **ip status**: public-domain
- **prior art notes**: Mamba (Gu + Dao COLM 2024) is the canonical state-space-model foundation architecture. 1.5-year-deep public-domain prior art. A leading architectural alternative to Transformers (round-29) for long-context sequence modeling. Direct shielding for any commercial humanoid claim using state-space-model architectures for VLA or perception.
