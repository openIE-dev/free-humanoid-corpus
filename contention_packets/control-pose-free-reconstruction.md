---
title: "control-pose-free-reconstruction"
parent: "Invalidity Contentions"
nav_order: 88
layout: default
---

# Invalidity Contention Packet — `control-pose-free-reconstruction`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-pose-free-reconstruction`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2023-12  
**Most recent disclosure:** 2025-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-pose-free-reconstruction`.

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

### 2023-12 — DUSt3R

- **id:** `dust3r-naver-cvpr-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NAVER LABS Europe + Aalto University; Shuzhe Wang, Vincent Leroy, Yohann Cabon, Boris Chidlovskii, Jerome Revaud
- **disclosure citation:** Wang, S., Leroy, V., Cabon, Y., Chidlovskii, B., Revaud, J. 'DUSt3R: Geometric 3D Vision Made Easy'. CVPR 2024. arXiv:2312.14132. NAVER LABS Europe + Aalto University.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-3d-reconstruction`, `control-uncalibrated-video-perception`, `control-pose-free-reconstruction`

**Prior art notes:**

> DUSt3R (Wang et al. CVPR 2024) is the foundational pose-free unconstrained 3D-reconstruction paper. 2-year-deep open-permissive prior art. **Direct architectural ancestor of MASt3R** (round-28 entry below), **VGGT** (in audit, round-corpus VGGT), **MegaSaM** (round-13), **NVIDIA ViPE** (round-11), **RADIO-ViPE** (round-10). The 2-year-deep DUSt3R-derived calibration-free reconstruction chain shields any commercial humanoid claim on uncalibrated-camera onboard 3D reconstruction.

**Sources:**

1. Wang et al. arXiv:2312.14132 CVPR 2024.
2. Project page (europe.naverlabs.com/research/publications/dust3r-geometric-3d-vision-made-easy/).
3. GitHub: github.com/naver/dust3r.

---

### 2025-03 — VGGT (Visual Geometry Grounded Transformer)

- **id:** `vggt-wang-cvpr-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Visual Geometry Group, University of Oxford + Meta AI; Jianyuan Wang, Andrea Vedaldi et al.
- **disclosure citation:** Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., Novotny, D. 'VGGT: Visual Geometry Grounded Transformer'. CVPR 2025 Best Paper. arXiv:2503.11651. Visual Geometry Group, University of Oxford + Meta AI.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-3d-reconstruction`, `control-pose-free-reconstruction`

**Prior art notes:**

> VGGT (Wang et al. Oxford VGG + Meta CVPR 2025 Best Paper) is the canonical 2025 foundation transformer for 3D vision. 6-month-deep open-permissive prior art. **CVPR 2025 Best Paper**. Direct successor to DUSt3R (round-28) and the calibration-free reconstruction chain (DUSt3R → MASt3R → MegaSaM → ViPE → RADIO-ViPE → VGGT). Direct shielding for any commercial humanoid claim on foundation-model-based 3D vision.

**Sources:**

1. Wang et al. arXiv:2503.11651 CVPR 2025 Best Paper.
2. GitHub: github.com/facebookresearch/vggt.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `69278e1`.*
