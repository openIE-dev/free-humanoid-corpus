---
title: "control-swarm"
parent: "Invalidity Contentions"
nav_order: 122
layout: default
---

# Invalidity Contention Packet — `control-swarm`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-swarm`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2011-01  
**Most recent disclosure:** 2016-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-swarm`.

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

### 2011-01 — GRASP Lab Nano Quadrotor Swarm (Kumar UPenn)

- **id:** `grasp-lab-nano-swarm-kumar-2011`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** UPenn GRASP Lab; Vijay Kumar + Daniel Mellinger + Alex Kushleyev
- **disclosure citation:** Kumar, V., Mellinger, D., Kushleyev, A. / University of Pennsylvania GRASP Lab. Nano-quadrotor swarm 2011-2013. Viral 20+ quadrotor formation flight + cooperative payload + structure assembly demos. KMel Robotics spinout 2011 (Mellinger + Kushleyev) → Qualcomm 2015.
- **disclosed subsystems:** `uav-quadrotor`, `control-swarm`

**Prior art notes:**

> GRASP Lab nano-quadrotor swarm (Kumar UPenn 2011-2013) is the canonical academic quadrotor swarm. 14-year-deep academic-publication prior art.

**Sources:**

1. kumarrobotics.org/

---

### 2016-10 — DARPA Perdix Swarm (103-drone test)

- **id:** `darpa-perdix-swarm-2016`
- **corpus:** academic
- **ip status:** trade-secret
- **creator:** MIT Lincoln Laboratory + Strategic Capabilities Office (DoD); USA
- **disclosure citation:** MIT Lincoln Laboratory / Strategic Capabilities Office (SCO). Perdix swarm test October 25, 2016 — 103 micro-drones dispensed from F/A-18 flare dispensers at Mach 0.6.
- **disclosed subsystems:** `uav-swarm`, `control-swarm`

**Prior art notes:**

> DARPA Perdix swarm (MIT Lincoln Lab + SCO 2016) is the world's largest micro-drone swarm test. 9-year-deep public-disclosure prior art.

**Sources:**

1. en.wikipedia.org/wiki/Perdix_(drone)

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
