---
title: control-bundle-adjustment
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-bundle-adjustment`

**5 corpus entries disclose this subsystem.**

Earliest disclosure: 2021-04

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## ORB-SLAM3 (2021-04)

- **id**: `orb-slam3-2021`
- **corpus**: academic
- **creator**: University of Zaragoza I3A; Carlos Campos, Juan Tardós et al.
- **disclosure**: Campos, C., Elvira, R., Rodríguez, J. J. G., Montiel, J. M. M., Tardós, J. D. 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM'. IEEE Transactions on Robotics 37(6) December 2021, pp. 1874-1890. arXiv:2007.11898. GPLv3 source: github.com/UZ-SLAMLab/ORB_SLAM3. University of Zaragoza.
- **ip status**: open-copyleft
- **prior art notes**: ORB-SLAM3 is the canonical academic visual-inertial SLAM library and 5-year-deep open-source baseline. Heavily-cited (>3000 citations). Anticipates: (1) monocular/stereo/RGB-D + IMU fusion in a unified factor-graph framework, (2) multi-map operation across sessions for long-term autonomy, (3) bag-of-words place recognition for loop closure. Establishes the geometric-only SLAM baseline that semantic/open-vocab SLAM systems (including RADIO-ViPE, round-10 entry) extend. Any humanoid platform claim on visual-inertial SLAM faces this lineage.

## DROID-SLAM (2021-12)

- **id**: `droid-slam-2021`
- **corpus**: academic
- **creator**: Princeton Vision and Learning Lab; Zachary Teed, Jia Deng
- **disclosure**: Teed, Z., Deng, J. 'DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras'. NeurIPS 2021. arXiv:2108.10869. BSD-3-Clause source: github.com/princeton-vl/DROID-SLAM. Princeton Vision and Learning Lab.
- **ip status**: open-permissive
- **prior art notes**: DROID-SLAM is the canonical dense differentiable-visual-SLAM academic system (NeurIPS 2021, BSD-3 open source). 4-year-deep prior art anticipating any humanoid claim on dense / differentiable / foundation-model-grounded visual SLAM. Immediate ancestor of ViPE (Princeton 2024-2025) and RADIO-ViPE (ITMO 2026 — round-10 entry). Together with ORB-SLAM3, establishes the academic SLAM baseline against which all modern humanoid perception claims must be evaluated.

## MegaSaM (2024-12)

- **id**: `megasam-google-2024`
- **corpus**: academic
- **creator**: Google DeepMind + UC Berkeley + U. Michigan (per arXiv 2412.04463)
- **disclosure**: Authors per arXiv 2412.04463. 'MegaSaM: Accurate, Fast, and Robust Structure and Motion from Casual Dynamic Videos'. arXiv:2412.04463, December 2024. Google DeepMind + UC Berkeley + University of Michigan.
- **ip status**: open-permissive
- **prior art notes**: MegaSaM (Dec 2024) is the immediate predecessor to NVIDIA ViPE in the calibration-free dynamic-monocular-video pose+depth lineage. 5-month-deep prior art for: differentiable BA with monocular depth priors + uncertainty-aware global BA on in-the-wild dynamic videos. ViPE explicitly outperforms MegaSaM in its results table; that comparison only exists if MegaSaM is the prior art baseline. Direct shielding for any commercial humanoid claim on calibration-free in-the-wild video perception.

## ViPE (Video Pose Engine) (2025-08)

- **id**: `nvidia-vipe-2025`
- **corpus**: academic
- **creator**: NVIDIA Toronto AI Lab (nv-tlabs); multi-author
- **disclosure**: Huang, J., et al. (NVIDIA Toronto AI Lab + collaborators). 'ViPE: Video Pose Engine for 3D Geometric Perception'. arXiv:2508.10934, August 2025. Open-source release via nv-tlabs/vipe.
- **ip status**: open-permissive
- **prior art notes**: ViPE is NVIDIA Toronto AI Lab's canonical Video Pose Engine, August 2025 arXiv. Sits **directly between DROID-SLAM (2021) and RADIO-ViPE (2026)** in the visual-SLAM lineage: it is RADIO-ViPE's explicit foundation per the round-10 paper's text ('we build upon ViPE [5]'). 9-month-deep open-permissive academic prior art for: calibration-free metric depth from uncalibrated video, dense bundle adjustment over heterogeneous camera models, online video pose estimation at 3-5 FPS. Direct shielding for any commercial humanoid claim on uncalibrated-camera onboard 3D perception. Plus the 96M-frame released dataset is itself prior art for any humanoid-vision data-curation IP.

## RADIO-ViPE (2026-04)

- **id**: `radio-vipe-itmo-2026`
- **corpus**: academic
- **creator**: ITMO University BE2R Lab; Nasser, Iumanov, Li, Popov, Mahmoud, Kolyubin
- **disclosure**: Nasser, Z., Iumanov, M., Li, T., Popov, M., Mahmoud, J., Kolyubin, S. 'RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM in Dynamic Environments'. arXiv:2604.26067v1, April 28, 2026. ITMO University, Biomechatronics and Energy-Efficient Robotics (BE2R) Lab, Saint Petersburg, Russia.
- **ip status**: open-permissive
- **prior art notes**: RADIO-ViPE is the most recent and architecturally complete online open-vocabulary semantic SLAM system. April 2026 arXiv preprint; 9 days before this corpus entry. Establishes very-recent (sub-1-week) open-academic prior art for: calibration-free monocular semantic SLAM, tightly-coupled multi-modal fusion (RADIO + SigLIP + geometric BA), adaptive-kernel dynamic-scene robustness, online operation at 8-10 FPS. Directly shields any commercial humanoid claim on: 'onboard semantic scene understanding from monocular video' (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo, etc. all face this), 'language-grounded robotic perception in dynamic environments', 'calibration-free humanoid camera deployment'. The TUM-RGBD ATE comparison table in Table II of the paper enumerates the prior art — RADIO-ViPE outperforms Dyna-SLAM, DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON, ViPE — every one of which is itself open-academic prior art for humanoid perception. Lineage: ORB-SLAM3 (geometric baseline) → DROID-SLAM (dense differentiable) → ViPE (Princeton in-the-wild metric depth) → RADIO-ViPE (ITMO open-vocab + calibration-free).
