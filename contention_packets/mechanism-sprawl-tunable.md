---
title: "mechanism-sprawl-tunable"
parent: "Invalidity Contentions"
nav_order: 119
layout: default
---

# Invalidity Contention Packet — `mechanism-sprawl-tunable`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-sprawl-tunable`  
**Entries:** 6 (3 commons-grade, 3 draft)  
**Earliest disclosure:** 2013-05  
**Most recent disclosure:** 2026-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-sprawl-tunable`.

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

### 2013-05 — STAR (Sprawl-Tuned Autonomous Robot)

- **id:** `star-fearing-2013`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley Biomimetic Millisystems Lab; Ronald Fearing group; Kohut, Karras, et al.
- **disclosure citation:** Karras, J. T., Fuller, C. L., Carpenter, K. C., Buscicchio, A., McKeeby, D., Norris, C. J., Parcheta, C. E., Royal, M. I., Wilcox, B. H., Fearing, R. S. 'Climbing with sprawl-tuned autonomous robots'. (Original Kohut/Fearing STAR variants 2010-2013.) IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2013. UC Berkeley Biomimetic Millisystems Lab.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-pcb-folded-linkage`, `control-open-loop-gait`

**Prior art notes:**

> STAR is the original sprawl-tuned reconfigurable miniature robot from the Fearing group at Berkeley. 13-year open-academic publication record. Establishes the 'sprawl-tuned wheel-leg-hybrid + four-bar mechanism' architectural pattern that the entire STAR family (RSTAR, TSTAR, FSTAR, FCSTAR, AmphiSTAR, DSTAR) descends from. Directly shields free-humanoid-centaur's wheel-leg-hybrid commitment and any commercial claim on compact reconfigurable-mechanism wheel-leg robotics.

**Sources:**

1. Karras et al. IROS 2013.
2. Kohut, N. J., Birkmeyer, P. M., Peterson, K. C., Fearing, R. S. 'Maneuverability and mobility in palm-sized legged robots'. SPIE 8389 2012.
3. UC Berkeley Biomimetic Millisystems Lab (robotics.eecs.berkeley.edu/~ronf/).

---

### 2018-05 — TSTAR (Tail STAR) *(draft)*

- **id:** `tstar-zarrouk-2018`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; David Zarrouk group
- **disclosure citation:** Zarrouk, D., et al. 'TSTAR: a reconfigurable robot with active two-link tail and sprawling mechanism, capable of running upright or inverted'. Ben-Gurion University, Bio-inspired and Medical Robotics Lab. ICRA / RA-L 2018-2019.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-active-tail`, `mechanism-reconfigurable`

**Prior art notes:**

> TSTAR (Ben-Gurion Zarrouk lab, ~2018) extends the STAR family with an active two-link tail for orientation-flip resilience. ~7-year-deep open-academic prior art for the active-tail-on-wheel-leg-hybrid pattern. Cited in star-fearing-2013's prior_art_notes; round-14 backfill closes the citation chain.

**Sources:**

1. Zarrouk lab publications (bgu.ac.il/zarrouklab).
2. IEEE Spectrum 'Sprawling Wheel Leg Robot Crawls and Climbs' coverage.

---

### 2019-05 — RSTAR (Rising STAR)

- **id:** `rstar-zarrouk-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; David Zarrouk group
- **disclosure citation:** Zarrouk, D., Mann, M., Degani, N., Yehuda, T., Jarbi, N., Hess, A. 'Single Actuator Wave-Like Robot (SAW): Design, Modeling, and Experiments' and follow-up RSTAR papers (IEEE RA-L 2018-2019). Ben-Gurion University of the Negev, Bio-inspired and Medical Robotics Lab. RSTAR = 'Rising STAR'.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-extensible-body`, `mechanism-reconfigurable`, `control-mode-switching`

**Prior art notes:**

> RSTAR is the immediate predecessor of DSTAR and the founding member of the Zarrouk-group Ben-Gurion STAR lineage. 7 years of open-academic publication via IEEE RA-L and IROS. Establishes element-by-element prior art for: wheel-leg-hybrid reconfigurable robots, body-extension step-climbing, turtle-gait crawling without wheels, mode-switching between rolling and walking. Directly shields free-humanoid-centaur commitments on wheel-leg hybrid morphology and mode-switching.

**Sources:**

1. Zarrouk, D. et al. 'RSTAR' IEEE RA-L 2018-2019.
2. Ben-Gurion University Bio-inspired and Medical Robotics Lab (bgu.ac.il/zarrouklab).

---

### 2019-05 — FSTAR (Flying STAR) *(draft)*

- **id:** `fstar-zarrouk-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; David Zarrouk group
- **disclosure citation:** Zarrouk, D., et al. 'Flying STAR (FSTAR): a hybrid flying-and-running quadcopter with sprawl-tuned mechanism'. Ben-Gurion University, ICRA 2019 era.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-aerial-thruster`, `mechanism-hybrid-locomotion`, `mechanism-reconfigurable`, `control-mode-switching`

**Prior art notes:**

> FSTAR (Ben-Gurion Zarrouk lab, ~2019) is the first hybrid flying + ground-running STAR-family member. 6-year-deep open-academic prior art for: shared-motor-pool hybrid aerial-ground locomotion, sprawl-tuned wheel-leg + propeller integration. Architectural cousin of Caltech LEONARDO (round-8/round-12 entry caltech-leonardo-2021): FSTAR is quadruped+thrust, LEONARDO is bipedal+thrust. Together they establish the hybrid-locomotion academic substrate.

**Sources:**

1. Zarrouk lab publications (bgu.ac.il/zarrouklab).
2. Times of Israel coverage (timesofisrael.com).

---

### 2021-07 — FCSTAR (Flying-Climbing STAR) *(draft)*

- **id:** `fcstar-zarrouk-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; David Zarrouk group
- **disclosure citation:** Zarrouk, D., et al. 'FCSTAR: Design and Analysis of a Hybrid Flying and Climbing Sprawl-Tuned Robot'. ResearchGate publication 353205537, July 2021. Ben-Gurion University. Builds on FSTAR with thrust-reversal wall-climbing capability.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-aerial-thruster`, `mechanism-thrust-reversal`, `mechanism-wall-climbing`, `mechanism-reconfigurable`, `control-mode-switching`

**Prior art notes:**

> FCSTAR (Ben-Gurion Zarrouk lab, ~2021) is the most architecturally ambitious STAR-family member: 4 modes (ground, wall-climb, pipe, flight) on a single actuator pool. 4-year-deep open-academic prior art for: thrust-reversal wall-climbing, multi-mode-on-shared-actuator-pool reconfiguration, narrow-pipe traversal. Closes the STAR family lineage chain that begins at star-fearing-2013 and ends with dstar-zarrouk-2026 (decoupled FBEM, Jan 2026). The full 13-year-deep STAR family chain: STAR (Berkeley 2013) → RSTAR (Zarrouk 2019) → TSTAR → FSTAR → FCSTAR → AmphiSTAR → DSTAR.

**Sources:**

1. ResearchGate publication 353205537 (July 2021).
2. Zarrouk lab publications (bgu.ac.il/zarrouklab).
3. ISRAEL21c coverage (israel21c.org).

---

### 2026-01 — Decoupled STAR (DSTAR)

- **id:** `dstar-zarrouk-2026`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; Tomer Siboni, Matan Coronel, David Zarrouk
- **disclosure citation:** Siboni, T., Coronel, M., Zarrouk, D. 'Design and Modeling of a Reconfigurable Robot: Decoupled STAR (DSTAR)'. IEEE Robotics and Automation Letters vol. 11 no. 1, January 2026, pp. 882-889. DOI: 10.1109/LRA.2025.3634888. Ben-Gurion University, Department of Mechanical Engineering / Bio-inspired Robotics Lab. Funded by Helmsley Charitable Trust + Marcus Endowment Fund.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-four-bar-extension`, `mechanism-reconfigurable`, `mechanism-3d-printed-platform`, `control-mode-switching`, `control-open-loop-gait`

**Prior art notes:**

> DSTAR is the most recent STAR-family member, published IEEE RA-L January 2026. Establishes very-recent (4-month-deep) open-academic prior art for: decoupled-FBEM wheel-leg reconfigurable robotics, sideways rolling via asymmetric mechanical configuration, COM-shifting via independent left/right leg actuation, 18-20 cm obstacle traversal in palm-sized class. Directly anticipates free-humanoid-centaur's wheel-leg hybrid mode-switching commitment, free-humanoid-wheeled's obstacle-climbing requirement, and any commercial humanoid claim on reconfigurable wheel-leg architectures (including any mid-size extrapolation of DSTAR to humanoid scale). The full STAR family lineage (Berkeley original 2013 → Zarrouk RSTAR 2019 → AmphiSTAR 2023 → DSTAR 2026) provides 13-year-deep open-academic continuous publication coverage of every architectural element. Highly relevant for shoal dock-A wetland service: DSTAR's terrain-adaptation gait library is a published reference design for centaur-class wetland mode-transition.

**Sources:**

1. Siboni, T., Coronel, M., Zarrouk, D. IEEE RA-L 11(1) January 2026, pp. 882-889. DOI 10.1109/LRA.2025.3634888.
2. Ben-Gurion University Bio-inspired and Medical Robotics Lab (bgu.ac.il/zarrouklab).
3. Supplementary video material via IEEE Xplore.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `d02ae55`.*
