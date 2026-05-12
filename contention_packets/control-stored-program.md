---
title: "control-stored-program"
parent: "Invalidity Contentions"
nav_order: 133
layout: default
---

# Invalidity Contention Packet — `control-stored-program`

**Generated:** 2026-05-11  
**Cross-cut tag:** `control-stored-program`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1954-12  
**Most recent disclosure:** 1961-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-stored-program`.

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

### 1954-12 — Devol Programmed Article Transfer (foundational arm patent)

- **id:** `devol-programmed-article-transfer-1954`
- **corpus:** academic
- **ip status:** public-domain (expired)
- **creator:** George C. Devol Jr.; later Unimation co-founder with Joseph Engelberger
- **disclosure citation:** Devol, G.C. 'Programmed Article Transfer'. US Patent 2,988,237; filed December 10, 1954; granted June 13, 1961. The originating patent for programmable manipulator arms. George Devol subsequently co-founded Unimation with Joseph Engelberger 1956.
- **disclosed subsystems:** `manipulator-arm`, `control-stored-program`

**Prior art notes:**

> Devol's 1954 'Programmed Article Transfer' patent (US 2,988,237) is the originating patent for programmable manipulator arms. 71-year-deep public-domain prior art. The foundational predicate for every commercial robot arm. Direct shielding for any commercial humanoid claim deriving from programmable position-controlled manipulator arms.

**Sources:**

1. US Patent 2,988,237 'Programmed Article Transfer'.
2. automate.org/robotics/engelberger/joseph-engelberger-unimate

---

### 1961-01 — Unimate (the first industrial robot arm)

- **id:** `unimate-unimation-1961`
- **corpus:** private
- **ip status:** public-domain
- **creator:** Unimation Inc. (Danbury, CT, USA); George Devol + Joseph Engelberger
- **disclosure citation:** Devol, G.C. + Engelberger, J.F. / Unimation Inc. (Danbury, CT, USA; founded 1956). Unimate first deployed at GM Inland Fisher Guide plant, Ewing Township NJ, 1961. The first industrial robot arm. Robot Hall of Fame inductee 2003.
- **disclosed subsystems:** `manipulator-arm`, `actuator-hydraulic`, `control-stored-program`

**Prior art notes:**

> Unimate (Unimation Danbury CT 1961) is the first industrial robot arm. 64-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from industrial articulated robot arms. The Kawasaki 1968 license seeded the entire Japanese arm-OEM industry; the Stäubli 1989 acquisition transferred the lineage to Europe.

**Sources:**

1. en.wikipedia.org/wiki/Unimate
2. automate.org/robotics/engelberger/joseph-engelberger-unimate

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0e58219`.*
