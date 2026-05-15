---
title: "auv-glider"
parent: "Invalidity Contentions"
nav_order: 28
layout: default
---

# Invalidity Contention Packet — `auv-glider`

**Generated:** 2026-05-15  
**Cross-cut tag:** `auv-glider`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2001-01  
**Most recent disclosure:** 2020-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `auv-glider`.

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

### 2001-01 — Spray underwater glider (Scripps + WHOI)

- **id:** `spray-glider-scripps-2001`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Scripps Institution of Oceanography + WHOI; Russ Davis, Jeff Sherman, Breck Owens, Doug Webb
- **disclosure citation:** Davis, R., Sherman, J. / Scripps Institution of Oceanography, with Owens, B., Webb, D. / Woods Hole Oceanographic Institution (USA). Spray glider 2001. First major Gulf Stream crossing September 11 2004. One of the three foundational US glider designs alongside Slocum (corpus) + Seaglider (corpus).
- **disclosed subsystems:** `auv-glider`, `mechanism-buoyancy-driven`

**Prior art notes:**

> Spray glider (Scripps + WHOI 2001+) is one of the three foundational US underwater gliders. 24-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or AUV claim deriving from buoyancy-driven gliders. Sister to Slocum (corpus slocum-glider-auv) and Seaglider (corpus seaglider-auv-2001).

**Sources:**

1. scripps.ucsd.edu/news/underwater-robot-makes-history-crossing-gulf-stream

---

### 2020-07 — Petrel-X glider (China full-ocean-depth glider)

- **id:** `petrel-x-tianjin-china-2020`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Tianjin University (China); subsequent Laoshan Laboratory partnership
- **disclosure citation:** Tianjin University (China). Petrel-II (2014, 1,500 m). Petrel-X 10,600 m dive in Mariana Trench July 2020 — first Chinese full-ocean-depth glider. Petrel-XPLUS (2023, Tianjin + Laoshan Laboratory, 5,000 km range, 80 dives to 11,000 m on a single mission).
- **disclosed subsystems:** `auv-glider`, `mechanism-buoyancy-driven`

**Prior art notes:**

> Petrel-X / Petrel-XPLUS (Tianjin University 2020-2023) is the first Chinese full-ocean-depth underwater glider. 5-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or AUV claim deriving from full-ocean-depth Chinese underwater gliders.

**Sources:**

1. en.tju.edu.cn/info/1011/4092.htm

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
