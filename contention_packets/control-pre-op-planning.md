---
title: "control-pre-op-planning"
parent: "Invalidity Contentions"
nav_order: 111
layout: default
---

# Invalidity Contention Packet — `control-pre-op-planning`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-pre-op-planning`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1992-01  
**Most recent disclosure:** 2017-08

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-pre-op-planning`.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2aee416`.*
