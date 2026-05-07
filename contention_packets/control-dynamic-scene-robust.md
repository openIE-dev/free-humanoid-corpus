---
title: "control-dynamic-scene-robust"
parent: "Invalidity Contentions"
nav_order: 19
layout: default
---

# Invalidity Contention Packet — `control-dynamic-scene-robust`

**Generated:** 2026-05-07  
**Cross-cut tag:** `control-dynamic-scene-robust`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2025-04  
**Most recent disclosure:** 2026-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-dynamic-scene-robust`.

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

### 2026-04 — RADIO-ViPE

- **id:** `radio-vipe-itmo-2026`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ITMO University BE2R Lab; Nasser, Iumanov, Li, Popov, Mahmoud, Kolyubin
- **disclosure citation:** Nasser, Z., Iumanov, M., Li, T., Popov, M., Mahmoud, J., Kolyubin, S. 'RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM in Dynamic Environments'. arXiv:2604.26067v1, April 28, 2026. ITMO University, Biomechatronics and Energy-Efficient Robotics (BE2R) Lab, Saint Petersburg, Russia.
- **disclosed subsystems:** `control-vio-slam`, `control-semantic-slam`, `control-open-vocabulary`, `control-bundle-adjustment`, `control-foundation-model-perception`, `control-dynamic-scene-robust`

**Prior art notes:**

> RADIO-ViPE is the most recent and architecturally complete online open-vocabulary semantic SLAM system. April 2026 arXiv preprint; 9 days before this corpus entry. Establishes very-recent (sub-1-week) open-academic prior art for: calibration-free monocular semantic SLAM, tightly-coupled multi-modal fusion (RADIO + SigLIP + geometric BA), adaptive-kernel dynamic-scene robustness, online operation at 8-10 FPS. Directly shields any commercial humanoid claim on: 'onboard semantic scene understanding from monocular video' (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo, etc. all face this), 'language-grounded robotic perception in dynamic environments', 'calibration-free humanoid camera deployment'. The TUM-RGBD ATE comparison table in Table II of the paper enumerates the prior art — RADIO-ViPE outperforms Dyna-SLAM, DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON, ViPE — every one of which is itself open-academic prior art for humanoid perception. Lineage: ORB-SLAM3 (geometric baseline) → DROID-SLAM (dense differentiable) → ViPE (Princeton in-the-wild metric depth) → RADIO-ViPE (ITMO open-vocab + calibration-free).

**Sources:**

1. Nasser et al. arXiv:2604.26067v1 April 2026.
2. ITMO BE2R Lab (itmo.ru/en/faculties_and_institutes/96/).
3. TUM-RGBD dynamic benchmark (vision.in.tum.de/data/datasets/rgbd-dataset).
4. Foundation models: NVIDIA RADIO (Ranzinger et al. 2024), SigLIP (Zhai et al. ICCV 2023).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `7da5df4`.*
