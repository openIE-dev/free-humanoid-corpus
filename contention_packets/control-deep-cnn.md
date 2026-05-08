---
title: "control-deep-cnn"
parent: "Invalidity Contentions"
nav_order: 32
layout: default
---

# Invalidity Contention Packet — `control-deep-cnn`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-deep-cnn`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2012-12  
**Most recent disclosure:** 2015-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-deep-cnn`.

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

### 2012-12 — AlexNet

- **id:** `alexnet-krizhevsky-nips-2012`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Toronto; Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton
- **disclosure citation:** Krizhevsky, A., Sutskever, I., Hinton, G. E. 'ImageNet Classification with Deep Convolutional Neural Networks'. NeurIPS 2012. University of Toronto.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-deep-cnn`

**Prior art notes:**

> AlexNet (Krizhevsky et al. NeurIPS 2012) is **the paper that started the deep-learning revolution in computer vision**. 13-year-deep public-domain prior art. >180,000 citations. The predecessor of ResNet (round-30), ViT (round-30), every modern vision encoder. Together with ImageNet (round-30), constitutes the foundational vision-DL substrate underlying every commercial humanoid vision system.

**Sources:**

1. Krizhevsky et al. NeurIPS 2012.

---

### 2015-12 — ResNet (Residual Networks)

- **id:** `resnet-he-cvpr-2016`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Microsoft Research Asia; Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
- **disclosure citation:** He, K., Zhang, X., Ren, S., Sun, J. 'Deep Residual Learning for Image Recognition'. CVPR 2016 Best Paper. arXiv:1512.03385. Microsoft Research Asia.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-deep-cnn`

**Prior art notes:**

> ResNet (He et al. CVPR 2016 Best Paper) is the foundational deep residual networks paper. 10-year-deep public-domain prior art. >250,000 citations — one of the most-cited ML papers of all time. The visual encoder underlying BC-Z (round-29), RT-1 (corpus), and most pre-Transformer robotic VLA. Direct shielding for any commercial humanoid claim using deep CNNs for vision encoding.

**Sources:**

1. He et al. arXiv:1512.03385 CVPR 2016 Best Paper.

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
