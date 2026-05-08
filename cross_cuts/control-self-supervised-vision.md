---
title: control-self-supervised-vision
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-self-supervised-vision`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2021-11

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Masked Autoencoders (MAE) (2021-11)

- **id**: `mae-he-cvpr-2022`
- **corpus**: academic
- **creator**: Meta AI Research (FAIR); Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, Ross Girshick
- **disclosure**: He, K., Chen, X., Xie, S., Li, Y., Dollár, P., Girshick, R. 'Masked Autoencoders Are Scalable Vision Learners'. CVPR 2022. arXiv:2111.06377. Meta AI Research (FAIR).
- **ip status**: public-domain
- **prior art notes**: MAE (He et al. CVPR 2022) is the canonical self-supervised masked-patch-reconstruction vision pretraining method. 4-year-deep public-domain prior art. **The pretraining method of VC-1** (round-29 entry) and many embodied AI vision encoders. Together with DINOv2 (round-13), establishes the self-supervised vision-pretraining academic substrate.

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
