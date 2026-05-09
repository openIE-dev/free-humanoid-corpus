---
title: "control-acoustic-comms"
parent: "Invalidity Contentions"
nav_order: 34
layout: default
---

# Invalidity Contention Packet — `control-acoustic-comms`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-acoustic-comms`  
**Entries:** 10 (9 commons-grade, 1 draft)  
**Earliest disclosure:** 1989-01  
**Most recent disclosure:** 2018-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-acoustic-comms`.

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

### 1995-01 — REMUS 100 AUV

- **id:** `kongsberg-remus-100-auv`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** WHOI Oceanographic Systems Lab (von Alt et al.); commercialized via Hydroid Inc.; now Kongsberg Maritime
- **disclosure citation:** von Alt, C., Allen, B., Austin, T., et al. 'Remote Environmental Measuring Unit System (REMUS): A Modular AUV for Coastal Oceanography'. Sea Technology, May 1995. Hydroid Inc. founded as WHOI spinout 2001; acquired by Kongsberg Maritime 2008. REMUS 100 commercially deployed 2001+.
- **disclosed subsystems:** `mechanism-thruster-axial`, `mechanism-control-fin`, `control-mission-script`, `control-dvl-positioning`, `control-acoustic-comms`

**Prior art notes:**

> REMUS 100 is the most-deployed compact-class survey AUV. Its lineage from the public academic WHOI publication (von Alt 1995) makes it a hybrid academic-commercial entry: the architectural specification is publicly disclosed, but Kongsberg's current commercial product carries trade-secret embellishments. Any humanoid AUV claim on 'compact survey AUV' or 'pre-programmed-mission underwater navigation' faces 30 years of public-academic + 24 years of commercial deployment prior art. The REMUS lineage complements Bluefin in the prior-art coverage of the survey AUV class.

**Sources:**

1. von Alt et al. Sea Technology May 1995.
2. Kongsberg Maritime REMUS 100 product page (kongsberg.com/maritime/products/marine-robotics/autonomous-underwater-vehicles/remus-100/).
3. B. Allen, T. Austin et al. OCEANS 2001 (REMUS commercial deployment paper).

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

### 2003-09 — Bluefin-21 AUV

- **id:** `bluefin-21-auv`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Bluefin Robotics Corp. (now General Dynamics Mission Systems / L3Harris)
- **disclosure citation:** Bluefin Robotics Corp. (founded 1997 as MIT-Sea-Grant spinout; acquired by General Dynamics 2016, divested to L3 Technologies 2020) Bluefin-21 product brochure (bluefinrobotics.com archived 2003+; current via gd-ms.com). Deployed 2014 in AF447 black-box search (Indian Ocean).
- **disclosed subsystems:** `mechanism-thruster-axial`, `mechanism-control-fin`, `control-mission-script`, `control-dvl-positioning`, `control-acoustic-comms`, `power-pressure-balanced-li-ion`

**Prior art notes:**

> Bluefin-21 is the canonical mid-class survey AUV. The 21-inch torpedo form factor is the Navy MCM/UUV standard. The Bluefin BPS pressure-balanced Li-ion battery system (commercial product since ~2008, with public academic-conference exposition in OCEANS 2010+) is the reference for any humanoid AUV claiming pressure-balanced subsea power. Directly anticipates free-humanoid-submersible's commitment to pressure-balanced Li-ion. The torpedo-form Bluefin is architecturally distinct from the hovering humanoid form, but its power, navigation, and acoustic-communication stacks are shared prior art.

**Sources:**

1. GD Mission Systems Bluefin-21 product page (gd-ms.com/products-services/uuvs/bluefin-21).
2. Vaganay et al., 'Bluefin Robotics' MTS/IEEE OCEANS proceedings 2003-2014.
3. DOD UUV Master Plan 2004 (publicly released).

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

### 2014-09 — UnetStack underwater networking framework

- **id:** `unetstack-subnero-2014`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Mandar Chitre group, Acoustic Research Laboratory, National University of Singapore; commercialized via Subnero Pte Ltd
- **disclosure citation:** Chitre, M., Bhatnagar, R., Soh, W. S. 'UnetStack: An Agent-Based Software Stack and Simulator for Underwater Networks'. OCEANS 2014 St. John's. Open-source via Subnero Pte Ltd / Acoustic Research Laboratory NUS. Apache-2.0.
- **disclosed subsystems:** `control-acoustic-comms`, `control-network-protocol`

**Prior art notes:**

> UnetStack is the canonical open-source underwater-networking framework. 11 years of academic + commercial deployment under Apache-2.0. Shields any humanoid AUV claim on 'underwater acoustic networking stack' or 'multi-vehicle subsea coordination protocol'. Directly relevant to free-humanoid-submersible's commitment to acoustic comms (SHOAL fleet coordination at dock-A/B requires multi-vehicle protocols).

**Sources:**

1. Chitre et al. OCEANS 2014 St. John's.
2. Subnero / ARL NUS UnetStack site (unetstack.net).
3. GitHub: github.com/org-arl/UnetStack3.

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

### 2017-03 — JANUS underwater acoustic communications standard

- **id:** `janus-stanag-4748-2017`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** NATO STO Centre for Maritime Research and Experimentation (CMRE); Joao Alves / John Potter et al.
- **disclosure citation:** Potter, J., Alves, J., Green, D., Zappa, G., Nissen, I., McCoy, K. 'The JANUS underwater communications standard'. UComms 2014; ratified as NATO STANAG 4748 March 2017. Reference implementation open via NATO Centre for Maritime Research and Experimentation (CMRE), La Spezia. Open standard.
- **disclosed subsystems:** `control-acoustic-comms`, `control-network-protocol`

**Prior art notes:**

> JANUS is the open NATO standard for underwater acoustic communication. 8 years of public-domain standard + reference implementation. Shields any humanoid AUV claim on standardized acoustic-comm waveforms. Directly relevant to free-humanoid-submersible's acoustic-comms commitment for shoal-fleet inter-vehicle coordination at dock-A subsurface.

**Sources:**

1. Potter et al. UComms 2014.
2. NATO STANAG 4748 (publicly released 2017).
3. NATO STO CMRE JANUS reference page (cmre.nato.int/janus).
4. JANUS reference implementation: github.com/janus-wg/janus.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `073503d`.*
