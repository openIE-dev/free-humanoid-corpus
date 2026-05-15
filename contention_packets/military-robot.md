---
title: "military-robot"
parent: "Invalidity Contentions"
nav_order: 241
layout: default
---

# Invalidity Contention Packet — `military-robot`

**Generated:** 2026-05-15  
**Cross-cut tag:** `military-robot`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2000-01  
**Most recent disclosure:** 2002-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `military-robot`.

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

### 2000-01 — Foster-Miller TALON / SWORDS (armed military robot)

- **id:** `talon-foster-miller-2000`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Foster-Miller Inc. (Waltham, MA, USA) → QinetiQ North America 2004
- **disclosure citation:** Foster-Miller Inc. (Waltham, MA, USA; acquired by QinetiQ 2004). TALON deployed ~2000; SWORDS armed variant deployed Iraq 2007 (first armed ground robot deployed to combat). ~3,000+ units delivered.
- **disclosed subsystems:** `military-robot`, `mechanism-tracked-locomotion`

**Prior art notes:**

> Foster-Miller TALON / SWORDS (Waltham MA 2000+; → QinetiQ 2004) is the armed military ground robot — first weaponized UGV deployed to combat. 25-year-deep public-disclosure prior art.

**Sources:**

1. Foster-Miller / QinetiQ TALON documentation.

---

### 2002-01 — iRobot PackBot (military EOD / reconnaissance robot)

- **id:** `packbot-irobot-2002`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** iRobot Corporation (Bedford, MA, USA); → Endeavor Robotics 2016 → FLIR/Teledyne 2019
- **disclosure citation:** iRobot Corporation (Bedford, MA, USA). PackBot deployed 2002 in Afghanistan (cave reconnaissance) and 2003 in Iraq. ~2,000 units delivered to US military. iRobot defense division spun off as Endeavor Robotics 2016 (acquired by FLIR/Teledyne 2019).
- **disclosed subsystems:** `military-robot`, `mechanism-tracked-locomotion`

**Prior art notes:**

> iRobot PackBot (Bedford MA 2002+) is the canonical military EOD / reconnaissance robot. 23-year-deep public-disclosure prior art.

**Sources:**

1. iRobot defense division historical documentation.

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
