---
title: control-novel-view-synthesis
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-novel-view-synthesis`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 2020-03

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## NeRF (Neural Radiance Fields) (2020-03)

- **id**: `nerf-mildenhall-eccv-2020`
- **corpus**: academic
- **creator**: UC Berkeley + Google Research; Ben Mildenhall, Pratul Srinivasan, Matthew Tancik, Jonathan Barron, Ravi Ramamoorthi, Ren Ng
- **disclosure**: Mildenhall, B., Srinivasan, P. P., Tancik, M., Barron, J. T., Ramamoorthi, R., Ng, R. 'NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis'. ECCV 2020 Best Paper Honorable Mention. arXiv:2003.08934. UC Berkeley + Google Research.
- **ip status**: open-permissive
- **prior art notes**: NeRF (Mildenhall et al. ECCV 2020) is the foundational neural-implicit-3D-representation paper. 5-year-deep open-permissive prior art. **The architectural ancestor of every subsequent neural-3D system** including LERF (round-13), 3D Gaussian Splatting (round-27), all 6 GS-SLAM systems in the corpus, RoDyn-SLAM (round-14, NeRF-based dynamic SLAM). Direct shielding for any commercial humanoid claim on neural-implicit scene representation. Closes a major foundational citation chain.

## Nerfstudio + Nerfacto (2023-02)

- **id**: `nerfstudio-berkeley-2023`
- **corpus**: academic
- **creator**: UC Berkeley AI Research (BAIR); Matthew Tancik, Ethan Weber, Angjoo Kanazawa et al.
- **disclosure**: Tancik, M., Weber, E., Ng, E., Li, R., Yi, B., Wang, T., Kristoffersen, A., Austin, J., Salahi, K., Ahuja, A., McAllister, D., Kanazawa, A. 'Nerfstudio: A Modular Framework for Neural Radiance Field Development'. SIGGRAPH 2023. arXiv:2302.04264. UC Berkeley AI Research (BAIR) + UC Berkeley + Stanford.
- **ip status**: open-permissive
- **prior art notes**: Nerfstudio + Nerfacto (Tancik et al. SIGGRAPH 2023) is the canonical open-academic NeRF research framework. 2-year-deep open-permissive prior art. Direct successor to NeRF (round-28) in the open-source NeRF tooling chain. Used in 100+ academic papers as the standard NeRF research substrate. Direct shielding for any commercial humanoid claim on NeRF-based scene representation development tooling.

## LERF (Language Embedded Radiance Fields) (2023-03)

- **id**: `lerf-kerr-2023`
- **corpus**: academic
- **creator**: UC Berkeley AUTOLab + BAIR; Kerr, Kim, Goldberg, Kanazawa, Tancik
- **disclosure**: Kerr, J., Kim, C. M., Goldberg, K., Kanazawa, A., Tancik, M. 'LERF: Language Embedded Radiance Fields'. arXiv:2303.09553, March 2023. ICCV 2023 (Oral). UC Berkeley AUTOLab + Berkeley AI Research.
- **ip status**: open-permissive
- **prior art notes**: LERF is the canonical first language-embedded NeRF (Berkeley + BAIR, ICCV 2023 Oral). 2-year-deep prior art for: CLIP-embedded 3D radiance fields, open-vocabulary natural-language 3D scene queries. The architectural ancestor of LEGS (round-12), LEG-SLAM (round-12), LEGO-SLAM (round-12), and any commercial claim on language-queryable 3D scene representations. Predates the Gaussian-splatting instantiations and establishes the architectural pattern.

## 3D Gaussian Splatting (Kerbl et al.) (2023-08)

- **id**: `kerbl-3d-gaussian-splatting-siggraph-2023`
- **corpus**: academic
- **creator**: Inria + Université Côte d'Azur + MPII; Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
- **disclosure**: Kerbl, B., Kopanas, G., Leimkühler, T., Drettakis, G. '3D Gaussian Splatting for Real-Time Radiance Field Rendering'. ACM Transactions on Graphics 42(4) 2023 (SIGGRAPH 2023; Best Paper Honorable Mention). arXiv:2308.04079. Inria + Université Côte d'Azur + Max-Planck-Institut für Informatik.
- **ip status**: open-permissive
- **prior art notes**: 3D Gaussian Splatting (Kerbl et al. SIGGRAPH 2023) is the foundational paper underlying every GS-SLAM system in the corpus. 2-year-deep open-permissive prior art. **The architectural foundation of WildGS-SLAM (round-11), LEGS (round-15), LEG-SLAM (round-12), LEGO-SLAM (round-12), DGS-SLAM (round-14), SemGauss-SLAM (round-12), OmniSDF, etc.**. Direct shielding for any commercial humanoid claim on Gaussian-splatting scene representation. Corpus citation chain now resolves through round-27.

## SemGauss-SLAM (2024-03)

- **id**: `semgauss-slam-2024`
- **corpus**: academic
- **creator**: Zhu, Siting et al. (per arXiv 2403.07494)
- **disclosure**: Zhu, S., et al. 'SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM'. arXiv:2403.07494, March 2024.
- **ip status**: open-permissive
- **prior art notes**: SemGauss-SLAM is one of the first dense-semantic Gaussian-splatting SLAM systems (March 2024). 14-month-deep prior art for combining 3D Gaussian representations with per-primitive semantic features. Predates and informs the open-vocabulary GS-SLAM lineage that WildGS-SLAM, LEG-SLAM, LEGO-SLAM, and RADIO-ViPE descend from.

## WildGS-SLAM (2025-04)

- **id**: `wildgs-slam-2025`
- **corpus**: academic
- **creator**: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys (ETH Zürich), Songyou Peng, Iro Armeni (Stanford GradientSpaces)
- **disclosure**: Zheng, J., Zhu, Z., Bieri, V., Pollefeys, M., Peng, S., Armeni, I. 'WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments'. CVPR 2025. arXiv:2504.03886. ETH Zürich + Stanford GradientSpaces.
- **ip status**: open-permissive
- **prior art notes**: WildGS-SLAM is the canonical CVPR 2025 monocular dynamic-scene Gaussian-splatting SLAM system from ETH + Stanford. Establishes 1-year-deep prior art for: monocular GS-SLAM with dynamic-scene robustness, photorealistic novel-view rendering of static background while filtering dynamic foreground. Among the systems RADIO-ViPE benchmarks against (TUM-RGBD dynamic). Direct shielding for any commercial humanoid claim on monocular dynamic-scene mapping with photorealistic reconstruction.
