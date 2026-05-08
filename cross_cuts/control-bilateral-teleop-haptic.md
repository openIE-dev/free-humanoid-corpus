---
title: control-bilateral-teleop-haptic
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-bilateral-teleop-haptic`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2011-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Force Dimension Sigma.7 (2011-06)

- **id**: `force-dimension-sigma7-2010s`
- **corpus**: private
- **creator**: Force Dimension SA (Lausanne, EPFL spinout); founded by Sébastien Grange + colleagues
- **disclosure**: Force Dimension SA (Lausanne, Switzerland; EPFL spinout). Sigma.7 haptic master controller product reveal ~2011 (after the Omega.x and Delta.x predecessor lines). EPFL Computational Robotics Lab spinout 2001. forcedimension.com.
- **ip status**: trade-secret
- **prior art notes**: The Force Dimension Sigma.7 is the canonical research-grade 7-DoF haptic master (~2011+). 14-year-deep public-disclosure prior art for: grasp-active 7-DoF haptic master, delta-kinematic parallel-mechanism haptic base, sub-millimeter / >1 kHz haptic rendering. **The OceanOne (round-9) and OceanOneK (round-9) academic publications explicitly use Sigma.7 as the bilateral-teleop master** — round-18 entry resolves that integration citation. Direct shielding for any commercial humanoid claim on bilateral haptic teleop or research-grade haptic-master controllers. Together with the SensAble Phantom (round-18 entry above), establishes the 32-year stylus-based haptic-master prior-art chain.

## OceanOne (2016-04)

- **id**: `oceanone-stanford-2016`
- **corpus**: academic
- **creator**: Stanford Robotics Laboratory; Oussama Khatib group; King Abdullah Univ. of Science and Technology partnership
- **disclosure**: Khatib, O., Yeh, X., Brantner, G., et al. 'Ocean One: A Robotic Avatar for Oceanic Discovery'. IEEE Robotics and Automation Magazine vol. 23 no. 4, 2016. First operational dive (La Lune wreck, Mediterranean, 100 m depth) April 2016.
- **ip status**: open-permissive
- **prior art notes**: OceanOne is the canonical academic bimanual humanoid AUV. 9-year-deep open academic publication via the Khatib group at Stanford. Establishes element-by-element prior art for: 8-thruster vectored layout for humanoid AUV (exact match to free-humanoid-submersible commitment), bimanual 7-DoF anthropomorphic arms underwater, bilateral haptic teleoperation, F/T-sensor-in-the-loop manipulation, integration with Khatib's operational-space framework. Directly anticipates every architectural element of free-humanoid-submersible's design and any Aquanaut/Nauticus commercial claim on the same. The Khatib lineage extends back through Stanford operational-space papers to 1987 (38 years).

## OceanOneK (2022-07)

- **id**: `ocean-onek-stanford-2022`
- **corpus**: academic
- **creator**: Stanford Robotics Laboratory; Khatib group; expanded design team
- **disclosure**: Khatib, O., Brantner, G., Yeh, X., Salisbury, S. et al. 'OceanOneK: A 1000-meter-depth, bimanual underwater humanoid for archeology and marine exploration'. Science Robotics 2022 (announced July 2022). Subsequent IEEE RA-L publications detail control and pressure-hull innovations.
- **ip status**: open-permissive
- **prior art notes**: OceanOneK extends the OceanOne lineage to 1000 m depth and adds pressure-tolerant oil-filled-actuator art. Directly shields any commercial humanoid AUV claim on: deep-depth (>500 m) bimanual humanoid manipulation, pressure-tolerant joint actuation (no rigid pressure hull on appendages), and integration of Khatib's 38-year operational-space framework with deep underwater manipulation. A 3-year-deep open-academic prior art chain with full element-by-element technical disclosure.

## HaptX Gloves G1 (2022-10)

- **id**: `haptx-gloves-g1-2022`
- **corpus**: private
- **creator**: HaptX Inc. (Redmond, WA; founded 2012)
- **disclosure**: HaptX Inc. Gloves G1 commercial reveal October 2022 via haptx.com / press releases. Successor to research-targeted DK1 (2018) and DK2 (2021). Public technical spec sheet Rev 1.4 (2024) at docs.haptx.com.
- **ip status**: trade-secret
- **prior art notes**: HaptX G1 is the canonical 2022+ commercial high-fidelity haptic glove. 3-year-deep public-disclosure prior art for: microfluidic tactile actuators in glove form factor, integrated tactile + force-feedback + hand-pose tracking. Direct shielding for any commercial humanoid teleop claim on glove-based haptic feedback. Architectural successor to the SensAble Phantom (stylus-based) and Force Dimension Sigma.7 (master-controller-based) lineages — HaptX adds the wearable glove form factor.
