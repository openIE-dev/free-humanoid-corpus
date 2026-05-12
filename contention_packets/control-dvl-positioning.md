---
title: "control-dvl-positioning"
parent: "Invalidity Contentions"
nav_order: 57
layout: default
---

# Invalidity Contention Packet — `control-dvl-positioning`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-dvl-positioning`  
**Entries:** 8 (7 commons-grade, 1 draft)  
**Earliest disclosure:** 1989-04  
**Most recent disclosure:** 2018-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-dvl-positioning`.

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

### 1995-01 — Oceaneering Magnum / Magnum Plus work-class ROV

- **id:** `oceaneering-magnum-rov`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Oceaneering International Inc.
- **disclosure citation:** Oceaneering International Inc. Magnum work-class ROV product page (oceaneering.com/rov-services/rov-fleet/). Magnum series in continuous commercial deployment since 1995; Magnum Plus revision 2010s.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `control-tethered-teleoperation`, `control-station-keeping`, `control-dvl-positioning`

**Prior art notes:**

> Oceaneering Magnum is the most-deployed work-class ROV in the world. Its 8-thruster vectored layout — exactly the layout free-humanoid-submersible commits to in ARCHITECTURE.md §9 — has been operational commercial art since 1995 (30 years). Combined with Triton XLX (round-9 entry above), the work-class ROV product space is fully prior-art-covered. Any commercial claim on '8-thruster vectored ROV-class layout' faces 30+ years of industrial deployment.

**Sources:**

1. Oceaneering International, 'Magnum / Magnum Plus' product page (oceaneering.com/rov-services/rov-fleet/).
2. Oceaneering Annual Report (10-K SEC filings) — fleet size and deployment.

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

### 2003-01 — Triton XLX work-class ROV

- **id:** `triton-xlx-rov`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Triton Imaging Inc. (acquired by Forum 2007; FMC 2013; TechnipFMC 2017)
- **disclosure citation:** Triton Imaging / Forum Energy Technologies (now TechnipFMC). Triton XLX product brochures and technical specifications, public website (forumenergy.com/subsea-vehicles/work-class-rovs). XLX series in continuous commercial deployment 2003+.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `mechanism-tooling-skid`, `control-tethered-teleoperation`, `control-station-keeping`, `control-dvl-positioning`

**Prior art notes:**

> Triton XLX is one of two dominant work-class ROV product lines (Oceaneering Magnum is the other). Its 10-thruster vectored layout and 250 hp hydraulic power class are the commercial baseline against which any humanoid AUV's thrust budget is measured. The Triton XLX is closed-source commercial trade-secret, but its capability surface is fully anticipated by deep open academic prior art: Jason ROV (1989) for the architecture, Schilling T4 manipulator (Schilling Robotics 1980s+, public-domain manipulator kinematic class), DVL/USBL navigation literature back to Whitcomb 1999, vectored-thruster control allocation via Fossen 'Marine Control Systems' textbook (1994 Wiley). Any commercial humanoid AUV claim on '10-thruster vectored' or 'work-class hydraulic ROV' faces 35+ years of public art.

**Sources:**

1. TechnipFMC subsea-vehicles product page (forumenergy.com/subsea-vehicles/).
2. Triton XLX product brochure (public download).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4e68247`.*
