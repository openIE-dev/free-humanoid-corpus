---
title: "control-mode-switching"
parent: "Invalidity Contentions"
nav_order: 79
layout: default
---

# Invalidity Contention Packet — `control-mode-switching`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-mode-switching`  
**Entries:** 8 (4 commons-grade, 4 draft)  
**Earliest disclosure:** 2008-05  
**Most recent disclosure:** 2026-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-mode-switching`.

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

### 2008-05 — Nereus HROV

- **id:** `nereus-hrov-2008`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** WHOI Deep Submergence Laboratory; Bowen / Yoerger / Whitcomb
- **disclosure citation:** Bowen, A. D., Yoerger, D. R., Taylor, C., et al. 'The Nereus Hybrid Underwater Robotic Vehicle for Global-Class Ocean Science', WHOI Deep Submergence Laboratory; OCEANS 2008. First Challenger Deep dive (10,902 m) May 2009. Lost during operations May 2014 at 9,990 m.
- **disclosed subsystems:** `mechanism-pressure-hull`, `mechanism-syntactic-foam-ballast`, `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `control-mode-switching`, `control-tethered-teleoperation`, `control-acoustic-comms`, `control-dvl-positioning`, `power-pressure-balanced-li-ion`

**Prior art notes:**

> Nereus is the canonical academic hybrid AUV/ROV. Establishes 6-year-deep public-domain prior art for: dual-mode AUV-ROV operation in a single hull, lightweight expendable fiber tether (no power conductor), pressure-balanced subsea Li-ion at full ocean depth, ceramic-sphere syntactic-foam buoyancy to 11 km. Directly shields free-humanoid-submersible's potential mode-switching commitments and pressure-balanced power architecture. Any commercial humanoid AUV claiming mode-switching as novel art faces a 16-year-deep WHOI academic lineage with explicit publication of every mechanism.

**Sources:**

1. Bowen et al. OCEANS 2008 IEEE.
2. WHOI Nereus operational reports 2008-2014 (whoi.edu/main/nereus).
3. C. R. German et al., 'Hydrothermal exploration of mid-ocean ridges: where might the largest sulfide deposits be forming?', Chemical Geology 2016 (cites Nereus surveys).

---

### 2018-04 — Aquanaut hybrid AUV/ROV *(draft)*

- **id:** `aquanaut-houston-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Houston Mechatronics Inc. / Nauticus Robotics Inc.; founded by ex-NASA Robonaut engineers (Pratt, Krause, et al.)
- **disclosure citation:** Houston Mechatronics Inc. (founded 2014; rebranded Nauticus Robotics 2021; public via SPAC 2022 ticker KITT). Aquanaut public reveal April 2018 via company website + Houston Chronicle / IEEE Spectrum coverage. Subsequent Nauticus 8-K SEC disclosures, 10-K filings, demo videos.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `mechanism-pressure-hull`, `control-mode-switching`, `control-acoustic-comms`, `control-supervised-autonomy`, `control-dvl-positioning`, `power-pressure-balanced-li-ion`

**Prior art notes:**

> Aquanaut is the **most direct existing prior art for free-humanoid-submersible**. Public-disclosure surface (corporate website, SEC filings, IEEE Spectrum coverage, demo videos) does not reveal specific actuator or control mechanism. The capability set claimed — hovering manipulation, anthropomorphic arms, hybrid AUV/ROV mode-switching, pressure-balanced subsea power, acoustic+RF-buoy supervised teleop — is fully covered by deep open academic prior art chains: Jason ROV (1989) for tethered manipulation; Nereus (2008) for AUV/ROV mode-switching; OceanOne (Stanford 2016) for bimanual humanoid AUV manipulation with full academic publication; Slocum/Seaglider (1989/2001) for variable-buoyancy as the documented alternative; DSV Alvin (1964) for pressure-hull design; Bluefin BPS (2008+) for pressure-balanced Li-ion. Any Aquanaut/Nauticus commercial claim on architectural elements faces deep open public-domain prior art chains. The submersible morphology in free-humanoid-submersible explicitly shields against Aquanaut's claim surface by anchoring every commitment in this open-academic lineage.

**Sources:**

1. Nauticus Robotics 10-K SEC filing (sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001849058).
2. Houston Mechatronics April 2018 press release (archived).
3. IEEE Spectrum, 'This Underwater Robot Transforms Into a Submarine That Can Stretch Out to Use Both Arms', April 2018.
4. Nauticus Robotics corporate website (nauticusrobotics.com), Aquanaut product page.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2b483e9`.*
