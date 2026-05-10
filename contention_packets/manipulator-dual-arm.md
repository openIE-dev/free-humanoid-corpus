---
title: "manipulator-dual-arm"
parent: "Invalidity Contentions"
nav_order: 162
layout: default
---

# Invalidity Contention Packet — `manipulator-dual-arm`

**Generated:** 2026-05-10  
**Cross-cut tag:** `manipulator-dual-arm`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2010-04  
**Most recent disclosure:** 2015-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `manipulator-dual-arm`.

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

### 2012-09 — Rethink Robotics Baxter (2012) + Sawyer (2015)

- **id:** `rethink-baxter-sawyer-2012`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Rethink Robotics Inc. (Boston, MA, USA); Rodney Brooks founder
- **disclosure citation:** Rethink Robotics Inc. (Boston, MA, USA; founded 2008 by Rodney Brooks as Heartland Robotics). Baxter dual-arm cobot reveal September 2012. Sawyer single-arm 7-DoF cobot 2015. Company shut down 2018; IP acquired by Hahn Group (Germany).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-dual-arm`, `manipulator-cobot`, `actuator-electric-series-elastic`

**Prior art notes:**

> Rethink Robotics Baxter (2012) + Sawyer (2015) are the first inherently-safe dual-arm + single-arm cobots. 13-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from inherently-safe dual-arm cobots or series-elastic-actuator-based force-limited-motion cobots. Lineage descends from Pratt-Williamson SEA (corpus pratt-williamson-sea). Failed-company status reinforces public-disclosure posture.

**Sources:**

1. en.wikipedia.org/wiki/Rethink_Robotics

---

### 2015-04 — ABB YuMi IRB 14000 dual-arm cobot

- **id:** `abb-yumi-irb-14000-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** ABB Asea Brown Boveri (Zurich + Västerås)
- **disclosure citation:** ABB Asea Brown Boveri (Zurich, Switzerland + Västerås, Sweden). YuMi IRB 14000 commercial reveal Hannover Fair April 2015. World's first truly collaborative dual-arm 7-DoF cobot.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-dual-arm`, `manipulator-cobot`, `actuator-electric`

**Prior art notes:**

> ABB YuMi IRB 14000 (ABB Zurich + Västerås 2015+) is the world's first truly collaborative dual-arm 7-DoF cobot. 10-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from collaborative dual-arm 7-DoF cobots. Lineage descends from ASEA IRB-6 (round-45).

**Sources:**

1. abb.com/global/en/areas/robotics/products/robots/collaborative-robots/dual-arm-yumi

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `7ee2634`.*
