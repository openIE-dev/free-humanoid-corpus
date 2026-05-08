---
title: "control-implicit-scene-representation"
parent: "Invalidity Contentions"
nav_order: 46
layout: default
---

# Invalidity Contention Packet — `control-implicit-scene-representation`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-implicit-scene-representation`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2020-03  
**Most recent disclosure:** 2023-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-implicit-scene-representation`.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `35dc1dd`.*
