---
title: "control-sensitivity-amplification"
parent: "Invalidity Contentions"
nav_order: 59
layout: default
---

# Invalidity Contention Packet — `control-sensitivity-amplification`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-sensitivity-amplification`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2004-03  
**Most recent disclosure:** 2018-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-sensitivity-amplification`.

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

### 2004-03 — Berkeley BLEEX (Lower Extremity Exoskeleton)

- **id:** `berkeley-bleex-kazerooni-2004`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** UC Berkeley HERL; Homayoon Kazerooni group
- **disclosure citation:** Kazerooni, H., Steger, R., Huang, L. 'Hybrid Control of the Berkeley Lower Extremity Exoskeleton (BLEEX)'. International Journal of Robotics Research 25(5-6) 2006. ICRA 2005 + IROS 2005 publications. UC Berkeley Human Engineering and Robotics Lab (HERL) under DARPA Exoskeletons for Human Performance Augmentation (EHPA) program.
- **disclosed subsystems:** `mechanism-exoskeleton`, `mechanism-hydraulic-actuator`, `control-sensitivity-amplification`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Berkeley BLEEX (Kazerooni et al. ICRA/IROS 2005, IJRR 2006) is the foundational academic load-carrying exoskeleton. 21-year-deep public-domain prior art for: energetically autonomous exoskeleton, hydraulic-actuated exoskeleton, sensitivity-amplification control. The architectural anchor of every subsequent commercial military/industrial exoskeleton: Sarcos Guardian XO (round-19 entry), Lockheed HULC (acquired Berkeley Bionics 2009), ReWalk (round-19 medical variant). Direct shielding for any commercial humanoid claim on exoskeleton load-carrying or hybrid human-robot locomotion.

**Sources:**

1. Kazerooni et al. IJRR 25(5-6) 2006.
2. Project page (bleex.me.berkeley.edu).
3. DARPA EHPA program documentation.

---

### 2018-09 — Sarcos Guardian XO

- **id:** `sarcos-guardian-xo-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Sarcos Robotics / Stephen Jacobsen (University of Utah Center for Engineering Design)
- **disclosure citation:** Sarcos Robotics / Sarcos Technology and Robotics Corporation (Salt Lake City, UT; founded 1983 by Stephen Jacobsen, University of Utah). Guardian XO commercial reveal 2018; subsequent deployments through 2023. Sarcos was a long-running DARPA exoskeleton recipient (XOS, XOS-2 hydraulic precursors). Acquired by Boeing 2024 + multiple subsequent restructurings.
- **disclosed subsystems:** `mechanism-exoskeleton`, `mechanism-full-body-exoskeleton`, `actuator-electric`, `control-sensitivity-amplification`

**Prior art notes:**

> Sarcos Guardian XO is the canonical 2018+ all-electric full-body industrial exoskeleton. 7-year-deep public-disclosure prior art for: 24-DoF whole-body industrial exoskeleton, all-electric (vs. hydraulic) heavy-lift exoskeleton. Architecturally extends Berkeley BLEEX (round-19) from lower-extremity-only to whole-body. Direct shielding for any commercial humanoid claim on full-body load-handling robotics — particularly for industrial-deployment commercial humanoid claims (Apptronik Apollo, Figure, Optimus all market industrial heavy-lift) which face 7-year-deep Sarcos commercial prior art.

**Sources:**

1. Sarcos corporate site (sarcos.com — historical, archived).
2. Boeing acquisition announcement 2024.
3. Wikipedia 'Sarcos' (en.wikipedia.org/wiki/Sarcos).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf892af`.*
