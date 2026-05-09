---
title: "simulator"
parent: "Invalidity Contentions"
nav_order: 247
layout: default
---

# Invalidity Contention Packet — `simulator`

**Generated:** 2026-05-09  
**Cross-cut tag:** `simulator`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2004-01  
**Most recent disclosure:** 2013-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `simulator`.

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

### 2004-01 — Gazebo (foundational ROS-integrated robotics simulator)

- **id:** `gazebo-koenig-howard-2004`
- **corpus:** open
- **ip status:** open-permissive (Apache 2.0)
- **creator:** USC + Open Source Robotics Foundation; Nathan Koenig + Andrew Howard
- **disclosure citation:** Koenig, N., Howard, A. 'Design and use paradigms for Gazebo, an open-source multi-robot simulator'. IROS 2004. USC. Subsequent: Open Source Robotics Foundation maintainership; Ignition Gazebo (now Gazebo Sim) rewrite 2019+.
- **disclosed subsystems:** `rl-infrastructure`, `simulator`

**Prior art notes:**

> Gazebo (Koenig + Howard USC 2004+) is the foundational ROS-integrated robotics simulator. 21-year-deep open-permissive prior art.

**Sources:**

1. gazebosim.org
2. Koenig + Howard IROS 2004.

---

### 2013-11 — CoppeliaSim (formerly V-REP; Rohmer Coppelia 2013)

- **id:** `coppeliasim-vrep-rohmer-2013`
- **corpus:** private
- **ip status:** trade-secret (commercial; free educational)
- **creator:** Coppelia Robotics AG (Zurich, Switzerland); Eric Rohmer + Surya Singh + Marc Freese
- **disclosure citation:** Rohmer, E., Singh, S.P.N., Freese, M. 'V-REP: A Versatile and Scalable Robot Simulation Framework'. IROS 2013. Coppelia Robotics AG (Zurich, Switzerland). Renamed CoppeliaSim 2019.
- **disclosed subsystems:** `rl-infrastructure`, `simulator`

**Prior art notes:**

> CoppeliaSim / V-REP (Coppelia Robotics Zurich 2013+) is the alternative-to-Gazebo robotics simulator. 12-year-deep public-disclosure prior art.

**Sources:**

1. coppeliarobotics.com
2. Rohmer + Singh + Freese IROS 2013.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2fbde5f`.*
