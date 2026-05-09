---
title: "control-gaussian-splatting-slam"
parent: "Invalidity Contentions"
nav_order: 48
layout: default
---

# Invalidity Contention Packet — `control-gaussian-splatting-slam`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-gaussian-splatting-slam`  
**Entries:** 6 (2 commons-grade, 4 draft)  
**Earliest disclosure:** 2024-03  
**Most recent disclosure:** 2025-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-gaussian-splatting-slam`.

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

### 2024-03 — SemGauss-SLAM *(draft)*

- **id:** `semgauss-slam-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Zhu, Siting et al. (per arXiv 2403.07494)
- **disclosure citation:** Zhu, S., et al. 'SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM'. arXiv:2403.07494, March 2024.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-semantic-slam`, `control-novel-view-synthesis`

**Prior art notes:**

> SemGauss-SLAM is one of the first dense-semantic Gaussian-splatting SLAM systems (March 2024). 14-month-deep prior art for combining 3D Gaussian representations with per-primitive semantic features. Predates and informs the open-vocabulary GS-SLAM lineage that WildGS-SLAM, LEG-SLAM, LEGO-SLAM, and RADIO-ViPE descend from.

**Sources:**

1. arXiv:2403.07494 March 2024.

---

### 2024-09 — LEGS (Language-Embedded Gaussian Splats)

- **id:** `legs-berkeley-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley AUTOLab; Goldberg group
- **disclosure citation:** Yu, J., et al. 'LEGS: Language-Embedded Gaussian Splats — Incrementally Building Room-Scale Representations with a Mobile Robot'. IROS 2024. arXiv:2409.18108. UC Berkeley AUTOLab.
- **disclosed subsystems:** `control-gaussian-splatting-slam`, `control-open-vocabulary`, `control-foundation-model-perception`

**Prior art notes:**

> LEGS is the canonical Berkeley AUTOLab open-vocabulary Gaussian-splatting representation (IROS 2024). 1.5-year-deep prior art for: CLIP-aligned per-primitive features in 3DGS, incremental room-scale construction by mobile robot, language-grounded mobile-manipulation scene representations. Predates and informs LEG-SLAM, LEGO-SLAM, and any commercial humanoid claim on language-queryable 3D scene maps built onboard.

**Sources:**

1. Yu et al. arXiv:2409.18108 September 2024.
2. IROS 2024 proceedings paper (autolab.berkeley.edu/assets/publications/media/2024_IROS_LEGS_CR.pdf).

---

### 2024-11 — DGS-SLAM *(draft)*

- **id:** `dgs-slam-kong-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim (per arXiv 2411.10722)
- **disclosure citation:** Kong, M., Lee, J., Lee, S., Kim, E. 'DGS-SLAM: Gaussian Splatting SLAM in Dynamic Environment'. arXiv:2411.10722, November 2024.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-dynamic-scene-robust`

**Prior art notes:**

> DGS-SLAM (Kong et al. arXiv 2411.10722, November 2024). 6-month-deep prior art on dynamic-aware Gaussian-splatting SLAM. Cited as a competitor in the RADIO-ViPE Table II TUM-RGBD ATE benchmark; the round-10 RADIO-ViPE entry's claim of SOTA is anchored by comparison against this and several sibling systems. Direct shielding for any commercial humanoid claim on dynamic-scene GS-SLAM.

**Sources:**

1. Kong et al. arXiv:2411.10722 November 2024.

---

### 2025-04 — WildGS-SLAM

- **id:** `wildgs-slam-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys (ETH Zürich), Songyou Peng, Iro Armeni (Stanford GradientSpaces)
- **disclosure citation:** Zheng, J., Zhu, Z., Bieri, V., Pollefeys, M., Peng, S., Armeni, I. 'WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments'. CVPR 2025. arXiv:2504.03886. ETH Zürich + Stanford GradientSpaces.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-dynamic-scene-robust`, `control-novel-view-synthesis`

**Prior art notes:**

> WildGS-SLAM is the canonical CVPR 2025 monocular dynamic-scene Gaussian-splatting SLAM system from ETH + Stanford. Establishes 1-year-deep prior art for: monocular GS-SLAM with dynamic-scene robustness, photorealistic novel-view rendering of static background while filtering dynamic foreground. Among the systems RADIO-ViPE benchmarks against (TUM-RGBD dynamic). Direct shielding for any commercial humanoid claim on monocular dynamic-scene mapping with photorealistic reconstruction.

**Sources:**

1. Zheng et al. CVPR 2025.
2. arXiv:2504.03886 April 2025.
3. Project page (wildgs-slam.github.io).
4. GitHub: github.com/GradientSpaces/WildGS-SLAM.

---

### 2025-06 — LEG-SLAM *(draft)*

- **id:** `leg-slam-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** LEG-SLAM authors (per arXiv 2506.03073)
- **disclosure citation:** Authors per arXiv 2506.03073. 'LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM'. arXiv:2506.03073, June 2025.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-semantic-slam`, `control-foundation-model-perception`

**Prior art notes:**

> LEG-SLAM (June 2025) is a real-time language-enhanced GS-SLAM system. 11-month-deep prior art on: real-time fps-class language-aligned GS-SLAM, DINOv2 feature compression for compact per-Gaussian language encoding. Distinct from but contemporary with LEGO-SLAM (Nov 2025). Both feed the open-vocab GS-SLAM lineage that RADIO-ViPE compares against.

**Sources:**

1. arXiv:2506.03073 June 2025.
2. Project page (titrom025.github.io/LEG-SLAM/).

---

### 2025-11 — LEGO-SLAM *(draft)*

- **id:** `lego-slam-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Lab of AI and Robotics (per github.com/Lab-of-AI-and-Robotics/LEGO-SLAM)
- **disclosure citation:** Authors per arXiv 2511.16144. 'LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM'. arXiv:2511.16144, November 2025. Lab of AI and Robotics.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-open-vocabulary`, `control-semantic-slam`, `control-foundation-model-perception`

**Prior art notes:**

> LEGO-SLAM (Nov 2025) is the first claimed real-time open-vocabulary GS-SLAM system. 6-month-deep prior art for: 16-dim language-feature compression in GS, language-guided Gaussian pruning. Direct shielding for any commercial humanoid claim on real-time onboard open-vocabulary scene mapping. Together with LEG-SLAM, LEGS, and SemGauss-SLAM, the open-vocab GS-SLAM corpus is now ~6-month to 14-month deep across five contemporary systems — fully covering the architectural surface of RADIO-ViPE's competitor table.

**Sources:**

1. arXiv:2511.16144 November 2025.
2. GitHub: github.com/Lab-of-AI-and-Robotics/LEGO-SLAM.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bd98079`.*
