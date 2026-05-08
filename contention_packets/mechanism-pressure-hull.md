---
title: "mechanism-pressure-hull"
parent: "Invalidity Contentions"
nav_order: 106
layout: default
---

# Invalidity Contention Packet — `mechanism-pressure-hull`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-pressure-hull`  
**Entries:** 7 (6 commons-grade, 1 draft)  
**Earliest disclosure:** 1964-06  
**Most recent disclosure:** 2018-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-pressure-hull`.

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

### 1964-06 — DSV Alvin

- **id:** `alvin-hov-1964`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Woods Hole Oceanographic Institution / Allyn Vine concept (1956); General Mills Mechanical Division built v1
- **disclosure citation:** Woods Hole Oceanographic Institution. DSV Alvin operational since June 1964; first published 4500 m dive Aug 1973. Extensive academic publication record via WHOI deep-submergence vehicle group: Ballard 1985 (Titanic dives), Yoerger et al. mission reports 1991+, Kohnen ed. 'Manned Submersibles' (1978). Operational and design details in the public domain via U.S. Navy / WHOI.
- **disclosed subsystems:** `mechanism-pressure-hull`, `mechanism-syntactic-foam-ballast`, `mechanism-variable-ballast-trim`, `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `control-station-keeping`, `control-teleoperation`

**Prior art notes:**

> DSV Alvin is the foundational manned deep-submergence vehicle. Its 60-year operational record establishes essentially every architectural element of modern submersible robotics as long-anticipated prior art: titanium pressure-hull design at 4500 m+ depth (1973), syntactic-foam buoyancy matched to depth pressure, variable-ballast trim tanks, vectored-thruster station-keeping, master-slave manipulator pairs for sample collection. Directly shields free-humanoid-submersible commitments on: 50 m pressure hull (62 years deeper than Alvin's 1964 baseline), 8-thruster vectored layout (the 6-thruster Alvin pattern is the lower bound), bimanual manipulator architecture (Alvin's Schilling/Kraft 7-function arms are the ROV-class equivalent of the bipedal upper body). Any commercial humanoid AUV claim on these elements faces a 62-year-deep public-domain academic lineage with extensive WHOI publication.

**Sources:**

1. Woods Hole Oceanographic Institution, DSV Alvin operational record 1964-present (whoi.edu/what-we-do/explore/underwater-vehicles/alvin/).
2. R. D. Ballard, 'The Discovery of the Titanic', Warner Books 1987.
3. D. R. Yoerger, A. M. Bradley, B. B. Walden, 'The Autonomous Benthic Explorer', J. Field Robotics 1991.
4. W. Kohnen (ed.), 'Manned Submersibles', U.S. Naval Institute 1978.

---

### 1989-01 — Slocum Glider

- **id:** `slocum-glider-auv`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Henry Stommel (concept, WHOI 1989); Doug Webb (engineering, Webb Research Corp 1996); Teledyne Webb Research (current)
- **disclosure citation:** Stommel, H. 'The Slocum mission'. Oceanography vol. 2 no. 1, 1989 — concept paper. Webb, D. C., Simonetti, P. J., Jones, C. P. 'SLOCUM: An Underwater Glider Propelled by Environmental Energy'. IEEE J. Oceanic Engineering vol. 26 no. 4 2001 — first deployments. Commercialized by Webb Research Corp.; acquired by Teledyne 2008.
- **disclosed subsystems:** `mechanism-variable-buoyancy-glider`, `mechanism-pitch-roll-trim`, `mechanism-pressure-hull`, `control-mission-script`, `control-acoustic-comms`

**Prior art notes:**

> Slocum is the canonical variable-buoyancy underwater glider. Stommel's 1989 concept paper and Webb's 2001 IEEE J. Oceanic Engineering paper establish a 36-year-deep open-academic prior-art chain on **variable-buoyancy propulsion as an alternative to thrust-active station-keeping**. Directly relevant to free-humanoid-submersible: the architectural choice between 'negatively-buoyant + thrust-active' (submersible's commitment) and 'variable-buoyancy + glider' (Slocum lineage) is a documented public-domain trade-off space. Any commercial AUV claim that one approach is novel art faces this 36-year-deep public-domain branching point.

**Sources:**

1. Stommel, H. 'The Slocum mission', Oceanography 2(1) 1989.
2. Webb, Simonetti, Jones, IEEE J. Oceanic Eng. 26(4) 2001.
3. Schofield et al. 'Slocum gliders: Robust and ready', J. Field Robotics 2007.
4. Rutgers Glider Lab operational record (rucool.marine.rutgers.edu).

---

### 1989-04 — Jason ROV

- **id:** `jason-rov-1989`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Woods Hole Oceanographic Institution Deep Submergence Laboratory; Ballard / Yoerger group
- **disclosure citation:** Ballard, R. D., Yoerger, D. R. et al. 'The discovery of HMS Britannic and the first deployment of the Argo/Jason imaging-and-sampling system'. Marine Technology Society Journal, vol. 23 no. 4 1989. WHOI Deep Submergence Laboratory operational since 1988-1989.
- **disclosed subsystems:** `mechanism-pressure-hull`, `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `control-tethered-teleoperation`, `control-station-keeping`, `control-acoustic-comms`, `control-dvl-positioning`

**Prior art notes:**

> Jason ROV is the foundational academic tethered ROV with bimanual manipulators. 36 years of operational record + extensive WHOI publication. Its 6-thruster vectored layout, Kraft 7-function arms, USBL+DVL navigation stack, and tethered-teleoperation control architecture are public-domain prior art for: every commercial work-class ROV (Triton XLX, Oceaneering Magnum), every academic underwater-manipulation system since (OceanOne, Aquanaut), and any commercial humanoid AUV claiming bimanual manipulation. Directly shields free-humanoid-submersible commitments on bimanual manipulation underwater, USBL acoustic positioning, DVL bottom-tracking, and tether-mode operation. The Jason → OceanOne lineage (Khatib's Stanford team explicitly cites Jason as the architectural baseline) is the public spine the commercial humanoid AUV vendors cannot dislodge.

**Sources:**

1. WHOI Deep Submergence Laboratory, Jason operational record (whoi.edu/what-we-do/explore/underwater-vehicles/jason/).
2. Ballard et al. MTS Journal 23(4) 1989.
3. D. R. Yoerger, A. M. Bradley, B. B. Walden, R. P. Stokey, 'Hydrodynamic Force-Augmented Multivariable Control for ROVs', IEEE J. Oceanic Engineering 1996.
4. M. V. Jakuba et al., 'Long-baseline acoustic navigation for under-ice AUV operations', J. Field Robotics 2008.

---

### 2001-09 — Seaglider AUV

- **id:** `seaglider-auv-2001`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Washington Applied Physics Laboratory; Eriksen et al.
- **disclosure citation:** Eriksen, C. C., Osse, T. J., Light, R. D., et al. 'Seaglider: A Long-Range Autonomous Underwater Vehicle for Oceanographic Research'. IEEE J. Oceanic Engineering vol. 26 no. 4 2001.
- **disclosed subsystems:** `mechanism-variable-buoyancy-glider`, `mechanism-pitch-roll-trim`, `mechanism-pressure-hull`, `control-mission-script`, `control-acoustic-comms`

**Prior art notes:**

> Seaglider is the second canonical variable-buoyancy glider lineage, with a fully open academic disclosure (Eriksen 2001). Together with Slocum, establishes that the variable-buoyancy-glider architecture is a 24-year-deep open-academic prior-art branch. Directly shields free-humanoid-submersible's architectural commitment to thrust-active vs. variable-buoyancy as the documented public choice.

**Sources:**

1. Eriksen et al. IEEE J. Oceanic Eng. 26(4) 2001.
2. Kongsberg Seaglider product page (kongsberg.com/maritime/products/marine-robotics/autonomous-underwater-vehicles/seaglider/).
3. UW APL Seaglider operational record.

---

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `46e9af2`.*
