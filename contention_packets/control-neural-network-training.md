---
title: "control-neural-network-training"
parent: "Invalidity Contentions"
nav_order: 75
layout: default
---

# Invalidity Contention Packet — `control-neural-network-training`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-neural-network-training`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1986-10  
**Most recent disclosure:** 2015-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-neural-network-training`.

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

### 1986-10 — Backpropagation

- **id:** `backpropagation-rumelhart-hinton-1986`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Carnegie Mellon University + UCSD; David E. Rumelhart, Geoffrey Hinton, Ronald Williams
- **disclosure citation:** Rumelhart, D. E., Hinton, G. E., Williams, R. J. 'Learning Representations by Back-Propagating Errors'. Nature 323 1986. Antecedent: Werbos, P. PhD thesis Harvard 1974 (the mathematical foundations); Linnainmaa, S. master's thesis Helsinki 1970 (chain-rule application to neural networks).
- **disclosed subsystems:** `control-neural-network-training`, `control-gradient-descent`

**Prior art notes:**

> Backpropagation (Rumelhart-Hinton-Williams Nature 1986; antecedents Werbos 1974, Linnainmaa 1970) is the foundational neural-network training algorithm. 39-year-deep public-domain prior art. The substrate of every neural network in the corpus, every VLA, every policy. Direct shielding for any commercial humanoid claim using neural networks (which is essentially every modern humanoid system).

**Sources:**

1. Rumelhart, D. E., Hinton, G. E., Williams, R. J. Nature 323 1986.
2. Werbos, P. PhD thesis Harvard 1974 (mathematical foundations).
3. Linnainmaa, S. master's thesis Helsinki 1970 (chain rule).

---

### 2014-06 — Dropout regularization

- **id:** `dropout-srivastava-jmlr-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Toronto; Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, Ruslan Salakhutdinov
- **disclosure citation:** Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., Salakhutdinov, R. 'Dropout: A Simple Way to Prevent Neural Networks from Overfitting'. Journal of Machine Learning Research 15 2014. University of Toronto.
- **disclosed subsystems:** `control-neural-network-training`, `control-regularization`

**Prior art notes:**

> Dropout (Srivastava + Hinton et al. JMLR 2014) is the canonical neural-network regularization technique. 11-year-deep public-domain prior art. Used in essentially every deep neural network in the corpus.

**Sources:**

1. Srivastava et al. JMLR 15 2014.

---

### 2015-02 — Batch Normalization

- **id:** `batchnorm-ioffe-szegedy-icml-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google; Sergey Ioffe, Christian Szegedy
- **disclosure citation:** Ioffe, S., Szegedy, C. 'Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift'. ICML 2015. arXiv:1502.03167. Google.
- **disclosed subsystems:** `control-neural-network-training`, `control-normalization`

**Prior art notes:**

> Batch Normalization (Ioffe + Szegedy ICML 2015) is the canonical deep-network training technique. 10-year-deep public-domain prior art. Used in essentially every neural network in the corpus. Direct shielding for any commercial humanoid claim using deep neural networks.

**Sources:**

1. Ioffe, S., Szegedy, C. arXiv:1502.03167 ICML 2015.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf3c8f5`.*
