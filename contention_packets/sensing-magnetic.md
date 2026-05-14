---
title: "sensing-magnetic"
parent: "Invalidity Contentions"
nav_order: 267
layout: default
---

# Invalidity Contention Packet — `sensing-magnetic`

**Generated:** 2026-05-14  
**Cross-cut tag:** `sensing-magnetic`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1879-01  
**Most recent disclosure:** 1960-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-magnetic`.

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

### 1879-01 — Hall Effect (Edwin Hall 1879) + Hall sensors

- **id:** `hall-effect-sensor-1879`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Johns Hopkins University; Edwin Herbert Hall (PhD student)
- **disclosure citation:** Hall, E.H. 'On a New Action of the Magnet on Electric Currents'. American Journal of Mathematics 2(3):287-292, 1879. Johns Hopkins University (Hall was a PhD student). Practical Hall-effect sensors became feasible with semiconductors in the 1950s-1960s.
- **disclosed subsystems:** `sensing-magnetic`

**Prior art notes:**

> The Hall Effect (Edwin Hall Johns Hopkins 1879) + Hall sensors are the foundational magnetic-field sensing effect. 146-year-deep public-domain prior art. Ubiquitous in every motor + robot joint.

**Sources:**

1. Hall, E.H. American Journal of Mathematics 2(3):287-292, 1879.

---

### 1960-01 — Strapdown IMU + Inertial Navigation (1960s; mechanical → MEMS lineage)

- **id:** `imu-strapdown-1960s`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT Instrumentation Laboratory (Charles Stark Draper Laboratory); Draper + collaborators
- **disclosure citation:** Strapdown inertial navigation theory developed at MIT Instrumentation Laboratory (Charles Stark Draper) + others through the 1950s-1960s. First operational strapdown system: NASA SIRU (Strapdown Inertial Reference Unit), 1971. Subsequent: Boeing 757/767 strapdown INS (1980s); MEMS IMU revolution (corpus mems-imu-foundational-1990s) 1990s+.
- **disclosed subsystems:** `sensing-magnetic`, `sensing-localization`

**Prior art notes:**

> Strapdown IMU + Inertial Navigation (MIT Instrumentation Laboratory / Draper Lab 1960s; operational SIRU 1971) is the foundational concept of strapped-down inertial navigation. 60+-year-deep public-domain prior art. Directly underlies MEMS IMU (corpus mems-imu-foundational-1990s); fused with Kalman filter (corpus) + GPS (corpus) for every modern robot's navigation stack.

**Sources:**

1. Charles Stark Draper Laboratory inertial navigation documentation.

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
