---
title: control-reduced-order-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-reduced-order-model`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 1979-04-07

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## RX-78-2 Gundam (additional Gundam mecha disclosures) (1979-04-07)

- **id**: `rx-78-2-gundam-2`
- **corpus**: fictional
- **creator**: Yoshiyuki Tomino, Sunrise studio
- **disclosure**: Tomino, Yoshiyuki et al. Mobile Suit Gundam. Nagoya Broadcasting, April 7, 1979 - January 26, 1980 (43 episodes).
- **ip status**: fictional
- **prior art notes**: Note: this entry is separate from the original RX-78-2 Gundam entry (rx-78-2-gundam) in the seed slice; this one disclosures additional engineering-flavored elements that the seed entry treated lightly. AMBAC (Active Mass Balance Auto-Control) is the disclosed mechanism for orientation in zero gravity using limb articulation as reaction mass — a clear anticipation of reduced-order-model approaches that exploit limb dynamics for whole-body control in modern humanoids.

## Raibert One-Legged Hopper (1983)

- **id**: `raibert-hopping-1leg`
- **corpus**: academic
- **creator**: Marc H. Raibert; CMU Leg Laboratory, then MIT Leg Laboratory
- **disclosure**: Raibert, Marc H. 'Hopping in legged systems — modeling and simulation for the two-dimensional one-legged case'. IEEE Transactions on Systems, Man, and Cybernetics SMC-14(3): 451-463, May/June 1984. Earlier: Raibert, M.H. and Brown, H.B. 'Experiments in balance with a 2D one-legged machine'. Trans. ASME, J. Dyn. Sys., Meas., Cont., 106:75-81, 1984.
- **ip status**: public-domain
- **prior art notes**: Raibert's hoppers are the foundational academic disclosure of dynamic legged balance and reduced-order-model control. The three-part decoupling (leg height / foot placement / body attitude) is the *exact* control architecture used by every subsequent dynamic-legged academic and commercial system, from Cassie to Atlas to MIT Mini Cheetah. Modern claims on reduced-order-model legged control all face Raibert's 1984 disclosure as 102 prior art. The 1985 book (Legged Robots that Balance, MIT Press) extends the disclosure to 2-legged and 4-legged versions and is one of the most-cited works in legged robotics. Publicly funded research; open publication.

## ATRIAS (2013)

- **id**: `atrias`
- **corpus**: academic
- **creator**: Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure**: Hubicki, C. et al. 'ATRIAS: Design and validation of a tether-free 3D-capable spring-mass bipedal robot.' International Journal of Robotics Research 35(12), 2016.
- **ip status**: open-permissive
- **prior art notes**: ATRIAS is foundational prior art for spring-mass bipedal locomotion. The SLIP-based reduced-order control approach has become a dominant paradigm in dynamic bipedal walking, anticipating many subsequent commercial control claims.

## DLR TORO (2014-07)

- **id**: `dlr-toro`
- **corpus**: academic
- **creator**: Englsberger, Werner, Ott, Henze, Roa, Garofalo, Burger, Beyer, Eiberger, Schmid, Albu-Schäffer; DLR Institute of Robotics and Mechatronics
- **disclosure**: Englsberger, J., Werner, A., Ott, C., Henze, B., Roa, M.A., Garofalo, G., Burger, R., Beyer, A., Eiberger, O., Schmid, K., Albu-Schäffer, A. 'Overview of the torque-controlled humanoid robot TORO'. IEEE-RAS Humanoids, July 2014.
- **ip status**: open-permissive
- **prior art notes**: TORO is the canonical academic disclosure of full-body torque-controlled bipedal humanoid with DCM (Divergent Component of Motion) walking control. Anticipates: (1) torque-controlled whole-body bipedal walking — directly relevant to claims on whole-body torque-controlled humanoid platforms; (2) DCM walking as an alternative to ZMP — relevant to walking-control IP; (3) impedance-control whole-body interaction with humans — relevant to safe-human-interaction humanoid claims. DLR's Englsberger paper introduced the DCM formulation that subsequent humanoids (HRP-5P, several private platforms) adopted. Publicly funded research with extensive IEEE-proceedings publication.

## Cassie (2017)

- **id**: `cassie-osu`
- **corpus**: academic
- **creator**: Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure**: Agility Robotics / Oregon State University Cassie release, 2017.
- **ip status**: patented
- **prior art notes**: Cassie and the broader Hurst lab work on reduced-order locomotion models is significant prior art for bipedal control claims industry-wide.

## Ascento (2019)

- **id**: `ascento`
- **corpus**: academic
- **creator**: ETH Zurich, RSL
- **disclosure**: Klemm, V. et al. 'Ascento: A Two-Wheeled Jumping Robot.' ICRA 2019.
- **ip status**: open-permissive
- **prior art notes**: Ascento is foundational prior art for wheeled-bipedal-with-jumping morphology. Anticipates designs combining wheeled efficiency with leg-based obstacle traversal.

## Digit (2019-01)

- **id**: `agility-digit`
- **corpus**: private
- **creator**: Agility Robotics
- **disclosure**: Agility Robotics public reveal, CES January 2019.
- **ip status**: patented
- **prior art notes**: Cassie/Digit derive from Oregon State University academic work (Hurst lab); the academic publications constitute substantial prior art for the bipedal control claims.

## Upkie (2022)

- **id**: `upkie`
- **corpus**: open
- **creator**: Stéphane Caron and contributors
- **disclosure**: Caron, S. et al. Upkie public release, 2022.
- **ip status**: open-permissive
- **prior art notes**: Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.
