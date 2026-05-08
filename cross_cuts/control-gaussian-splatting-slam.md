---
title: control-gaussian-splatting-slam
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-gaussian-splatting-slam`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 2024-03

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## SemGauss-SLAM (2024-03)

- **id**: `semgauss-slam-2024`
- **corpus**: academic
- **creator**: Zhu, Siting et al. (per arXiv 2403.07494)
- **disclosure**: Zhu, S., et al. 'SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM'. arXiv:2403.07494, March 2024.
- **ip status**: open-permissive
- **prior art notes**: SemGauss-SLAM is one of the first dense-semantic Gaussian-splatting SLAM systems (March 2024). 14-month-deep prior art for combining 3D Gaussian representations with per-primitive semantic features. Predates and informs the open-vocabulary GS-SLAM lineage that WildGS-SLAM, LEG-SLAM, LEGO-SLAM, and RADIO-ViPE descend from.

## LEGS (Language-Embedded Gaussian Splats) (2024-09)

- **id**: `legs-berkeley-2024`
- **corpus**: academic
- **creator**: UC Berkeley AUTOLab; Goldberg group
- **disclosure**: Yu, J., et al. 'LEGS: Language-Embedded Gaussian Splats — Incrementally Building Room-Scale Representations with a Mobile Robot'. IROS 2024. arXiv:2409.18108. UC Berkeley AUTOLab.
- **ip status**: open-permissive
- **prior art notes**: LEGS is the canonical Berkeley AUTOLab open-vocabulary Gaussian-splatting representation (IROS 2024). 1.5-year-deep prior art for: CLIP-aligned per-primitive features in 3DGS, incremental room-scale construction by mobile robot, language-grounded mobile-manipulation scene representations. Predates and informs LEG-SLAM, LEGO-SLAM, and any commercial humanoid claim on language-queryable 3D scene maps built onboard.

## DGS-SLAM (2024-11)

- **id**: `dgs-slam-kong-2024`
- **corpus**: academic
- **creator**: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim (per arXiv 2411.10722)
- **disclosure**: Kong, M., Lee, J., Lee, S., Kim, E. 'DGS-SLAM: Gaussian Splatting SLAM in Dynamic Environment'. arXiv:2411.10722, November 2024.
- **ip status**: open-permissive
- **prior art notes**: DGS-SLAM (Kong et al. arXiv 2411.10722, November 2024). 6-month-deep prior art on dynamic-aware Gaussian-splatting SLAM. Cited as a competitor in the RADIO-ViPE Table II TUM-RGBD ATE benchmark; the round-10 RADIO-ViPE entry's claim of SOTA is anchored by comparison against this and several sibling systems. Direct shielding for any commercial humanoid claim on dynamic-scene GS-SLAM.

## WildGS-SLAM (2025-04)

- **id**: `wildgs-slam-2025`
- **corpus**: academic
- **creator**: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys (ETH Zürich), Songyou Peng, Iro Armeni (Stanford GradientSpaces)
- **disclosure**: Zheng, J., Zhu, Z., Bieri, V., Pollefeys, M., Peng, S., Armeni, I. 'WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments'. CVPR 2025. arXiv:2504.03886. ETH Zürich + Stanford GradientSpaces.
- **ip status**: open-permissive
- **prior art notes**: WildGS-SLAM is the canonical CVPR 2025 monocular dynamic-scene Gaussian-splatting SLAM system from ETH + Stanford. Establishes 1-year-deep prior art for: monocular GS-SLAM with dynamic-scene robustness, photorealistic novel-view rendering of static background while filtering dynamic foreground. Among the systems RADIO-ViPE benchmarks against (TUM-RGBD dynamic). Direct shielding for any commercial humanoid claim on monocular dynamic-scene mapping with photorealistic reconstruction.

## LEG-SLAM (2025-06)

- **id**: `leg-slam-2025`
- **corpus**: academic
- **creator**: LEG-SLAM authors (per arXiv 2506.03073)
- **disclosure**: Authors per arXiv 2506.03073. 'LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM'. arXiv:2506.03073, June 2025.
- **ip status**: open-permissive
- **prior art notes**: LEG-SLAM (June 2025) is a real-time language-enhanced GS-SLAM system. 11-month-deep prior art on: real-time fps-class language-aligned GS-SLAM, DINOv2 feature compression for compact per-Gaussian language encoding. Distinct from but contemporary with LEGO-SLAM (Nov 2025). Both feed the open-vocab GS-SLAM lineage that RADIO-ViPE compares against.

## LEGO-SLAM (2025-11)

- **id**: `lego-slam-2025`
- **corpus**: academic
- **creator**: Lab of AI and Robotics (per github.com/Lab-of-AI-and-Robotics/LEGO-SLAM)
- **disclosure**: Authors per arXiv 2511.16144. 'LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM'. arXiv:2511.16144, November 2025. Lab of AI and Robotics.
- **ip status**: open-permissive
- **prior art notes**: LEGO-SLAM (Nov 2025) is the first claimed real-time open-vocabulary GS-SLAM system. 6-month-deep prior art for: 16-dim language-feature compression in GS, language-guided Gaussian pruning. Direct shielding for any commercial humanoid claim on real-time onboard open-vocabulary scene mapping. Together with LEG-SLAM, LEGS, and SemGauss-SLAM, the open-vocab GS-SLAM corpus is now ~6-month to 14-month deep across five contemporary systems — fully covering the architectural surface of RADIO-ViPE's competitor table.
