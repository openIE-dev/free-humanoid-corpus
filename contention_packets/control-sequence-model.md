---
title: "control-sequence-model"
parent: "Invalidity Contentions"
nav_order: 93
layout: default
---

# Invalidity Contention Packet — `control-sequence-model`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-sequence-model`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 1997-11  
**Most recent disclosure:** 2023-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-sequence-model`.

To use it:

1. Identify the patent claim element being challenged.
2. Match the element against the entries below in chronological order (earliest
   first). The earliest entry that discloses the element is the strongest 102
   anticipation candidate.
3. For 103 obviousness contentions, identify the closest two-or-more entries
   that together disclose all claim elements.
4. Each entry's **prior_art_notes** field is element-by-element 102/103
   anticipation analysis — citable as-is.
5. Verify the timestamp authority via the procedures in Verification (below).

The Free Humanoid Corpus is licensed CC0 1.0; no permission is required to
cite, copy, or redistribute these contentions.

---

## Entries (chronological)

### 1997-11 — Long Short-Term Memory (LSTM)

- **id:** `lstm-hochreiter-schmidhuber-1997`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** TU München + IDSIA Lugano; Sepp Hochreiter, Jürgen Schmidhuber
- **disclosure citation:** Hochreiter, S., Schmidhuber, J. 'Long Short-Term Memory'. Neural Computation 9(8) 1997. Technische Universität München + IDSIA Lugano.
- **disclosed subsystems:** `control-foundation-model`, `control-sequence-model`, `control-recurrent-network`

**Prior art notes:**

> LSTM (Hochreiter + Schmidhuber 1997) is the foundational recurrent neural network architecture. 28-year-deep public-domain prior art. >85,000 citations. The pre-Transformer-era sequence-modeling standard, still used in modern robotic policy architectures (RoboFlamingo round-29 uses LSTM action decoder). Direct shielding for any commercial humanoid claim using recurrent neural network architectures.

**Sources:**

1. Hochreiter, S., Schmidhuber, J. Neural Computation 9(8) 1997.

---

### 2014-09 — Sequence to Sequence Learning

- **id:** `sutskever-seq2seq-nips-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google; Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **disclosure citation:** Sutskever, I., Vinyals, O., Le, Q. V. 'Sequence to Sequence Learning with Neural Networks'. NeurIPS 2014. arXiv:1409.3215. Google.
- **disclosed subsystems:** `control-foundation-model`, `control-encoder-decoder`, `control-sequence-model`

**Prior art notes:**

> Seq2Seq (Sutskever-Vinyals-Le NeurIPS 2014) is the foundational encoder-decoder neural network paper. 11-year-deep public-domain prior art. The architectural pattern underlying every encoder-decoder system in the corpus, including every VLA's action-decoder pattern. Together with LSTM (round-30) + Transformer (round-29), establishes the sequence-modeling chain underlying every modern AI system.

**Sources:**

1. Sutskever, I., Vinyals, O., Le, Q. V. arXiv:1409.3215 NeurIPS 2014.

---

### 2017-06 — Transformer (Attention Is All You Need)

- **id:** `transformer-vaswani-neurips-2017`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Brain + Google Research; Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin
- **disclosure citation:** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., Polosukhin, I. 'Attention Is All You Need'. NeurIPS 2017. arXiv:1706.03762. Google Brain + Google Research.
- **disclosed subsystems:** `control-foundation-model`, `control-attention-mechanism`, `control-sequence-model`

**Prior art notes:**

> The Transformer (Vaswani et al. NeurIPS 2017) is **the single most-cited prior-art-everything-in-the-corpus reference**. 8-year-deep public-domain prior art. Direct architectural ancestor of every modern foundation model + every VLA. This entry resolves ~50 prior_art_notes references that previously cited 'Transformer architecture' or 'Vaswani 2017' informally. **Direct shielding for any commercial humanoid claim that uses transformer architectures**, which is essentially every modern humanoid VLA + perception system.

**Sources:**

1. Vaswani et al. arXiv:1706.03762 NeurIPS 2017.

---

### 2023-07 — Retentive Network (RetNet)

- **id:** `retentive-network-microsoft-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Microsoft Research + Tsinghua University; Yutao Sun, Furu Wei et al.
- **disclosure citation:** Sun, Y., Dong, L., Huang, S., Ma, S., Xia, Y., Xue, J., Wang, J., Wei, F. 'Retentive Network: A Successor to Transformer for Large Language Models'. arXiv:2307.08621, July 2023. Microsoft Research + Tsinghua University.
- **disclosed subsystems:** `control-foundation-model`, `control-sequence-model`

**Prior art notes:**

> RetNet (Sun et al. Microsoft + Tsinghua 2023) is one of the canonical post-Transformer architecture explorations. 2-year-deep public-domain prior art. Together with Mamba (round-34), establishes the alternative-architecture prior-art chain that challenges Transformer dominance in long-context sequence modeling.

**Sources:**

1. Sun et al. arXiv:2307.08621 July 2023.

---

### 2023-12 — Mamba (Selective State-Space Model)

- **id:** `mamba-state-space-model-gu-dao-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** CMU + Princeton + Together AI; Albert Gu, Tri Dao
- **disclosure citation:** Gu, A., Dao, T. 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces'. COLM 2024. arXiv:2312.00752. CMU + Princeton + Together AI. Antecedent: S4 / S4D / S5 (Gu 2022).
- **disclosed subsystems:** `control-foundation-model`, `control-state-space-model`, `control-sequence-model`

**Prior art notes:**

> Mamba (Gu + Dao COLM 2024) is the canonical state-space-model foundation architecture. 1.5-year-deep public-domain prior art. A leading architectural alternative to Transformers (round-29) for long-context sequence modeling. Direct shielding for any commercial humanoid claim using state-space-model architectures for VLA or perception.

**Sources:**

1. Gu, A., Dao, T. arXiv:2312.00752 COLM 2024.
2. Gu, A. PhD thesis (Stanford 2023) on S4/S5.

---

## Verification

This packet's entries are anchored by the Free Humanoid Corpus 2026.Q2
release with three independent cryptographic timestamps proving
pre-existence:

- **FreeTSA RFC 3161** — `releases/2026.Q2/freetsa.tsr` in the corpus repo
- **DigiCert RFC 3161** — `releases/2026.Q2/digicert.tsr`
- **OpenTimestamps Bitcoin-anchored** — `releases/2026.Q2/corpus-2026.Q2.tar.gz.ots`,
  with Bitcoin block headers at heights **948142** (bob),
  **948151** (eternitywall), and **948161** (catallaxy).

The full release tarball SHA-256 is `aa9430c6e785a409e3dbb10042b16e0e5677752c85eeffcba2c6b5605cde27ce`,
archived on Zenodo at <https://doi.org/10.5281/zenodo.20049531>.

Anyone with a Bitcoin block explorer can independently verify that the corpus
tarball — containing all entries cited in this packet — existed at or before
the timestamps anchored in those blocks.

For verification procedure see <https://github.com/openIE-dev/free-humanoid-corpus/blob/main/tools/verify_release.sh>.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `f228137`.*
