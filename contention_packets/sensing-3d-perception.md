---
title: "sensing-3d-perception"
parent: "Invalidity Contentions"
nav_order: 241
layout: default
---

# Invalidity Contention Packet — `sensing-3d-perception`

**Generated:** 2026-05-11  
**Cross-cut tag:** `sensing-3d-perception`  
**Entries:** 6 (6 commons-grade, 0 draft)  
**Earliest disclosure:** 2007-01  
**Most recent disclosure:** 2023-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-3d-perception`.

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

### 2007-01 — Velodyne HDL-64E LIDAR

- **id:** `velodyne-hdl-64-lidar-2007`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Velodyne LIDAR (Morgan Hill, CA); David Hall founder
- **disclosure citation:** Velodyne LIDAR, Inc. (Morgan Hill, CA; founded 1983 by David Hall as audio-equipment maker, transitioned to LIDAR 2005). HDL-64E commercial release January 2007. Used by every team in DARPA Urban Challenge November 2007 (Stanley + Boss + others). Subsequent: HDL-32E (2010), VLP-16 (2014), VLP-32C (2017).
- **disclosed subsystems:** `sensing-lidar`, `sensing-rotating-lidar`, `sensing-3d-perception`

**Prior art notes:**

> Velodyne HDL-64E (Velodyne 2007+) is the foundational consumer-grade rotating LIDAR. 18-year-deep public-disclosure prior art. **Used by every team in DARPA Urban Challenge 2007** (Stanford Stanley + CMU Boss + others). The sensor that enabled the autonomous-vehicle revolution + every modern humanoid + quadruped LIDAR perception stack (CSIRO Wildcat, ANYmal-D, BD Spot, etc.). Direct shielding for any commercial humanoid claim using rotating-LIDAR perception.

**Sources:**

1. Velodyne LIDAR corporate site (velodynelidar.com).
2. DARPA Urban Challenge 2007 results.

---

### 2016-01 — Mech-Mind Robotics (3D vision + AI for industrial manipulation)

- **id:** `mech-mind-robotics-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Mech-Mind Robotics (Beijing, China); Shao Tianlan
- **disclosure citation:** Mech-Mind Robotics (Beijing, China; founded 2016 by Shao Tianlan). 15,000+ installations in 50+ countries.
- **disclosed subsystems:** `sensing-3d-perception`, `warehouse-robot`

**Prior art notes:**

> Mech-Mind Robotics (Beijing 2016+) is the dominant Chinese industrial-vision software stack. 9-year-deep public-disclosure prior art.

**Sources:**

1. en.wikipedia.org/wiki/Mech-Mind_Robotics

---

### 2016-01 — Apera AI 4D Vision (Canadian bin-pick vision software)

- **id:** `apera-ai-4d-vision-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Apera AI (Vancouver, Canada); Sina Afrooze (ex-AWS Alexa + Avigilon) + Armin Khatoonabadi
- **disclosure citation:** Apera AI (Vancouver, Canada; founded 2016 by Sina Afrooze, ex-AWS Alexa voice + Avigilon, + Armin Khatoonabadi). Patented '4D Vision' for bin-pick / assembly / packaging.
- **disclosed subsystems:** `warehouse-robot`, `sensing-3d-perception`

**Prior art notes:**

> Apera AI 4D Vision (Vancouver 2016+) is the Canadian industrial-vision-software player. 9-year-deep public-disclosure prior art.

**Sources:**

1. apera.ai/about-apera-ai/

---

### 2017-03 — Dex-Net 2.0 (Mahler Goldberg Berkeley)

- **id:** `dex-net-goldberg-berkeley-2017`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley Goldberg Lab AUTOLAB; Jeffrey Mahler, Ken Goldberg
- **disclosure citation:** Mahler, J., Liang, J., Niyaz, S., Laskey, M., Doan, R., Liu, X., Aparicio, J., Goldberg, K. 'Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics'. Robotics: Science and Systems (RSS) 2017. arXiv:1703.09312. UC Berkeley Goldberg Lab AUTOLAB. Dex-Net 1.0 (2016 ICRA) preceded; subsequent Dex-Net 3.0 (suction grasps, 2018) + Dex-Net 4.0 (ambidextrous parallel-jaw + suction, *Science Robotics* 2019).
- **disclosed subsystems:** `control-grasp-planning`, `sensing-3d-perception`, `control-deep-learning-policy`

**Prior art notes:**

> Dex-Net 2.0 (Mahler / Goldberg Berkeley AUTOLAB RSS 2017, arXiv 1703.09312) is the foundational deep grasp-quality network. 8-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from deep-learning grasp quality networks, synthetic-data + analytic-metric grasp training, or ambidextrous parallel-jaw + suction grasp policies. Anchors the grasp-learning chain leading to Contact-GraspNet (round-42) + GraspNet-1Billion (round-42) + AnyGrasp (round-42).

**Sources:**

1. arxiv.org/abs/1703.09312
2. berkeleyautomation.github.io/dex-net/

---

### 2020-03 — GraspNet-1Billion (Fang Lu SJTU)

- **id:** `graspnet-1billion-fang-sjtu-2020`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Shanghai Jiao Tong University Lu Cewu Lab; Hao-Shu Fang, Chenxi Wang, Minghao Gou, Cewu Lu
- **disclosure citation:** Fang, H.-S., Wang, C., Gou, M., Lu, C. 'GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping'. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2020. Shanghai Jiao Tong University Lu Cewu Lab.
- **disclosed subsystems:** `control-grasp-planning`, `sensing-3d-perception`, `control-deep-learning-policy`

**Prior art notes:**

> GraspNet-1Billion (Fang / Lu SJTU CVPR 2020) is the dominant academic grasp benchmark. 5-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from large-scale grasp annotation datasets or benchmark-driven grasp policy evaluation. Together with Dex-Net (round-42), Contact-GraspNet (round-42), AnyGrasp (round-42), establishes the global grasp-learning benchmark prior-art chain.

**Sources:**

1. openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf

---

### 2023-01 — AnyGrasp (Fang Lu SJTU 2023)

- **id:** `anygrasp-fang-sjtu-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Shanghai Jiao Tong University Lu Cewu Lab; Hao-Shu Fang et al.
- **disclosure citation:** Fang, H.-S., Wang, C., Fang, H., Gou, M., Liu, J., Yan, H., Liu, W., Xie, Y., Lu, C. 'AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains'. IEEE Transactions on Robotics 39(5), 2023. arXiv:2212.08333. Shanghai Jiao Tong University Lu Cewu Lab.
- **disclosed subsystems:** `control-grasp-planning`, `sensing-3d-perception`, `control-deep-learning-policy`

**Prior art notes:**

> AnyGrasp (Fang / Lu SJTU T-RO 2023, arXiv 2212.08333) is the state-of-the-art Chinese academic grasp-perception benchmark. 2-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from billion-scale self-supervised grasp perception or temporal-spatial 7-DoF grasp generation. Lineage descends from GraspNet-1Billion (round-42) and Dex-Net (round-42).

**Sources:**

1. arxiv.org/abs/2212.08333

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0e58219`.*
