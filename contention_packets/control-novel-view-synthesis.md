---
title: "control-novel-view-synthesis"
parent: "Invalidity Contentions"
nav_order: 92
layout: default
---

# Invalidity Contention Packet — `control-novel-view-synthesis`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-novel-view-synthesis`  
**Entries:** 6 (5 commons-grade, 1 draft)  
**Earliest disclosure:** 2020-03  
**Most recent disclosure:** 2025-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-novel-view-synthesis`.

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

### 2024-03 — SemGauss-SLAM *(draft)*

- **id:** `semgauss-slam-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Zhu, Siting et al. (per arXiv 2403.07494)
- **disclosure citation:** Zhu, S., et al. 'SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM'. arXiv:2403.07494, March 2024.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-semantic-slam`, `control-novel-view-synthesis`

**Prior art notes:**

> SemGauss-SLAM is one of the first dense-semantic Gaussian-splatting SLAM systems (March 2024). 14-month-deep prior art for combining 3D Gaussian representations with per-primitive semantic features. Predates and informs the open-vocabulary GS-SLAM lineage that WildGS-SLAM, LEG-SLAM, LEGO-SLAM, and RADIO-ViPE descend from.

**Sources:**

1. arXiv:2403.07494 March 2024.

---

### 2025-04 — WildGS-SLAM

- **id:** `wildgs-slam-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys (ETH Zürich), Songyou Peng, Iro Armeni (Stanford GradientSpaces)
- **disclosure citation:** Zheng, J., Zhu, Z., Bieri, V., Pollefeys, M., Peng, S., Armeni, I. 'WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments'. CVPR 2025. arXiv:2504.03886. ETH Zürich + Stanford GradientSpaces.
- **disclosed subsystems:** `control-vio-slam`, `control-gaussian-splatting-slam`, `control-dynamic-scene-robust`, `control-novel-view-synthesis`

**Prior art notes:**

> WildGS-SLAM is the canonical CVPR 2025 monocular dynamic-scene Gaussian-splatting SLAM system from ETH + Stanford. Establishes 1-year-deep prior art for: monocular GS-SLAM with dynamic-scene robustness, photorealistic novel-view rendering of static background while filtering dynamic foreground. Among the systems RADIO-ViPE benchmarks against (TUM-RGBD dynamic). Direct shielding for any commercial humanoid claim on monocular dynamic-scene mapping with photorealistic reconstruction.

**Sources:**

1. Zheng et al. CVPR 2025.
2. arXiv:2504.03886 April 2025.
3. Project page (wildgs-slam.github.io).
4. GitHub: github.com/GradientSpaces/WildGS-SLAM.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `88b8beb`.*
