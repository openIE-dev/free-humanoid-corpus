---
title: "control-impedance-control"
parent: "Invalidity Contentions"
nav_order: 51
layout: default
---

# Invalidity Contention Packet — `control-impedance-control`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-impedance-control`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1994-09  
**Most recent disclosure:** 2008-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-impedance-control`.

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

### 1994-09 — SensAble Phantom haptic device

- **id:** `sensable-phantom-1994`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** MIT Salisbury Robotics Lab (Thomas Massie + Kenneth Salisbury); commercialized via SensAble Technologies / Geomagic / 3D Systems
- **disclosure citation:** Massie, T. H., Salisbury, J. K. 'The PHANTOM Haptic Interface: A Device for Probing Virtual Objects'. ASME Dynamic Systems and Control Division 1994. MIT Salisbury Robotics Lab; commercialized via SensAble Technologies (founded 1993, MIT spinout). Acquired by Geomagic 2012; subsequently 3D Systems (Geomagic Touch, Phantom Premium product lines).
- **disclosed subsystems:** `control-haptic-rendering`, `mechanism-parallel-kinematic-haptic`, `control-impedance-control`

**Prior art notes:**

> The SensAble Phantom is the canonical foundational stylus haptic interface (Massie + Salisbury MIT 1994). 31-year-deep public-disclosure prior art for: 6-DoF stylus haptic device, parallel-kinematic haptic mechanism, OpenHaptics SDK, impedance-controlled force rendering at kHz rates. **Salisbury's Stanford-JPL hand (corpus entry) → Salisbury's MIT haptic interface (this entry) → da Vinci Surgical (round-16) is one architectural lineage**; Salisbury was advisor on da Vinci's EndoWrist instrument design. Direct shielding for any commercial humanoid claim on stylus-based teleoperation interfaces or impedance-controlled haptic rendering.

**Sources:**

1. Massie, T. H., Salisbury, J. K. ASME DSC 1994.
2. 3D Systems Geomagic Touch product page.
3. OpenHaptics SDK (openhaptics.com, archived).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `1a8c3f7`.*
