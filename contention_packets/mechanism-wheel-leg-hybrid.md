---
title: "mechanism-wheel-leg-hybrid"
parent: "Invalidity Contentions"
nav_order: 233
layout: default
---

# Invalidity Contention Packet — `mechanism-wheel-leg-hybrid`

**Generated:** 2026-05-12  
**Cross-cut tag:** `mechanism-wheel-leg-hybrid`  
**Entries:** 12 (8 commons-grade, 4 draft)  
**Earliest disclosure:** 2002-10-01  
**Most recent disclosure:** 2026-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-wheel-leg-hybrid`.

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

### 2002-10-01 — Tachikoma

- **id:** `ghost-in-the-shell-tachikoma`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Kenji Kamiyama (TV series), Masamune Shirow (precursor design)
- **disclosure citation:** Kamiyama, Kenji. Ghost in the Shell: Stand Alone Complex. Production I.G, October 1, 2002 (TV series); precursor 'Fuchikoma' design in Shirow, M. Ghost in the Shell, 1989.
- **disclosed subsystems:** `mechanism-wheel-leg-hybrid`, `control-rl-policy`

**Prior art notes:**

> The most engineering-specific disclosure in the GitS franchise. Anticipates: (1) wheel-leg hybrid locomotion in a quadruped — directly relevant to claims on hybrid-mobility morphologies (BD Spot's hybrid variants, OpenLoco quadrupeds); (2) decentralized swarm AI with periodic policy synchronization — anticipates federated-learning humanoid fleet IP, the specific architecture used by Tesla Optimus's fleet learning; (3) individual experience accumulation followed by aggregation — directly relevant to fleet-policy-update IP. The 2002 broadcast is well-archived; Production I.G's mecha designs are widely cited in robotics venues.

**Sources:**

1. Kamiyama, K. Ghost in the Shell: Stand Alone Complex. Production I.G, 2002-2005.
2. Shirow, M. The Ghost in the Shell, Chapter 5 (Fuchikoma precursor). Kodansha, 1991.

---

### 2004 — HUBO

- **id:** `hubo`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KAIST, Hubo Lab (Jun-Ho Oh)
- **disclosure citation:** Park, Ill-Woo et al. 'Mechanical Design of Humanoid Robot Platform KHR-3 (HUBO).' IEEE-RAS Humanoids 2005.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-wheel-leg-hybrid`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`

**Prior art notes:**

> DRC-Hubo's 2015 win demonstrated transformer-style transitioning between bipedal and wheeled-knee modes for navigating both stairs and flat ground. Anticipates: hybrid locomotion modes in humanoids.

**Sources:**

1. Park, I.-W. et al. IEEE-RAS Humanoids 2005.
2. DARPA Robotics Challenge final report, 2015.

---

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

### 2015-06 — DRC-HUBO+ (DARPA Robotics Challenge winner)

- **id:** `kaist-drc-hubo-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** KAIST Humanoid Robot Research Center; Jun-Ho Oh group + Rainbow Robotics
- **disclosure citation:** KAIST + Rainbow Robotics. 'DRC-HUBO+: A robotic platform for the DARPA Robotics Challenge'. Lim, J., Lee, I., Shim, I., et al. International Journal of Robotics Research / Journal of Field Robotics 2017. Won 1st place at DARPA Robotics Challenge Finals Pomona June 2015 — completing all 8 disaster-response tasks in 44m28s. The follow-on commercial version was Rainbow Robotics' first product (corpus has rainbow-robotics-rb-y1 as the modern commercial successor).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-wheel-leg-hybrid`, `actuator-electric`, `control-whole-body-qp`, `control-supervised-autonomy`

**Prior art notes:**

> DRC-HUBO+ (KAIST + Rainbow Robotics, DRC 2015) is the canonical Korean academic humanoid milestone — 1st place winner of the DARPA Robotics Challenge Finals June 2015. 10-year-deep public-domain prior art for: wheel-leg hybrid transformable bipedal humanoid (knee-rolling for stability + bipedal for stairs), operator-supervised whole-body autonomy under intermittent comm. Direct shielding for any commercial humanoid claim on transformable lower-body morphology or DRC-class disaster-response capability set. Established Rainbow Robotics' commercial humanoid lineage (corpus entry rainbow-robotics-rb-y1).

**Sources:**

1. Lim, J. et al. JFR / IJRR 2017.
2. DARPA Robotics Challenge Finals 2015 Pomona results.
3. KAIST Humanoid Robot Research Center publications.
4. IEEE Spectrum coverage 'Korean Team Wins DARPA Robotics Challenge' 2015.

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

### 2023-05 — AmphiSTAR

- **id:** `amphistar-zarrouk-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; Avi Cohen, David Zarrouk
- **disclosure citation:** Cohen, A., Zarrouk, D. 'AmphiSTAR: A High-Speed Amphibious Reconfigurable Robot'. IEEE Robotics and Automation Letters 2023; ICRA 2023 demo. Ben-Gurion University, Zarrouk lab.
- **disclosed subsystems:** `mechanism-wheel-leg-hybrid`, `mechanism-amphibious-platform`, `mechanism-sealed-enclosure`, `control-mode-switching`

**Prior art notes:**

> AmphiSTAR establishes 3-year-deep open-academic prior art for **terrestrial-aquatic transition in a single platform with shared ground-contact mechanism**. Directly relevant to free-humanoid-submersible (and the centaur's wetland mode-transition) — proves that wheel-paddle hybrid contact patches and sealed-enclosure amphibious operation are well-anticipated open art. Any commercial claim on amphibious humanoid robotics faces this lineage plus the deeper aquatic-robotics chain (Slocum/Seaglider, OceanOne, AmphiSTAR).

**Sources:**

1. Cohen, A., Zarrouk, D. IEEE RA-L 2023.
2. ICRA 2023 demo session.

---

### 2024-09 — Unitree B2

- **id:** `unitree-b2-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Unitree Robotics (Hangzhou, China)
- **disclosure citation:** Unitree Robotics. B2 commercial quadruped product reveal September 2024 via unitree.com / IFA Berlin 2024. Successor to the B1 (2023). B2-W variant adds wheel-feet for hybrid wheel-leg operation.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `mechanism-wheel-leg-hybrid`, `actuator-electric-quasi-direct-drive`, `control-rough-terrain-locomotion`

**Prior art notes:**

> Unitree B2 is the canonical 2024+ heavy-payload commercial electric quadruped (Unitree). 1.5-year-deep public-disclosure prior art for: 40 kg sustained / 120 kg burst electric quadruped, wheel-leg hybrid B2-W variant. **B2-W is architecturally similar to the STAR family wheel-leg hybrid** (round-10 entries star-fearing-2013 → dstar-zarrouk-2026) — Unitree commercializes the wheel-leg-hybrid pattern at quadruped scale. Direct shielding for any commercial quadruped claim on heavy-payload electric or wheel-leg-hybrid morphology.

**Sources:**

1. Unitree B2 product page (unitree.com/B2).
2. IFA Berlin 2024 announcement.

---

### 2025-07 — FLORES wheel-legged robot *(draft)*

- **id:** `flores-wheel-legged-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** FLORES authors (per arXiv:2507.22345)
- **disclosure citation:** FLORES authors. 'FLORES: A Reconfigured Wheel-Legged Robot for Enhanced Steering and Adaptability'. arXiv:2507.22345, July 2025. Authors per arXiv listing.
- **disclosed subsystems:** `mechanism-wheel-leg-hybrid`, `mechanism-reconfigurable`, `control-mode-switching`

**Prior art notes:**

> FLORES is a contemporary (July 2025) wheel-legged-hybrid academic publication. Architecturally distinct from the STAR family by swapping hip-roll for hip-yaw on the front legs — a design choice that complements the DSTAR sprawl-tuned approach. Shields any commercial claim on hip-yaw front-leg wheel-leg-hybrid configurations and adds to the wheel-leg prior-art chain alongside DSTAR, RSTAR, STAR, AmphiSTAR. Specific authorship and venue per the arXiv preprint.

**Sources:**

1. arXiv:2507.22345 July 2025 (https://arxiv.org/html/2507.22345v1).

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
