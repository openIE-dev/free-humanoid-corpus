---
title: "sensing-tactile"
parent: "Invalidity Contentions"
nav_order: 147
layout: default
---

# Invalidity Contention Packet — `sensing-tactile`

**Generated:** 2026-05-08  
**Cross-cut tag:** `sensing-tactile`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2009-12  
**Most recent disclosure:** 2014-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-tactile`.

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

### 2009-12 — Modular Prosthetic Limb (MPL)

- **id:** `apl-mpl-revolutionizing-prosthetics-2009`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** JHU Applied Physics Laboratory; led under DARPA Revolutionizing Prosthetics program (Geoffrey Ling DARPA PM)
- **disclosure citation:** Johns Hopkins Applied Physics Laboratory. Modular Prosthetic Limb (MPL) v1.0 completed December 2009 under DARPA Revolutionizing Prosthetics program (2006-present). Johnson, M. J. et al. clinical evaluation: Scientific Reports 11 (2021). DARPA + APL + Johns Hopkins Medicine + multiple consortium partners.
- **disclosed subsystems:** `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `sensing-tactile`, `sensing-fingertip-tactile`, `control-bci`, `control-prosthetic-control`

**Prior art notes:**

> The Modular Prosthetic Limb is the canonical sophisticated anthropomorphic prosthetic arm + hand from the DARPA Revolutionizing Prosthetics program (APL/JHU 2009+). 16-year-deep public-domain prior art for: 25-DoF anthropomorphic arm-and-hand at human-limb mass, integrated 100+-sensor tactile/position/force network, BCI-controlled prosthetic operation. Direct shielding for any commercial humanoid claim on anthropomorphic arm + hand integration. Particularly relevant for Tesla Optimus Gen 3 (round-15 entry, 22-DoF hands × 50 actuators) — the MPL's 25-DoF arm-and-hand at 100+ sensors establishes 16-year-deep prior art at the architectural level.

**Sources:**

1. JHU APL Revolutionizing Prosthetics page (jhuapl.edu/work/projects-and-missions/revolutionizing-prosthetics).
2. DARPA Revolutionizing Prosthetics page (darpa.mil/research/programs/revolutionizing-prosthetics).
3. Johnson et al. Scientific Reports 11 2021 ('Clinical evaluation of the Revolutionizing Prosthetics modular prosthetic limb system').
4. Bridges, M. M. et al. 'The Modular Prosthetic Limb: A Year of Operational Experience' (APL Tech Digest 2011).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4440aa4`.*
