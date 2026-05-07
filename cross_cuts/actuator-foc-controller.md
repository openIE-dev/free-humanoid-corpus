---
title: actuator-foc-controller
parent: Cross-cuts
layout: default
---

# Cross-cut: `actuator-foc-controller`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 1929-07

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Park's Transformation (dq0 transformation) (1929-07)

- **id**: `park-transformation-1929`
- **corpus**: academic
- **creator**: Robert H. Park
- **disclosure**: Park, Robert H. 'Two-reaction theory of synchronous machines — generalized method of analysis — Part I'. AIEE Transactions 48(3): 716-727, July 1929.
- **ip status**: public-domain
- **prior art notes**: Park's 1929 transformation is the mathematical foundation underlying FOC (Field-Oriented Control) of every modern brushless DC and AC servo motor in humanoid platforms. Anticipates with 97 years of prior art: (1) the dq0 reference-frame transformation as the basis for vector control — every modern humanoid actuator controller (Moteus, ODrive, SimpleFOC, T-Motor, plus closed proprietary controllers) uses this transformation; (2) the decoupling of torque-producing and flux-producing current components — foundational for any motor-control humanoid IP. Modern claims on FOC implementations in humanoid actuators all face this 97-year academic prior art.

## ODrive (2017)

- **id**: `odrive`
- **corpus**: open
- **creator**: ODrive Robotics
- **disclosure**: Sirkin, Oskar. ODrive open hardware release, 2017.
- **ip status**: open-permissive
- **prior art notes**: ODrive is significant prior art for open BLDC controller designs. Has been used in countless academic and hobbyist robotics projects since 2017.

## mjbots Moteus (2019)

- **id**: `mjbots-moteus`
- **corpus**: open
- **creator**: mjbots Robotic Systems (Josh Katz)
- **disclosure**: Katz, Josh (mjbots). Moteus controller release, 2019.
- **ip status**: open-permissive
- **prior art notes**: mjbots Moteus is foundational prior art for compact open BLDC controllers in legged robotics. Used in Berkeley Humanoid, Upkie, and many academic platforms.

## SimpleFOC (2020)

- **id**: `simplefoc`
- **corpus**: open
- **creator**: SimpleFOC community
- **disclosure**: Skuric, Antun et al. SimpleFOC library release, 2020.
- **ip status**: open-permissive
- **prior art notes**: SimpleFOC is significant prior art for educational/open FOC implementations. Has lowered the barrier to entry for hobbyist robotics actuator development.

## Upkie (2022)

- **id**: `upkie`
- **corpus**: open
- **creator**: Stéphane Caron and contributors
- **disclosure**: Caron, S. et al. Upkie public release, 2022.
- **ip status**: open-permissive
- **prior art notes**: Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.

## MuJoCo MPC (Howell-Tassa) (2025-03)

- **id**: `howell-tassa-mujoco-mpc-2025`
- **corpus**: academic
- **creator**: Google DeepMind; Howell, Lutter, Tassa et al.
- **disclosure**: Howell, T., Lutter, M., Acero, F., Yuan, M., Tassa, Y., et al. 'Whole-Body Model-Predictive Control of Legged Robots with MuJoCo'. arXiv:2503.04613, March 2025. Google DeepMind / Tassa group.
- **ip status**: open-permissive
- **prior art notes**: Howell-Tassa MuJoCo MPC is the direct 2025 successor to the Tassa iLQG 2012 entry already in the corpus. 14-month-deep open-permissive prior art for: real-time whole-body humanoid MPC using MuJoCo dynamics + finite-difference iLQR. Demonstrated on full-sized humanoid hardware, which closes the simulation-to-real gap that the 2012 Tassa work left open. Direct shielding for any commercial humanoid claim on real-time whole-body trajectory optimization.
