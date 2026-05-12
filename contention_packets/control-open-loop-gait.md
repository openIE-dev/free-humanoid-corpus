---
title: "control-open-loop-gait"
parent: "Invalidity Contentions"
nav_order: 109
layout: default
---

# Invalidity Contention Packet — `control-open-loop-gait`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-open-loop-gait`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2013-05  
**Most recent disclosure:** 2026-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-open-loop-gait`.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4e68247`.*
