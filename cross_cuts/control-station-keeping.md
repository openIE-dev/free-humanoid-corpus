---
title: control-station-keeping
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-station-keeping`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 1964-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DSV Alvin (1964-06)

- **id**: `alvin-hov-1964`
- **corpus**: academic
- **creator**: Woods Hole Oceanographic Institution / Allyn Vine concept (1956); General Mills Mechanical Division built v1
- **disclosure**: Woods Hole Oceanographic Institution. DSV Alvin operational since June 1964; first published 4500 m dive Aug 1973. Extensive academic publication record via WHOI deep-submergence vehicle group: Ballard 1985 (Titanic dives), Yoerger et al. mission reports 1991+, Kohnen ed. 'Manned Submersibles' (1978). Operational and design details in the public domain via U.S. Navy / WHOI.
- **ip status**: public-domain
- **prior art notes**: DSV Alvin is the foundational manned deep-submergence vehicle. Its 60-year operational record establishes essentially every architectural element of modern submersible robotics as long-anticipated prior art: titanium pressure-hull design at 4500 m+ depth (1973), syntactic-foam buoyancy matched to depth pressure, variable-ballast trim tanks, vectored-thruster station-keeping, master-slave manipulator pairs for sample collection. Directly shields free-humanoid-submersible commitments on: 50 m pressure hull (62 years deeper than Alvin's 1964 baseline), 8-thruster vectored layout (the 6-thruster Alvin pattern is the lower bound), bimanual manipulator architecture (Alvin's Schilling/Kraft 7-function arms are the ROV-class equivalent of the bipedal upper body). Any commercial humanoid AUV claim on these elements faces a 62-year-deep public-domain academic lineage with extensive WHOI publication.

## Jason ROV (1989-04)

- **id**: `jason-rov-1989`
- **corpus**: academic
- **creator**: Woods Hole Oceanographic Institution Deep Submergence Laboratory; Ballard / Yoerger group
- **disclosure**: Ballard, R. D., Yoerger, D. R. et al. 'The discovery of HMS Britannic and the first deployment of the Argo/Jason imaging-and-sampling system'. Marine Technology Society Journal, vol. 23 no. 4 1989. WHOI Deep Submergence Laboratory operational since 1988-1989.
- **ip status**: public-domain
- **prior art notes**: Jason ROV is the foundational academic tethered ROV with bimanual manipulators. 36 years of operational record + extensive WHOI publication. Its 6-thruster vectored layout, Kraft 7-function arms, USBL+DVL navigation stack, and tethered-teleoperation control architecture are public-domain prior art for: every commercial work-class ROV (Triton XLX, Oceaneering Magnum), every academic underwater-manipulation system since (OceanOne, Aquanaut), and any commercial humanoid AUV claiming bimanual manipulation. Directly shields free-humanoid-submersible commitments on bimanual manipulation underwater, USBL acoustic positioning, DVL bottom-tracking, and tether-mode operation. The Jason → OceanOne lineage (Khatib's Stanford team explicitly cites Jason as the architectural baseline) is the public spine the commercial humanoid AUV vendors cannot dislodge.

## Oceaneering Magnum / Magnum Plus work-class ROV (1995-01)

- **id**: `oceaneering-magnum-rov`
- **corpus**: private
- **creator**: Oceaneering International Inc.
- **disclosure**: Oceaneering International Inc. Magnum work-class ROV product page (oceaneering.com/rov-services/rov-fleet/). Magnum series in continuous commercial deployment since 1995; Magnum Plus revision 2010s.
- **ip status**: trade-secret
- **prior art notes**: Oceaneering Magnum is the most-deployed work-class ROV in the world. Its 8-thruster vectored layout — exactly the layout free-humanoid-submersible commits to in ARCHITECTURE.md §9 — has been operational commercial art since 1995 (30 years). Combined with Triton XLX (round-9 entry above), the work-class ROV product space is fully prior-art-covered. Any commercial claim on '8-thruster vectored ROV-class layout' faces 30+ years of industrial deployment.

## Triton XLX work-class ROV (2003-01)

- **id**: `triton-xlx-rov`
- **corpus**: private
- **creator**: Triton Imaging Inc. (acquired by Forum 2007; FMC 2013; TechnipFMC 2017)
- **disclosure**: Triton Imaging / Forum Energy Technologies (now TechnipFMC). Triton XLX product brochures and technical specifications, public website (forumenergy.com/subsea-vehicles/work-class-rovs). XLX series in continuous commercial deployment 2003+.
- **ip status**: trade-secret
- **prior art notes**: Triton XLX is one of two dominant work-class ROV product lines (Oceaneering Magnum is the other). Its 10-thruster vectored layout and 250 hp hydraulic power class are the commercial baseline against which any humanoid AUV's thrust budget is measured. The Triton XLX is closed-source commercial trade-secret, but its capability surface is fully anticipated by deep open academic prior art: Jason ROV (1989) for the architecture, Schilling T4 manipulator (Schilling Robotics 1980s+, public-domain manipulator kinematic class), DVL/USBL navigation literature back to Whitcomb 1999, vectored-thruster control allocation via Fossen 'Marine Control Systems' textbook (1994 Wiley). Any commercial humanoid AUV claim on '10-thruster vectored' or 'work-class hydraulic ROV' faces 35+ years of public art.

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
