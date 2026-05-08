---
title: "mechanism-collaborative-robot"
parent: "Invalidity Contentions"
nav_order: 85
layout: default
---

# Invalidity Contention Packet — `mechanism-collaborative-robot`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-collaborative-robot`  
**Entries:** 3 (2 commons-grade, 1 draft)  
**Earliest disclosure:** 2002-01  
**Most recent disclosure:** 2017-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-collaborative-robot`.

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

### 2002-01 — A*STAR Institute for Infocomm Research (I2R) robotics *(draft)*

- **id:** `a-star-singapore-i2r-robotics`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Agency for Science, Technology and Research (A*STAR), Singapore
- **disclosure citation:** Agency for Science, Technology and Research (A*STAR), Singapore. Institute for Infocomm Research (I2R) and Institute for High Performance Computing (IHPC) host Singapore's national robotics research. a-star.edu.sg. Notable: industrial-collaboration research (cobot integration with Singapore manufacturing), AI + vision research, autonomous-vehicle technology.
- **disclosed subsystems:** `control-research-cluster`, `mechanism-collaborative-robot`

**Prior art notes:**

> A*STAR I2R is Singapore's national robotics research aggregator. Together with NUS UnetStack (round-9 entry, NUS robotics), NTU robotics (round-23 entry below), establishes the Singapore + ASEAN robotics prior-art baseline. Aggregator-style; specific A*STAR papers should be added in future rounds.

**Sources:**

1. A*STAR Institute for Infocomm Research (i2r.a-star.edu.sg).
2. A*STAR corporate site (a-star.edu.sg).

---

### 2008-12 — Universal Robots (Odense, Denmark)

- **id:** `universal-robots-denmark-2008`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Universal Robots A/S (Odense, Denmark; SDU spinout); Østergaard, Støy, Kassow founders
- **disclosure citation:** Universal Robots A/S (Odense, Denmark; founded 2005 by Esben Østergaard, Kasper Støy, Kristian Kassow as a University of Southern Denmark spinout). UR5 first commercial cobot reveal December 2008. Subsequently: UR3 (2015), UR10 (2012), UR16 (2019), e-Series (2018+), UR20/UR30 (2022+). Acquired by Teradyne 2015 for $285M. universal-robots.com.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-collaborative-robot`, `actuator-electric`, `control-impedance-control`

**Prior art notes:**

> Universal Robots is the canonical 2008+ commercial cobot anchor (Odense Denmark, SDU spinout). 17-year-deep public-disclosure prior art for: 6-DoF anthropomorphic cobot at the educational/industrial price point, ISO 10218 + ISO/TS 15066 collaborative-safety compliance, PolyScope teach-pendant programming model. **The architectural anchor of every subsequent commercial cobot** — Doosan (round-22 entry), Franka Emika, Aubo, Elite, Jaka, Universal Robots' own e-Series. The Odense Denmark cobot cluster (Robocluster consortium) is the Nordic robotics anchor. Direct shielding for any commercial humanoid claim that includes cobot-class collaborative-arm derivative applications. Closes the Denmark / Nordic gap (corpus had no Danish entries prior).

**Sources:**

1. Universal Robots corporate site (universal-robots.com).
2. Teradyne 10-K SEC filings (post-2015 acquisition).
3. Wikipedia 'Universal Robots' (en.wikipedia.org/wiki/Universal_Robots).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `6b58593`.*
