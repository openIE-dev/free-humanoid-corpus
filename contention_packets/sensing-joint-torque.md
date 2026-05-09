---
title: "sensing-joint-torque"
parent: "Invalidity Contentions"
nav_order: 202
layout: default
---

# Invalidity Contention Packet — `sensing-joint-torque`

**Generated:** 2026-05-09  
**Cross-cut tag:** `sensing-joint-torque`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 1991-01  
**Most recent disclosure:** 2019-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-joint-torque`.

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

### 1991-01 — DLR Lightweight Robot LWR I/II/III (foundational torque-sensor arm)

- **id:** `dlr-lwr-1991-2003`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** DLR (German Aerospace Center) Institute of Robotics and Mechatronics; Gerd Hirzinger group
- **disclosure citation:** Hirzinger, G. et al. DLR (German Aerospace Center) Institute of Robotics and Mechatronics. LWR I (1991), LWR II (1998), LWR III (2003), LWR IV (~2007). The seminal torque-sensor 7-DoF lightweight arm; basis for KUKA LBR iiwa (round-45) via license.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> DLR Lightweight Robot LWR (DLR Hirzinger group 1991-2007) is the seminal torque-sensor 7-DoF lightweight research arm. 34-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from torque-sensor 7-DoF cobots. Anchors the entire 7-DoF cobot category via KUKA LBR iiwa (round-45) and Franka Panda (round-45) descendants.

**Sources:**

1. DLR Institute of Robotics and Mechatronics LWR documentation.

---

### 2013-04 — KUKA LBR iiwa (intelligent industrial work assistant)

- **id:** `kuka-lbr-iiwa-2013`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** KUKA AG (Augsburg, Germany); DLR LWR licensee
- **disclosure citation:** KUKA AG (Augsburg, Germany; founded 1898). LBR iiwa commercial reveal Hannover Messe April 2013. World's first series-produced HRC-compatible 7-DoF cobot with joint torque sensors. Direct descendant of DLR LWR III (round-45 dlr-lwr-1991-2003) via licensing agreement.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> KUKA LBR iiwa (KUKA Augsburg 2013+) is the world's first series-produced HRC 7-DoF cobot with joint torque sensors. 12-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from 7-DoF cobots with joint torque sensing. Lineage descends from DLR LWR III (round-45 dlr-lwr-1991-2003).

**Sources:**

1. kuka.com/en-us/products/robotics-systems/industrial-robots/lbr-iiwa

---

### 2017-04 — Franka Emika Panda 7-DoF research cobot

- **id:** `franka-emika-panda-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Franka Emika GmbH (Munich, Germany); Sami Haddadin (ex-DLR)
- **disclosure citation:** Franka Emika GmbH (Munich, Germany; founded 2016 by Sami Haddadin + colleagues, ex-DLR). Panda commercial reveal 2017. Successor: Franka Research 3 (2022 post-restructure as Franka Robotics).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> Franka Emika Panda (Munich 2017+; Franka Research 3 2022) is the canonical sub-€10K research-grade torque-sensor 7-DoF cobot. 8-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from low-cost 7-DoF research cobots with joint torque sensing. Lineage descends from DLR LWR III (round-45 dlr-lwr-1991-2003).

**Sources:**

1. franka.de/

---

### 2017-09 — Doosan Robotics M-series cobots

- **id:** `doosan-robotics-cobots-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Doosan Robotics (Suwon, South Korea)
- **disclosure citation:** Doosan Robotics, Inc. (Suwon, South Korea; Doosan Group subsidiary, founded 2015). M-series cobot product reveal September 2017 via doosanrobotics.com. M0609, M1013, M1509, M1013 lineup. Subsequent A-series (2021), H-series (2022) commercial expansions. KOSDAQ IPO 2023.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-collaborative-robot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> Doosan Robotics M-series is the canonical Korean commercial collaborative-robot arm family (2017+). 8-year-deep public-disclosure prior art for: 6-axis joint-torque-sensing cobot, ISO 10218 + ISO/TS 15066 compliant collaborative robot. The Korean commercial cobot leader (vs. Universal Robots Denmark / Franka Emika Germany / Kuka Germany). Direct shielding for any commercial humanoid claim on collaborative-robot-arm derivative applications, particularly anthropomorphic-arm joint-torque sensing as deployed in Optimus Gen 3 / Apptronik Apollo.

**Sources:**

1. Doosan Robotics corporate site (doosanrobotics.com).
2. KOSDAQ IPO filings 2023.

---

### 2019-09 — FANUC CRX collaborative robot family

- **id:** `fanuc-crx-collaborative-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** FANUC Corporation (Yamanashi, Japan)
- **disclosure citation:** FANUC Corporation. CRX collaborative robot family commercial reveal September 2019. CRX-10iA (10 kg payload) initial product; subsequent CRX-25iA (25 kg payload) + CRX-5iA (5 kg payload). fanuc.com. The cobot variant of FANUC's industrial-arm family (corpus round-34 fanuc-industrial-robotics-1956).
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-collaborative-robot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> FANUC CRX (FANUC Yamanashi 2019+) is FANUC's cobot variant of the industrial-arm family (round-34 fanuc-industrial-robotics-1956). 6-year-deep public-disclosure prior art. The Japanese cobot answer to Universal Robots (Denmark) + Doosan (Korea) + Franka Emika (Germany). Together, the global cobot prior-art chain spans 4 distinct national-origin commercial cobot product lines.

**Sources:**

1. FANUC CRX product page (fanuc.com).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `d6a964d`.*
