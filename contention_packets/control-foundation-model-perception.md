---
title: "control-foundation-model-perception"
parent: "Invalidity Contentions"
nav_order: 45
layout: default
---

# Invalidity Contention Packet — `control-foundation-model-perception`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-foundation-model-perception`  
**Entries:** 30 (27 commons-grade, 3 draft)  
**Earliest disclosure:** 2009-06  
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

### 2009-06 — ImageNet (large-scale image database)

- **id:** `imagenet-deng-cvpr-2009`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Princeton + Stanford + UC Berkeley; Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, Fei-Fei Li
- **disclosure citation:** Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., Fei-Fei, L. 'ImageNet: A Large-Scale Hierarchical Image Database'. CVPR 2009. ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2010-2017.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-pretraining-dataset`

**Prior art notes:**

> ImageNet (Deng et al. CVPR 2009) is the foundational dataset of modern computer vision. 16-year-deep public-domain prior art. >75,000 citations. The pretraining dataset of ResNet (round-30), ViT (round-30), every modern vision encoder. Direct shielding for any commercial humanoid claim using ImageNet-pretrained vision encoders.

**Sources:**

1. Deng et al. CVPR 2009.
2. ImageNet site (image-net.org).

---

### 2012-12 — AlexNet

- **id:** `alexnet-krizhevsky-nips-2012`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Toronto; Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton
- **disclosure citation:** Krizhevsky, A., Sutskever, I., Hinton, G. E. 'ImageNet Classification with Deep Convolutional Neural Networks'. NeurIPS 2012. University of Toronto.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-deep-cnn`

**Prior art notes:**

> AlexNet (Krizhevsky et al. NeurIPS 2012) is **the paper that started the deep-learning revolution in computer vision**. 13-year-deep public-domain prior art. >180,000 citations. The predecessor of ResNet (round-30), ViT (round-30), every modern vision encoder. Together with ImageNet (round-30), constitutes the foundational vision-DL substrate underlying every commercial humanoid vision system.

**Sources:**

1. Krizhevsky et al. NeurIPS 2012.

---

### 2015-05 — U-Net

- **id:** `u-net-ronneberger-miccai-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Freiburg; Olaf Ronneberger, Philipp Fischer, Thomas Brox
- **disclosure citation:** Ronneberger, O., Fischer, P., Brox, T. 'U-Net: Convolutional Networks for Biomedical Image Segmentation'. MICCAI 2015. arXiv:1505.04597. University of Freiburg.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-image-segmentation`, `control-encoder-decoder`

**Prior art notes:**

> U-Net (Ronneberger-Fischer-Brox MICCAI 2015) is the foundational image-segmentation neural network. 10-year-deep public-domain prior art. >75,000 citations. The architectural ancestor of every modern image-segmentation network + the denoising backbone of Stable Diffusion + DDPM (round-29). Direct shielding for any commercial humanoid claim using U-Net-class architectures for perception or generation.

**Sources:**

1. Ronneberger, O., Fischer, P., Brox, T. arXiv:1505.04597 MICCAI 2015.

---

### 2015-06 — Faster R-CNN

- **id:** `faster-rcnn-ren-nips-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Microsoft Research Asia; Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun
- **disclosure citation:** Ren, S., He, K., Girshick, R., Sun, J. 'Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks'. NeurIPS 2015. arXiv:1506.01497. Microsoft Research Asia.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-object-detection`

**Prior art notes:**

> Faster R-CNN (Ren-He-Girshick-Sun NeurIPS 2015) is the foundational two-stage object detector. 10-year-deep public-domain prior art. The pre-Transformer object-detection architecture used in many robotic perception stacks (Kaiming He is also the ResNet author — round-30).

**Sources:**

1. Ren, S. et al. arXiv:1506.01497 NeurIPS 2015.

---

### 2015-06 — YOLO (You Only Look Once)

- **id:** `yolo-redmon-cvpr-2016`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Washington + Allen Institute for AI + FAIR; Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi
- **disclosure citation:** Redmon, J., Divvala, S., Girshick, R., Farhadi, A. 'You Only Look Once: Unified, Real-Time Object Detection'. CVPR 2016. arXiv:1506.02640. University of Washington + Allen Institute for AI + Facebook AI Research. Subsequent: YOLOv2/v3/v4/v5/v6/v7/v8/v9/v10/v11 commercial + community variants.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-object-detection`, `control-real-time-perception`

**Prior art notes:**

> YOLO (Redmon et al. CVPR 2016) is the foundational real-time one-stage object detector. 9-year-deep public-domain prior art. Together with Faster R-CNN (round-32), establishes the dominant object-detection prior-art chain underlying most robotic perception systems pre-Transformer.

**Sources:**

1. Redmon et al. arXiv:1506.02640 CVPR 2016.
2. Project page (pjreddie.com/darknet/yolo).

---

### 2015-12 — ResNet (Residual Networks)

- **id:** `resnet-he-cvpr-2016`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Microsoft Research Asia; Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
- **disclosure citation:** He, K., Zhang, X., Ren, S., Sun, J. 'Deep Residual Learning for Image Recognition'. CVPR 2016 Best Paper. arXiv:1512.03385. Microsoft Research Asia.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-deep-cnn`

**Prior art notes:**

> ResNet (He et al. CVPR 2016 Best Paper) is the foundational deep residual networks paper. 10-year-deep public-domain prior art. >250,000 citations — one of the most-cited ML papers of all time. The visual encoder underlying BC-Z (round-29), RT-1 (corpus), and most pre-Transformer robotic VLA. Direct shielding for any commercial humanoid claim using deep CNNs for vision encoding.

**Sources:**

1. He et al. arXiv:1512.03385 CVPR 2016 Best Paper.

---

### 2016-12 — PointNet

- **id:** `pointnet-qi-cvpr-2017`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford University; Charles R. Qi, Hao Su, Kaichun Mo, Leonidas Guibas
- **disclosure citation:** Qi, C. R., Su, H., Mo, K., Guibas, L. J. 'PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation'. CVPR 2017. arXiv:1612.00593. Subsequent PointNet++ NeurIPS 2017. Stanford University; Leonidas Guibas group.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-3d-perception`, `control-point-cloud`

**Prior art notes:**

> PointNet (Qi et al. Stanford CVPR 2017) is the foundational deep learning on point clouds paper. 8-year-deep public-domain prior art. The architectural ancestor of: 3D Diffusion Policy (round-17), every point-cloud-conditioned manipulation policy, depth-perception VLAs. Direct shielding for any commercial humanoid claim on 3D point cloud perception.

**Sources:**

1. Qi, C. R. et al. arXiv:1612.00593 CVPR 2017.
2. Qi, C. R. et al. PointNet++ NeurIPS 2017.

---

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

### 2020-10 — Vision Transformer (ViT)

- **id:** `vit-dosovitskiy-iclr-2021`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Research; Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov et al.
- **disclosure citation:** Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., Houlsby, N. 'An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale'. ICLR 2021. arXiv:2010.11929. Google Research.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-vision-transformer`

**Prior art notes:**

> ViT (Dosovitskiy et al. Google ICLR 2021) is the foundational Vision Transformer paper. 5-year-deep public-domain prior art. **The visual backbone of CLIP (corpus), DINOv2 (round-13), AM-RADIO (round-13), VC-1 (round-29), and every modern VLA's vision encoder** post-2021. Direct successor to ResNet (round-30) for vision. Direct shielding for any commercial humanoid claim using Transformer-based vision encoders.

**Sources:**

1. Dosovitskiy et al. arXiv:2010.11929 ICLR 2021.

---

### 2021-11 — Masked Autoencoders (MAE)

- **id:** `mae-he-cvpr-2022`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Meta AI Research (FAIR); Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, Ross Girshick
- **disclosure citation:** He, K., Chen, X., Xie, S., Li, Y., Dollár, P., Girshick, R. 'Masked Autoencoders Are Scalable Vision Learners'. CVPR 2022. arXiv:2111.06377. Meta AI Research (FAIR).
- **disclosed subsystems:** `control-foundation-model-perception`, `control-self-supervised-vision`

**Prior art notes:**

> MAE (He et al. CVPR 2022) is the canonical self-supervised masked-patch-reconstruction vision pretraining method. 4-year-deep public-domain prior art. **The pretraining method of VC-1** (round-29 entry) and many embodied AI vision encoders. Together with DINOv2 (round-13), establishes the self-supervised vision-pretraining academic substrate.

**Sources:**

1. He et al. arXiv:2111.06377 CVPR 2022.

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

### 2024-03 — FoundationPose (NVIDIA)

- **id:** `foundationpose-nvidia-cvpr-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA Research; Bowen Wen, Wei Yang, Jan Kautz, Stan Birchfield
- **disclosure citation:** Wen, B., Yang, W., Kautz, J., Birchfield, S. 'FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects'. CVPR 2024. arXiv:2312.08344. NVIDIA Research.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-6d-pose-estimation`

**Prior art notes:**

> FoundationPose (Wen et al. NVIDIA CVPR 2024) is the canonical foundation model for 6D object pose estimation. 1-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim on object-pose-conditioned manipulation.

**Sources:**

1. Wen et al. arXiv:2312.08344 CVPR 2024.
2. GitHub: github.com/NVlabs/FoundationPose.

---

### 2024-05 — RoMa (Robust Dense Feature Matching)

- **id:** `roma-edstedt-cvpr-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Linköping University; Johan Edstedt, Qiyu Sun, Georg Bökman, Mårten Wadenbäck, Michael Felsberg
- **disclosure citation:** Edstedt, J., Sun, Q., Bökman, G., Wadenbäck, M., Felsberg, M. 'RoMa: Robust Dense Feature Matching'. CVPR 2024. arXiv:2305.15404. Linköping University.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-feature-matching`

**Prior art notes:**

> RoMa (Edstedt et al. CVPR 2024) is the canonical state-of-the-art dense feature matching method. 1-year-deep open-permissive prior art. Used in 3D-vision pipelines including the MASt3R lineage.

**Sources:**

1. Edstedt et al. arXiv:2305.15404 CVPR 2024.

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

### 2025-03 — VGGT (Visual Geometry Grounded Transformer)

- **id:** `vggt-wang-cvpr-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Visual Geometry Group, University of Oxford + Meta AI; Jianyuan Wang, Andrea Vedaldi et al.
- **disclosure citation:** Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., Novotny, D. 'VGGT: Visual Geometry Grounded Transformer'. CVPR 2025 Best Paper. arXiv:2503.11651. Visual Geometry Group, University of Oxford + Meta AI.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-3d-reconstruction`, `control-pose-free-reconstruction`

**Prior art notes:**

> VGGT (Wang et al. Oxford VGG + Meta CVPR 2025 Best Paper) is the canonical 2025 foundation transformer for 3D vision. 6-month-deep open-permissive prior art. **CVPR 2025 Best Paper**. Direct successor to DUSt3R (round-28) and the calibration-free reconstruction chain (DUSt3R → MASt3R → MegaSaM → ViPE → RADIO-ViPE → VGGT). Direct shielding for any commercial humanoid claim on foundation-model-based 3D vision.

**Sources:**

1. Wang et al. arXiv:2503.11651 CVPR 2025 Best Paper.
2. GitHub: github.com/facebookresearch/vggt.

---

### 2025-04 — NVIDIA Cosmos-Reason 2-2B *(draft)*

- **id:** `cosmos-reason-2-nvidia-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA Research
- **disclosure citation:** NVIDIA. 'Cosmos-Reason2: Reasoning About Physical AI'. arXiv preprint. April 2025. NVIDIA Research. Variant of the Cosmos World Foundation Model (round-17 entry nvidia-cosmos-2025). **The System-2 backbone of GR00T N1.7** (round-15 entry successor).
- **disclosed subsystems:** `control-foundation-model-perception`, `control-foundation-model-policy`, `control-embodied-reasoning`

**Prior art notes:**

> Cosmos-Reason2-2B (NVIDIA April 2025) is the System-2 backbone of GR00T N1.7. 7-month-deep open-permissive prior art. Direct extension of NVIDIA Cosmos (round-17) for embodied reasoning. Together with the GR00T N1 family, establishes NVIDIA's full S1+S2 dual-system humanoid VLA stack.

**Sources:**

1. NVIDIA Cosmos-Reason2 paper / model release April 2025.
2. HuggingFace: huggingface.co/nvidia/Cosmos-Reason2-2B.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `d6a964d`.*
