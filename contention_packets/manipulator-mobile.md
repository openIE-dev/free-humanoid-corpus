---
title: "manipulator-mobile"
parent: "Invalidity Contentions"
nav_order: 167
layout: default
---

# Invalidity Contention Packet — `manipulator-mobile`

**Generated:** 2026-05-10  
**Cross-cut tag:** `manipulator-mobile`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2010-04  
**Most recent disclosure:** 2022-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `manipulator-mobile`.

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

### 2010-04 — Willow Garage PR2 (defining ROS mobile-manipulation platform)

- **id:** `willow-garage-pr2-2010`
- **corpus:** academic
- **ip status:** open-permissive (ROS-integrated; hardware open-spec)
- **creator:** Willow Garage Inc. (Menlo Park, CA, USA); Scott Hassan + Steve Cousins
- **disclosure citation:** Willow Garage Inc. (Menlo Park, CA, USA; founded 2006 by Scott Hassan + Steve Cousins). PR2 (Personal Robot 2) commercial reveal 2010 ('PR2 Beta Program'). Mobile manipulator with two 7-DoF arms on omnidirectional base. Defining open-source ROS mobile-manipulation platform.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-mobile`, `manipulator-dual-arm`, `actuator-electric`, `control-ros`

**Prior art notes:**

> Willow Garage PR2 (Menlo Park 2010-2014) is the defining open-source ROS mobile-manipulation platform. 15-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from dual-arm mobile manipulators or ROS-integrated platforms. Steve Cousins lineage continues to Savioke (corpus savioke-relay-2014).

**Sources:**

1. Willow Garage PR2 documentation (historical).

---

### 2022-04 — Cobot / Collaborative Robotics (Proxie wheeled-arm cobot)

- **id:** `cobot-collaborative-porter-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Collaborative Robotics (Santa Clara, CA, USA); Brad Porter + Jane Mooney + Steph Tryphonas
- **disclosure citation:** Collaborative Robotics (Santa Clara, CA, USA; founded 2022 by Brad Porter (ex-Amazon VP Robotics, deployed 500K+ Kiva descendants) + Jane Mooney + Steph Tryphonas). Backed by Sequoia + General Catalyst + Khosla.
- **disclosed subsystems:** `manipulator-mobile`

**Prior art notes:**

> Cobot / Collaborative Robotics (Santa Clara 2022+) is the wheeled-arm cobot architectural counter-thesis to bipedal humanoids. 3-year-deep public-disclosure prior art.

**Sources:**

1. techcrunch.com/2023/07/26/collaborative-robotics-raises-30m

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b980619`.*
