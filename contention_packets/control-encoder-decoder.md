---
title: "control-encoder-decoder"
parent: "Invalidity Contentions"
nav_order: 56
layout: default
---

# Invalidity Contention Packet — `control-encoder-decoder`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-encoder-decoder`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2014-09  
**Most recent disclosure:** 2015-05

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-encoder-decoder`.

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

### 2015-05 — U-Net

- **id:** `u-net-ronneberger-miccai-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Freiburg; Olaf Ronneberger, Philipp Fischer, Thomas Brox
- **disclosure citation:** Ronneberger, O., Fischer, P., Brox, T. 'U-Net: Convolutional Networks for Biomedical Image Segmentation'. MICCAI 2015. arXiv:1505.04597. University of Freiburg.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-image-segmentation`, `control-encoder-decoder`

**Prior art notes:**

> U-Net (Ronneberger-Fischer-Brox MICCAI 2015) is the foundational image-segmentation neural network. 10-year-deep public-domain prior art. >75,000 citations. The architectural ancestor of every modern image-segmentation network + the denoising backbone of Stable Diffusion + DDPM (round-29). Direct shielding for any commercial humanoid claim using U-Net-class architectures for perception or generation.

**Sources:**

1. Ronneberger, O., Fischer, P., Brox, T. arXiv:1505.04597 MICCAI 2015.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2fbde5f`.*
