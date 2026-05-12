---
title: "control-numerical"
parent: "Invalidity Contentions"
nav_order: 107
layout: default
---

# Invalidity Contention Packet — `control-numerical`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-numerical`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1952-03  
**Most recent disclosure:** 1973-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-numerical`.

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

### 1952-03 — MIT Numerical Control (NC machine tool; 1952)

- **id:** `mit-numerical-control-1952`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT Servomechanisms Laboratory + John T. Parsons + US Air Force
- **disclosure citation:** MIT Servomechanisms Laboratory (with John T. Parsons + US Air Force). First numerically-controlled milling machine demonstrated March 1952 (a modified Cincinnati Hydrotel). Parsons conceived the idea ~1948-1949; MIT built the prototype 1949-1952; the APT (Automatically Programmed Tool) language followed (Douglas T. Ross, 1956-1959).
- **disclosed subsystems:** `manipulator-arm`, `control-numerical`, `control-stored-program`

**Prior art notes:**

> MIT Numerical Control (MIT Servomechanisms Lab + Parsons + USAF 1952; APT language 1956-1959) is the first numerically-controlled machine tool. 73-year-deep public-domain prior art. The bridge from Jacquard punch cards to modern CNC + industrial robots.

**Sources:**

1. MIT Servomechanisms Laboratory NC machine documentation, 1952.

---

### 1973-04 — Cincinnati Milacron T³ (first US revolute computer-controlled arm)

- **id:** `cincinnati-milacron-t3-1973`
- **corpus:** private
- **ip status:** public-domain
- **creator:** Cincinnati Milacron Inc. (Cincinnati, OH, USA); Richard Hohn
- **disclosure citation:** Cincinnati Milacron Inc. (Cincinnati, OH, USA). T³ ('The Tomorrow Tool') commercial reveal April 1973. First commercially available minicomputer-controlled industrial robot. Developed by Richard Hohn.
- **disclosed subsystems:** `manipulator-arm`, `actuator-hydraulic`, `control-numerical`

**Prior art notes:**

> Cincinnati Milacron T³ (Cincinnati 1973) is the first commercially available minicomputer-controlled industrial robot and first US revolute-config arm. 52-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from minicomputer-controlled anthropomorphic arms.

**Sources:**

1. collection.powerhouse.com.au/object/574553

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4e68247`.*
