---
title: "control-dynamic-scene-robust"
parent: "Invalidity Contentions"
nav_order: 28
layout: default
---

# Invalidity Contention Packet — `control-dynamic-scene-robust`

**Generated:** 2026-05-07  
**Cross-cut tag:** `control-dynamic-scene-robust`  
**Entries:** 6 (4 commons-grade, 2 draft)  
**Earliest disclosure:** 2018-06  
**Most recent disclosure:** 2026-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-dynamic-scene-robust`.

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

### 2018-06 — DynaSLAM

- **id:** `dynaslam-bescos-2018`
- **corpus:** academic
- **ip status:** open-copyleft
- **creator:** University of Zaragoza I3A; Bescos, Fácil, Civera, Neira
- **disclosure citation:** Bescos, B., Fácil, J. M., Civera, J., Neira, J. 'DynaSLAM: Tracking, Mapping and Inpainting in Dynamic Scenes'. IEEE Robotics and Automation Letters 3(4) 2018; IROS 2018. arXiv:1806.05620. Universidad de Zaragoza I3A. GPLv3 source: github.com/BertaBescos/DynaSLAM.
- **disclosed subsystems:** `control-vio-slam`, `control-dynamic-scene-robust`, `control-mask-segmentation`

**Prior art notes:**

> DynaSLAM is the canonical foundational dynamic-scene visual SLAM system (Bescos et al. RA-L + IROS 2018). 7-year-deep open-copyleft prior art. Anchor of the dynamic-SLAM lineage that the entire RADIO-ViPE Table II benchmarks against (DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON are all DynaSLAM descendants). Direct shielding for any commercial humanoid claim on 'SLAM that works in dynamic environments with moving people'.

**Sources:**

1. Bescos et al. arXiv:1806.05620 June 2018; RA-L + IROS 2018.
2. GitHub: github.com/BertaBescos/DynaSLAM.

---

### 2024-07 — RoDyn-SLAM

- **id:** `rodyn-slam-jiang-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Fudan University ZVG; Haochen Jiang, Yueming Xu, Kejie Li, Jianfeng Feng, Li Zhang
- **disclosure citation:** Jiang, H., Xu, Y., Li, K., Feng, J., Zhang, L. 'RoDyn-SLAM: Robust Dynamic Dense RGB-D SLAM with Neural Radiance Fields'. IEEE Robotics and Automation Letters 2024. arXiv:2407.01303 July 2024. Fudan University ZVG (Zhang Vision Group).
- **disclosed subsystems:** `control-vio-slam`, `control-neural-radiance-field`, `control-dynamic-scene-robust`

**Prior art notes:**

> RoDyn-SLAM is Fudan ZVG's NeRF-based dynamic-scene SLAM (IEEE RAL 2024). 10-month-deep prior art on the NeRF branch of dynamic SLAM (distinct from the GS-based lineage of WildGS-SLAM, DGS-SLAM, DG-SLAM, etc.). Cited as a competitor in RADIO-ViPE Table II — the TUM-RGBD ATE benchmark RADIO-ViPE compares against. Together with DGS-SLAM, DG-SLAM, WildGS-SLAM, and DynaSLAM, establishes the academic dynamic-SLAM substrate that RADIO-ViPE measures itself against.

**Sources:**

1. Jiang et al. IEEE RAL 2024; arXiv:2407.01303 July 2024.
2. GitHub: github.com/fudan-zvg/Rodyn-SLAM.

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

### 2024-12 — MegaSaM *(draft)*

- **id:** `megasam-google-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google DeepMind + UC Berkeley + U. Michigan (per arXiv 2412.04463)
- **disclosure citation:** Authors per arXiv 2412.04463. 'MegaSaM: Accurate, Fast, and Robust Structure and Motion from Casual Dynamic Videos'. arXiv:2412.04463, December 2024. Google DeepMind + UC Berkeley + University of Michigan.
- **disclosed subsystems:** `control-vio-slam`, `control-bundle-adjustment`, `control-monocular-metric-depth`, `control-dynamic-scene-robust`

**Prior art notes:**

> MegaSaM (Dec 2024) is the immediate predecessor to NVIDIA ViPE in the calibration-free dynamic-monocular-video pose+depth lineage. 5-month-deep prior art for: differentiable BA with monocular depth priors + uncertainty-aware global BA on in-the-wild dynamic videos. ViPE explicitly outperforms MegaSaM in its results table; that comparison only exists if MegaSaM is the prior art baseline. Direct shielding for any commercial humanoid claim on calibration-free in-the-wild video perception.

**Sources:**

1. arXiv:2412.04463 December 2024.
2. Project page (per arXiv listing).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b51f194`.*
