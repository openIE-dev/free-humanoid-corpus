---
title: control-dynamic-scene-robust
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-dynamic-scene-robust`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2025-04

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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
