---
title: "sensing-depth-camera"
parent: "Invalidity Contentions"
nav_order: 161
layout: default
---

# Invalidity Contention Packet — `sensing-depth-camera`

**Generated:** 2026-05-08  
**Cross-cut tag:** `sensing-depth-camera`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2010-11  
**Most recent disclosure:** 2015-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-depth-camera`.

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

### 2010-11 — Microsoft Kinect

- **id:** `kinect-microsoft-2010`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Microsoft + PrimeSense (Israeli structured-light technology)
- **disclosure citation:** Microsoft Corporation. Kinect for Xbox 360 reveal + commercial release November 4 2010. Subsequent: Kinect for Windows (2012), Kinect v2 (2014), Azure Kinect DK (2019). Built on PrimeSense structured-light depth-sensing technology (Israeli startup, acquired by Apple 2013).
- **disclosed subsystems:** `sensing-depth-camera`, `sensing-structured-light`, `sensing-time-of-flight`

**Prior art notes:**

> Microsoft Kinect (Microsoft + PrimeSense November 2010) is the foundational consumer-grade depth camera. 15-year-deep public-disclosure prior art. **Triggered the depth-camera revolution in academic robotics** — used in thousands of papers 2010-2017+. Direct architectural ancestor of Intel RealSense (round-33 entry below). Direct shielding for any commercial humanoid claim using consumer-grade depth-camera perception.

**Sources:**

1. Microsoft Kinect launch announcement November 2010.
2. Wikipedia 'Kinect'.

---

### 2015-01 — Intel RealSense depth camera lineage

- **id:** `intel-realsense-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Intel Corporation
- **disclosure citation:** Intel Corporation. RealSense D-series depth cameras commercial reveal January 2015 via intel.com. Subsequent product lineage: F200/R200 (2014-2015), D415/D435 (2018), D455 (2020), L515 (2020), D405 (2021).
- **disclosed subsystems:** `sensing-depth-camera`, `sensing-active-stereo`, `sensing-rgbd`

**Prior art notes:**

> Intel RealSense D-series (Intel 2015+) is the dominant academic-research depth camera lineage. 10-year-deep public-disclosure prior art. Successor to Kinect (round-33 entry above) for robot-deployment applications. Used in essentially every academic humanoid + manipulation paper 2018-2025 that uses RGBD perception.

**Sources:**

1. Intel RealSense corporate site (intelrealsense.com).
2. GitHub: github.com/IntelRealSense/librealsense.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `a27a0cf`.*
