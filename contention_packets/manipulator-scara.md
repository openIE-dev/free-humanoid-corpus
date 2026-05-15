---
title: "manipulator-scara"
parent: "Invalidity Contentions"
nav_order: 188
layout: default
---

# Invalidity Contention Packet — `manipulator-scara`

**Generated:** 2026-05-15  
**Cross-cut tag:** `manipulator-scara`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1978-01  
**Most recent disclosure:** 1983-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `manipulator-scara`.

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

### 1978-01 — Makino SCARA (Selective Compliance Assembly Robot Arm)

- **id:** `makino-scara-yamanashi-1978`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Yamanashi (Japan); Hiroshi Makino + 13-company consortium; productized by Sankyo Seiki, Pentel, NEC
- **disclosure citation:** Makino, H. et al. SCARA architecture developed at University of Yamanashi 1978-1981 in consortium with 13 Japanese companies. Productized by Sankyo Seiki, Pentel, and NEC starting 1981. Hiroshi Makino (Yamanashi University) is the inventor.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-scara`, `actuator-electric`

**Prior art notes:**

> Makino SCARA (Yamanashi University + 13-company consortium 1978-1981) is the foundational SCARA architecture. 47-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from SCARA-architecture assembly arms. The dominant assembly-arm architecture worldwide; productized by every major arm OEM.

**Sources:**

1. en.wikipedia.org/wiki/SCARA

---

### 1983-01 — Epson SCARA (global SCARA volume leader)

- **id:** `epson-scara-1983`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Seiko Epson Corporation (Suwa, Japan)
- **disclosure citation:** Seiko Epson Corporation (Suwa, Japan; Suwa Seikosha). First Epson SCARA reveal 1983 (originally for in-house quartz-watch assembly automation). Now #1 SCARA-arm maker worldwide. Modern G-series (2000s+), LS-series, N-series 6-axis.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-scara`, `actuator-electric`

**Prior art notes:**

> Epson SCARA (Seiko Epson Suwa 1983+) is the global SCARA-arm volume leader. 42-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from SCARA-architecture assembly arms. Lineage descends from Makino SCARA (round-45).

**Sources:**

1. en.wikipedia.org/wiki/Epson_Robots

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `cd2f551`.*
