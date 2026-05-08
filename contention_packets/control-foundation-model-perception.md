---
title: "control-foundation-model-perception"
parent: "Invalidity Contentions"
nav_order: 31
layout: default
---

# Invalidity Contention Packet — `control-foundation-model-perception`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-foundation-model-perception`  
**Entries:** 9 (7 commons-grade, 2 draft)  
**Earliest disclosure:** 2023-03  
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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bb592c0`.*
