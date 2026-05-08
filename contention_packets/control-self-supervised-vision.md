---
title: "control-self-supervised-vision"
parent: "Invalidity Contentions"
nav_order: 93
layout: default
---

# Invalidity Contention Packet — `control-self-supervised-vision`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-self-supervised-vision`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2021-11  
**Most recent disclosure:** 2023-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-self-supervised-vision`.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `55e963d`.*
