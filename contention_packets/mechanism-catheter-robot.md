---
title: "mechanism-catheter-robot"
parent: "Invalidity Contentions"
nav_order: 111
layout: default
---

# Invalidity Contention Packet — `mechanism-catheter-robot`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-catheter-robot`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2007-08  
**Most recent disclosure:** 2012-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-catheter-robot`.

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

### 2007-08 — Hansen Medical Sensei catheter robotic system

- **id:** `sensei-hansen-medical-2009`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Hansen Medical (Mountain View, CA); now Auris Health / Johnson & Johnson
- **disclosure citation:** Hansen Medical, Inc. (Mountain View, CA). Sensei catheter robotic system FDA cleared August 2007. Subsequent: Magellan vascular system. Acquired by Auris Health 2016 → Johnson & Johnson 2019.
- **disclosed subsystems:** `mechanism-surgical-robot`, `mechanism-catheter-robot`, `control-master-slave-teleoperation`

**Prior art notes:**

> Hansen Medical Sensei (FDA cleared August 2007) is the canonical robotic catheter system for cardiac electrophysiology. 18-year-deep public-disclosure prior art. Distinct architectural branch from Intuitive da Vinci by application + kinematics. The Hansen→Auris→J&J lineage is the major intravascular robotic-surgery commercial platform.

**Sources:**

1. Hansen Medical / Auris Health / Johnson & Johnson corporate history.
2. FDA 510(k) Sensei clearance 2007.

---

### 2012-07 — CorPath GRX (Corindus / Siemens Healthineers)

- **id:** `corpath-grx-corindus-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Corindus Vascular Robotics (Waltham, MA); acquired by Siemens Healthineers 2019
- **disclosure citation:** Corindus Vascular Robotics, Inc. CorPath 200 FDA cleared July 2012; CorPath GRX FDA cleared October 2016. Acquired by Siemens Healthineers 2019.
- **disclosed subsystems:** `mechanism-surgical-robot`, `mechanism-catheter-robot`, `control-master-slave-teleoperation`

**Prior art notes:**

> Corindus CorPath GRX (FDA 2012/2016, Siemens Healthineers 2019) is the canonical robotic-PCI commercial platform. 13-year-deep public-disclosure prior art. Together with Hansen Medical Sensei (round-33 entry above), establishes the intravascular surgical-robot prior-art chain.

**Sources:**

1. Corindus / Siemens Healthineers corporate history.
2. FDA 510(k) CorPath 200 clearance 2012; CorPath GRX 2016.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `94b7a2a`.*
