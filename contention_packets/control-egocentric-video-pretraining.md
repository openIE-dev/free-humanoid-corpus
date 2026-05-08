---
title: "control-egocentric-video-pretraining"
parent: "Invalidity Contentions"
nav_order: 37
layout: default
---

# Invalidity Contention Packet — `control-egocentric-video-pretraining`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-egocentric-video-pretraining`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2021-08  
**Most recent disclosure:** 2025-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-egocentric-video-pretraining`.

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

### 2021-08 — DexMV (Dexterous Manipulation from Videos)

- **id:** `dexmv-qin-cvpr-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UCSD; Yuzhe Qin, Hao Su, Xiaolong Wang
- **disclosure citation:** Qin, Y., Su, H., Wang, X. 'DexMV: Imitation Learning for Dexterous Manipulation from Human Videos'. ECCV 2022 (also accepted at earlier 2021 venues). arXiv:2108.05877. UC San Diego.
- **disclosed subsystems:** `control-imitation-learning`, `control-egocentric-video-pretraining`, `mechanism-anthropomorphic-hand`

**Prior art notes:**

> DexMV is the canonical academic dexterous-manipulation-from-human-videos system (Qin et al. ECCV 2022). 3-year-deep open-permissive prior art for: training robot manipulation policies directly from in-the-wild human videos, hand-pose retargeting from human to robot. **Direct conceptual ancestor of NVIDIA GR00T N1's 20K-hour EgoScale egocentric-video pre-training** (round-15 entry). Direct shielding for any commercial humanoid claim on 'we trained on YouTube videos' or 'egocentric-video-based policy pretraining'.

**Sources:**

1. Qin et al. arXiv:2108.05877 ECCV 2022.
2. Project page (yzqin.github.io/dexmv).

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

### 2025-03 — NVIDIA Isaac GR00T N1

- **id:** `nvidia-groot-n1-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA; multi-author research team
- **disclosure citation:** NVIDIA. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025. NVIDIA GTC 2025 announcement. Open commercial license; open weights via HuggingFace nvidia/GR00T-N1-2B. Successor versions N1.6 (full-body) and N1.7 (Cosmos-Reason2 + EgoScale 20K-hour egocentric pre-training) released subsequently.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-dual-system-architecture`, `control-egocentric-video-pretraining`, `control-cross-embodiment`

**Prior art notes:**

> NVIDIA GR00T N1 is the canonical first open commercial-licensed humanoid foundation model (GTC March 2025). 2-month-deep open prior art for: dual-system S1/S2 humanoid VLA, egocentric-human-video pre-training at scale, NVIDIA Isaac platform integration. Direct architectural sibling of Figure Helix (round-15 entry). Both adopt the dual-system pattern from cognitive science. The N1.7 EgoScale 20K-hour pre-training corpus is itself prior art for any commercial humanoid claim on egocentric-video-trained policy datasets. Direct shielding for any commercial humanoid VLA claim.

**Sources:**

1. arXiv:2503.14734 March 2025.
2. NVIDIA Newsroom announcement (nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks).
3. HuggingFace: huggingface.co/nvidia/GR00T-N1-2B.
4. GitHub: github.com/NVIDIA/Isaac-GR00T (versions through N1.7).
5. N1.7 model card (huggingface.co/blog/nvidia/gr00t-n1-7).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4846ab1`.*
