---
title: "mechanism-hexapod"
parent: "Invalidity Contentions"
nav_order: 127
layout: default
---

# Invalidity Contention Packet — `mechanism-hexapod`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-hexapod`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1965-06  
**Most recent disclosure:** 2000-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-hexapod`.

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

### 1965-06 — Stewart platform / Gough-Stewart parallel mechanism

- **id:** `stewart-platform-gough-1965`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Bristol; D. Stewart (with antecedent V. E. Gough at Dunlop tire Ltd 1947)
- **disclosure citation:** Stewart, D. 'A Platform with Six Degrees of Freedom'. Proceedings of the Institution of Mechanical Engineers 180(1) 1965. Antecedent: Gough, V. E., Whitehall, S. G. 'Universal Tyre Test Machine' FISITA 9th International Conference 1962.
- **disclosed subsystems:** `mechanism-parallel-kinematic`, `mechanism-stewart-platform`, `mechanism-hexapod`

**Prior art notes:**

> The Stewart platform (Stewart Proc. IME 1965 + Gough Dunlop 1947) is the foundational 6-DoF parallel mechanism. 60-year-deep public-domain prior art. The architectural anchor of every subsequent parallel-kinematic system: flight simulators, motion bases, **the SensAble Phantom haptic interface (round-18)** + **Force Dimension Sigma.7 (round-18)** parallel-kinematic haptic devices, parallel-kinematic machine tools. Direct shielding for any commercial humanoid claim that uses parallel mechanisms or hexapod-class actuator architectures.

**Sources:**

1. Stewart, D. Proc. IME 180(1) 1965.
2. Gough, V. E., Whitehall, S. G. FISITA 1962.

---

### 2000-04 — RHex hexapod (Saranli-Buehler-Koditschek)

- **id:** `saranli-buehler-koditschek-rhex-ijrr-2001`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** McGill University + UMich + UPenn; Uluc Saranli, Martin Buehler, Daniel Koditschek
- **disclosure citation:** Saranli, U., Buehler, M., Koditschek, D. E. 'RHex: A Simple and Highly Mobile Hexapod Robot'. International Journal of Robotics Research 20(7) 2001. ICRA 2000 first publication. McGill University + University of Michigan + University of Pennsylvania. Saranli later moved to METU Ankara and continued the SLIP-model research lineage that informs Turkish academic robotics.
- **disclosed subsystems:** `mechanism-hexapod`, `mechanism-whegs`, `mechanism-passive-spring`, `control-tripod-gait`, `control-rough-terrain-locomotion`

**Prior art notes:**

> RHex (Saranli-Buehler-Koditschek IJRR 2001) is the foundational simple hexapod robot. 24-year-deep public-domain prior art. **The architectural ancestor of the STAR family** (corpus round-10 entries star-fearing-2013 + descendants → DSTAR 2026). Saranli later moved to METU Ankara, continuing the SLIP-model research lineage that informs the round-24 METU Turkey aggregator. Direct shielding for any commercial humanoid claim deriving from simple-leg or wheel-leg-hybrid morphologies.

**Sources:**

1. Saranli, U., Buehler, M., Koditschek, D. E. IJRR 20(7) 2001.
2. Saranli, U., Buehler, M., Koditschek, D. E. ICRA 2000.
3. Saranli post-RHex career at METU Ankara.

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
