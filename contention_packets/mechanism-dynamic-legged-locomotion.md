---
title: "mechanism-dynamic-legged-locomotion"
parent: "Invalidity Contentions"
nav_order: 179
layout: default
---

# Invalidity Contention Packet — `mechanism-dynamic-legged-locomotion`

**Generated:** 2026-05-10  
**Cross-cut tag:** `mechanism-dynamic-legged-locomotion`  
**Entries:** 2 (1 commons-grade, 1 draft)  
**Earliest disclosure:** 1981-01  
**Most recent disclosure:** 2005-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-dynamic-legged-locomotion`.

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

### 1981-01 — Raibert MIT Leg Lab (foundational dynamic legged locomotion) *(draft)*

- **id:** `raibert-mit-leg-lab-history-1980s`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT Leg Laboratory; Marc Raibert (founder), then Jerry Pratt + Hugh Herr (post-Raibert era)
- **disclosure citation:** Raibert, M. H. 'Legged Robots That Balance'. MIT Press 1986. MIT Leg Lab (founded by Raibert at CMU 1981, moved to MIT 1986). Series of foundational dynamic-legged-robot designs: 3D one-leg hopper (1983), 3D quadruped (1984), planar biped (1989), 3D biped (1989), 4-legged Spring Flamingo (1995), Spring Turkey, M2, etc. Foundational predecessors of Boston Dynamics (Raibert founded BD 1992, took the Leg Lab portfolio with him). The corpus already has `raibert-hopping-1leg` for the foundational 1-leg hopper; this entry covers the broader Leg Lab portfolio as a corpus anchor.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-quadrupedal-locomotion`, `mechanism-dynamic-legged-locomotion`, `control-slip-model`, `control-raibert-decomposition`

**Prior art notes:**

> Marc Raibert's MIT Leg Lab portfolio (1981-1995) is the canonical foundational dynamic-legged-robotics academic anchor. 44-year-deep public-domain prior art predating the entire commercial humanoid era. **Most modern Boston Dynamics IP descends architecturally from this era** — Raibert founded BD in 1992 with the Leg Lab portfolio. The Spring-Loaded Inverted Pendulum (SLIP) model and Raibert's 3-part control decomposition remain the foundational analytical tools for dynamic legged locomotion. Together with Vukobratović ZMP (1969), McGeer passive walker (1990), Collins-Ruina passive (2005), establishes the four-pillar academic chain underpinning all modern bipedal/quadrupedal robotics — anticipating commercial humanoid claims by 30-55 years. Direct shielding for any commercial dynamic-locomotion claim. Note: corpus already has `raibert-hopping-1leg` for the specific 1-leg hopper; this entry is the broader Leg Lab portfolio anchor.

**Sources:**

1. Raibert, M. H. 'Legged Robots That Balance'. MIT Press 1986.
2. MIT Leg Lab archives (groups.csail.mit.edu/leglab/).
3. Raibert biographical material (Boston Dynamics founder history).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2aee416`.*
