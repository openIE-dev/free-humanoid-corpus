---
title: "manipulator-parallel"
parent: "Invalidity Contentions"
nav_order: 185
layout: default
---

# Invalidity Contention Packet — `manipulator-parallel`

**Generated:** 2026-05-12  
**Cross-cut tag:** `manipulator-parallel`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1985-01  
**Most recent disclosure:** 2011-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `manipulator-parallel`.

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

### 1985-01 — Clavel Delta Robot (EPFL 1985 patent)

- **id:** `clavel-delta-epfl-1985`
- **corpus:** academic
- **ip status:** public-domain (EPFL patent expired 2007)
- **creator:** EPFL (Lausanne, Switzerland); Reymond Clavel + Marc-Olivier Demaurex
- **disclosure citation:** Clavel, R., Demaurex, M.-O. 'Delta, A Fast Robot with Parallel Geometry'. 18th International Symposium on Industrial Robots 1988; original patent 1985 (EP 0250470, expired 2007). EPFL (École Polytechnique Fédérale de Lausanne, Switzerland). Commercialized 1987 via Demaurex SA (Romont, Switzerland; acquired by Bosch 1999, then to ABB ecosystem).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-parallel`, `manipulator-delta`, `actuator-electric`

**Prior art notes:**

> Clavel Delta Robot (EPFL 1985 patent; expired 2007) is the first parallel pick-and-place delta robot. 40-year-deep public-domain prior art (patent expired 2007). Direct shielding for any commercial humanoid claim deriving from parallel delta-mechanism arms. Ancestor of ABB FlexPicker (round-45), Adept Quattro, and every commercial delta robot.

**Sources:**

1. en.wikipedia.org/wiki/Reymond_Clavel

---

### 2011-01 — Mazor Renaissance / Stealth Spine guidance

- **id:** `mazor-renaissance-medtronic-2011`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Mazor Robotics Ltd. (Caesarea, Israel; Moshe Shoham Technion); → Medtronic 2018
- **disclosure citation:** Mazor Robotics Ltd. (Caesarea, Israel; founded 2000 by Moshe Shoham, Technion). SpineAssist FDA-cleared 2004; Renaissance FDA-cleared 2011 (1.5 mm accuracy bone-mounted spine guidance). Mazor X 2017. Acquired by Medtronic 2018 for USD 1.6B.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-parallel`, `actuator-electric`

**Prior art notes:**

> Mazor Robotics SpineAssist + Renaissance + Mazor X (Caesarea Israel 2004-2017+; Medtronic 2018) is the bone-mounted spine surgical guidance system. 21-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from bone-mounted parallel-mechanism surgical guidance arms.

**Sources:**

1. en.wikipedia.org/wiki/Mazor_Robotics

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `dd66352`.*
