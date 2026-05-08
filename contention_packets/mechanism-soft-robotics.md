---
title: "mechanism-soft-robotics"
parent: "Invalidity Contentions"
nav_order: 109
layout: default
---

# Invalidity Contention Packet — `mechanism-soft-robotics`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-soft-robotics`  
**Entries:** 3 (1 commons-grade, 2 draft)  
**Earliest disclosure:** 2000-01  
**Most recent disclosure:** 2014-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-soft-robotics`.

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

### 2000-01 — University of Auckland (NZ) robotics *(draft)*

- **id:** `auckland-university-nz-robotics`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Auckland (Auckland, New Zealand)
- **disclosure citation:** University of Auckland (Auckland, New Zealand). Robotics + AI research distributed across Auckland Bioengineering Institute (ABI), Department of Mechanical and Mechatronics Engineering, Department of Computer Science. Notable: bioengineering robots, soft robotics (collaborator with Harvard), agricultural robotics.
- **disclosed subsystems:** `control-research-cluster`, `mechanism-soft-robotics`, `mechanism-bioengineering-robot`

**Prior art notes:**

> University of Auckland is New Zealand's largest research university and the dominant NZ robotics academic cluster. **First entry in the corpus from New Zealand** — closes a regional gap. Together with CSIRO Data61 (round-23, Australia), brings Antipodean coverage to 2.

**Sources:**

1. University of Auckland corporate site (auckland.ac.nz).
2. Auckland Bioengineering Institute (abi.auckland.ac.nz).

---

### 2000-01 — TU Delft Netherlands robotics *(draft)*

- **id:** `tu-delft-netherlands-robotics`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Delft University of Technology (TU Delft, Netherlands)
- **disclosure citation:** Delft University of Technology (TU Delft), Netherlands. Cognitive Robotics + Robotics Institute. Notable: Wisse passive-dynamic walker (round-19 collins-ruina-tedrake-wisse-passive-walker-2005 entry includes Wisse), TU Delft Robotics Institute spinouts (SenseGlove round-19 entry). The dominant Dutch academic robotics cluster.
- **disclosed subsystems:** `control-research-cluster`, `mechanism-passive-dynamic-walking`, `mechanism-soft-robotics`

**Prior art notes:**

> TU Delft is the Netherlands' flagship robotics academic anchor. Direct ancestor of SenseGlove (round-19) and contributor to Collins-Ruina-Tedrake-Wisse passive-dynamic walker (round-19). Brings Netherlands depth in the corpus from 3 to 4 entries.

**Sources:**

1. TU Delft corporate site (tudelft.nl).
2. TU Delft Cognitive Robotics (cor.tudelft.nl).
3. TU Delft Robotics Institute (robotics.tudelft.nl).

---

### 2014-09 — Harvard Soft Robotics Toolkit

- **id:** `harvard-soft-robotics-toolkit-2017`
- **corpus:** academic
- **ip status:** open-copyleft
- **creator:** Harvard Biodesign Lab + Harvard Microrobotics Lab; Conor Walsh, Robert Wood, Dónal Holland et al.
- **disclosure citation:** Holland, D. P., Park, E. J., Polygerinos, P., Bennett, G. J., Walsh, C. J. 'The Soft Robotics Toolkit: Shared Resources for Research and Design'. Soft Robotics Vol. 1 No. 3 2014. Wood + Walsh groups, Harvard Biodesign Lab + Harvard Microrobotics Lab.
- **disclosed subsystems:** `actuator-soft-elastomeric`, `actuator-pneumatic`, `sensing-tactile`, `mechanism-soft-robotics`

**Prior art notes:**

> The Harvard Soft Robotics Toolkit is the canonical open-academic soft-robotics fabrication library (Holland et al. Soft Robotics 1(3) 2014; Wood + Walsh group lineage). 11-year-deep open prior art for: elastomeric soft actuators (PneuNets, fiber-reinforced bending), soft sensors, complete fabrication recipes. Direct shielding for any commercial humanoid claim on soft-actuator fabrication or soft-sensor design. Particularly relevant for any future free-humanoid-soft variant.

**Sources:**

1. Holland et al. Soft Robotics 1(3) 2014.
2. Soft Robotics Toolkit site (softroboticstoolkit.com).
3. Wood + Walsh group publications (biodesign.seas.harvard.edu).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `46e9af2`.*
