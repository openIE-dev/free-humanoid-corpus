---
title: "control-bilateral-teleop-haptic"
parent: "Invalidity Contentions"
nav_order: 21
layout: default
---

# Invalidity Contention Packet — `control-bilateral-teleop-haptic`

**Generated:** 2026-05-07  
**Cross-cut tag:** `control-bilateral-teleop-haptic`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2011-06  
**Most recent disclosure:** 2022-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-bilateral-teleop-haptic`.

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

### 2011-06 — Force Dimension Sigma.7

- **id:** `force-dimension-sigma7-2010s`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Force Dimension SA (Lausanne, EPFL spinout); founded by Sébastien Grange + colleagues
- **disclosure citation:** Force Dimension SA (Lausanne, Switzerland; EPFL spinout). Sigma.7 haptic master controller product reveal ~2011 (after the Omega.x and Delta.x predecessor lines). EPFL Computational Robotics Lab spinout 2001. forcedimension.com.
- **disclosed subsystems:** `control-haptic-rendering`, `control-bilateral-teleop-haptic`, `mechanism-parallel-kinematic-haptic`

**Prior art notes:**

> The Force Dimension Sigma.7 is the canonical research-grade 7-DoF haptic master (~2011+). 14-year-deep public-disclosure prior art for: grasp-active 7-DoF haptic master, delta-kinematic parallel-mechanism haptic base, sub-millimeter / >1 kHz haptic rendering. **The OceanOne (round-9) and OceanOneK (round-9) academic publications explicitly use Sigma.7 as the bilateral-teleop master** — round-18 entry resolves that integration citation. Direct shielding for any commercial humanoid claim on bilateral haptic teleop or research-grade haptic-master controllers. Together with the SensAble Phantom (round-18 entry above), establishes the 32-year stylus-based haptic-master prior-art chain.

**Sources:**

1. Force Dimension corporate site (forcedimension.com).
2. Khatib et al. OceanOne IEEE RAM 2016 (uses Sigma.7).

---

### 2016-04 — OceanOne

- **id:** `oceanone-stanford-2016`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Laboratory; Oussama Khatib group; King Abdullah Univ. of Science and Technology partnership
- **disclosure citation:** Khatib, O., Yeh, X., Brantner, G., et al. 'Ocean One: A Robotic Avatar for Oceanic Discovery'. IEEE Robotics and Automation Magazine vol. 23 no. 4, 2016. First operational dive (La Lune wreck, Mediterranean, 100 m depth) April 2016.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `mechanism-pressure-hull`, `control-bilateral-teleop-haptic`, `control-operational-space`, `control-station-keeping`, `control-acoustic-comms`, `control-dvl-positioning`

**Prior art notes:**

> OceanOne is the canonical academic bimanual humanoid AUV. 9-year-deep open academic publication via the Khatib group at Stanford. Establishes element-by-element prior art for: 8-thruster vectored layout for humanoid AUV (exact match to free-humanoid-submersible commitment), bimanual 7-DoF anthropomorphic arms underwater, bilateral haptic teleoperation, F/T-sensor-in-the-loop manipulation, integration with Khatib's operational-space framework. Directly anticipates every architectural element of free-humanoid-submersible's design and any Aquanaut/Nauticus commercial claim on the same. The Khatib lineage extends back through Stanford operational-space papers to 1987 (38 years).

**Sources:**

1. Khatib et al. IEEE RAM 23(4) 2016.
2. G. Brantner, O. Khatib, 'Controlling Ocean One', Stanford Robotics Lab tech reports 2014-2016.
3. ICRA 2017 OceanOne workshop proceedings.

---

### 2022-07 — OceanOneK

- **id:** `ocean-onek-stanford-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Laboratory; Khatib group; expanded design team
- **disclosure citation:** Khatib, O., Brantner, G., Yeh, X., Salisbury, S. et al. 'OceanOneK: A 1000-meter-depth, bimanual underwater humanoid for archeology and marine exploration'. Science Robotics 2022 (announced July 2022). Subsequent IEEE RA-L publications detail control and pressure-hull innovations.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `mechanism-pressure-tolerant-actuator`, `mechanism-glass-sphere-buoyancy`, `control-bilateral-teleop-haptic`, `control-operational-space`, `control-station-keeping`

**Prior art notes:**

> OceanOneK extends the OceanOne lineage to 1000 m depth and adds pressure-tolerant oil-filled-actuator art. Directly shields any commercial humanoid AUV claim on: deep-depth (>500 m) bimanual humanoid manipulation, pressure-tolerant joint actuation (no rigid pressure hull on appendages), and integration of Khatib's 38-year operational-space framework with deep underwater manipulation. A 3-year-deep open-academic prior art chain with full element-by-element technical disclosure.

**Sources:**

1. Khatib et al. Science Robotics 2022.
2. Stanford Robotics Lab 'OceanOneK' project page (cs.stanford.edu/groups/manips/ocean-one-k/).
3. BBC, Le Monde, IEEE Spectrum coverage of Mediterranean shipwreck operations 2022-2023.

---

### 2022-10 — HaptX Gloves G1

- **id:** `haptx-gloves-g1-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** HaptX Inc. (Redmond, WA; founded 2012)
- **disclosure citation:** HaptX Inc. Gloves G1 commercial reveal October 2022 via haptx.com / press releases. Successor to research-targeted DK1 (2018) and DK2 (2021). Public technical spec sheet Rev 1.4 (2024) at docs.haptx.com.
- **disclosed subsystems:** `control-haptic-rendering`, `actuator-microfluidic`, `sensing-hand-pose-tracking`, `control-bilateral-teleop-haptic`

**Prior art notes:**

> HaptX G1 is the canonical 2022+ commercial high-fidelity haptic glove. 3-year-deep public-disclosure prior art for: microfluidic tactile actuators in glove form factor, integrated tactile + force-feedback + hand-pose tracking. Direct shielding for any commercial humanoid teleop claim on glove-based haptic feedback. Architectural successor to the SensAble Phantom (stylus-based) and Force Dimension Sigma.7 (master-controller-based) lineages — HaptX adds the wearable glove form factor.

**Sources:**

1. HaptX corporate site (haptx.com).
2. HaptX G1 spec sheet Rev 1.4 (docs.haptx.com).
3. Freethink, XR Today, Magnetics Magazine coverage 2022-2024.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `3119648`.*
