---
title: "manipulator-mobile"
parent: "Invalidity Contentions"
nav_order: 185
layout: default
---

# Invalidity Contention Packet — `manipulator-mobile`

**Generated:** 2026-05-15  
**Cross-cut tag:** `manipulator-mobile`  
**Entries:** 7 (7 commons-grade, 0 draft)  
**Earliest disclosure:** 1966-04  
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

### 1966-04 — Shakey the Robot (SRI International 1966-1972; the first mobile reasoning robot)

- **id:** `shakey-sri-1966`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** SRI International (Menlo Park, CA, USA); Nils Nilsson + Charles Rosen + Bert Raphael + Richard Fikes + Peter Hart + team
- **disclosure citation:** Nilsson, N.J. et al. Shakey the Robot project at SRI International (Menlo Park, CA, USA), 1966-1972. DARPA-funded. Key papers: Fikes, R.E., Nilsson, N.J. 'STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving'. Artificial Intelligence 2(3-4):189-208, 1971. Hart, P.E., Nilsson, N.J., Raphael, B. 'A Formal Basis for the Heuristic Determination of Minimum Cost Paths'. IEEE Transactions on Systems Science and Cybernetics 4(2):100-107, 1968 (the A* algorithm).
- **disclosed subsystems:** `manipulator-mobile`, `control-motion-planning`

**Prior art notes:**

> Shakey the Robot (SRI International 1966-1972; Nilsson + Rosen + Raphael + Fikes + Hart + team) is the first mobile reasoning robot — and the origin of A* + STRIPS. 59-year-deep public-domain prior art. Direct ancestor of every subsequent mobile robot + autonomous vehicle.

**Sources:**

1. Fikes, R.E., Nilsson, N.J. AI 2(3-4):189-208, 1971.
2. Hart, P.E. et al. IEEE T-SSC 4(2):100-107, 1968.

---

### 1971-01 — Stanford Cart (Hans Moravec 1971-1979; pioneer autonomous vision)

- **id:** `stanford-cart-moravec-1971`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford Artificial Intelligence Laboratory (SAIL); Hans Moravec (1971-1980 as Stanford PhD student)
- **disclosure citation:** Moravec, H.P. PhD thesis 'Obstacle Avoidance and Navigation in the Real World by a Seeing Robot Rover'. Stanford University, 1980. Cart active 1971-1980 at Stanford AI Lab (SAIL). Famous 1979 demonstration: 5 hours to cross a 20-meter chair-cluttered room without hitting obstacles.
- **disclosed subsystems:** `manipulator-mobile`

**Prior art notes:**

> Stanford Cart (Hans Moravec at Stanford AI Lab, 1971-1980 PhD work) is the foundational vision-based autonomous mobile robot. 54-year-deep public-domain prior art. Direct Stanford lineage to Stanley (corpus DARPA Grand Challenge 2005) + Waymo (corpus).

**Sources:**

1. Moravec, H.P. PhD thesis, Stanford 1980.

---

### 1986-01 — CMU NREC + Field Robotics Center (Red Whittaker 1986-2026+)

- **id:** `nrec-cmu-whittaker-1996`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** CMU Robotics Institute; William 'Red' Whittaker (founder + PI)
- **disclosure citation:** Carnegie Mellon University. Field Robotics Center founded 1986 by William 'Red' Whittaker. NREC (National Robotics Engineering Center) founded 1996 as the commercial/applied arm. Key projects: Three Mile Island cleanup robots (1984+), Dante I + II volcano-exploration robots (1992-1994), Nomad Antarctic meteorite-hunting robot (1997-2000), Crusher autonomous off-road vehicle (2006), DARPA Urban Challenge 2007 Tartan Racing 'Boss' (corpus darpa-grand-challenge-2004-2005), DARPA Robotics Challenge entries, Lunar X Prize Astrobotic (now corpus astrobotic-peregrine, Whittaker founded Astrobotic 2007).
- **disclosed subsystems:** `autonomous-vehicle`, `manipulator-mobile`

**Prior art notes:**

> CMU NREC + Field Robotics Center (Red Whittaker 1986+) is the patriarch of field robotics — and the lab that built robots for the world's hardest environments. 39-year-deep academic-publication prior art. Spun out Astrobotic (corpus); Tartan Racing won DARPA Urban Challenge (corpus).

**Sources:**

1. CMU NREC + Field Robotics Center publications 1986+.

---

### 2009-06 — Clearpath Robotics Husky + Jackal + Warthog (2009+; Canadian field-research mobile robots)

- **id:** `clearpath-husky-jackal-2009`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Clearpath Robotics (Waterloo, Ontario, Canada); Matthew Rendall + Ryan Gariepy + Bryan Webb + Pat Martinson
- **disclosure citation:** Clearpath Robotics (Waterloo, Canada). Founded 2009 by Matthew Rendall + Ryan Gariepy + Bryan Webb + Pat Martinson. Husky UGV launched 2010; Jackal 2014; Warthog 2017; Otto autonomous indoor fleet (now Otto Motors 2015). Acquired by Rockwell Automation 2023.
- **disclosed subsystems:** `manipulator-mobile`

**Prior art notes:**

> Clearpath Robotics Husky + Jackal + Warthog (Waterloo, Canada, 2009+; Rockwell Automation acquisition 2023) is the Canadian research-mobile-robot supplier. 16-year-deep public-disclosure prior art.

**Sources:**

1. clearpathrobotics.com (corporate site).

---

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

### 2010-09 — TurtleBot (Willow Garage 2010; foundational education + research mobile robot)

- **id:** `turtlebot-2010`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Willow Garage (Menlo Park, CA, USA); Melonee Wise + Tully Foote
- **disclosure citation:** Wise, M., Foote, T. TurtleBot (Willow Garage, 2010). Subsequent: TurtleBot 2 (Yujin Kobuki base, 2012), TurtleBot 3 (Robotis Burger + Waffle, 2017), TurtleBot 4 (Clearpath Robotics, 2022). Open Source Robotics Foundation reference platform.
- **disclosed subsystems:** `manipulator-mobile`, `rl-infrastructure`

**Prior art notes:**

> TurtleBot (Willow Garage 2010 + subsequent generations) is the foundational education + research mobile robot — ROS's reference platform. 15-year-deep open-permissive prior art.

**Sources:**

1. Willow Garage / Open Robotics TurtleBot documentation 2010-2022.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `cd2f551`.*
