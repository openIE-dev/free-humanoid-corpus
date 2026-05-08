---
title: "mechanism-control-fin"
parent: "Invalidity Contentions"
nav_order: 73
layout: default
---

# Invalidity Contention Packet — `mechanism-control-fin`

**Generated:** 2026-05-07  
**Cross-cut tag:** `mechanism-control-fin`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1995-01  
**Most recent disclosure:** 2003-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-control-fin`.

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

### 1995-01 — REMUS 100 AUV

- **id:** `kongsberg-remus-100-auv`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** WHOI Oceanographic Systems Lab (von Alt et al.); commercialized via Hydroid Inc.; now Kongsberg Maritime
- **disclosure citation:** von Alt, C., Allen, B., Austin, T., et al. 'Remote Environmental Measuring Unit System (REMUS): A Modular AUV for Coastal Oceanography'. Sea Technology, May 1995. Hydroid Inc. founded as WHOI spinout 2001; acquired by Kongsberg Maritime 2008. REMUS 100 commercially deployed 2001+.
- **disclosed subsystems:** `mechanism-thruster-axial`, `mechanism-control-fin`, `control-mission-script`, `control-dvl-positioning`, `control-acoustic-comms`

**Prior art notes:**

> REMUS 100 is the most-deployed compact-class survey AUV. Its lineage from the public academic WHOI publication (von Alt 1995) makes it a hybrid academic-commercial entry: the architectural specification is publicly disclosed, but Kongsberg's current commercial product carries trade-secret embellishments. Any humanoid AUV claim on 'compact survey AUV' or 'pre-programmed-mission underwater navigation' faces 30 years of public-academic + 24 years of commercial deployment prior art. The REMUS lineage complements Bluefin in the prior-art coverage of the survey AUV class.

**Sources:**

1. von Alt et al. Sea Technology May 1995.
2. Kongsberg Maritime REMUS 100 product page (kongsberg.com/maritime/products/marine-robotics/autonomous-underwater-vehicles/remus-100/).
3. B. Allen, T. Austin et al. OCEANS 2001 (REMUS commercial deployment paper).

---

### 2003-09 — Bluefin-21 AUV

- **id:** `bluefin-21-auv`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Bluefin Robotics Corp. (now General Dynamics Mission Systems / L3Harris)
- **disclosure citation:** Bluefin Robotics Corp. (founded 1997 as MIT-Sea-Grant spinout; acquired by General Dynamics 2016, divested to L3 Technologies 2020) Bluefin-21 product brochure (bluefinrobotics.com archived 2003+; current via gd-ms.com). Deployed 2014 in AF447 black-box search (Indian Ocean).
- **disclosed subsystems:** `mechanism-thruster-axial`, `mechanism-control-fin`, `control-mission-script`, `control-dvl-positioning`, `control-acoustic-comms`, `power-pressure-balanced-li-ion`

**Prior art notes:**

> Bluefin-21 is the canonical mid-class survey AUV. The 21-inch torpedo form factor is the Navy MCM/UUV standard. The Bluefin BPS pressure-balanced Li-ion battery system (commercial product since ~2008, with public academic-conference exposition in OCEANS 2010+) is the reference for any humanoid AUV claiming pressure-balanced subsea power. Directly anticipates free-humanoid-submersible's commitment to pressure-balanced Li-ion. The torpedo-form Bluefin is architecturally distinct from the hovering humanoid form, but its power, navigation, and acoustic-communication stacks are shared prior art.

**Sources:**

1. GD Mission Systems Bluefin-21 product page (gd-ms.com/products-services/uuvs/bluefin-21).
2. Vaganay et al., 'Bluefin Robotics' MTS/IEEE OCEANS proceedings 2003-2014.
3. DOD UUV Master Plan 2004 (publicly released).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b51f194`.*
