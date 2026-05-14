---
title: "control-open-vocabulary"
parent: "Invalidity Contentions"
nav_order: 112
layout: default
---

# Invalidity Contention Packet — `control-open-vocabulary`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-open-vocabulary`  
**Entries:** 4 (3 commons-grade, 1 draft)  
**Earliest disclosure:** 2023-03  
**Most recent disclosure:** 2026-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-open-vocabulary`.

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

### 2023-03 — LERF (Language Embedded Radiance Fields)

- **id:** `lerf-kerr-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley AUTOLab + BAIR; Kerr, Kim, Goldberg, Kanazawa, Tancik
- **disclosure citation:** Kerr, J., Kim, C. M., Goldberg, K., Kanazawa, A., Tancik, M. 'LERF: Language Embedded Radiance Fields'. arXiv:2303.09553, March 2023. ICCV 2023 (Oral). UC Berkeley AUTOLab + Berkeley AI Research.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-open-vocabulary`, `control-novel-view-synthesis`

**Prior art notes:**

> LERF is the canonical first language-embedded NeRF (Berkeley + BAIR, ICCV 2023 Oral). 2-year-deep prior art for: CLIP-embedded 3D radiance fields, open-vocabulary natural-language 3D scene queries. The architectural ancestor of LEGS (round-12), LEG-SLAM (round-12), LEGO-SLAM (round-12), and any commercial claim on language-queryable 3D scene representations. Predates the Gaussian-splatting instantiations and establishes the architectural pattern.

**Sources:**

1. Kerr et al. arXiv:2303.09553 March 2023; ICCV 2023.
2. Project page (lerf.io).
3. GitHub: github.com/kerrj/lerf.

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

### 2026-04 — RADIO-ViPE

- **id:** `radio-vipe-itmo-2026`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ITMO University BE2R Lab; Nasser, Iumanov, Li, Popov, Mahmoud, Kolyubin
- **disclosure citation:** Nasser, Z., Iumanov, M., Li, T., Popov, M., Mahmoud, J., Kolyubin, S. 'RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM in Dynamic Environments'. arXiv:2604.26067v1, April 28, 2026. ITMO University, Biomechatronics and Energy-Efficient Robotics (BE2R) Lab, Saint Petersburg, Russia.
- **disclosed subsystems:** `control-vio-slam`, `control-semantic-slam`, `control-open-vocabulary`, `control-bundle-adjustment`, `control-foundation-model-perception`, `control-dynamic-scene-robust`

**Prior art notes:**

> RADIO-ViPE is the most recent and architecturally complete online open-vocabulary semantic SLAM system. April 2026 arXiv preprint; 9 days before this corpus entry. Establishes very-recent (sub-1-week) open-academic prior art for: calibration-free monocular semantic SLAM, tightly-coupled multi-modal fusion (RADIO + SigLIP + geometric BA), adaptive-kernel dynamic-scene robustness, online operation at 8-10 FPS. Directly shields any commercial humanoid claim on: 'onboard semantic scene understanding from monocular video' (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo, etc. all face this), 'language-grounded robotic perception in dynamic environments', 'calibration-free humanoid camera deployment'. The TUM-RGBD ATE comparison table in Table II of the paper enumerates the prior art — RADIO-ViPE outperforms Dyna-SLAM, DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON, ViPE — every one of which is itself open-academic prior art for humanoid perception. Lineage: ORB-SLAM3 (geometric baseline) → DROID-SLAM (dense differentiable) → ViPE (Princeton in-the-wild metric depth) → RADIO-ViPE (ITMO open-vocab + calibration-free).

**Sources:**

1. Nasser et al. arXiv:2604.26067v1 April 2026.
2. ITMO BE2R Lab (itmo.ru/en/faculties_and_institutes/96/).
3. TUM-RGBD dynamic benchmark (vision.in.tum.de/data/datasets/rgbd-dataset).
4. Foundation models: NVIDIA RADIO (Ranzinger et al. 2024), SigLIP (Zhai et al. ICCV 2023).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `c61fc91`.*
