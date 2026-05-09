---
title: "power-li-po"
parent: "Invalidity Contentions"
nav_order: 207
layout: default
---

# Invalidity Contention Packet — `power-li-po`

**Generated:** 2026-05-09  
**Cross-cut tag:** `power-li-po`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2010  
**Most recent disclosure:** 2022

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `power-li-po`.

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

### 2010 — DARwIn-OP

- **id:** `darwin-op`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Robotis Co. with University of Pennsylvania, Virginia Tech, Purdue
- **disclosure citation:** Ha, I. et al. 'Development of Open Humanoid Platform DARwIn-OP.' SICE 2011.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `control-behavior-tree`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-imu`, `power-li-po`, `software-ros1`

**Prior art notes:**

> DARwIn-OP is foundational prior art for fully-open small-scale humanoid platforms. Predates Poppy by several years for the academic-open category.

**Sources:**

1. Ha, I. et al. SICE 2011.
2. DARwIn-OP project documentation.

---

### 2013 — Crazyflie

- **id:** `crazyflie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Bitcraze AB
- **disclosure citation:** Bitcraze AB. Crazyflie 1.0 release, 2013.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `sensing-imu`, `sensing-monocular-depth`, `power-li-po`

**Prior art notes:**

> Open hardware aerial platform with extensive academic citation. Anticipates: open nano-UAV designs broadly.

**Sources:**

1. bitcraze.io
2. Crazyflie GitHub repositories.

---

### 2022 — Upkie

- **id:** `upkie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Stéphane Caron and contributors
- **disclosure citation:** Caron, S. et al. Upkie public release, 2022.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `actuator-foc-controller`, `mechanism-wheeled-balancing`, `control-reduced-order-model`, `control-mpc`, `sensing-imu`, `power-li-po`, `software-mjbots-stack`, `software-ros2`

**Prior art notes:**

> Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.

**Sources:**

1. github.com/upkie
2. Caron, S. publications and project documentation.

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
