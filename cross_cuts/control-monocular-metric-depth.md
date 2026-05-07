---
title: control-monocular-metric-depth
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-monocular-metric-depth`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2024-12

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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
