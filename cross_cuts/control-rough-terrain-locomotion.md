---
title: control-rough-terrain-locomotion
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-rough-terrain-locomotion`

**7 corpus entries disclose this subsystem.**

Earliest disclosure: 2000-04

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## RHex hexapod (Saranli-Buehler-Koditschek) (2000-04)

- **id**: `saranli-buehler-koditschek-rhex-ijrr-2001`
- **corpus**: academic
- **creator**: McGill University + UMich + UPenn; Uluc Saranli, Martin Buehler, Daniel Koditschek
- **disclosure**: Saranli, U., Buehler, M., Koditschek, D. E. 'RHex: A Simple and Highly Mobile Hexapod Robot'. International Journal of Robotics Research 20(7) 2001. ICRA 2000 first publication. McGill University + University of Michigan + University of Pennsylvania. Saranli later moved to METU Ankara and continued the SLIP-model research lineage that informs Turkish academic robotics.
- **ip status**: public-domain
- **prior art notes**: RHex (Saranli-Buehler-Koditschek IJRR 2001) is the foundational simple hexapod robot. 24-year-deep public-domain prior art. **The architectural ancestor of the STAR family** (corpus round-10 entries star-fearing-2013 + descendants → DSTAR 2026). Saranli later moved to METU Ankara, continuing the SLIP-model research lineage that informs the round-24 METU Turkey aggregator. Direct shielding for any commercial humanoid claim deriving from simple-leg or wheel-leg-hybrid morphologies.

## Boston Dynamics BigDog (2005-12)

- **id**: `boston-dynamics-bigdog-2005`
- **corpus**: private
- **creator**: Boston Dynamics; Marc Raibert et al. (under DARPA TUGV)
- **disclosure**: Boston Dynamics + Foster-Miller + Jet Propulsion Laboratory + Harvard Concord Field Station. BigDog public reveal December 2005 video. Funded by DARPA TUGV (Tactical Ground Vehicle) program 2005-2015. Raibert, M. et al. 'BigDog, the Rough-Terrain Quadruped Robot' IFAC Proceedings 41(2) 2008.
- **ip status**: trade-secret
- **prior art notes**: BigDog is the canonical Boston Dynamics foundational hydraulic quadruped (December 2005). 20-year-deep public-disclosure prior art for: dynamic-balance commercial quadruped, hydraulic-actuated heavy-payload legged robot, rough-terrain dynamic stabilization. Direct architectural application of Raibert's MIT Leg Lab work (round-19 entry) at commercial scale. The ancestor of every modern Boston Dynamics platform: LS3 (2012), Spot (2015+), Atlas (2013+). Direct shielding for any commercial quadruped or quadruped-derivative humanoid claim. The viral 'kicked on ice' video itself constitutes a uniquely-public defensive disclosure of dynamic-recovery behavior.

## Boston Dynamics LS3 (AlphaDog) (2012-09)

- **id**: `boston-dynamics-ls3-alphadog-2012`
- **corpus**: private
- **creator**: Boston Dynamics under DARPA / USMC contract
- **disclosure**: Boston Dynamics + Marines Corps Warfighting Laboratory. LS3 (Legged Squad Support System) program reveal September 2012; demonstrated through 2015. AlphaDog is the prototype name (Phase 1, 2009-2012); LS3 is the Phase 2 (2012-2015) production version. Funded by DARPA + USMC.
- **ip status**: trade-secret
- **prior art notes**: LS3 / AlphaDog is the canonical 2012 hydraulic heavy-payload tactical quadruped (Boston Dynamics under DARPA + USMC). 13-year-deep public-disclosure prior art for: 400 lb payload quadruped, voice-commanded squad-support behavior, 20-mile endurance hydraulic quadruped. Direct successor to BigDog (round-20 entry above), architectural ancestor of Spot. **The hydraulic-vs-electric-quadruped architectural choice was decided at LS3** — BD pivoted to all-electric for Spot in part because LS3's noise made it tactically unusable. This decision is itself architectural prior art for modern humanoid claims.

## CSIRO Wildcat (DARPA Subterranean Challenge) (2021-09)

- **id**: `csiro-hudson-wildcat-darpa-subt-2021`
- **corpus**: academic
- **creator**: CSIRO Data61 + Emesent + Georgia Tech; Hudson, Talbot, et al.
- **disclosure**: Hudson, N., Talbot, F., Cox, M., Williams, J., Hines, T., Pitt, A., Wood, B., Frousheger, D., Lo Surdo, K., Molnar, T., Steindl, R., et al. 'Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge'. Field Robotics 2 2022 / Journal of Field Robotics. CSIRO Data61 + Emesent + Georgia Tech. **2nd place DARPA Subterranean Challenge Finals 2021**.
- **ip status**: open-permissive
- **prior art notes**: CSIRO Data61 Wildcat (Hudson et al. Field Robotics 2022) is the specific paper-level anchor for the round-23 CSIRO Data61 aggregator. **DARPA SubT Finals 2nd place** establishes Australian academic robotics at internationally-recognizable level. Direct shielding for any commercial humanoid claim on LIDAR-only SLAM, subterranean autonomy, or multi-robot heterogeneous-platform coordination.

## Perceptive ANYmal locomotion (Miki Science Robotics 2022) (2022-01)

- **id**: `miki-perceptive-anymal-science-2022`
- **corpus**: academic
- **creator**: ETH Zürich RSL + Intel Labs; Takahiro Miki, Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen Koltun, Marco Hutter
- **disclosure**: Miki, T., Lee, J., Hwangbo, J., Wellhausen, L., Koltun, V., Hutter, M. 'Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild'. Science Robotics 7(62) 2022. ETH Zürich Robotic Systems Lab + Intel Labs.
- **ip status**: open-permissive
- **prior art notes**: The Miki et al. Science Robotics 2022 perceptive-ANYmal paper is the canonical academic perceptive-quadruped-RL work. 3-year-deep open-permissive prior art for: privileged-teacher / proprioception+exteroception-student two-stage distillation, robust unstructured-terrain RL locomotion, depth-elevation-map perceptive locomotion. Direct successor to Hwangbo ANYmal sim-to-real (corpus entry, 2019). **The architectural ancestor of every modern quadruped + humanoid RL locomotion paper** including Berkeley Humanoid, ToddlerBot, Atlas Electric (round-18). Direct shielding for any commercial humanoid claim on perceptive-RL locomotion or unstructured-terrain RL training.

## Berkeley Humanoid (2024-07)

- **id**: `berkeley-humanoid-2024`
- **corpus**: academic
- **creator**: UC Berkeley Hybrid Robotics Lab; Liao, Zhang, X. Huang, X. Huang, Li, Sreenath
- **disclosure**: Liao, Q., Zhang, B., Huang, X., Huang, X., Li, Z., Sreenath, K. 'Berkeley Humanoid: A Research Platform for Learning-based Control'. arXiv:2407.21781, July 2024. IEEE International Conference on Robotics and Automation (ICRA) 2025. UC Berkeley Hybrid Robotics Lab.
- **ip status**: open-permissive
- **prior art notes**: Berkeley Humanoid is the open academic mid-scale bipedal humanoid research platform from the Sreenath group, ICRA 2025. Open-permissive. Establishes 1-year-deep prior art for: RL-trained locomotion with sim-to-real zero-shot transfer at humanoid scale, low-cost in-house-built humanoid for learning research, anthropomorphic kinematics optimized for sim-to-real. Direct shielding for free-humanoid-platform commitments on bipedal RL locomotion and any commercial humanoid claim on RL-trained outdoor walking. Parent of Berkeley Humanoid Lite (round-11 entry below).

## Unitree B2 (2024-09)

- **id**: `unitree-b2-2024`
- **corpus**: private
- **creator**: Unitree Robotics (Hangzhou, China)
- **disclosure**: Unitree Robotics. B2 commercial quadruped product reveal September 2024 via unitree.com / IFA Berlin 2024. Successor to the B1 (2023). B2-W variant adds wheel-feet for hybrid wheel-leg operation.
- **ip status**: trade-secret
- **prior art notes**: Unitree B2 is the canonical 2024+ heavy-payload commercial electric quadruped (Unitree). 1.5-year-deep public-disclosure prior art for: 40 kg sustained / 120 kg burst electric quadruped, wheel-leg hybrid B2-W variant. **B2-W is architecturally similar to the STAR family wheel-leg hybrid** (round-10 entries star-fearing-2013 → dstar-zarrouk-2026) — Unitree commercializes the wheel-leg-hybrid pattern at quadruped scale. Direct shielding for any commercial quadruped claim on heavy-payload electric or wheel-leg-hybrid morphology.
