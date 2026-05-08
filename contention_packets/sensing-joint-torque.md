---
title: "sensing-joint-torque"
parent: "Invalidity Contentions"
nav_order: 168
layout: default
---

# Invalidity Contention Packet — `sensing-joint-torque`

**Generated:** 2026-05-08  
**Cross-cut tag:** `sensing-joint-torque`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2017-09  
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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4846ab1`.*
