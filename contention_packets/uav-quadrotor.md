---
title: "uav-quadrotor"
parent: "Invalidity Contentions"
nav_order: 265
layout: default
---

# Invalidity Contention Packet — `uav-quadrotor`

**Generated:** 2026-05-10  
**Cross-cut tag:** `uav-quadrotor`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2007-01  
**Most recent disclosure:** 2011-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `uav-quadrotor`.

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

### 2007-01 — AscTec Pelican / Hummingbird / Firefly research quadrotors

- **id:** `asctec-research-quadrotors-2007`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Ascending Technologies GmbH (Krailling, Germany); → Intel 2016
- **disclosure citation:** Ascending Technologies GmbH (Krailling, Germany). Founded 2007 by Daniel Gurdan + Klaus Ulbrich + Jan Stumpf. Pelican / Hummingbird / Firefly research quadrotors. Acquired by Intel January 2016.
- **disclosed subsystems:** `uav-quadrotor`

**Prior art notes:**

> AscTec research quadrotors (Krailling 2007-2016 → Intel) are the industry-standard 2010s academic research drones. 18-year-deep public-disclosure prior art.

**Sources:**

1. AscTec product documentation (historical).

---

### 2008-01 — ETH Flying Machine Arena (D'Andrea)

- **id:** `eth-flying-machine-arena-dandrea-2008`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** ETH Zurich IDSC; Raffaello D'Andrea
- **disclosure citation:** Raffaello D'Andrea / ETH Zurich Institute for Dynamic Systems and Control. Flying Machine Arena indoor motion-capture cube 2008-2019. Predecessor: Cornell Lab for Intelligent Vehicles 2003.
- **disclosed subsystems:** `uav-quadrotor`, `control-aggressive-maneuvers`

**Prior art notes:**

> ETH Flying Machine Arena (D'Andrea 2008-2019) is the canonical aggressive-quadrotor research testbed. 17-year-deep academic-publication prior art.

**Sources:**

1. flyingmachinearena.ethz.ch/history/

---

### 2011-01 — Crazyflie / Bitcraze (open-source nano-quadcopter)

- **id:** `crazyflie-bitcraze-2011`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Bitcraze AB (Malmö, Sweden); Eliasson + Taffanel + Antonsson
- **disclosure citation:** Bitcraze AB (Sweden); Marcus Eliasson + Arnaud Taffanel + Tobias Antonsson. Project 2009; company 2011; Crazyflie 2.0 2013. Open-source open-hardware.
- **disclosed subsystems:** `uav-quadrotor`, `control-open-source`

**Prior art notes:**

> Crazyflie / Bitcraze (Malmö 2011+) is the de-facto research/education swarm platform. 14-year-deep open-permissive prior art.

**Sources:**

1. en.wikipedia.org/wiki/Crazyflie_2.0
2. bitcraze.io

---

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
