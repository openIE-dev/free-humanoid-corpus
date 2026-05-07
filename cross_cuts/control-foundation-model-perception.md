---
title: control-foundation-model-perception
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-foundation-model-perception`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 2023-03

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## SigLIP (2023-03)

- **id**: `siglip-zhai-2023`
- **corpus**: academic
- **creator**: Google Research; Zhai, Mustafa, Kolesnikov, Beyer
- **disclosure**: Zhai, X., Mustafa, B., Kolesnikov, A., Beyer, L. 'Sigmoid Loss for Language Image Pre-Training'. arXiv:2303.15343, March 2023. ICCV 2023. Google Research.
- **ip status**: open-permissive
- **prior art notes**: SigLIP is the canonical sigmoid-loss vision-language foundation model (Google ICCV 2023). 2-year-deep prior art for: sigmoid-loss contrastive vision-language training, large-batch-friendly training regime. The text-encoder backbone in OpenVLA, RADIO-ViPE, and many VLA systems. Direct shielding for any commercial humanoid claim on open-vocabulary text-image alignment for instruction following.

## LERF (Language Embedded Radiance Fields) (2023-03)

- **id**: `lerf-kerr-2023`
- **corpus**: academic
- **creator**: UC Berkeley AUTOLab + BAIR; Kerr, Kim, Goldberg, Kanazawa, Tancik
- **disclosure**: Kerr, J., Kim, C. M., Goldberg, K., Kanazawa, A., Tancik, M. 'LERF: Language Embedded Radiance Fields'. arXiv:2303.09553, March 2023. ICCV 2023 (Oral). UC Berkeley AUTOLab + Berkeley AI Research.
- **ip status**: open-permissive
- **prior art notes**: LERF is the canonical first language-embedded NeRF (Berkeley + BAIR, ICCV 2023 Oral). 2-year-deep prior art for: CLIP-embedded 3D radiance fields, open-vocabulary natural-language 3D scene queries. The architectural ancestor of LEGS (round-12), LEG-SLAM (round-12), LEGO-SLAM (round-12), and any commercial claim on language-queryable 3D scene representations. Predates the Gaussian-splatting instantiations and establishes the architectural pattern.

## DINOv2 (2023-04)

- **id**: `dinov2-oquab-2023`
- **corpus**: academic
- **creator**: Meta AI Research (FAIR); Oquab, Darcet, Moutakanni et al.
- **disclosure**: Oquab, M., Darcet, T., Moutakanni, T., Vo, H., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., et al. 'DINOv2: Learning Robust Visual Features without Supervision'. arXiv:2304.07193, April 2023. Meta AI Research (FAIR). Apache-2.0 release.
- **ip status**: open-permissive
- **prior art notes**: DINOv2 is the canonical Meta self-supervised vision foundation model (April 2023). 2-year-deep open-permissive prior art for: self-supervised dense visual features at scale, ViT-g-class image encoders for robotics. The vision encoder in OpenVLA, LEG-SLAM, and many other systems in the corpus. Direct shielding for any commercial humanoid claim on self-supervised onboard visual feature learning.

## AM-RADIO (NVIDIA) (2023-12)

- **id**: `nvidia-am-radio-2024`
- **corpus**: academic
- **creator**: NVIDIA Learning and Perception Research; Ranzinger, Heinrich, Kautz, Molchanov
- **disclosure**: Ranzinger, M., Heinrich, G., Kautz, J., Molchanov, P. 'AM-RADIO: Agglomerative Vision Foundation Model -- Reduce All Domains Into One'. arXiv:2312.06709, December 2023. CVPR 2024. NVIDIA Learning and Perception Research. RADIOv2.5 follow-up: arXiv:2412.07679 December 2024.
- **ip status**: open-permissive
- **prior art notes**: AM-RADIO is the canonical agglomerative-distillation vision foundation model (NVIDIA, CVPR 2024). 1.5-year-deep open-permissive prior art for: multi-teacher vision-foundation distillation, single-backbone CLIP+DINOv2+SAM amalgamation. **The literal embedding substrate of RADIO-ViPE** — the round-10 RADIO-ViPE entry's name comes from this. Direct shielding for any commercial humanoid claim on multi-modal vision-foundation backbones for onboard perception.

## LEGS (Language-Embedded Gaussian Splats) (2024-09)

- **id**: `legs-berkeley-2024`
- **corpus**: academic
- **creator**: UC Berkeley AUTOLab; Goldberg group
- **disclosure**: Yu, J., et al. 'LEGS: Language-Embedded Gaussian Splats — Incrementally Building Room-Scale Representations with a Mobile Robot'. IROS 2024. arXiv:2409.18108. UC Berkeley AUTOLab.
- **ip status**: open-permissive
- **prior art notes**: LEGS is the canonical Berkeley AUTOLab open-vocabulary Gaussian-splatting representation (IROS 2024). 1.5-year-deep prior art for: CLIP-aligned per-primitive features in 3DGS, incremental room-scale construction by mobile robot, language-grounded mobile-manipulation scene representations. Predates and informs LEG-SLAM, LEGO-SLAM, and any commercial humanoid claim on language-queryable 3D scene maps built onboard.

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

## RADIO-ViPE (2026-04)

- **id**: `radio-vipe-itmo-2026`
- **corpus**: academic
- **creator**: ITMO University BE2R Lab; Nasser, Iumanov, Li, Popov, Mahmoud, Kolyubin
- **disclosure**: Nasser, Z., Iumanov, M., Li, T., Popov, M., Mahmoud, J., Kolyubin, S. 'RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM in Dynamic Environments'. arXiv:2604.26067v1, April 28, 2026. ITMO University, Biomechatronics and Energy-Efficient Robotics (BE2R) Lab, Saint Petersburg, Russia.
- **ip status**: open-permissive
- **prior art notes**: RADIO-ViPE is the most recent and architecturally complete online open-vocabulary semantic SLAM system. April 2026 arXiv preprint; 9 days before this corpus entry. Establishes very-recent (sub-1-week) open-academic prior art for: calibration-free monocular semantic SLAM, tightly-coupled multi-modal fusion (RADIO + SigLIP + geometric BA), adaptive-kernel dynamic-scene robustness, online operation at 8-10 FPS. Directly shields any commercial humanoid claim on: 'onboard semantic scene understanding from monocular video' (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo, etc. all face this), 'language-grounded robotic perception in dynamic environments', 'calibration-free humanoid camera deployment'. The TUM-RGBD ATE comparison table in Table II of the paper enumerates the prior art — RADIO-ViPE outperforms Dyna-SLAM, DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON, ViPE — every one of which is itself open-academic prior art for humanoid perception. Lineage: ORB-SLAM3 (geometric baseline) → DROID-SLAM (dense differentiable) → ViPE (Princeton in-the-wild metric depth) → RADIO-ViPE (ITMO open-vocab + calibration-free).
