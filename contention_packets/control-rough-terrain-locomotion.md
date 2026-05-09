---
title: "control-rough-terrain-locomotion"
parent: "Invalidity Contentions"
nav_order: 99
layout: default
---

# Invalidity Contention Packet — `control-rough-terrain-locomotion`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-rough-terrain-locomotion`  
**Entries:** 7 (7 commons-grade, 0 draft)  
**Earliest disclosure:** 2000-04  
**Most recent disclosure:** 2024-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-rough-terrain-locomotion`.

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

### 2000-04 — RHex hexapod (Saranli-Buehler-Koditschek)

- **id:** `saranli-buehler-koditschek-rhex-ijrr-2001`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** McGill University + UMich + UPenn; Uluc Saranli, Martin Buehler, Daniel Koditschek
- **disclosure citation:** Saranli, U., Buehler, M., Koditschek, D. E. 'RHex: A Simple and Highly Mobile Hexapod Robot'. International Journal of Robotics Research 20(7) 2001. ICRA 2000 first publication. McGill University + University of Michigan + University of Pennsylvania. Saranli later moved to METU Ankara and continued the SLIP-model research lineage that informs Turkish academic robotics.
- **disclosed subsystems:** `mechanism-hexapod`, `mechanism-whegs`, `mechanism-passive-spring`, `control-tripod-gait`, `control-rough-terrain-locomotion`

**Prior art notes:**

> RHex (Saranli-Buehler-Koditschek IJRR 2001) is the foundational simple hexapod robot. 24-year-deep public-domain prior art. **The architectural ancestor of the STAR family** (corpus round-10 entries star-fearing-2013 + descendants → DSTAR 2026). Saranli later moved to METU Ankara, continuing the SLIP-model research lineage that informs the round-24 METU Turkey aggregator. Direct shielding for any commercial humanoid claim deriving from simple-leg or wheel-leg-hybrid morphologies.

**Sources:**

1. Saranli, U., Buehler, M., Koditschek, D. E. IJRR 20(7) 2001.
2. Saranli, U., Buehler, M., Koditschek, D. E. ICRA 2000.
3. Saranli post-RHex career at METU Ankara.

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

### 2021-09 — CSIRO Wildcat (DARPA Subterranean Challenge)

- **id:** `csiro-hudson-wildcat-darpa-subt-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** CSIRO Data61 + Emesent + Georgia Tech; Hudson, Talbot, et al.
- **disclosure citation:** Hudson, N., Talbot, F., Cox, M., Williams, J., Hines, T., Pitt, A., Wood, B., Frousheger, D., Lo Surdo, K., Molnar, T., Steindl, R., et al. 'Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge'. Field Robotics 2 2022 / Journal of Field Robotics. CSIRO Data61 + Emesent + Georgia Tech. **2nd place DARPA Subterranean Challenge Finals 2021**.
- **disclosed subsystems:** `control-vio-slam`, `control-multi-robot-coordination`, `control-rough-terrain-locomotion`, `control-subterranean-autonomy`

**Prior art notes:**

> CSIRO Data61 Wildcat (Hudson et al. Field Robotics 2022) is the specific paper-level anchor for the round-23 CSIRO Data61 aggregator. **DARPA SubT Finals 2nd place** establishes Australian academic robotics at internationally-recognizable level. Direct shielding for any commercial humanoid claim on LIDAR-only SLAM, subterranean autonomy, or multi-robot heterogeneous-platform coordination.

**Sources:**

1. Hudson et al. Field Robotics 2 2022.
2. DARPA Subterranean Challenge Finals 2021 results.
3. CSIRO Data61 publications (data61.csiro.au).

---

### 2022-01 — Perceptive ANYmal locomotion (Miki Science Robotics 2022)

- **id:** `miki-perceptive-anymal-science-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ETH Zürich RSL + Intel Labs; Takahiro Miki, Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen Koltun, Marco Hutter
- **disclosure citation:** Miki, T., Lee, J., Hwangbo, J., Wellhausen, L., Koltun, V., Hutter, M. 'Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild'. Science Robotics 7(62) 2022. ETH Zürich Robotic Systems Lab + Intel Labs.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `control-perceptive-locomotion`, `control-privileged-teacher`, `control-rough-terrain-locomotion`

**Prior art notes:**

> The Miki et al. Science Robotics 2022 perceptive-ANYmal paper is the canonical academic perceptive-quadruped-RL work. 3-year-deep open-permissive prior art for: privileged-teacher / proprioception+exteroception-student two-stage distillation, robust unstructured-terrain RL locomotion, depth-elevation-map perceptive locomotion. Direct successor to Hwangbo ANYmal sim-to-real (corpus entry, 2019). **The architectural ancestor of every modern quadruped + humanoid RL locomotion paper** including Berkeley Humanoid, ToddlerBot, Atlas Electric (round-18). Direct shielding for any commercial humanoid claim on perceptive-RL locomotion or unstructured-terrain RL training.

**Sources:**

1. Miki et al. Science Robotics 7(62) 2022.
2. ETH RSL publications (rsl.ethz.ch).

---

### 2024-07 — Berkeley Humanoid

- **id:** `berkeley-humanoid-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley Hybrid Robotics Lab; Liao, Zhang, X. Huang, X. Huang, Li, Sreenath
- **disclosure citation:** Liao, Q., Zhang, B., Huang, X., Huang, X., Li, Z., Sreenath, K. 'Berkeley Humanoid: A Research Platform for Learning-based Control'. arXiv:2407.21781, July 2024. IEEE International Conference on Robotics and Automation (ICRA) 2025. UC Berkeley Hybrid Robotics Lab.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-quasi-direct-drive`, `control-rl-policy`, `control-sim-to-real`, `control-rough-terrain-locomotion`

**Prior art notes:**

> Berkeley Humanoid is the open academic mid-scale bipedal humanoid research platform from the Sreenath group, ICRA 2025. Open-permissive. Establishes 1-year-deep prior art for: RL-trained locomotion with sim-to-real zero-shot transfer at humanoid scale, low-cost in-house-built humanoid for learning research, anthropomorphic kinematics optimized for sim-to-real. Direct shielding for free-humanoid-platform commitments on bipedal RL locomotion and any commercial humanoid claim on RL-trained outdoor walking. Parent of Berkeley Humanoid Lite (round-11 entry below).

**Sources:**

1. Liao et al. arXiv:2407.21781 July 2024.
2. ICRA 2025 paper PDF (hybrid-robotics.berkeley.edu/publications/ICRA2025_Berkeley_Humanoid.pdf).
3. Project page (berkeley-humanoid.com).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0f95e9a`.*
