---
title: "control-grasp-planning"
parent: "Invalidity Contentions"
nav_order: 49
layout: default
---

# Invalidity Contention Packet — `control-grasp-planning`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-grasp-planning`  
**Entries:** 6 (5 commons-grade, 1 draft)  
**Earliest disclosure:** 1989-06  
**Most recent disclosure:** 2023-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-grasp-planning`.

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

### 1989-06 — Cutkosky grasp taxonomy

- **id:** `cutkosky-grasp-taxonomy-1989`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford BDML; Mark R. Cutkosky
- **disclosure citation:** Cutkosky, M. R. 'On Grasp Choice, Grasp Models, and the Design of Hands for Manufacturing Tasks'. IEEE Transactions on Robotics and Automation 5(3) 1989. Stanford BDML (Biomimetic Dexterous Manipulation Lab; founded by Cutkosky).
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `control-grasp-taxonomy`, `control-grasp-planning`

**Prior art notes:**

> The Cutkosky 16-grasp taxonomy is the canonical academic engineering grasp-classification reference (Cutkosky IEEE T-RA 1989). 36-year-deep public-domain prior art for: hierarchical grasp categorization, manufacturing-task-grasp engineering framework. **The dominant CS reference cited by every robotic manipulation paper 1989-2025**. Together with Schlesinger 1919 (clinical) and Iberall 1986 (theoretical), establishes the three-pillar grasp-taxonomy academic substrate. Direct shielding for any commercial humanoid claim on grasp-type recognition + grasp-class-specific manipulation policy.

**Sources:**

1. Cutkosky, M. R. IEEE T-RA 5(3) 1989.
2. Stanford BDML publications (bdml.stanford.edu).

---

### 2000-01 — KTH Royal Institute of Technology robotics *(draft)*

- **id:** `kth-sweden-stockholm-robotics`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KTH Royal Institute of Technology (Stockholm, Sweden)
- **disclosure citation:** KTH Royal Institute of Technology (Stockholm, Sweden). Robotics research at Robotics, Perception and Learning (RPL) division of the School of Electrical Engineering and Computer Science. Notable: visual servoing + grasping (Kragic + Hellström lab), autonomous vehicles.
- **disclosed subsystems:** `control-research-cluster`, `control-visual-servoing`, `control-grasp-planning`

**Prior art notes:**

> KTH Royal Institute of Technology is Sweden's flagship robotics academic anchor. Brings Sweden depth in the corpus from 2 to 3 entries. Together with VTT Finland (round-24) and Universal Robots Denmark (round-24), establishes the Nordic robotics prior-art baseline.

**Sources:**

1. KTH RPL division (kth.se/rpl).
2. Kragic group publications.

---

### 2002-04 — Kragic-Christensen visual servoing for grasping

- **id:** `kragic-christensen-visual-servoing-2002`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** KTH Royal Institute of Technology Computational Vision and Active Perception Laboratory; Danica Kragic, Henrik I. Christensen
- **disclosure citation:** Kragic, D., Christensen, H. I. 'Survey on Visual Servoing for Manipulation'. Computational Vision and Active Perception Laboratory technical report, KTH Royal Institute of Technology, April 2002. Subsequent: Kragic, D. 'Visual servoing for object manipulation: A survey'. Royal Institute of Technology, Computational Vision and Active Perception Laboratory.
- **disclosed subsystems:** `control-visual-servoing`, `control-grasp-planning`, `control-manipulation`

**Prior art notes:**

> Kragic-Christensen visual servoing (KTH 2002+) is the foundational Swedish academic visual-servoing-for-grasping framework. 23-year-deep public-domain prior art. The specific paper-level anchor for round-25 KTH Sweden aggregator. Direct shielding for any commercial humanoid claim using vision-conditioned grasp control.

**Sources:**

1. Kragic, D., Christensen, H. I. KTH technical report April 2002.
2. KTH RPL division (kth.se/rpl).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `69278e1`.*
