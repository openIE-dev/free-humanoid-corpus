---
title: "sensing-localization"
parent: "Invalidity Contentions"
nav_order: 266
layout: default
---

# Invalidity Contention Packet — `sensing-localization`

**Generated:** 2026-05-14  
**Cross-cut tag:** `sensing-localization`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1960-01  
**Most recent disclosure:** 1978-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-localization`.

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

### 1978-02 — GPS / NAVSTAR (US DoD 1978; satellite navigation)

- **id:** `gps-navstar-1978`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** US Department of Defense (Roger Easton NRL + Bradford Parkinson USAF + Aerospace Corporation)
- **disclosure citation:** US Department of Defense. NAVSTAR GPS — first Block I satellite launched February 1978. Full Operational Capability declared April 1995. Concept developed 1973 (Roger Easton/NRL Timation + Bradford Parkinson/USAF 621B + Aerospace Corp). Selective Availability disabled May 2000 (civilian precision improved 10x).
- **disclosed subsystems:** `sensing-localization`

**Prior art notes:**

> GPS / NAVSTAR (US DoD 1978-1995) is the foundational satellite navigation system. 47-year-deep public-domain prior art. Global outdoor localization for every outdoor robot + drone + AV.

**Sources:**

1. US DoD NAVSTAR GPS documentation.

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
