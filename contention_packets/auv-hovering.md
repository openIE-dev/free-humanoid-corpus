---
title: "auv-hovering"
parent: "Invalidity Contentions"
nav_order: 29
layout: default
---

# Invalidity Contention Packet — `auv-hovering`

**Generated:** 2026-05-14  
**Cross-cut tag:** `auv-hovering`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1995-06  
**Most recent disclosure:** 2006-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `auv-hovering`.

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

### 1995-06 — Autonomous Benthic Explorer (ABE; WHOI 1995)

- **id:** `abe-whoi-1995`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Woods Hole Oceanographic Institution; Dana Yoerger group
- **disclosure citation:** Yoerger, D. et al. / Woods Hole Oceanographic Institution (USA). ABE developed 1994; first mission 1995-1996. Lost at sea March 5, 2010 off Chile. 222 missions before loss.
- **disclosed subsystems:** `auv`, `auv-hovering`, `actuator-electric`

**Prior art notes:**

> ABE (WHOI 1995-2010) is the pioneering hovering AUV. 30-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or AUV claim deriving from hovering AUV architectures. Direct ancestor of Sentry (round-47).

**Sources:**

1. en.wikipedia.org/wiki/Autonomous_Benthic_Explorer

---

### 2006-04 — Sentry AUV (WHOI ABE successor; deep-search workhorse)

- **id:** `sentry-auv-whoi-2006`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Woods Hole Oceanographic Institution; Dana Yoerger group
- **disclosure citation:** Yoerger, D. et al. / Woods Hole Oceanographic Institution (USA). Sentry first deep-sea trials April 2006. Direct ABE successor; National Deep Submergence Facility workhorse for Deepwater Horizon (2010), hydrothermal-vent mapping, and deep-ocean exploration.
- **disclosed subsystems:** `auv`, `auv-hovering`, `actuator-electric`

**Prior art notes:**

> Sentry (WHOI 2006+) is the deep-search workhorse AUV — ABE successor. 19-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or AUV claim deriving from twin-hull hovering deep-search AUVs.

**Sources:**

1. en.wikipedia.org/wiki/Sentry_(AUV)

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `c61fc91`.*
