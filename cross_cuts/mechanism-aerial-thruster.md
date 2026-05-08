---
title: mechanism-aerial-thruster
parent: Cross-cuts
layout: default
---

# Cross-cut: `mechanism-aerial-thruster`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2010-01

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Parrot AR.Drone (2010-01)

- **id**: `parrot-ar-drone-2010`
- **corpus**: private
- **creator**: Parrot SA (Paris, France)
- **disclosure**: Parrot SA (Paris, France). AR.Drone reveal CES 2010 + commercial release August 2010. AR.Drone 2.0 (2012); Bebop (2014). The first commercial WiFi-controllable consumer quadcopter with open developer SDK.
- **ip status**: trade-secret
- **prior art notes**: Parrot AR.Drone (Parrot Paris 2010+) is the foundational commercial WiFi-controllable consumer quadcopter. 15-year-deep public-disclosure prior art. **Predates DJI Phantom (2013, round-35 entry) by 3 years**. Open developer SDK drove early academic robotics research. Together with Crazyflie (corpus) + DJI Phantom (round-35) + Skydio R1 (round-35), establishes the consumer-drone prior-art chain.

## DJI Phantom + Mavic consumer drone lineage (2013-01)

- **id**: `dji-phantom-2013`
- **corpus**: private
- **creator**: DJI (Da-Jiang Innovations, Shenzhen, China)
- **disclosure**: DJI (Da-Jiang Innovations Science and Technology Co., Shenzhen, China; founded 2006). Phantom 1 reveal January 2013. Subsequent Phantom 2/3/4, Mavic Pro/Air/Mini lineage. dji.com. **The dominant commercial consumer drone manufacturer worldwide** (~70%+ market share).
- **ip status**: trade-secret
- **prior art notes**: DJI Phantom + Mavic (DJI Shenzhen 2013+) is the canonical dominant consumer drone lineage. 12-year-deep public-disclosure prior art with ~70%+ market share. **Architecturally adjacent to humanoid robotics** via the LEONARDO (corpus caltech-leonardo-2021) bipedal-aerial hybrid + FSTAR/FCSTAR (corpus round-14) wheel-leg-aerial hybrid lineage — both inherit propeller + IMU + flight-controller stacks from the consumer-drone industry.

## FSTAR (Flying STAR) (2019-05)

- **id**: `fstar-zarrouk-2019`
- **corpus**: academic
- **creator**: Ben-Gurion University; David Zarrouk group
- **disclosure**: Zarrouk, D., et al. 'Flying STAR (FSTAR): a hybrid flying-and-running quadcopter with sprawl-tuned mechanism'. Ben-Gurion University, ICRA 2019 era.
- **ip status**: open-permissive
- **prior art notes**: FSTAR (Ben-Gurion Zarrouk lab, ~2019) is the first hybrid flying + ground-running STAR-family member. 6-year-deep open-academic prior art for: shared-motor-pool hybrid aerial-ground locomotion, sprawl-tuned wheel-leg + propeller integration. Architectural cousin of Caltech LEONARDO (round-8/round-12 entry caltech-leonardo-2021): FSTAR is quadruped+thrust, LEONARDO is bipedal+thrust. Together they establish the hybrid-locomotion academic substrate.

## FCSTAR (Flying-Climbing STAR) (2021-07)

- **id**: `fcstar-zarrouk-2021`
- **corpus**: academic
- **creator**: Ben-Gurion University; David Zarrouk group
- **disclosure**: Zarrouk, D., et al. 'FCSTAR: Design and Analysis of a Hybrid Flying and Climbing Sprawl-Tuned Robot'. ResearchGate publication 353205537, July 2021. Ben-Gurion University. Builds on FSTAR with thrust-reversal wall-climbing capability.
- **ip status**: open-permissive
- **prior art notes**: FCSTAR (Ben-Gurion Zarrouk lab, ~2021) is the most architecturally ambitious STAR-family member: 4 modes (ground, wall-climb, pipe, flight) on a single actuator pool. 4-year-deep open-academic prior art for: thrust-reversal wall-climbing, multi-mode-on-shared-actuator-pool reconfiguration, narrow-pipe traversal. Closes the STAR family lineage chain that begins at star-fearing-2013 and ends with dstar-zarrouk-2026 (decoupled FBEM, Jan 2026). The full 13-year-deep STAR family chain: STAR (Berkeley 2013) → RSTAR (Zarrouk 2019) → TSTAR → FSTAR → FCSTAR → AmphiSTAR → DSTAR.
