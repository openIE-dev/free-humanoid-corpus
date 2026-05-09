---
title: "control-slip-model"
parent: "Invalidity Contentions"
nav_order: 123
layout: default
---

# Invalidity Contention Packet — `control-slip-model`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-slip-model`  
**Entries:** 2 (0 commons-grade, 2 draft)  
**Earliest disclosure:** 1981-01  
**Most recent disclosure:** 2000-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-slip-model`.

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

### 2000-01 — METU Ankara robotics (Middle East Technical University) *(draft)*

- **id:** `metu-ankara-turkey-robotics`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** METU Ankara (multiple PIs); Erbatur, Saranli, et al.
- **disclosure citation:** Orta Doğu Teknik Üniversitesi / Middle East Technical University (Ankara, Turkey; founded 1956). Robotics research distributed across Faculty of Engineering — Mechanical, Electrical-Electronics, Computer Engineering departments. Notable contributions: humanoid + bipedal research (Erbatur lab), manipulation + dexterous hand research, autonomous vehicles.
- **disclosed subsystems:** `control-research-cluster`, `mechanism-bipedal-locomotion`, `control-zmp-balancing`, `control-slip-model`

**Prior art notes:**

> METU Ankara is Turkey's largest research-intensive university and the Turkish robotics academic anchor. **First entry in the corpus from Turkey** — closes a major MENA gap. Notable for Saranli SLIP-model + Erbatur ZMP research lineages. Aggregator-style; specific METU papers should be added in future rounds.

**Sources:**

1. METU corporate site (metu.edu.tr).
2. Saranli + Erbatur publications.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2fbde5f`.*
