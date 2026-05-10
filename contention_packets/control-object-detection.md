---
title: "control-object-detection"
parent: "Invalidity Contentions"
nav_order: 100
layout: default
---

# Invalidity Contention Packet — `control-object-detection`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-object-detection`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2015-06  
**Most recent disclosure:** 2015-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-object-detection`.

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

### 2015-06 — Faster R-CNN

- **id:** `faster-rcnn-ren-nips-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Microsoft Research Asia; Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun
- **disclosure citation:** Ren, S., He, K., Girshick, R., Sun, J. 'Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks'. NeurIPS 2015. arXiv:1506.01497. Microsoft Research Asia.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-object-detection`

**Prior art notes:**

> Faster R-CNN (Ren-He-Girshick-Sun NeurIPS 2015) is the foundational two-stage object detector. 10-year-deep public-domain prior art. The pre-Transformer object-detection architecture used in many robotic perception stacks (Kaiming He is also the ResNet author — round-30).

**Sources:**

1. Ren, S. et al. arXiv:1506.01497 NeurIPS 2015.

---

### 2015-06 — YOLO (You Only Look Once)

- **id:** `yolo-redmon-cvpr-2016`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Washington + Allen Institute for AI + FAIR; Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi
- **disclosure citation:** Redmon, J., Divvala, S., Girshick, R., Farhadi, A. 'You Only Look Once: Unified, Real-Time Object Detection'. CVPR 2016. arXiv:1506.02640. University of Washington + Allen Institute for AI + Facebook AI Research. Subsequent: YOLOv2/v3/v4/v5/v6/v7/v8/v9/v10/v11 commercial + community variants.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-object-detection`, `control-real-time-perception`

**Prior art notes:**

> YOLO (Redmon et al. CVPR 2016) is the foundational real-time one-stage object detector. 9-year-deep public-domain prior art. Together with Faster R-CNN (round-32), establishes the dominant object-detection prior-art chain underlying most robotic perception systems pre-Transformer.

**Sources:**

1. Redmon et al. arXiv:1506.02640 CVPR 2016.
2. Project page (pjreddie.com/darknet/yolo).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `7ee2634`.*
