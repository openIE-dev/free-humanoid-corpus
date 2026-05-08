---
title: control-foundation-model-perception
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-foundation-model-perception`

**26 corpus entries disclose this subsystem.**

Earliest disclosure: 2009-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## ImageNet (large-scale image database) (2009-06)

- **id**: `imagenet-deng-cvpr-2009`
- **corpus**: academic
- **creator**: Princeton + Stanford + UC Berkeley; Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, Fei-Fei Li
- **disclosure**: Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., Fei-Fei, L. 'ImageNet: A Large-Scale Hierarchical Image Database'. CVPR 2009. ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2010-2017.
- **ip status**: public-domain
- **prior art notes**: ImageNet (Deng et al. CVPR 2009) is the foundational dataset of modern computer vision. 16-year-deep public-domain prior art. >75,000 citations. The pretraining dataset of ResNet (round-30), ViT (round-30), every modern vision encoder. Direct shielding for any commercial humanoid claim using ImageNet-pretrained vision encoders.

## AlexNet (2012-12)

- **id**: `alexnet-krizhevsky-nips-2012`
- **corpus**: academic
- **creator**: University of Toronto; Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton
- **disclosure**: Krizhevsky, A., Sutskever, I., Hinton, G. E. 'ImageNet Classification with Deep Convolutional Neural Networks'. NeurIPS 2012. University of Toronto.
- **ip status**: public-domain
- **prior art notes**: AlexNet (Krizhevsky et al. NeurIPS 2012) is **the paper that started the deep-learning revolution in computer vision**. 13-year-deep public-domain prior art. >180,000 citations. The predecessor of ResNet (round-30), ViT (round-30), every modern vision encoder. Together with ImageNet (round-30), constitutes the foundational vision-DL substrate underlying every commercial humanoid vision system.

## ResNet (Residual Networks) (2015-12)

- **id**: `resnet-he-cvpr-2016`
- **corpus**: academic
- **creator**: Microsoft Research Asia; Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
- **disclosure**: He, K., Zhang, X., Ren, S., Sun, J. 'Deep Residual Learning for Image Recognition'. CVPR 2016 Best Paper. arXiv:1512.03385. Microsoft Research Asia.
- **ip status**: public-domain
- **prior art notes**: ResNet (He et al. CVPR 2016 Best Paper) is the foundational deep residual networks paper. 10-year-deep public-domain prior art. >250,000 citations — one of the most-cited ML papers of all time. The visual encoder underlying BC-Z (round-29), RT-1 (corpus), and most pre-Transformer robotic VLA. Direct shielding for any commercial humanoid claim using deep CNNs for vision encoding.

## NeRF (Neural Radiance Fields) (2020-03)

- **id**: `nerf-mildenhall-eccv-2020`
- **corpus**: academic
- **creator**: UC Berkeley + Google Research; Ben Mildenhall, Pratul Srinivasan, Matthew Tancik, Jonathan Barron, Ravi Ramamoorthi, Ren Ng
- **disclosure**: Mildenhall, B., Srinivasan, P. P., Tancik, M., Barron, J. T., Ramamoorthi, R., Ng, R. 'NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis'. ECCV 2020 Best Paper Honorable Mention. arXiv:2003.08934. UC Berkeley + Google Research.
- **ip status**: open-permissive
- **prior art notes**: NeRF (Mildenhall et al. ECCV 2020) is the foundational neural-implicit-3D-representation paper. 5-year-deep open-permissive prior art. **The architectural ancestor of every subsequent neural-3D system** including LERF (round-13), 3D Gaussian Splatting (round-27), all 6 GS-SLAM systems in the corpus, RoDyn-SLAM (round-14, NeRF-based dynamic SLAM). Direct shielding for any commercial humanoid claim on neural-implicit scene representation. Closes a major foundational citation chain.

## Vision Transformer (ViT) (2020-10)

- **id**: `vit-dosovitskiy-iclr-2021`
- **corpus**: academic
- **creator**: Google Research; Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov et al.
- **disclosure**: Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., Houlsby, N. 'An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale'. ICLR 2021. arXiv:2010.11929. Google Research.
- **ip status**: public-domain
- **prior art notes**: ViT (Dosovitskiy et al. Google ICLR 2021) is the foundational Vision Transformer paper. 5-year-deep public-domain prior art. **The visual backbone of CLIP (corpus), DINOv2 (round-13), AM-RADIO (round-13), VC-1 (round-29), and every modern VLA's vision encoder** post-2021. Direct successor to ResNet (round-30) for vision. Direct shielding for any commercial humanoid claim using Transformer-based vision encoders.

## Masked Autoencoders (MAE) (2021-11)

- **id**: `mae-he-cvpr-2022`
- **corpus**: academic
- **creator**: Meta AI Research (FAIR); Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, Ross Girshick
- **disclosure**: He, K., Chen, X., Xie, S., Li, Y., Dollár, P., Girshick, R. 'Masked Autoencoders Are Scalable Vision Learners'. CVPR 2022. arXiv:2111.06377. Meta AI Research (FAIR).
- **ip status**: public-domain
- **prior art notes**: MAE (He et al. CVPR 2022) is the canonical self-supervised masked-patch-reconstruction vision pretraining method. 4-year-deep public-domain prior art. **The pretraining method of VC-1** (round-29 entry) and many embodied AI vision encoders. Together with DINOv2 (round-13), establishes the self-supervised vision-pretraining academic substrate.

## Nerfstudio + Nerfacto (2023-02)

- **id**: `nerfstudio-berkeley-2023`
- **corpus**: academic
- **creator**: UC Berkeley AI Research (BAIR); Matthew Tancik, Ethan Weber, Angjoo Kanazawa et al.
- **disclosure**: Tancik, M., Weber, E., Ng, E., Li, R., Yi, B., Wang, T., Kristoffersen, A., Austin, J., Salahi, K., Ahuja, A., McAllister, D., Kanazawa, A. 'Nerfstudio: A Modular Framework for Neural Radiance Field Development'. SIGGRAPH 2023. arXiv:2302.04264. UC Berkeley AI Research (BAIR) + UC Berkeley + Stanford.
- **ip status**: open-permissive
- **prior art notes**: Nerfstudio + Nerfacto (Tancik et al. SIGGRAPH 2023) is the canonical open-academic NeRF research framework. 2-year-deep open-permissive prior art. Direct successor to NeRF (round-28) in the open-source NeRF tooling chain. Used in 100+ academic papers as the standard NeRF research substrate. Direct shielding for any commercial humanoid claim on NeRF-based scene representation development tooling.

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

## Visual Cortex 1 (VC-1) (2023-03)

- **id**: `meta-vc-1-majumdar-2023`
- **corpus**: academic
- **creator**: Meta AI + UC Berkeley + Georgia Tech; Arjun Majumdar, Karmesh Yadav, Pieter Abbeel, Jitendra Malik et al.
- **disclosure**: Majumdar, A., Yadav, K., Arnaud, S., Ma, J., Chen, C., Silwal, S., Jain, A., Berges, V.-P., Abbeel, P., Malik, J., Batra, D., Lin, Y., Maksymets, O., Rajeswaran, A., Meier, F. 'Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?'. NeurIPS 2023. arXiv:2303.18240. Meta AI + UC Berkeley + Georgia Tech.
- **ip status**: open-permissive
- **prior art notes**: VC-1 (Majumdar et al. Meta NeurIPS 2023) is the canonical foundation vision model for embodied AI. 2-year-deep open-permissive prior art. Direct architectural ancestor of: subsequent embodied-vision foundation models, NVIDIA AM-RADIO (round-13), DexMV (round-17 entry — egocentric-video-trained manipulation policies). Direct shielding for any commercial humanoid claim on embodied-vision foundation models.

## DINOv2 (2023-04)

- **id**: `dinov2-oquab-2023`
- **corpus**: academic
- **creator**: Meta AI Research (FAIR); Oquab, Darcet, Moutakanni et al.
- **disclosure**: Oquab, M., Darcet, T., Moutakanni, T., Vo, H., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., et al. 'DINOv2: Learning Robust Visual Features without Supervision'. arXiv:2304.07193, April 2023. Meta AI Research (FAIR). Apache-2.0 release.
- **ip status**: open-permissive
- **prior art notes**: DINOv2 is the canonical Meta self-supervised vision foundation model (April 2023). 2-year-deep open-permissive prior art for: self-supervised dense visual features at scale, ViT-g-class image encoders for robotics. The vision encoder in OpenVLA, LEG-SLAM, and many other systems in the corpus. Direct shielding for any commercial humanoid claim on self-supervised onboard visual feature learning.

## 3D Gaussian Splatting (Kerbl et al.) (2023-08)

- **id**: `kerbl-3d-gaussian-splatting-siggraph-2023`
- **corpus**: academic
- **creator**: Inria + Université Côte d'Azur + MPII; Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
- **disclosure**: Kerbl, B., Kopanas, G., Leimkühler, T., Drettakis, G. '3D Gaussian Splatting for Real-Time Radiance Field Rendering'. ACM Transactions on Graphics 42(4) 2023 (SIGGRAPH 2023; Best Paper Honorable Mention). arXiv:2308.04079. Inria + Université Côte d'Azur + Max-Planck-Institut für Informatik.
- **ip status**: open-permissive
- **prior art notes**: 3D Gaussian Splatting (Kerbl et al. SIGGRAPH 2023) is the foundational paper underlying every GS-SLAM system in the corpus. 2-year-deep open-permissive prior art. **The architectural foundation of WildGS-SLAM (round-11), LEGS (round-15), LEG-SLAM (round-12), LEGO-SLAM (round-12), DGS-SLAM (round-14), SemGauss-SLAM (round-12), OmniSDF, etc.**. Direct shielding for any commercial humanoid claim on Gaussian-splatting scene representation. Corpus citation chain now resolves through round-27.

## AM-RADIO (NVIDIA) (2023-12)

- **id**: `nvidia-am-radio-2024`
- **corpus**: academic
- **creator**: NVIDIA Learning and Perception Research; Ranzinger, Heinrich, Kautz, Molchanov
- **disclosure**: Ranzinger, M., Heinrich, G., Kautz, J., Molchanov, P. 'AM-RADIO: Agglomerative Vision Foundation Model -- Reduce All Domains Into One'. arXiv:2312.06709, December 2023. CVPR 2024. NVIDIA Learning and Perception Research. RADIOv2.5 follow-up: arXiv:2412.07679 December 2024.
- **ip status**: open-permissive
- **prior art notes**: AM-RADIO is the canonical agglomerative-distillation vision foundation model (NVIDIA, CVPR 2024). 1.5-year-deep open-permissive prior art for: multi-teacher vision-foundation distillation, single-backbone CLIP+DINOv2+SAM amalgamation. **The literal embedding substrate of RADIO-ViPE** — the round-10 RADIO-ViPE entry's name comes from this. Direct shielding for any commercial humanoid claim on multi-modal vision-foundation backbones for onboard perception.

## DUSt3R (2023-12)

- **id**: `dust3r-naver-cvpr-2024`
- **corpus**: academic
- **creator**: NAVER LABS Europe + Aalto University; Shuzhe Wang, Vincent Leroy, Yohann Cabon, Boris Chidlovskii, Jerome Revaud
- **disclosure**: Wang, S., Leroy, V., Cabon, Y., Chidlovskii, B., Revaud, J. 'DUSt3R: Geometric 3D Vision Made Easy'. CVPR 2024. arXiv:2312.14132. NAVER LABS Europe + Aalto University.
- **ip status**: open-permissive
- **prior art notes**: DUSt3R (Wang et al. CVPR 2024) is the foundational pose-free unconstrained 3D-reconstruction paper. 2-year-deep open-permissive prior art. **Direct architectural ancestor of MASt3R** (round-28 entry below), **VGGT** (in audit, round-corpus VGGT), **MegaSaM** (round-13), **NVIDIA ViPE** (round-11), **RADIO-ViPE** (round-10). The 2-year-deep DUSt3R-derived calibration-free reconstruction chain shields any commercial humanoid claim on uncalibrated-camera onboard 3D reconstruction.

## FoundationPose (NVIDIA) (2024-03)

- **id**: `foundationpose-nvidia-cvpr-2024`
- **corpus**: academic
- **creator**: NVIDIA Research; Bowen Wen, Wei Yang, Jan Kautz, Stan Birchfield
- **disclosure**: Wen, B., Yang, W., Kautz, J., Birchfield, S. 'FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects'. CVPR 2024. arXiv:2312.08344. NVIDIA Research.
- **ip status**: open-permissive
- **prior art notes**: FoundationPose (Wen et al. NVIDIA CVPR 2024) is the canonical foundation model for 6D object pose estimation. 1-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim on object-pose-conditioned manipulation.

## RoMa (Robust Dense Feature Matching) (2024-05)

- **id**: `roma-edstedt-cvpr-2024`
- **corpus**: academic
- **creator**: Linköping University; Johan Edstedt, Qiyu Sun, Georg Bökman, Mårten Wadenbäck, Michael Felsberg
- **disclosure**: Edstedt, J., Sun, Q., Bökman, G., Wadenbäck, M., Felsberg, M. 'RoMa: Robust Dense Feature Matching'. CVPR 2024. arXiv:2305.15404. Linköping University.
- **ip status**: open-permissive
- **prior art notes**: RoMa (Edstedt et al. CVPR 2024) is the canonical state-of-the-art dense feature matching method. 1-year-deep open-permissive prior art. Used in 3D-vision pipelines including the MASt3R lineage.

## MASt3R (Matching And Stereo 3D Reconstruction) (2024-06)

- **id**: `mast3r-naver-2024`
- **corpus**: academic
- **creator**: NAVER LABS Europe; Vincent Leroy, Yohann Cabon, Jerome Revaud
- **disclosure**: Leroy, V., Cabon, Y., Revaud, J. 'Grounding Image Matching in 3D with MASt3R'. ECCV 2024. arXiv:2406.09756. NAVER LABS Europe.
- **ip status**: open-permissive
- **prior art notes**: MASt3R (Leroy et al. ECCV 2024) is DUSt3R's direct successor adding image-matching. 1-year-deep open-permissive prior art. Together with DUSt3R (round-28), MegaSaM (round-13), ViPE (round-11), RADIO-ViPE (round-10), establishes the calibration-free reconstruction chain that any commercial humanoid camera-perception claim must contend with.

## Depth Anything V2 (2024-06)

- **id**: `bytedance-depth-anything-v2-2024`
- **corpus**: academic
- **creator**: ByteDance + University of Hong Kong + Zhejiang University; Lihe Yang, Bingyi Kang, Hengshuang Zhao et al.
- **disclosure**: Yang, L., Kang, B., Huang, Z., Zhao, Z., Xu, X., Feng, J., Zhao, H. 'Depth Anything V2'. NeurIPS 2024. arXiv:2406.09414. ByteDance + University of Hong Kong + Zhejiang University.
- **ip status**: open-permissive
- **prior art notes**: Depth Anything V2 (Yang et al. NeurIPS 2024) is the canonical open monocular depth estimation foundation model. 1-year-deep open-permissive prior art. **Used in NVIDIA ViPE (round-11) + RADIO-ViPE (round-10) as the metric-depth backbone**. Direct shielding for any commercial humanoid claim on monocular depth estimation as part of an onboard perception stack.

## Segment Anything 2 (SAM 2) (2024-07)

- **id**: `meta-sam-2-2024`
- **corpus**: academic
- **creator**: Meta AI / FAIR; Nikhila Ravi + multi-author team
- **disclosure**: Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Khedr, H., Rädle, R., Rolland, C., Gustafson, L., Mintun, E., Pan, J., Alwala, K. V., Carion, N., Wu, C.-Y., Girshick, R., Dollár, P., Feichtenhofer, C. 'SAM 2: Segment Anything in Images and Videos'. arXiv:2408.00714, July 2024. Meta AI / FAIR. Apache-2.0.
- **ip status**: open-permissive
- **prior art notes**: SAM 2 (Ravi et al. Meta FAIR July 2024) is the canonical open-source promptable video segmentation foundation model. 1-year-deep open-permissive prior art. **A teacher in NVIDIA AM-RADIO's agglomerative-distillation training** (corpus entry round-13). Direct shielding for any commercial humanoid claim on video segmentation, real-time object tracking, or promptable segmentation. Together with DINOv2 (round-13) + SigLIP (round-13) + AM-RADIO (round-13), establishes the foundation-vision-model chain.

## LEGS (Language-Embedded Gaussian Splats) (2024-09)

- **id**: `legs-berkeley-2024`
- **corpus**: academic
- **creator**: UC Berkeley AUTOLab; Goldberg group
- **disclosure**: Yu, J., et al. 'LEGS: Language-Embedded Gaussian Splats — Incrementally Building Room-Scale Representations with a Mobile Robot'. IROS 2024. arXiv:2409.18108. UC Berkeley AUTOLab.
- **ip status**: open-permissive
- **prior art notes**: LEGS is the canonical Berkeley AUTOLab open-vocabulary Gaussian-splatting representation (IROS 2024). 1.5-year-deep prior art for: CLIP-aligned per-primitive features in 3DGS, incremental room-scale construction by mobile robot, language-grounded mobile-manipulation scene representations. Predates and informs LEG-SLAM, LEGO-SLAM, and any commercial humanoid claim on language-queryable 3D scene maps built onboard.

## NVIDIA Cosmos (2025-01)

- **id**: `nvidia-cosmos-2025`
- **corpus**: academic
- **creator**: NVIDIA; multi-author research team
- **disclosure**: NVIDIA. 'Cosmos World Foundation Model Platform for Physical AI'. arXiv:2501.03575, January 2025. NVIDIA CES 2025 announcement. Open weights via HuggingFace nvidia/Cosmos-* family. Cosmos-Reason2-2B variant subsequently used as the System 2 backbone in GR00T N1.7.
- **ip status**: open-permissive
- **prior art notes**: NVIDIA Cosmos is the canonical world-foundation-model platform for physical AI (NVIDIA CES January 2025). 4-month-deep open-permissive prior art for: video generation + understanding + sim-to-real-transfer foundation models, world-modeling for physical-AI policy training. **Cosmos-Reason2-2B is the System-2 backbone of GR00T N1.7** (round-15 entry); round-17 now resolves that lineage citation. Direct shielding for any commercial humanoid claim on world-model-based policy training or on video-generation-based simulation augmentation.

## VGGT (Visual Geometry Grounded Transformer) (2025-03)

- **id**: `vggt-wang-cvpr-2025`
- **corpus**: academic
- **creator**: Visual Geometry Group, University of Oxford + Meta AI; Jianyuan Wang, Andrea Vedaldi et al.
- **disclosure**: Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., Novotny, D. 'VGGT: Visual Geometry Grounded Transformer'. CVPR 2025 Best Paper. arXiv:2503.11651. Visual Geometry Group, University of Oxford + Meta AI.
- **ip status**: open-permissive
- **prior art notes**: VGGT (Wang et al. Oxford VGG + Meta CVPR 2025 Best Paper) is the canonical 2025 foundation transformer for 3D vision. 6-month-deep open-permissive prior art. **CVPR 2025 Best Paper**. Direct successor to DUSt3R (round-28) and the calibration-free reconstruction chain (DUSt3R → MASt3R → MegaSaM → ViPE → RADIO-ViPE → VGGT). Direct shielding for any commercial humanoid claim on foundation-model-based 3D vision.

## NVIDIA Cosmos-Reason 2-2B (2025-04)

- **id**: `cosmos-reason-2-nvidia-2025`
- **corpus**: academic
- **creator**: NVIDIA Research
- **disclosure**: NVIDIA. 'Cosmos-Reason2: Reasoning About Physical AI'. arXiv preprint. April 2025. NVIDIA Research. Variant of the Cosmos World Foundation Model (round-17 entry nvidia-cosmos-2025). **The System-2 backbone of GR00T N1.7** (round-15 entry successor).
- **ip status**: open-permissive
- **prior art notes**: Cosmos-Reason2-2B (NVIDIA April 2025) is the System-2 backbone of GR00T N1.7. 7-month-deep open-permissive prior art. Direct extension of NVIDIA Cosmos (round-17) for embodied reasoning. Together with the GR00T N1 family, establishes NVIDIA's full S1+S2 dual-system humanoid VLA stack.

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
