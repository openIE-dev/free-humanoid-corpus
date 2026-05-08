---
title: "actuator-spherical-multi-dof"
parent: "Invalidity Contentions"
nav_order: 16
layout: default
---

# Invalidity Contention Packet — `actuator-spherical-multi-dof`

**Generated:** 2026-05-08  
**Cross-cut tag:** `actuator-spherical-multi-dof`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2020  
**Most recent disclosure:** 2023-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-spherical-multi-dof`.

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

### 2020 — Reachy

- **id:** `reachy`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Pollen Robotics
- **disclosure citation:** Pollen Robotics. Reachy public release, 2020.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `actuator-spherical-multi-dof`, `mechanism-anthropomorphic-hand`, `sensing-stereo-camera`

**Prior art notes:**

> Reachy's Orbita 3-DoF spherical actuator is novel-ish but anticipated by extensive academic spherical-motor literature. Open hardware files constitute prior art for the specific implementation.

**Sources:**

1. pollen-robotics.com
2. Pollen Robotics GitHub.

---

### 2023-10 — Reachy-2 open-source humanoid platform (Pollen Robotics)

- **id:** `reachy-2-pollen-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Pollen Robotics SAS (Matthieu Lapeyre, Pierre Rouanet et al.)
- **disclosure citation:** Pollen Robotics. 'Introducing Reachy 2.' Pollen Robotics blog and product launch, October 2023; technical hardware repository pollen-robotics/reachy2_sdk, GitHub, 2023-2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-spherical-multi-dof`, `sensing-stereo-camera`, `sensing-imu`, `sensing-proprioceptive-actuator`, `control-teleoperation`, `software-ros2`

**Prior art notes:**

> Reachy-2 is the 2023 successor to the open-source Reachy-1 platform and is one of the few European-origin commercial humanoid upper-bodies released with full open hardware/firmware. It anticipates with full specificity: (1) claims on open-source humanoid SDKs with VR-teleoperation for imitation-learning data collection — Pollen publishes the SDK and Quest-Pro tele-op pipeline on GitHub Apache-2.0; (2) claims on parallel-spherical-mechanism necks (Orbita 3-DoF) — Reachy-2 ships and documents the kinematic with patent-expired joint topology; (3) claims on quasi-direct-drive humanoid arm modules at sub-40kg torso mass — Reachy-2 datasheet and CAD release. Modern humanoid commercial platforms claiming open-hardware tele-op pipelines face this timestamped 2023 anchor.

**Sources:**

1. Pollen Robotics. 'Reachy 2 product launch.' October 2023.
2. GitHub: pollen-robotics/reachy2_sdk, 2023-2024.
3. Reachy 2 hardware documentation (CC-BY-4.0 / Apache-2.0).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bb592c0`.*
