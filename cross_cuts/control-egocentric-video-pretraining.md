---
title: control-egocentric-video-pretraining
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-egocentric-video-pretraining`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2021-08

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DexMV (Dexterous Manipulation from Videos) (2021-08)

- **id**: `dexmv-qin-cvpr-2022`
- **corpus**: academic
- **creator**: UCSD; Yuzhe Qin, Hao Su, Xiaolong Wang
- **disclosure**: Qin, Y., Su, H., Wang, X. 'DexMV: Imitation Learning for Dexterous Manipulation from Human Videos'. ECCV 2022 (also accepted at earlier 2021 venues). arXiv:2108.05877. UC San Diego.
- **ip status**: open-permissive
- **prior art notes**: DexMV is the canonical academic dexterous-manipulation-from-human-videos system (Qin et al. ECCV 2022). 3-year-deep open-permissive prior art for: training robot manipulation policies directly from in-the-wild human videos, hand-pose retargeting from human to robot. **Direct conceptual ancestor of NVIDIA GR00T N1's 20K-hour EgoScale egocentric-video pre-training** (round-15 entry). Direct shielding for any commercial humanoid claim on 'we trained on YouTube videos' or 'egocentric-video-based policy pretraining'.

## NVIDIA Isaac GR00T N1 (2025-03)

- **id**: `nvidia-groot-n1-2025`
- **corpus**: academic
- **creator**: NVIDIA; multi-author research team
- **disclosure**: NVIDIA. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025. NVIDIA GTC 2025 announcement. Open commercial license; open weights via HuggingFace nvidia/GR00T-N1-2B. Successor versions N1.6 (full-body) and N1.7 (Cosmos-Reason2 + EgoScale 20K-hour egocentric pre-training) released subsequently.
- **ip status**: open-permissive
- **prior art notes**: NVIDIA GR00T N1 is the canonical first open commercial-licensed humanoid foundation model (GTC March 2025). 2-month-deep open prior art for: dual-system S1/S2 humanoid VLA, egocentric-human-video pre-training at scale, NVIDIA Isaac platform integration. Direct architectural sibling of Figure Helix (round-15 entry). Both adopt the dual-system pattern from cognitive science. The N1.7 EgoScale 20K-hour pre-training corpus is itself prior art for any commercial humanoid claim on egocentric-video-trained policy datasets. Direct shielding for any commercial humanoid VLA claim.
