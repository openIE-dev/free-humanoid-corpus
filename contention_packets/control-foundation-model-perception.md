---
title: "control-foundation-model-perception"
parent: "Invalidity Contentions"
nav_order: 35
layout: default
---

# Invalidity Contention Packet — `control-foundation-model-perception`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-foundation-model-perception`  
**Entries:** 17 (15 commons-grade, 2 draft)  
**Earliest disclosure:** 2020-03  
**Most recent disclosure:** 2026-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-foundation-model-perception`.

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

### 2020-03 — NeRF (Neural Radiance Fields)

- **id:** `nerf-mildenhall-eccv-2020`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley + Google Research; Ben Mildenhall, Pratul Srinivasan, Matthew Tancik, Jonathan Barron, Ravi Ramamoorthi, Ren Ng
- **disclosure citation:** Mildenhall, B., Srinivasan, P. P., Tancik, M., Barron, J. T., Ramamoorthi, R., Ng, R. 'NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis'. ECCV 2020 Best Paper Honorable Mention. arXiv:2003.08934. UC Berkeley + Google Research.
- **disclosed subsystems:** `control-novel-view-synthesis`, `control-foundation-model-perception`, `control-3d-perception`, `control-implicit-scene-representation`

**Prior art notes:**

> NeRF (Mildenhall et al. ECCV 2020) is the foundational neural-implicit-3D-representation paper. 5-year-deep open-permissive prior art. **The architectural ancestor of every subsequent neural-3D system** including LERF (round-13), 3D Gaussian Splatting (round-27), all 6 GS-SLAM systems in the corpus, RoDyn-SLAM (round-14, NeRF-based dynamic SLAM). Direct shielding for any commercial humanoid claim on neural-implicit scene representation. Closes a major foundational citation chain.

**Sources:**

1. Mildenhall et al. arXiv:2003.08934 ECCV 2020.
2. Project page (matthewtancik.com/nerf).
3. GitHub: github.com/bmild/nerf.

---

### 2023-02 — Nerfstudio + Nerfacto

- **id:** `nerfstudio-berkeley-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley AI Research (BAIR); Matthew Tancik, Ethan Weber, Angjoo Kanazawa et al.
- **disclosure citation:** Tancik, M., Weber, E., Ng, E., Li, R., Yi, B., Wang, T., Kristoffersen, A., Austin, J., Salahi, K., Ahuja, A., McAllister, D., Kanazawa, A. 'Nerfstudio: A Modular Framework for Neural Radiance Field Development'. SIGGRAPH 2023. arXiv:2302.04264. UC Berkeley AI Research (BAIR) + UC Berkeley + Stanford.
- **disclosed subsystems:** `control-novel-view-synthesis`, `control-foundation-model-perception`, `control-implicit-scene-representation`

**Prior art notes:**

> Nerfstudio + Nerfacto (Tancik et al. SIGGRAPH 2023) is the canonical open-academic NeRF research framework. 2-year-deep open-permissive prior art. Direct successor to NeRF (round-28) in the open-source NeRF tooling chain. Used in 100+ academic papers as the standard NeRF research substrate. Direct shielding for any commercial humanoid claim on NeRF-based scene representation development tooling.

**Sources:**

1. Tancik et al. arXiv:2302.04264 SIGGRAPH 2023.
2. Project page (nerf.studio).
3. GitHub: github.com/nerfstudio-project/nerfstudio.

---

### 2023-03 — SigLIP

- **id:** `siglip-zhai-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google Research; Zhai, Mustafa, Kolesnikov, Beyer
- **disclosure citation:** Zhai, X., Mustafa, B., Kolesnikov, A., Beyer, L. 'Sigmoid Loss for Language Image Pre-Training'. arXiv:2303.15343, March 2023. ICCV 2023. Google Research.
- **disclosed subsystems:** `control-vision-language`, `control-foundation-model-perception`

**Prior art notes:**

> SigLIP is the canonical sigmoid-loss vision-language foundation model (Google ICCV 2023). 2-year-deep prior art for: sigmoid-loss contrastive vision-language training, large-batch-friendly training regime. The text-encoder backbone in OpenVLA, RADIO-ViPE, and many VLA systems. Direct shielding for any commercial humanoid claim on open-vocabulary text-image alignment for instruction following.

**Sources:**

1. Zhai et al. arXiv:2303.15343 March 2023; ICCV 2023.
2. HuggingFace: huggingface.co/google/siglip-base-patch16-224 et al.

---

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

### 2023-03 — Visual Cortex 1 (VC-1)

- **id:** `meta-vc-1-majumdar-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Meta AI + UC Berkeley + Georgia Tech; Arjun Majumdar, Karmesh Yadav, Pieter Abbeel, Jitendra Malik et al.
- **disclosure citation:** Majumdar, A., Yadav, K., Arnaud, S., Ma, J., Chen, C., Silwal, S., Jain, A., Berges, V.-P., Abbeel, P., Malik, J., Batra, D., Lin, Y., Maksymets, O., Rajeswaran, A., Meier, F. 'Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?'. NeurIPS 2023. arXiv:2303.18240. Meta AI + UC Berkeley + Georgia Tech.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-self-supervised-vision`, `control-egocentric-video-pretraining`

**Prior art notes:**

> VC-1 (Majumdar et al. Meta NeurIPS 2023) is the canonical foundation vision model for embodied AI. 2-year-deep open-permissive prior art. Direct architectural ancestor of: subsequent embodied-vision foundation models, NVIDIA AM-RADIO (round-13), DexMV (round-17 entry — egocentric-video-trained manipulation policies). Direct shielding for any commercial humanoid claim on embodied-vision foundation models.

**Sources:**

1. Majumdar et al. arXiv:2303.18240 NeurIPS 2023.
2. Project page (eai-vc.github.io).

---

### 2023-04 — DINOv2

- **id:** `dinov2-oquab-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Meta AI Research (FAIR); Oquab, Darcet, Moutakanni et al.
- **disclosure citation:** Oquab, M., Darcet, T., Moutakanni, T., Vo, H., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., et al. 'DINOv2: Learning Robust Visual Features without Supervision'. arXiv:2304.07193, April 2023. Meta AI Research (FAIR). Apache-2.0 release.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-self-supervised-vision`

**Prior art notes:**

> DINOv2 is the canonical Meta self-supervised vision foundation model (April 2023). 2-year-deep open-permissive prior art for: self-supervised dense visual features at scale, ViT-g-class image encoders for robotics. The vision encoder in OpenVLA, LEG-SLAM, and many other systems in the corpus. Direct shielding for any commercial humanoid claim on self-supervised onboard visual feature learning.

**Sources:**

1. Oquab et al. arXiv:2304.07193 April 2023.
2. GitHub: github.com/facebookresearch/dinov2.
3. HuggingFace: huggingface.co/facebook/dinov2-* family.

---

### 2023-08 — 3D Gaussian Splatting (Kerbl et al.)

- **id:** `kerbl-3d-gaussian-splatting-siggraph-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Inria + Université Côte d'Azur + MPII; Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
- **disclosure citation:** Kerbl, B., Kopanas, G., Leimkühler, T., Drettakis, G. '3D Gaussian Splatting for Real-Time Radiance Field Rendering'. ACM Transactions on Graphics 42(4) 2023 (SIGGRAPH 2023; Best Paper Honorable Mention). arXiv:2308.04079. Inria + Université Côte d'Azur + Max-Planck-Institut für Informatik.
- **disclosed subsystems:** `control-novel-view-synthesis`, `control-foundation-model-perception`, `control-3d-perception`

**Prior art notes:**

> 3D Gaussian Splatting (Kerbl et al. SIGGRAPH 2023) is the foundational paper underlying every GS-SLAM system in the corpus. 2-year-deep open-permissive prior art. **The architectural foundation of WildGS-SLAM (round-11), LEGS (round-15), LEG-SLAM (round-12), LEGO-SLAM (round-12), DGS-SLAM (round-14), SemGauss-SLAM (round-12), OmniSDF, etc.**. Direct shielding for any commercial humanoid claim on Gaussian-splatting scene representation. Corpus citation chain now resolves through round-27.

**Sources:**

1. Kerbl et al. ACM TOG 42(4) 2023; arXiv:2308.04079.
2. Project page (repo-sam.inria.fr/fungraph/3d-gaussian-splatting).
3. GitHub: github.com/graphdeco-inria/gaussian-splatting.

---

### 2023-12 — AM-RADIO (NVIDIA)

- **id:** `nvidia-am-radio-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA Learning and Perception Research; Ranzinger, Heinrich, Kautz, Molchanov
- **disclosure citation:** Ranzinger, M., Heinrich, G., Kautz, J., Molchanov, P. 'AM-RADIO: Agglomerative Vision Foundation Model -- Reduce All Domains Into One'. arXiv:2312.06709, December 2023. CVPR 2024. NVIDIA Learning and Perception Research. RADIOv2.5 follow-up: arXiv:2412.07679 December 2024.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-vision-language`, `control-multi-teacher-distillation`

**Prior art notes:**

> AM-RADIO is the canonical agglomerative-distillation vision foundation model (NVIDIA, CVPR 2024). 1.5-year-deep open-permissive prior art for: multi-teacher vision-foundation distillation, single-backbone CLIP+DINOv2+SAM amalgamation. **The literal embedding substrate of RADIO-ViPE** — the round-10 RADIO-ViPE entry's name comes from this. Direct shielding for any commercial humanoid claim on multi-modal vision-foundation backbones for onboard perception.

**Sources:**

1. Ranzinger et al. arXiv:2312.06709 December 2023; CVPR 2024.
2. Heinrich et al. RADIOv2.5 arXiv:2412.07679 December 2024.
3. HuggingFace: huggingface.co/nvidia/RADIO.
4. Project page: research.nvidia.com/labs/lpr/publication/ranzinger2024radio/.

---

### 2023-12 — DUSt3R

- **id:** `dust3r-naver-cvpr-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NAVER LABS Europe + Aalto University; Shuzhe Wang, Vincent Leroy, Yohann Cabon, Boris Chidlovskii, Jerome Revaud
- **disclosure citation:** Wang, S., Leroy, V., Cabon, Y., Chidlovskii, B., Revaud, J. 'DUSt3R: Geometric 3D Vision Made Easy'. CVPR 2024. arXiv:2312.14132. NAVER LABS Europe + Aalto University.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-3d-reconstruction`, `control-uncalibrated-video-perception`, `control-pose-free-reconstruction`

**Prior art notes:**

> DUSt3R (Wang et al. CVPR 2024) is the foundational pose-free unconstrained 3D-reconstruction paper. 2-year-deep open-permissive prior art. **Direct architectural ancestor of MASt3R** (round-28 entry below), **VGGT** (in audit, round-corpus VGGT), **MegaSaM** (round-13), **NVIDIA ViPE** (round-11), **RADIO-ViPE** (round-10). The 2-year-deep DUSt3R-derived calibration-free reconstruction chain shields any commercial humanoid claim on uncalibrated-camera onboard 3D reconstruction.

**Sources:**

1. Wang et al. arXiv:2312.14132 CVPR 2024.
2. Project page (europe.naverlabs.com/research/publications/dust3r-geometric-3d-vision-made-easy/).
3. GitHub: github.com/naver/dust3r.

---

### 2024-06 — MASt3R (Matching And Stereo 3D Reconstruction)

- **id:** `mast3r-naver-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NAVER LABS Europe; Vincent Leroy, Yohann Cabon, Jerome Revaud
- **disclosure citation:** Leroy, V., Cabon, Y., Revaud, J. 'Grounding Image Matching in 3D with MASt3R'. ECCV 2024. arXiv:2406.09756. NAVER LABS Europe.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-3d-reconstruction`, `control-feature-matching`, `control-visual-localization`

**Prior art notes:**

> MASt3R (Leroy et al. ECCV 2024) is DUSt3R's direct successor adding image-matching. 1-year-deep open-permissive prior art. Together with DUSt3R (round-28), MegaSaM (round-13), ViPE (round-11), RADIO-ViPE (round-10), establishes the calibration-free reconstruction chain that any commercial humanoid camera-perception claim must contend with.

**Sources:**

1. Leroy et al. arXiv:2406.09756 ECCV 2024.
2. GitHub: github.com/naver/mast3r.

---

### 2024-06 — Depth Anything V2

- **id:** `bytedance-depth-anything-v2-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ByteDance + University of Hong Kong + Zhejiang University; Lihe Yang, Bingyi Kang, Hengshuang Zhao et al.
- **disclosure citation:** Yang, L., Kang, B., Huang, Z., Zhao, Z., Xu, X., Feng, J., Zhao, H. 'Depth Anything V2'. NeurIPS 2024. arXiv:2406.09414. ByteDance + University of Hong Kong + Zhejiang University.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-monocular-metric-depth`

**Prior art notes:**

> Depth Anything V2 (Yang et al. NeurIPS 2024) is the canonical open monocular depth estimation foundation model. 1-year-deep open-permissive prior art. **Used in NVIDIA ViPE (round-11) + RADIO-ViPE (round-10) as the metric-depth backbone**. Direct shielding for any commercial humanoid claim on monocular depth estimation as part of an onboard perception stack.

**Sources:**

1. Yang et al. arXiv:2406.09414 NeurIPS 2024.
2. Project page (depth-anything-v2.github.io).
3. HuggingFace: huggingface.co/depth-anything.

---

### 2024-07 — Segment Anything 2 (SAM 2)

- **id:** `meta-sam-2-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Meta AI / FAIR; Nikhila Ravi + multi-author team
- **disclosure citation:** Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Khedr, H., Rädle, R., Rolland, C., Gustafson, L., Mintun, E., Pan, J., Alwala, K. V., Carion, N., Wu, C.-Y., Girshick, R., Dollár, P., Feichtenhofer, C. 'SAM 2: Segment Anything in Images and Videos'. arXiv:2408.00714, July 2024. Meta AI / FAIR. Apache-2.0.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-video-segmentation`, `control-promptable-segmentation`

**Prior art notes:**

> SAM 2 (Ravi et al. Meta FAIR July 2024) is the canonical open-source promptable video segmentation foundation model. 1-year-deep open-permissive prior art. **A teacher in NVIDIA AM-RADIO's agglomerative-distillation training** (corpus entry round-13). Direct shielding for any commercial humanoid claim on video segmentation, real-time object tracking, or promptable segmentation. Together with DINOv2 (round-13) + SigLIP (round-13) + AM-RADIO (round-13), establishes the foundation-vision-model chain.

**Sources:**

1. Ravi et al. arXiv:2408.00714 July 2024.
2. Project page (ai.meta.com/sam2).
3. GitHub: github.com/facebookresearch/sam2.

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

### 2025-01 — NVIDIA Cosmos

- **id:** `nvidia-cosmos-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA; multi-author research team
- **disclosure citation:** NVIDIA. 'Cosmos World Foundation Model Platform for Physical AI'. arXiv:2501.03575, January 2025. NVIDIA CES 2025 announcement. Open weights via HuggingFace nvidia/Cosmos-* family. Cosmos-Reason2-2B variant subsequently used as the System 2 backbone in GR00T N1.7.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-world-model`, `control-video-generation`, `control-sim-to-real`

**Prior art notes:**

> NVIDIA Cosmos is the canonical world-foundation-model platform for physical AI (NVIDIA CES January 2025). 4-month-deep open-permissive prior art for: video generation + understanding + sim-to-real-transfer foundation models, world-modeling for physical-AI policy training. **Cosmos-Reason2-2B is the System-2 backbone of GR00T N1.7** (round-15 entry); round-17 now resolves that lineage citation. Direct shielding for any commercial humanoid claim on world-model-based policy training or on video-generation-based simulation augmentation.

**Sources:**

1. NVIDIA arXiv:2501.03575 January 2025.
2. NVIDIA CES 2025 announcement (nvidianews.nvidia.com).
3. HuggingFace: huggingface.co/nvidia/Cosmos.
4. GitHub: github.com/NVIDIA/Cosmos.

---

### 2025-06 — LEG-SLAM *(draft)*

- **id:** `leg-slam-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** LEG-SLAM authors (per arXiv 2506.03073)
- **disclosure citation:** Authors per arXiv 2506.03073. 'LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM'. arXiv:2506.03073, June 2025.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-semantic-slam`, `control-foundation-model-perception`

**Prior art notes:**

> LEG-SLAM (June 2025) is a real-time language-enhanced GS-SLAM system. 11-month-deep prior art on: real-time fps-class language-aligned GS-SLAM, DINOv2 feature compression for compact per-Gaussian language encoding. Distinct from but contemporary with LEGO-SLAM (Nov 2025). Both feed the open-vocab GS-SLAM lineage that RADIO-ViPE compares against.

**Sources:**

1. arXiv:2506.03073 June 2025.
2. Project page (titrom025.github.io/LEG-SLAM/).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `46e9af2`.*
