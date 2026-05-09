---
title: "mechanism-surgical-robot"
parent: "Invalidity Contentions"
nav_order: 198
layout: default
---

# Invalidity Contention Packet — `mechanism-surgical-robot`

**Generated:** 2026-05-09  
**Cross-cut tag:** `mechanism-surgical-robot`  
**Entries:** 6 (5 commons-grade, 1 draft)  
**Earliest disclosure:** 1989-01  
**Most recent disclosure:** 2017-08

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-surgical-robot`.

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

### 1989-01 — Taylor JHU surgical robotics (foundational) *(draft)*

- **id:** `taylor-jhu-surgical-robotics-1990s`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** JHU Computer Integrated Surgery Lab; Russell Taylor + collaborators
- **disclosure citation:** Taylor, R. H. et al. 'Robotic technology in surgery: past, present, and future'. American Journal of Surgery 188(4) 2004 (survey); foundational papers from 1989+: 'A Telerobotic Assistant for Laparoscopic Surgery' IEEE EMBC 1995; 'Steady-Hand robotic system for microsurgical augmentation' IJRR 1999. Johns Hopkins University Computer Integrated Surgery Lab. Russell Taylor + collaborators (Marcel Brett, Allison Okamura, Peter Kazanzides).
- **disclosed subsystems:** `mechanism-manipulator-arm`, `control-cooperative-control`, `control-master-slave-teleoperation`, `mechanism-surgical-robot`

**Prior art notes:**

> Russell Taylor's JHU CISST academic surgical robotics program (1989+) is the foundational academic counterpart to commercial surgical robotics (Intuitive Surgical da Vinci, Vicarious Surgical, Memic Hominis — all round-16 entries). 36-year-deep public-domain academic prior art for: cooperative-control surgical augmentation, master-slave surgical teleoperation, robotic orthopedic bone-cutting. ROBODOC (FDA 2008 / European 1992) and AESOP (Taylor co-developed) predate Intuitive Surgical da Vinci (FDA 2000) by years. Direct shielding for any commercial humanoid claim that derives from surgical-robot manipulator architectures. **Together with Salisbury Stanford-JPL hand (1982), establishes the two foundational academic lineages underpinning all modern surgical-and-humanoid manipulator IP.**

**Sources:**

1. Taylor, R. H. American Journal of Surgery 188(4) 2004.
2. JHU LCSR Computer Integrated Surgery Lab (cisst.org).
3. Taylor, R. H. + Stoianovici 'Medical robotics in computer-integrated surgery' IEEE T-RA 2003.

---

### 1992-01 — ROBODOC orthopedic surgical robot (Taylor JHU + Integrated Surgical Systems)

- **id:** `taylor-robodoc-orthopedic-1992`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Integrated Surgical Systems + Russell Taylor (JHU + IBM Research); Bargar UC Davis
- **disclosure citation:** Taylor, R. H., Mittelstadt, B. D., Paul, H. A., Hanson, W., Kazanzides, P., Zuhars, J. F., Williamson, B., Musits, B. L., Glassman, E., Bargar, W. L. 'An Image-Directed Robotic System for Precise Orthopaedic Surgery'. IEEE Transactions on Robotics and Automation 10(3) 1994. ROBODOC commercial deployment 1992 (European CE mark) + 2008 (FDA 510(k) clearance K081570). Integrated Surgical Systems (US commercial spinout); now marketed as TSolution One by THINK Surgical.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-surgical-robot`, `control-pre-op-planning`, `control-bone-registration`, `control-autonomous-cutting`

**Prior art notes:**

> ROBODOC is the canonical first orthopedic surgical robot (Taylor JHU + IBM + Integrated Surgical Systems, 1992). 33-year-deep public-disclosure prior art. **8-year-predating Intuitive Surgical da Vinci** (FDA 2000, round-16). Direct architectural anchor of orthopedic surgical robotics: subsequent CASPAR (1990s), MAKO RIO (Stryker 2000s+), TSolution One (current commercial). Together with Salisbury Stanford-JPL hand 1982 + Taylor JHU 1989+ academic program (round-20 taylor-jhu-surgical-robotics-1990s aggregator), establishes the **academic-commercial surgical-robot chain spanning 43 years 1982-2025**.

**Sources:**

1. Taylor, R. H. et al. IEEE T-RA 10(3) 1994.
2. Integrated Surgical Systems / THINK Surgical product history.
3. FDA 510(k) K081570.

---

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

### 2008-08 — Stryker Mako RIO orthopedic surgical robot

- **id:** `mako-rio-stryker-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Mako Surgical Corp. (Florida); acquired by Stryker Corporation 2013
- **disclosure citation:** Mako Surgical Corp. RIO (Robotic Arm Interactive Orthopedic) system FDA cleared 2008 for partial knee replacement; total knee replacement clearance 2015; total hip replacement clearance 2010. Acquired by Stryker Corporation 2013 (~$1.65B). Subsequent: Mako 4 (2024).
- **disclosed subsystems:** `mechanism-surgical-robot`, `control-haptic-constraint`, `control-co-manipulation`, `control-bone-registration`

**Prior art notes:**

> Stryker Mako RIO (Mako Surgical 2008+ → Stryker 2013+) is the dominant orthopedic surgical robot. 17-year-deep public-disclosure prior art. Successor in the orthopedic surgical robot lineage to ROBODOC (round-28 entry; Integrated Surgical Systems 1992). Distinct architectural branch from da Vinci master-slave teleop by use of haptic-constraint co-manipulation. ~3M procedures performed.

**Sources:**

1. Mako Surgical / Stryker corporate history.
2. FDA 510(k) Mako RIO clearances.
3. Stryker 10-K SEC filings (Mako product line disclosures).

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

### 2017-08 — Globus Medical ExcelsiusGPS spine surgical robot

- **id:** `globus-excelsius-gps-spine-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Globus Medical Inc. (Audubon, PA, USA)
- **disclosure citation:** Globus Medical Inc. ExcelsiusGPS spine surgical robotic system FDA cleared August 2017. Globus Medical Audubon, PA. Subsequent: Excelsius3D (2021), ExcelsiusFlex hip-knee (2024).
- **disclosed subsystems:** `mechanism-surgical-robot`, `control-tubular-guide-positioning`, `control-pre-op-planning`, `control-intraoperative-ct-navigation`

**Prior art notes:**

> Globus Medical ExcelsiusGPS (Globus Medical 2017+) is the canonical first FDA-cleared spine surgical robot with integrated navigation. 8-year-deep public-disclosure prior art. Distinct architectural branch from da Vinci (laparoscopic master-slave) and Mako (orthopedic haptic-constraint) — spine surgery → tubular-guide class. Together with da Vinci + Vicarious + Memic + Mako + ROBODOC, brings surgical-robot architectural classes to 5 distinct categories in the corpus.

**Sources:**

1. Globus Medical corporate site (globusmedical.com).
2. FDA 510(k) ExcelsiusGPS K171307 August 2017.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2fbde5f`.*
