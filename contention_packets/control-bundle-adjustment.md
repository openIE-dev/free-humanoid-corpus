---
title: "control-bundle-adjustment"
parent: "Invalidity Contentions"
nav_order: 46
layout: default
---

# Invalidity Contention Packet — `control-bundle-adjustment`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-bundle-adjustment`  
**Entries:** 5 (4 commons-grade, 1 draft)  
**Earliest disclosure:** 2021-04  
**Most recent disclosure:** 2026-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-bundle-adjustment`.

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

### 2021-04 — ORB-SLAM3

- **id:** `orb-slam3-2021`
- **corpus:** academic
- **ip status:** open-copyleft
- **creator:** University of Zaragoza I3A; Carlos Campos, Juan Tardós et al.
- **disclosure citation:** Campos, C., Elvira, R., Rodríguez, J. J. G., Montiel, J. M. M., Tardós, J. D. 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM'. IEEE Transactions on Robotics 37(6) December 2021, pp. 1874-1890. arXiv:2007.11898. GPLv3 source: github.com/UZ-SLAMLab/ORB_SLAM3. University of Zaragoza.
- **disclosed subsystems:** `control-vio-slam`, `control-bundle-adjustment`, `control-place-recognition`

**Prior art notes:**

> ORB-SLAM3 is the canonical academic visual-inertial SLAM library and 5-year-deep open-source baseline. Heavily-cited (>3000 citations). Anticipates: (1) monocular/stereo/RGB-D + IMU fusion in a unified factor-graph framework, (2) multi-map operation across sessions for long-term autonomy, (3) bag-of-words place recognition for loop closure. Establishes the geometric-only SLAM baseline that semantic/open-vocab SLAM systems (including RADIO-ViPE, round-10 entry) extend. Any humanoid platform claim on visual-inertial SLAM faces this lineage.

**Sources:**

1. Campos et al. IEEE T-RO 37(6) 2021.
2. ORB-SLAM3 GitHub (github.com/UZ-SLAMLab/ORB_SLAM3) GPLv3.
3. ORB-SLAM lineage: Mur-Artal/Tardós ORB-SLAM (2015), ORB-SLAM2 (2017).

---

### 2021-12 — DROID-SLAM

- **id:** `droid-slam-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Princeton Vision and Learning Lab; Zachary Teed, Jia Deng
- **disclosure citation:** Teed, Z., Deng, J. 'DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras'. NeurIPS 2021. arXiv:2108.10869. BSD-3-Clause source: github.com/princeton-vl/DROID-SLAM. Princeton Vision and Learning Lab.
- **disclosed subsystems:** `control-vio-slam`, `control-bundle-adjustment`, `control-differentiable-slam`

**Prior art notes:**

> DROID-SLAM is the canonical dense differentiable-visual-SLAM academic system (NeurIPS 2021, BSD-3 open source). 4-year-deep prior art anticipating any humanoid claim on dense / differentiable / foundation-model-grounded visual SLAM. Immediate ancestor of ViPE (Princeton 2024-2025) and RADIO-ViPE (ITMO 2026 — round-10 entry). Together with ORB-SLAM3, establishes the academic SLAM baseline against which all modern humanoid perception claims must be evaluated.

**Sources:**

1. Teed, Z., Deng, J. NeurIPS 2021.
2. DROID-SLAM GitHub (github.com/princeton-vl/DROID-SLAM) BSD-3-Clause.
3. Predecessor: RAFT (Teed/Deng ECCV 2020) for optical flow.

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

### 2025-08 — ViPE (Video Pose Engine)

- **id:** `nvidia-vipe-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA Toronto AI Lab (nv-tlabs); multi-author
- **disclosure citation:** Huang, J., et al. (NVIDIA Toronto AI Lab + collaborators). 'ViPE: Video Pose Engine for 3D Geometric Perception'. arXiv:2508.10934, August 2025. Open-source release via nv-tlabs/vipe.
- **disclosed subsystems:** `control-vio-slam`, `control-bundle-adjustment`, `control-monocular-metric-depth`, `control-uncalibrated-video-perception`

**Prior art notes:**

> ViPE is NVIDIA Toronto AI Lab's canonical Video Pose Engine, August 2025 arXiv. Sits **directly between DROID-SLAM (2021) and RADIO-ViPE (2026)** in the visual-SLAM lineage: it is RADIO-ViPE's explicit foundation per the round-10 paper's text ('we build upon ViPE [5]'). 9-month-deep open-permissive academic prior art for: calibration-free metric depth from uncalibrated video, dense bundle adjustment over heterogeneous camera models, online video pose estimation at 3-5 FPS. Direct shielding for any commercial humanoid claim on uncalibrated-camera onboard 3D perception. Plus the 96M-frame released dataset is itself prior art for any humanoid-vision data-curation IP.

**Sources:**

1. arXiv:2508.10934 August 2025.
2. GitHub: github.com/nv-tlabs/vipe.
3. HuggingFace paper page (huggingface.co/papers/2508.10934).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2aee416`.*
