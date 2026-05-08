---
title: control-uncalibrated-video-perception
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-uncalibrated-video-perception`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2023-12

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DUSt3R (2023-12)

- **id**: `dust3r-naver-cvpr-2024`
- **corpus**: academic
- **creator**: NAVER LABS Europe + Aalto University; Shuzhe Wang, Vincent Leroy, Yohann Cabon, Boris Chidlovskii, Jerome Revaud
- **disclosure**: Wang, S., Leroy, V., Cabon, Y., Chidlovskii, B., Revaud, J. 'DUSt3R: Geometric 3D Vision Made Easy'. CVPR 2024. arXiv:2312.14132. NAVER LABS Europe + Aalto University.
- **ip status**: open-permissive
- **prior art notes**: DUSt3R (Wang et al. CVPR 2024) is the foundational pose-free unconstrained 3D-reconstruction paper. 2-year-deep open-permissive prior art. **Direct architectural ancestor of MASt3R** (round-28 entry below), **VGGT** (in audit, round-corpus VGGT), **MegaSaM** (round-13), **NVIDIA ViPE** (round-11), **RADIO-ViPE** (round-10). The 2-year-deep DUSt3R-derived calibration-free reconstruction chain shields any commercial humanoid claim on uncalibrated-camera onboard 3D reconstruction.

## ViPE (Video Pose Engine) (2025-08)

- **id**: `nvidia-vipe-2025`
- **corpus**: academic
- **creator**: NVIDIA Toronto AI Lab (nv-tlabs); multi-author
- **disclosure**: Huang, J., et al. (NVIDIA Toronto AI Lab + collaborators). 'ViPE: Video Pose Engine for 3D Geometric Perception'. arXiv:2508.10934, August 2025. Open-source release via nv-tlabs/vipe.
- **ip status**: open-permissive
- **prior art notes**: ViPE is NVIDIA Toronto AI Lab's canonical Video Pose Engine, August 2025 arXiv. Sits **directly between DROID-SLAM (2021) and RADIO-ViPE (2026)** in the visual-SLAM lineage: it is RADIO-ViPE's explicit foundation per the round-10 paper's text ('we build upon ViPE [5]'). 9-month-deep open-permissive academic prior art for: calibration-free metric depth from uncalibrated video, dense bundle adjustment over heterogeneous camera models, online video pose estimation at 3-5 FPS. Direct shielding for any commercial humanoid claim on uncalibrated-camera onboard 3D perception. Plus the 96M-frame released dataset is itself prior art for any humanoid-vision data-curation IP.
