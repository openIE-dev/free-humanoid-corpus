---
title: "mechanism-variable-buoyancy-glider"
parent: "Invalidity Contentions"
nav_order: 148
layout: default
---

# Invalidity Contention Packet — `mechanism-variable-buoyancy-glider`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-variable-buoyancy-glider`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1989-01  
**Most recent disclosure:** 2001-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-variable-buoyancy-glider`.

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

### 1989-01 — Slocum Glider

- **id:** `slocum-glider-auv`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Henry Stommel (concept, WHOI 1989); Doug Webb (engineering, Webb Research Corp 1996); Teledyne Webb Research (current)
- **disclosure citation:** Stommel, H. 'The Slocum mission'. Oceanography vol. 2 no. 1, 1989 — concept paper. Webb, D. C., Simonetti, P. J., Jones, C. P. 'SLOCUM: An Underwater Glider Propelled by Environmental Energy'. IEEE J. Oceanic Engineering vol. 26 no. 4 2001 — first deployments. Commercialized by Webb Research Corp.; acquired by Teledyne 2008.
- **disclosed subsystems:** `mechanism-variable-buoyancy-glider`, `mechanism-pitch-roll-trim`, `mechanism-pressure-hull`, `control-mission-script`, `control-acoustic-comms`

**Prior art notes:**

> Slocum is the canonical variable-buoyancy underwater glider. Stommel's 1989 concept paper and Webb's 2001 IEEE J. Oceanic Engineering paper establish a 36-year-deep open-academic prior-art chain on **variable-buoyancy propulsion as an alternative to thrust-active station-keeping**. Directly relevant to free-humanoid-submersible: the architectural choice between 'negatively-buoyant + thrust-active' (submersible's commitment) and 'variable-buoyancy + glider' (Slocum lineage) is a documented public-domain trade-off space. Any commercial AUV claim that one approach is novel art faces this 36-year-deep public-domain branching point.

**Sources:**

1. Stommel, H. 'The Slocum mission', Oceanography 2(1) 1989.
2. Webb, Simonetti, Jones, IEEE J. Oceanic Eng. 26(4) 2001.
3. Schofield et al. 'Slocum gliders: Robust and ready', J. Field Robotics 2007.
4. Rutgers Glider Lab operational record (rucool.marine.rutgers.edu).

---

### 2001-09 — Seaglider AUV

- **id:** `seaglider-auv-2001`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Washington Applied Physics Laboratory; Eriksen et al.
- **disclosure citation:** Eriksen, C. C., Osse, T. J., Light, R. D., et al. 'Seaglider: A Long-Range Autonomous Underwater Vehicle for Oceanographic Research'. IEEE J. Oceanic Engineering vol. 26 no. 4 2001.
- **disclosed subsystems:** `mechanism-variable-buoyancy-glider`, `mechanism-pitch-roll-trim`, `mechanism-pressure-hull`, `control-mission-script`, `control-acoustic-comms`

**Prior art notes:**

> Seaglider is the second canonical variable-buoyancy glider lineage, with a fully open academic disclosure (Eriksen 2001). Together with Slocum, establishes that the variable-buoyancy-glider architecture is a 24-year-deep open-academic prior-art branch. Directly shields free-humanoid-submersible's architectural commitment to thrust-active vs. variable-buoyancy as the documented public choice.

**Sources:**

1. Eriksen et al. IEEE J. Oceanic Eng. 26(4) 2001.
2. Kongsberg Seaglider product page (kongsberg.com/maritime/products/marine-robotics/autonomous-underwater-vehicles/seaglider/).
3. UW APL Seaglider operational record.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `a27a0cf`.*
