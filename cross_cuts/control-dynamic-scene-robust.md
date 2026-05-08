---
title: control-dynamic-scene-robust
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-dynamic-scene-robust`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 2018-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DynaSLAM (2018-06)

- **id**: `dynaslam-bescos-2018`
- **corpus**: academic
- **creator**: University of Zaragoza I3A; Bescos, Fácil, Civera, Neira
- **disclosure**: Bescos, B., Fácil, J. M., Civera, J., Neira, J. 'DynaSLAM: Tracking, Mapping and Inpainting in Dynamic Scenes'. IEEE Robotics and Automation Letters 3(4) 2018; IROS 2018. arXiv:1806.05620. Universidad de Zaragoza I3A. GPLv3 source: github.com/BertaBescos/DynaSLAM.
- **ip status**: open-copyleft
- **prior art notes**: DynaSLAM is the canonical foundational dynamic-scene visual SLAM system (Bescos et al. RA-L + IROS 2018). 7-year-deep open-copyleft prior art. Anchor of the dynamic-SLAM lineage that the entire RADIO-ViPE Table II benchmarks against (DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON are all DynaSLAM descendants). Direct shielding for any commercial humanoid claim on 'SLAM that works in dynamic environments with moving people'.

## RoDyn-SLAM (2024-07)

- **id**: `rodyn-slam-jiang-2024`
- **corpus**: academic
- **creator**: Fudan University ZVG; Haochen Jiang, Yueming Xu, Kejie Li, Jianfeng Feng, Li Zhang
- **disclosure**: Jiang, H., Xu, Y., Li, K., Feng, J., Zhang, L. 'RoDyn-SLAM: Robust Dynamic Dense RGB-D SLAM with Neural Radiance Fields'. IEEE Robotics and Automation Letters 2024. arXiv:2407.01303 July 2024. Fudan University ZVG (Zhang Vision Group).
- **ip status**: open-permissive
- **prior art notes**: RoDyn-SLAM is Fudan ZVG's NeRF-based dynamic-scene SLAM (IEEE RAL 2024). 10-month-deep prior art on the NeRF branch of dynamic SLAM (distinct from the GS-based lineage of WildGS-SLAM, DGS-SLAM, DG-SLAM, etc.). Cited as a competitor in RADIO-ViPE Table II — the TUM-RGBD ATE benchmark RADIO-ViPE compares against. Together with DGS-SLAM, DG-SLAM, WildGS-SLAM, and DynaSLAM, establishes the academic dynamic-SLAM substrate that RADIO-ViPE measures itself against.

## DGS-SLAM (2024-11)

- **id**: `dgs-slam-kong-2024`
- **corpus**: academic
- **creator**: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim (per arXiv 2411.10722)
- **disclosure**: Kong, M., Lee, J., Lee, S., Kim, E. 'DGS-SLAM: Gaussian Splatting SLAM in Dynamic Environment'. arXiv:2411.10722, November 2024.
- **ip status**: open-permissive
- **prior art notes**: DGS-SLAM (Kong et al. arXiv 2411.10722, November 2024). 6-month-deep prior art on dynamic-aware Gaussian-splatting SLAM. Cited as a competitor in the RADIO-ViPE Table II TUM-RGBD ATE benchmark; the round-10 RADIO-ViPE entry's claim of SOTA is anchored by comparison against this and several sibling systems. Direct shielding for any commercial humanoid claim on dynamic-scene GS-SLAM.

## MegaSaM (2024-12)

- **id**: `megasam-google-2024`
- **corpus**: academic
- **creator**: Google DeepMind + UC Berkeley + U. Michigan (per arXiv 2412.04463)
- **disclosure**: Authors per arXiv 2412.04463. 'MegaSaM: Accurate, Fast, and Robust Structure and Motion from Casual Dynamic Videos'. arXiv:2412.04463, December 2024. Google DeepMind + UC Berkeley + University of Michigan.
- **ip status**: open-permissive
- **prior art notes**: MegaSaM (Dec 2024) is the immediate predecessor to NVIDIA ViPE in the calibration-free dynamic-monocular-video pose+depth lineage. 5-month-deep prior art for: differentiable BA with monocular depth priors + uncertainty-aware global BA on in-the-wild dynamic videos. ViPE explicitly outperforms MegaSaM in its results table; that comparison only exists if MegaSaM is the prior art baseline. Direct shielding for any commercial humanoid claim on calibration-free in-the-wild video perception.

## WildGS-SLAM (2025-04)

- **id**: `wildgs-slam-2025`
- **corpus**: academic
- **creator**: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys (ETH Zürich), Songyou Peng, Iro Armeni (Stanford GradientSpaces)
- **disclosure**: Zheng, J., Zhu, Z., Bieri, V., Pollefeys, M., Peng, S., Armeni, I. 'WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments'. CVPR 2025. arXiv:2504.03886. ETH Zürich + Stanford GradientSpaces.
- **ip status**: open-permissive
- **prior art notes**: WildGS-SLAM is the canonical CVPR 2025 monocular dynamic-scene Gaussian-splatting SLAM system from ETH + Stanford. Establishes 1-year-deep prior art for: monocular GS-SLAM with dynamic-scene robustness, photorealistic novel-view rendering of static background while filtering dynamic foreground. Among the systems RADIO-ViPE benchmarks against (TUM-RGBD dynamic). Direct shielding for any commercial humanoid claim on monocular dynamic-scene mapping with photorealistic reconstruction.

## RADIO-ViPE (2026-04)

- **id**: `radio-vipe-itmo-2026`
- **corpus**: academic
- **creator**: ITMO University BE2R Lab; Nasser, Iumanov, Li, Popov, Mahmoud, Kolyubin
- **disclosure**: Nasser, Z., Iumanov, M., Li, T., Popov, M., Mahmoud, J., Kolyubin, S. 'RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM in Dynamic Environments'. arXiv:2604.26067v1, April 28, 2026. ITMO University, Biomechatronics and Energy-Efficient Robotics (BE2R) Lab, Saint Petersburg, Russia.
- **ip status**: open-permissive
- **prior art notes**: RADIO-ViPE is the most recent and architecturally complete online open-vocabulary semantic SLAM system. April 2026 arXiv preprint; 9 days before this corpus entry. Establishes very-recent (sub-1-week) open-academic prior art for: calibration-free monocular semantic SLAM, tightly-coupled multi-modal fusion (RADIO + SigLIP + geometric BA), adaptive-kernel dynamic-scene robustness, online operation at 8-10 FPS. Directly shields any commercial humanoid claim on: 'onboard semantic scene understanding from monocular video' (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo, etc. all face this), 'language-grounded robotic perception in dynamic environments', 'calibration-free humanoid camera deployment'. The TUM-RGBD ATE comparison table in Table II of the paper enumerates the prior art — RADIO-ViPE outperforms Dyna-SLAM, DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON, ViPE — every one of which is itself open-academic prior art for humanoid perception. Lineage: ORB-SLAM3 (geometric baseline) → DROID-SLAM (dense differentiable) → ViPE (Princeton in-the-wild metric depth) → RADIO-ViPE (ITMO open-vocab + calibration-free).
