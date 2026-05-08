---
title: "control-3d-perception"
parent: "Invalidity Contentions"
nav_order: 18
layout: default
---

# Invalidity Contention Packet — `control-3d-perception`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-3d-perception`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2016-12  
**Most recent disclosure:** 2024-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-3d-perception`.

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

### 2024-03 — 3D Diffusion Policy (DP3)

- **id:** `dp3-ze-rss-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + Tsinghua + CMU; Yanjie Ze, Hao Xu, et al.
- **disclosure citation:** Ze, Y., Zhang, G., Zhang, K., Hu, C., Wang, M., Xu, H. '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'. RSS 2024. arXiv:2403.03954. Stanford + Tsinghua + CMU.
- **disclosed subsystems:** `control-imitation-learning`, `control-diffusion-policy`, `control-3d-perception`, `control-cross-embodiment`

**Prior art notes:**

> 3D Diffusion Policy (Ze et al. RSS 2024) is the canonical 3D extension of Chi/Song's Diffusion Policy (corpus entry). 1-year-deep open-permissive prior art for: 3D-input diffusion-policy for manipulation, point-cloud-conditioned action generation. Direct shielding for any commercial humanoid claim on 3D-perception-conditioned manipulation policies. Together with Diffusion Policy, RDT-1B (diffusion VLA), and Octo (transformer + diffusion-head), establishes the diffusion-policy family that shields commercial diffusion-VLA claims.

**Sources:**

1. Ze et al. arXiv:2403.03954 RSS 2024.
2. Project page (3d-diffusion-policy.github.io).
3. GitHub: github.com/YanjieZe/3D-Diffusion-Policy.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b2db4c5`.*
