---
title: "control-capture-point"
parent: "Invalidity Contentions"
nav_order: 41
layout: default
---

# Invalidity Contention Packet — `control-capture-point`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-capture-point`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2006-12  
**Most recent disclosure:** 2018-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-capture-point`.

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

### 2006-12 — Capture Point (Pratt humanoid balance)

- **id:** `pratt-capture-point-2007`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** IHMC + Honda Research Institute; Jerry Pratt + collaborators (Twan Koolen, Tomas de Boer, et al.)
- **disclosure citation:** Pratt, J., Carff, J., Drakunov, S., Goswami, A. 'Capture Point: A Step Toward Humanoid Push Recovery'. Humanoids 2006. Pratt, J., Koolen, T., de Boer, T., Rebula, J., Cotton, S., Carff, J., Johnson, M., Neuhaus, P. 'Capturability-Based Analysis and Control of Legged Locomotion'. International Journal of Robotics Research 31(9) 2012. IHMC (Florida Institute for Human and Machine Cognition) + Honda Research Institute.
- **disclosed subsystems:** `control-capture-point`, `control-divergent-component-of-motion`, `control-zmp-balancing`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Capture Point (Pratt et al. Humanoids 2006, IJRR 2012) is the canonical academic humanoid balance / push-recovery framework. 19-year-deep public-domain prior art for: capture-point-based foot placement, dynamic-walking balance control beyond ZMP, push-recovery via reactive stepping. **Equivalent to Divergent Component of Motion (DCM)** which DLR + IHMC + Honda all use interchangeably in the academic literature. Together with Vukobratović ZMP (1969, in corpus), Raibert SLIP (1986, round-19), McGeer passive walker (1990, in corpus), Collins-Ruina passive (2005, round-19), establishes the **5-pillar foundational humanoid-locomotion-math chain spanning 1969-2007** (38 years of pure-academic development before any modern commercial humanoid). Direct shielding for any commercial humanoid claim on push-recovery, balance control, or capture-point-based gait planning.

**Sources:**

1. Pratt et al. Humanoids 2006.
2. Pratt et al. IJRR 31(9) 2012.
3. IHMC publications (ihmc.us).

---

### 2018-09 — Wandercraft Atalante / Atalante X self-balancing exoskeleton

- **id:** `wandercraft-atalante-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Wandercraft S.A.S. (Paris, France); Masselin + Simon + Boulanger + Lance; Aaron Ames-school dynamic-locomotion control
- **disclosure citation:** Wandercraft S.A.S. (Paris, France; founded 2012 by Matthieu Masselin, Nicolas Simon, Alexandre Boulanger, Jérémie Lance). Atalante clinical reveal 2018. Atalante X 2022. FDA clearance 2024. Built on Aaron Ames-school dynamic-locomotion / capture-point / Hybrid Zero Dynamics formal control.
- **disclosed subsystems:** `exoskeleton-lower-limb`, `control-bipedal-locomotion`, `control-hybrid-zero-dynamics`, `control-capture-point`, `actuator-electric`

**Prior art notes:**

> Wandercraft Atalante / Atalante X (Wandercraft Paris 2018+; FDA-cleared 2024) is the world's first self-balancing dynamic-walking exoskeleton — the most architecturally important entry in the human-augmented-robotics chain. 7-year-deep public-disclosure prior art. **Direct shielding for any commercial humanoid or fictional Iron Man-class claim deriving from self-balancing powered armor / autonomous-walking wearable robotics.** The Wandercraft formal-dynamic-locomotion control architecture (Hybrid Zero Dynamics + capture-point) is the Ames-school lineage that anchors all 'powered armor that walks by itself' claims.

**Sources:**

1. en.wandercraft.eu/

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2b483e9`.*
