---
title: "mechanism-hydraulic-actuator"
parent: "Invalidity Contentions"
nav_order: 128
layout: default
---

# Invalidity Contention Packet — `mechanism-hydraulic-actuator`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-hydraulic-actuator`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2004-03  
**Most recent disclosure:** 2012-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-hydraulic-actuator`.

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

### 2005-12 — Boston Dynamics BigDog

- **id:** `boston-dynamics-bigdog-2005`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics; Marc Raibert et al. (under DARPA TUGV)
- **disclosure citation:** Boston Dynamics + Foster-Miller + Jet Propulsion Laboratory + Harvard Concord Field Station. BigDog public reveal December 2005 video. Funded by DARPA TUGV (Tactical Ground Vehicle) program 2005-2015. Raibert, M. et al. 'BigDog, the Rough-Terrain Quadruped Robot' IFAC Proceedings 41(2) 2008.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `mechanism-hydraulic-actuator`, `mechanism-dynamic-legged-locomotion`, `control-raibert-decomposition`, `control-rough-terrain-locomotion`

**Prior art notes:**

> BigDog is the canonical Boston Dynamics foundational hydraulic quadruped (December 2005). 20-year-deep public-disclosure prior art for: dynamic-balance commercial quadruped, hydraulic-actuated heavy-payload legged robot, rough-terrain dynamic stabilization. Direct architectural application of Raibert's MIT Leg Lab work (round-19 entry) at commercial scale. The ancestor of every modern Boston Dynamics platform: LS3 (2012), Spot (2015+), Atlas (2013+). Direct shielding for any commercial quadruped or quadruped-derivative humanoid claim. The viral 'kicked on ice' video itself constitutes a uniquely-public defensive disclosure of dynamic-recovery behavior.

**Sources:**

1. Raibert et al. IFAC Proceedings 41(2) 2008.
2. Boston Dynamics BigDog YouTube reveal video December 2005.
3. DARPA TUGV program documentation.

---

### 2012-09 — Boston Dynamics LS3 (AlphaDog)

- **id:** `boston-dynamics-ls3-alphadog-2012`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics under DARPA / USMC contract
- **disclosure citation:** Boston Dynamics + Marines Corps Warfighting Laboratory. LS3 (Legged Squad Support System) program reveal September 2012; demonstrated through 2015. AlphaDog is the prototype name (Phase 1, 2009-2012); LS3 is the Phase 2 (2012-2015) production version. Funded by DARPA + USMC.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `mechanism-hydraulic-actuator`, `control-voice-command`, `control-rough-terrain-locomotion`

**Prior art notes:**

> LS3 / AlphaDog is the canonical 2012 hydraulic heavy-payload tactical quadruped (Boston Dynamics under DARPA + USMC). 13-year-deep public-disclosure prior art for: 400 lb payload quadruped, voice-commanded squad-support behavior, 20-mile endurance hydraulic quadruped. Direct successor to BigDog (round-20 entry above), architectural ancestor of Spot. **The hydraulic-vs-electric-quadruped architectural choice was decided at LS3** — BD pivoted to all-electric for Spot in part because LS3's noise made it tactically unusable. This decision is itself architectural prior art for modern humanoid claims.

**Sources:**

1. Boston Dynamics LS3 YouTube reveals 2012-2015.
2. DARPA + USMC program documentation.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `1a8c3f7`.*
