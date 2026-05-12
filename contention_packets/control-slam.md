---
title: "control-slam"
parent: "Invalidity Contentions"
nav_order: 136
layout: default
---

# Invalidity Contention Packet — `control-slam`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-slam`  
**Entries:** 6 (6 commons-grade, 0 draft)  
**Earliest disclosure:** 1992-02  
**Most recent disclosure:** 2020-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-slam`.

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

### 1992-02 — ICP (Iterative Closest Point; Besl & McKay 1992)

- **id:** `icp-besl-mckay-1992`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** General Motors Research Laboratories; Paul Besl + Neil McKay
- **disclosure citation:** Besl, P.J., McKay, N.D. 'A Method for Registration of 3-D Shapes'. IEEE Transactions on Pattern Analysis and Machine Intelligence 14(2):239-256, February 1992. General Motors Research Laboratories. (Independent near-simultaneous: Chen & Medioni 1991.)
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> ICP (Besl & McKay GM Research IEEE PAMI 1992) is the foundational 3D point-cloud registration algorithm. 33-year-deep public-domain prior art.

**Sources:**

1. IEEE PAMI 14(2):239-256, 1992.

---

### 1999-09 — Bundle Adjustment (Triggs et al. 1999; the SfM optimization backbone)

- **id:** `bundle-adjustment-triggs-1999`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** INRIA Rhône-Alpes + Univ. of Surrey + ANU + Oxford; Bill Triggs + Philip McLauchlan + Richard Hartley + Andrew Fitzgibbon
- **disclosure citation:** Triggs, B., McLauchlan, P.F., Hartley, R.I., Fitzgibbon, A.W. 'Bundle Adjustment — A Modern Synthesis'. In 'Vision Algorithms: Theory and Practice' (ICCV '99 workshop), Springer LNCS 1883, 2000. INRIA Rhône-Alpes + others. (The underlying technique dates to photogrammetry in the 1950s-1960s; this paper is the definitive computer-vision synthesis.)
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> Bundle Adjustment (Triggs et al. 'A Modern Synthesis', ICCV '99 workshop; technique from 1950s-60s photogrammetry) is the foundational nonlinear-least-squares optimization at the heart of all geometric vision. 26-year-deep public-domain prior art (70+-year for the underlying technique). Foundational to COLMAP (corpus) + ORB-SLAM back-end (corpus).

**Sources:**

1. Triggs, B. et al. 'Bundle Adjustment — A Modern Synthesis'. Springer LNCS 1883, 2000.

---

### 2014-07 — LOAM (LIDAR Odometry and Mapping; Zhang & Singh 2014)

- **id:** `loam-zhang-singh-2014`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Carnegie Mellon University; Ji Zhang + Sanjiv Singh
- **disclosure citation:** Zhang, J., Singh, S. 'LOAM: Lidar Odometry and Mapping in Real-time'. Robotics: Science and Systems (RSS) 2014. Carnegie Mellon University. Won RSS 2014 best-paper-finalist; topped KITTI odometry leaderboard for years.
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> LOAM (Zhang & Singh CMU RSS 2014) is the foundational real-time LIDAR odometry + mapping system. 11-year-deep academic-publication prior art.

**Sources:**

1. Zhang, J., Singh, S. RSS 2014.

---

### 2016-05 — Cartographer (Google Hess et al. 2016; LIDAR SLAM)

- **id:** `cartographer-google-hess-2016`
- **corpus:** open
- **ip status:** open-permissive (Apache 2.0)
- **creator:** Google; Wolfgang Hess + Damon Kohler + Holger Rapp + Daniel Andor
- **disclosure citation:** Hess, W., Kohler, D., Rapp, H., Andor, D. 'Real-Time Loop Closure in 2D LIDAR SLAM'. ICRA 2016. Google. Open-sourced October 2016 under Apache 2.0.
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> Cartographer (Google Hess et al. ICRA 2016) is the foundational open-source LIDAR SLAM system. 9-year-deep open-permissive prior art.

**Sources:**

1. ICRA 2016 paper.
2. github.com/cartographer-project/cartographer

---

### 2016-06 — COLMAP (Schönberger & Frahm 2016; foundational structure-from-motion)

- **id:** `colmap-schoenberger-frahm-2016`
- **corpus:** open
- **ip status:** open-permissive (BSD)
- **creator:** UNC Chapel Hill + ETH Zurich; Johannes L. Schönberger + Jan-Michael Frahm
- **disclosure citation:** Schönberger, J.L., Frahm, J.-M. 'Structure-from-Motion Revisited'. IEEE CVPR 2016. University of North Carolina at Chapel Hill + ETH Zurich. Open-source (BSD license). Also: Schönberger et al. 'Pixelwise View Selection for Unstructured Multi-View Stereo'. ECCV 2016 (the MVS component).
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> COLMAP (Schönberger & Frahm UNC + ETH CVPR 2016) is the de-facto open-source structure-from-motion + multi-view-stereo pipeline. 9-year-deep open-permissive prior art. The standard tool for NeRF (corpus) + Gaussian Splatting (corpus) camera-pose estimation; uses bundle adjustment (corpus).

**Sources:**

1. IEEE CVPR 2016 (Structure-from-Motion Revisited).

---

### 2020-06 — SuperGlue + SuperPoint + LightGlue (learned feature matching; 2018-2023)

- **id:** `superglue-sarlin-2020`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Magic Leap + ETH Zurich; Paul-Edouard Sarlin + Daniel DeTone + Tomasz Malisiewicz + Andrew Rabinovich (SuperGlue/SuperPoint); Philipp Lindenberger + Marc Pollefeys (LightGlue)
- **disclosure citation:** Sarlin, P.-E., DeTone, D., Malisiewicz, T., Rabinovich, A. 'SuperGlue: Learning Feature Matching with Graph Neural Networks'. IEEE CVPR 2020. Magic Leap + ETH Zurich. Predecessor: DeTone et al. 'SuperPoint: Self-Supervised Interest Point Detection and Description'. CVPRW 2018. Successor: Lindenberger et al. 'LightGlue'. ICCV 2023. Open-source.
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> SuperGlue + SuperPoint + LightGlue (Magic Leap + ETH 2018-2023) are the learned replacement for hand-crafted feature detection + matching. 7-year-deep open-permissive prior art (5-year for SuperGlue). The modern successor to Harris corner detector (corpus) + SIFT (corpus) + nearest-neighbor matching.

**Sources:**

1. IEEE CVPR 2020 (SuperGlue); CVPRW 2018 (SuperPoint); ICCV 2023 (LightGlue).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `dd66352`.*
