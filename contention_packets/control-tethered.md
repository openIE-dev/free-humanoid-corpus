---
title: "control-tethered"
parent: "Invalidity Contentions"
nav_order: 124
layout: default
---

# Invalidity Contention Packet — `control-tethered`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-tethered`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 1965-01  
**Most recent disclosure:** 2003-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-tethered`.

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

### 1965-01 — CURV (Cable-controlled Underwater Recovery Vehicle)

- **id:** `curv-us-navy-1965`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** US Navy Naval Ocean Systems Center (NOSC); Jack L. Sayer Jr.
- **disclosure citation:** US Navy Naval Ocean Systems Center (NOSC) (USA); Jack L. Sayer Jr. CURV-I 1965 — Cable-controlled Underwater Recovery Vehicle, recovered the 1966 Palomares H-bomb. Successor CURV-III 1972 (7,200 ft depth) recovered Pisces III crew 1973.
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> CURV (US Navy NOSC 1965+) is the foundational tethered-ROV architecture. 60-year-deep public-domain prior art. Direct shielding for any commercial humanoid or ROV claim deriving from cable-controlled underwater recovery vehicles. Predicate for every tethered ROV downstream.

**Sources:**

1. en.wikipedia.org/wiki/CURV

---

### 1995-03 — Kaiko ROV (first ROV to Challenger Deep)

- **id:** `kaiko-jamstec-1995`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** JAMSTEC (Japan)
- **disclosure citation:** JAMSTEC (Japan). Kaiko first dive to Challenger Deep March 1995. ~296 dives to 1999 servicing. Lost May 29, 2003 in typhoon. Successor: ABISMO (round-47 lineage).
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> Kaiko (JAMSTEC 1995-2003) is the first ROV ever to reach Challenger Deep. 30-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or ROV claim deriving from full-ocean-depth tethered ROVs.

**Sources:**

1. en.wikipedia.org/wiki/Kaikō_ROV

---

### 1999-01 — VideoRay Pro / Mission Specialist (microROV market leader)

- **id:** `videoray-pro-1999`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** VideoRay LLC (Pottstown, PA, USA); Scott Bentley founder
- **disclosure citation:** VideoRay LLC (Pottstown, PA, USA; founded 1999). VideoRay Pro (1999) → Pro 4 → Mission Specialist (2017+) → Defender (US Navy EOD 2017+). Global volume leader in microROV; >3,000 units delivered.
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> VideoRay Pro / Mission Specialist (Pottstown PA 1999+) is the global volume leader in microROV. 26-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or ROV claim deriving from small-class portable observation/inspection ROVs.

**Sources:**

1. en.wikipedia.org/wiki/VideoRay_UROVs
2. videoray.com

---

### 2003-01 — Hercules + Argus (Ballard deep-archaeology two-body ROV)

- **id:** `hercules-argus-ballard-2003`
- **corpus:** private
- **ip status:** trade-secret (academic-publication for some systems)
- **creator:** Institute for Exploration + Inner Space Center + Ocean Exploration Trust (Bob Ballard); USA
- **disclosure citation:** Institute for Exploration / Inner Space Center / Ocean Exploration Trust (Bob Ballard) (USA). Hercules + Argus two-body deep-archaeology ROV system 2003+. Pair operates tethered: Argus (tow-sled providing lighting + 2nd-camera perspective) + Hercules (work-class ROV with manipulator + sample collection).
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> Hercules + Argus (Ballard 2003+) is the canonical deep-archaeology two-body ROV system. 22-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or ROV claim deriving from two-body cultural-heritage ROV operations.

**Sources:**

1. Ocean Exploration Trust + E/V Nautilus documentation.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `88b8beb`.*
