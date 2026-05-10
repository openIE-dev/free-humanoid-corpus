---
title: "actuator-electric"
parent: "Invalidity Contentions"
nav_order: 7
layout: default
---

# Invalidity Contention Packet — `actuator-electric`

**Generated:** 2026-05-10  
**Cross-cut tag:** `actuator-electric`  
**Entries:** 106 (99 commons-grade, 7 draft)  
**Earliest disclosure:** 1956-01  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-electric`.

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

### 1956-01 — FANUC industrial robotics

- **id:** `fanuc-industrial-robotics-1956`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** FANUC Corporation (Yamanashi, Japan; Fujitsu spinout)
- **disclosure citation:** FANUC Corporation (Oshino-mura, Yamanashi, Japan; founded 1956 as Fuji Communication Apparatus Co., spun out of Fujitsu 1972 as FANUC Ltd.). Industrial robot product line: M-series, R-series, LR Mate, CRX cobot series. **The largest industrial robot company in the world by deployed-unit count** (~750,000 units cumulative).
- **disclosed subsystems:** `mechanism-manipulator-arm`, `actuator-electric`, `mechanism-collaborative-robot`

**Prior art notes:**

> FANUC (founded 1956 as Fujitsu spinout; FANUC Ltd 1972) is the world's largest industrial robot company by deployed units. 70-year-deep public-disclosure prior art across multi-product industrial-arm + cobot lineage. ~750,000 units cumulative. Direct shielding for any commercial humanoid claim that includes industrial-arm derivative applications. Together with SCARA (round-32), Universal Robots (round-24), Doosan (round-22), KUKA, ABB, Yaskawa, establishes the industrial-robot prior-art chain spanning 1956-2026.

**Sources:**

1. FANUC corporate site (fanuc.com).
2. Wikipedia 'FANUC'.
3. International Federation of Robotics annual industrial-robot deployment statistics.

---

### 1957-08 — SPURV (Self-Propelled Underwater Research Vehicle; the FIRST AUV)

- **id:** `spurv-uw-apl-1957`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Washington Applied Physics Laboratory; Bob Van Wagennen + Wayne Nodland; ONR-funded
- **disclosure citation:** Van Wagennen, R. + Nodland, W. / University of Washington Applied Physics Laboratory; ONR-funded. First cruise to Cobb Seamount August 1957. The FIRST autonomous underwater vehicle. 3,000 m torpedo-form.
- **disclosed subsystems:** `auv`, `actuator-electric`

**Prior art notes:**

> SPURV (UW APL 1957) is the FIRST autonomous underwater vehicle. 68-year-deep public-domain prior art. Direct shielding for any commercial humanoid or AUV claim deriving from autonomous underwater vehicles. Foundational predicate for every commercial AUV downstream.

**Sources:**

1. en.wikipedia.org/wiki/SPURV

---

### 1963-01 — Belgrade / Belgrade-USC Hand (Tomović + Bekey)

- **id:** `belgrade-usc-tomovic-bekey-hand-1963`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Mihailo Pupin Institute (Belgrade, Yugoslavia); Rajko Tomović + Miodrag Rakić; later Belgrade-USC version with George Bekey at USC
- **disclosure citation:** Tomović, R., Boni, G. 'An Adaptive Artificial Hand'. IRE Transactions on Automatic Control AC-7(3), 1962. Belgrade Hand developed at Mihailo Pupin Institute (Belgrade, Yugoslavia) 1961-1963. Subsequent Belgrade-USC Hand version with George Bekey at University of Southern California ~1988.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-underactuated-finger`, `control-myoelectric`, `actuator-electric`

**Prior art notes:**

> Belgrade / Belgrade-USC Hand (Tomović + Rakić 1963; Bekey USC 1988) is the foundational anthropomorphic prosthetic hand and the world's first externally-powered five-finger myoelectric prosthetic. 62-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from five-finger anthropomorphic hands, underactuated finger mechanisms, or myoelectric prosthetic control. Foundational to every modern anthropomorphic hand including Robotiq (round-42), Shadow Dexterous Hand (corpus), Salisbury Stanford-JPL Hand (corpus), Utah/MIT Hand (round-42), and the entire dexterous-hand research lineage.

**Sources:**

1. Tomović, R. + Boni, G. 'An Adaptive Artificial Hand'. IRE Transactions on Automatic Control AC-7(3), 1962.
2. en.techfokus.rs/belgrade-hand-first-bionic-prosthetic-robotics/
3. en.wikipedia.org/wiki/Rajko_Tomović

---

### 1965-01 — CURV (Cable-controlled Underwater Recovery Vehicle)

- **id:** `curv-us-navy-1965`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** US Navy Naval Ocean Systems Center (NOSC); Jack L. Sayer Jr.
- **disclosure citation:** US Navy Naval Ocean Systems Center (NOSC) (USA); Jack L. Sayer Jr. CURV-I 1965 — Cable-controlled Underwater Recovery Vehicle, recovered the 1966 Palomares H-bomb. Successor CURV-III 1972 (7,200 ft depth) recovered Pisces III crew 1973.
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> CURV (US Navy NOSC 1965+) is the foundational tethered-ROV architecture. 60-year-deep public-domain prior art. Direct shielding for any commercial humanoid or ROV claim deriving from cable-controlled underwater recovery vehicles. Predicate for every tethered ROV downstream.

**Sources:**

1. en.wikipedia.org/wiki/CURV

---

### 1969-06 — Stanford Arm (Scheinman 1969)

- **id:** `stanford-arm-scheinman-1969`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford AI Laboratory; Victor Scheinman
- **disclosure citation:** Scheinman, V.D. 'Design of a Computer Controlled Manipulator'. Stanford AI Memo 92, June 1969. Stanford Artificial Intelligence Laboratory. Subsequently commercialized as Vicarm (Scheinman's company), then sold to Unimation.
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`, `control-inverse-kinematics`, `mechanism-spherical-wrist`

**Prior art notes:**

> Stanford Arm (Scheinman Stanford AI Lab 1969) is the foundational all-electric 6-axis arm with closed-form kinematics. 56-year-deep public-domain prior art. The Scheinman spherical wrist became the industrial standard. Direct shielding for any commercial humanoid claim deriving from 6-DoF anthropomorphic arm geometry. Direct ancestor of PUMA (round-45) and every modern 6-DoF industrial arm.

**Sources:**

1. en.wikipedia.org/wiki/Stanford_arm
2. en.wikipedia.org/wiki/Victor_Scheinman

---

### 1973-09 — ASEA IRB-6 (first microprocessor-controlled all-electric robot)

- **id:** `asea-irb6-1973`
- **corpus:** private
- **ip status:** public-domain
- **creator:** ASEA AB (Västerås, Sweden; → ABB 1988); Björn Weichbrodt et al.
- **disclosure citation:** ASEA AB (Västerås, Sweden; merged with Brown Boveri 1988 → ABB). IRB-6 commercial reveal September 1973. World's first microprocessor-controlled (Intel 8008) all-electric industrial robot. Developed by Björn Weichbrodt et al.
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`, `control-microprocessor`

**Prior art notes:**

> ASEA IRB-6 (Västerås Sweden 1973) is the world's first microprocessor-controlled all-electric industrial robot. 52-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from all-electric microprocessor-controlled industrial arms. Ancestor of the entire ABB IRB product line including YuMi (round-45) and FlexPicker (round-45).

**Sources:**

1. historyofinformation.com/detail.php?entryid=4352
2. new.abb.com/news/detail/106125/140-years-of-asea

---

### 1978-01 — Makino SCARA (Selective Compliance Assembly Robot Arm)

- **id:** `makino-scara-yamanashi-1978`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Yamanashi (Japan); Hiroshi Makino + 13-company consortium; productized by Sankyo Seiki, Pentel, NEC
- **disclosure citation:** Makino, H. et al. SCARA architecture developed at University of Yamanashi 1978-1981 in consortium with 13 Japanese companies. Productized by Sankyo Seiki, Pentel, and NEC starting 1981. Hiroshi Makino (Yamanashi University) is the inventor.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-scara`, `actuator-electric`

**Prior art notes:**

> Makino SCARA (Yamanashi University + 13-company consortium 1978-1981) is the foundational SCARA architecture. 47-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from SCARA-architecture assembly arms. The dominant assembly-arm architecture worldwide; productized by every major arm OEM.

**Sources:**

1. en.wikipedia.org/wiki/SCARA

---

### 1978-05 — PUMA (Programmable Universal Machine for Assembly)

- **id:** `puma-unimation-1978`
- **corpus:** private
- **ip status:** public-domain
- **creator:** Unimation Inc. (Danbury, CT, USA); Victor Scheinman; GM-funded contract
- **disclosure citation:** Unimation Inc. (Danbury, CT, USA). PUMA reveal 1978; GM-funded design contract. Designed by Victor Scheinman based on his Stanford Arm (round-45). PUMA 560 became the canonical 6-DoF research arm of the 1980s-1990s. Unimation → Westinghouse 1983 → Stäubli 1989.
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`, `mechanism-spherical-wrist`

**Prior art notes:**

> PUMA (Unimation 1978; Scheinman) is the canonical 6-DoF anthropomorphic arm geometry. 47-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from 6-DoF revolute anthropomorphic arms. Ancestor of UR (corpus universal-robots-denmark-2008) and most modern industrial arms.

**Sources:**

1. en.wikipedia.org/wiki/Victor_Scheinman

---

### 1979-01 — SCARA (Selective Compliance Articulated Robot Arm)

- **id:** `scara-makino-1979`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Yamanashi University, Japan; Hiroshi Makino
- **disclosure citation:** Makino, H. 'SCARA Robot' development at Yamanashi University, Japan, 1978-1981. Initial commercial SCARA robots from Sankyo Seiki + Yamaha + others early 1980s. SCARA stands for Selective Compliance Articulated Robot Arm.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-selective-compliance`, `actuator-electric`

**Prior art notes:**

> SCARA (Makino Yamanashi University 1979) is the foundational selective-compliance manipulator architecture. 46-year-deep public-domain prior art. The dominant industrial-arm class for electronics assembly. Direct shielding for any commercial humanoid claim that includes SCARA-class arm derivatives or selective-compliance manipulation.

**Sources:**

1. Makino, H. SCARA development at Yamanashi University 1978-1981.
2. Wikipedia 'SCARA' (en.wikipedia.org/wiki/SCARA).
3. Sankyo Seiki + Yamaha early 1980s SCARA commercialization.

---

### 1983-01 — Epson SCARA (global SCARA volume leader)

- **id:** `epson-scara-1983`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Seiko Epson Corporation (Suwa, Japan)
- **disclosure citation:** Seiko Epson Corporation (Suwa, Japan; Suwa Seikosha). First Epson SCARA reveal 1983 (originally for in-house quartz-watch assembly automation). Now #1 SCARA-arm maker worldwide. Modern G-series (2000s+), LS-series, N-series 6-axis.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-scara`, `actuator-electric`

**Prior art notes:**

> Epson SCARA (Seiko Epson Suwa 1983+) is the global SCARA-arm volume leader. 42-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from SCARA-architecture assembly arms. Lineage descends from Makino SCARA (round-45).

**Sources:**

1. en.wikipedia.org/wiki/Epson_Robots

---

### 1984-12 — Nautile (IFREMER 6000 m HOV)

- **id:** `nautile-ifremer-1984`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** IFREMER / Genavir (France)
- **disclosure citation:** IFREMER (Institut français de recherche pour l'exploitation de la mer) / Genavir (France). Nautile commissioned 1984; first 6,000 m dive April 3, 1985.
- **disclosed subsystems:** `hov`, `actuator-electric`

**Prior art notes:**

> Nautile (IFREMER France 1984+) is Europe's flagship operational scientific 6,000 m HOV. 41-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from titanium-pressure-sphere 6,000 m crewed vehicles.

**Sources:**

1. ifremer.fr/en/Nautile40ans

---

### 1985-01 — Clavel Delta Robot (EPFL 1985 patent)

- **id:** `clavel-delta-epfl-1985`
- **corpus:** academic
- **ip status:** public-domain (EPFL patent expired 2007)
- **creator:** EPFL (Lausanne, Switzerland); Reymond Clavel + Marc-Olivier Demaurex
- **disclosure citation:** Clavel, R., Demaurex, M.-O. 'Delta, A Fast Robot with Parallel Geometry'. 18th International Symposium on Industrial Robots 1988; original patent 1985 (EP 0250470, expired 2007). EPFL (École Polytechnique Fédérale de Lausanne, Switzerland). Commercialized 1987 via Demaurex SA (Romont, Switzerland; acquired by Bosch 1999, then to ABB ecosystem).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-parallel`, `manipulator-delta`, `actuator-electric`

**Prior art notes:**

> Clavel Delta Robot (EPFL 1985 patent; expired 2007) is the first parallel pick-and-place delta robot. 40-year-deep public-domain prior art (patent expired 2007). Direct shielding for any commercial humanoid claim deriving from parallel delta-mechanism arms. Ancestor of ABB FlexPicker (round-45), Adept Quattro, and every commercial delta robot.

**Sources:**

1. en.wikipedia.org/wiki/Reymond_Clavel

---

### 1987-12 — Mir-1 + Mir-2 deep submergence vehicles

- **id:** `mir-1-and-mir-2-rauma-repola-1987`
- **corpus:** private
- **ip status:** trade-secret (Cold War origin)
- **creator:** Rauma-Repola Oceanics (Finland) / USSR Shirshov Institute of Oceanology
- **disclosure citation:** Rauma-Repola Oceanics (Finland) for the USSR Academy of Sciences Shirshov Institute of Oceanology. Mir-1 + Mir-2 twin 6,000 m HOVs delivered December 1987. Cold War Finnish-Soviet co-build. Used at Titanic + Komsomolets wrecks; filming Cameron's 'Titanic' (1997).
- **disclosed subsystems:** `hov`, `actuator-electric`

**Prior art notes:**

> Mir-1 + Mir-2 (Rauma-Repola Finland for Shirshov Institute 1987+) are twin 6,000 m steel-alloy HOVs. 38-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from twin-HOV simultaneous-dive operations.

**Sources:**

1. en.wikipedia.org/wiki/Mir_(submersible)

---

### 1988-01 — BarrettHand BH8-280 / BH8-282

- **id:** `barrett-hand-1988`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Barrett Technology / William Townsend (MIT spinout)
- **disclosure citation:** Barrett Technology, LLC. (Cambridge, MA, USA; founded 1988 by William Townsend, MIT spinout). BarrettHand BH8-280 commercial release 1988+. The first commercial multi-fingered dexterous hand. barrett.com.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-driven`, `mechanism-underactuated-hand`, `actuator-electric`

**Prior art notes:**

> BarrettHand is **the first commercial multi-fingered dexterous hand** (Barrett Technology MIT spinout 1988+). 37-year-deep public-disclosure prior art. The architectural ancestor of every subsequent commercial dexterous hand: Shadow (corpus), Allegro (round-27), Schunk SVH (round-27), Pisa-IIT SoftHand (corpus). Direct shielding for any commercial humanoid claim on multi-fingered dexterous hand commercial deployment.

**Sources:**

1. Barrett Technology corporate site (barrett.com).
2. Townsend, W. T. 'The BarrettHand Grasper' Industrial Robot 27(3) 2000.

---

### 1990-01 — Barrett WAM Arm (cable-driven backdrivable research arm)

- **id:** `barrett-wam-arm-1990`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** MIT AI Lab + Barrett Technology Inc. (Cambridge, MA, USA); William Townsend
- **disclosure citation:** Townsend, W. PhD thesis 'The Effect of Transmission Design on Force-Controlled Manipulator Performance'. MIT 1988. Barrett Technology Inc. founded 1990 in Cambridge MA. WAM (Whole-Arm Manipulator) commercial reveal 1990. The canonical compliant-research-arm; licensed into MAKO/RIO surgical platform (round-45).
- **disclosed subsystems:** `manipulator-arm`, `mechanism-cable-driven`, `mechanism-backdrivable`, `actuator-electric`

**Prior art notes:**

> Barrett WAM Arm (Townsend MIT 1988 → Barrett Technology 1990) is the canonical cable-driven backdrivable research arm. 35-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from cable-driven backdrivable manipulator arms. Licensed into MAKO RIO surgical platform (round-45). Sister to Barrett Hand (corpus barrett-hand-1988).

**Sources:**

1. barrett.com/wam
2. en.wikipedia.org/wiki/Barrett_Technology

---

### 1990-01 — Shinkai 6500 (JAMSTEC 6500 m HOV)

- **id:** `shinkai-6500-jamstec-1990`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** JAMSTEC / Mitsubishi Heavy Industries (Japan)
- **disclosure citation:** JAMSTEC (Japan Agency for Marine-Earth Science and Technology) / Mitsubishi Heavy Industries (Japan). Shinkai 6500 completed 1990; operational from 1991. 6,500 m operational depth.
- **disclosed subsystems:** `hov`, `actuator-electric`

**Prior art notes:**

> Shinkai 6500 (JAMSTEC Japan 1990+) is Japan's flagship 6,500 m HOV. 35-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from titanium-pressure-sphere Japanese deep HOVs.

**Sources:**

1. en.wikipedia.org/wiki/DSV_Shinkai_6500

---

### 1991-01 — Stäubli TX/RX series high-precision sealed arms

- **id:** `staubli-tx-rx-series-1991`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Stäubli AG (Pfäffikon, Switzerland + Faverges, France); Unimation acquisition 1989
- **disclosure citation:** Stäubli AG (Pfäffikon, Switzerland + Faverges, France; founded 1892). RX-series industrial arm reveal 1991, following Stäubli's 1989 acquisition of Unimation's robot business (transferring the PUMA / Stanford Arm IP lineage to Europe). TX2-series 2017 with safety-rated SIL3/PLe controller.
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`, `control-safety-rated`

**Prior art notes:**

> Stäubli TX/RX series (Stäubli Switzerland + France 1991+) are the high-precision sealed-arm reference for pharma + clean-room. 34-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from clean-room-rated industrial arms. Lineage descends from PUMA (round-45 puma-unimation-1978) via Unimation's 1989 sale to Stäubli.

**Sources:**

1. Stäubli corporate site.

---

### 1991-01 — DLR Lightweight Robot LWR I/II/III (foundational torque-sensor arm)

- **id:** `dlr-lwr-1991-2003`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** DLR (German Aerospace Center) Institute of Robotics and Mechatronics; Gerd Hirzinger group
- **disclosure citation:** Hirzinger, G. et al. DLR (German Aerospace Center) Institute of Robotics and Mechatronics. LWR I (1991), LWR II (1998), LWR III (2003), LWR IV (~2007). The seminal torque-sensor 7-DoF lightweight arm; basis for KUKA LBR iiwa (round-45) via license.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> DLR Lightweight Robot LWR (DLR Hirzinger group 1991-2007) is the seminal torque-sensor 7-DoF lightweight research arm. 34-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from torque-sensor 7-DoF cobots. Anchors the entire 7-DoF cobot category via KUKA LBR iiwa (round-45) and Franka Panda (round-45) descendants.

**Sources:**

1. DLR Institute of Robotics and Mechatronics LWR documentation.

---

### 1994-09 — RoboTuna (MIT first robot fish; biomimetic propulsion)

- **id:** `robotuna-mit-triantafyllou-1994`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** MIT Department of Ocean Engineering; Michael Triantafyllou + George Triantafyllou + David Barrett
- **disclosure citation:** Triantafyllou, M.S., Triantafyllou, G.S., Barrett, D.S. / MIT Department of Ocean Engineering (USA). RoboTuna ('Charlie I') maiden swim 1994/1995. The first robot fish. Defined the biomimetic underwater propulsion research field.
- **disclosed subsystems:** `biomimetic-aquatic`, `mechanism-undulating-tail`, `actuator-electric`

**Prior art notes:**

> RoboTuna (MIT Triantafyllou 1994) is the first robot fish — defined the biomimetic underwater propulsion research field. 31-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or aquatic-robot claim deriving from biomimetic undulating-tail propulsion. Foundational to every subsequent biomimetic underwater robot.

**Sources:**

1. news.mit.edu/1994/robotuna-0921

---

### 1995-03 — Kaiko ROV (first ROV to Challenger Deep)

- **id:** `kaiko-jamstec-1995`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** JAMSTEC (Japan)
- **disclosure citation:** JAMSTEC (Japan). Kaiko first dive to Challenger Deep March 1995. ~296 dives to 1999 servicing. Lost May 29, 2003 in typhoon. Successor: ABISMO (round-47 lineage).
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> Kaiko (JAMSTEC 1995-2003) is the first ROV ever to reach Challenger Deep. 30-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or ROV claim deriving from full-ocean-depth tethered ROVs.

**Sources:**

1. en.wikipedia.org/wiki/Kaikō_ROV

---

### 1995-06 — Autonomous Benthic Explorer (ABE; WHOI 1995)

- **id:** `abe-whoi-1995`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Woods Hole Oceanographic Institution; Dana Yoerger group
- **disclosure citation:** Yoerger, D. et al. / Woods Hole Oceanographic Institution (USA). ABE developed 1994; first mission 1995-1996. Lost at sea March 5, 2010 off Chile. 222 missions before loss.
- **disclosed subsystems:** `auv`, `auv-hovering`, `actuator-electric`

**Prior art notes:**

> ABE (WHOI 1995-2010) is the pioneering hovering AUV. 30-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or AUV claim deriving from hovering AUV architectures. Direct ancestor of Sentry (round-47).

**Sources:**

1. en.wikipedia.org/wiki/Autonomous_Benthic_Explorer

---

### 1995-08 — Theseus AUV (long-range Arctic under-ice cable-layer)

- **id:** `theseus-ise-canada-1995`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** International Submarine Engineering Ltd. (Port Coquitlam, BC, Canada)
- **disclosure citation:** International Submarine Engineering Ltd. (ISE; Port Coquitlam, BC, Canada). Theseus construction 1993-1994; first Arctic deployment 1995; full mission 1996. Long-range under-ice fiber-optic cable-laying AUV.
- **disclosed subsystems:** `auv`, `actuator-electric`

**Prior art notes:**

> Theseus (ISE Canada 1995-1996) is the foundational long-range under-ice cable-laying AUV. 30-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or AUV claim deriving from ultra-long-range polar under-ice autonomous operations.

**Sources:**

1. en.wikipedia.org/wiki/Theseus_(AUV)

---

### 1996-06 — Hugin AUV (Kongsberg/FFI dominant European commercial)

- **id:** `hugin-kongsberg-ffi-1996`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Norwegian Defence Research Establishment (FFI) + Kongsberg Simrad + Statoil (Norway)
- **disclosure citation:** Norwegian Defence Research Establishment (FFI) + Kongsberg Simrad + Statoil (Norway). Hugin 1 first sea trial summer 1996; first commercial survey 1997. Hugin Endurance 2024 (8,000 km range).
- **disclosed subsystems:** `auv`, `actuator-electric`

**Prior art notes:**

> Hugin AUV (FFI + Kongsberg + Statoil Norway 1996+) is the dominant European commercial survey AUV. 29-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or AUV claim deriving from offshore-survey commercial AUVs.

**Sources:**

1. ffi.no/en/news/the-story-of-hugin--an-autonomous-underwater-vehicle
2. kongsberg.com/discovery/autonomous-and-uncrewed-solutions/auv/hugin/

---

### 1996-09 — Autosub family (NOC Southampton UK; Boaty McBoatface)

- **id:** `autosub-noc-southampton-1996`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** National Oceanography Centre Southampton (UK)
- **disclosure citation:** National Oceanography Centre Southampton (UK). Autosub-1 1996; Autosub-6000 2007; Autosub Long Range ('Boaty McBoatface') 2017. UK academic + scientific AUV lineage focused on polar + under-ice missions.
- **disclosed subsystems:** `auv`, `actuator-electric`

**Prior art notes:**

> Autosub family (NOC Southampton UK 1996+; Boaty McBoatface 2017) is the UK academic AUV lineage with polar + under-ice focus. 29-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or AUV claim deriving from UK polar + Antarctic under-ice AUV operations.

**Sources:**

1. noc.ac.uk/technology/technology-development/autosub-long-range-boaty-mcboatface

---

### 1998-01 — KIT ARMAR humanoid lineage

- **id:** `kit-armar-humanoid-2000-2020`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Karlsruhe Institute of Technology (KIT); Tamim Asfour group (founded by Rüdiger Dillmann)
- **disclosure citation:** Karlsruhe Institute of Technology (KIT, formerly Universität Karlsruhe). ARMAR humanoid lineage 1998-2020+: ARMAR-I (1998), ARMAR-II (2002), ARMAR-III (2005), ARMAR-IV (2013), ARMAR-VI (2018), ARMAR-7 (2024). Albers + Asfour + Dillmann group (now led by Tamim Asfour). The foundational German academic humanoid lineage.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `actuator-electric`, `control-whole-body-control`

**Prior art notes:**

> The KIT ARMAR humanoid lineage is the foundational German academic humanoid program (Asfour + Dillmann at KIT, 1998-2020+). 27-year-deep public-domain prior art across 7 generations of ARMAR humanoid. Together with DLR Justin (corpus entry justin / dlr-justin), DLR Hand-II (corpus), DLR Hand-Arm System (corpus round-8), establishes the German academic humanoid + manipulator prior-art baseline. Direct shielding for any commercial humanoid claim that descends architecturally from German academic humanoid lineages.

**Sources:**

1. KIT High Performance Humanoid Technologies Lab (h2t.iar.kit.edu).
2. Asfour + Dillmann publications.
3. Master Motor Map (mmm.humanoids.kit.edu).

---

### 1998-01 — ABB FlexPicker IRB 360 (dominant industrial delta robot)

- **id:** `abb-flexpicker-irb-360-1998`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** ABB Asea Brown Boveri (Zurich + Västerås); Clavel-EPFL patent licensee
- **disclosure citation:** ABB Asea Brown Boveri (Zurich, Switzerland + Västerås, Sweden). FlexPicker IRB 360 commercial reveal 1998. The first commercially dominant industrial delta robot; Clavel-EPFL-patent-derived (round-45 clavel-delta-epfl-1985).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-delta`, `actuator-electric`

**Prior art notes:**

> ABB FlexPicker IRB 360 (ABB 1998+) is the dominant industrial delta robot. 27-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from delta-mechanism pick-and-place arms. Lineage descends from Clavel-EPFL patent (round-45 clavel-delta-epfl-1985).

**Sources:**

1. new.abb.com/products/robotics/robots/delta-robots/irb-360

---

### 1999-01 — Hocoma Lokomat treadmill-mounted gait orthosis

- **id:** `hocoma-lokomat-1999`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Hocoma AG (Volketswil, Switzerland) + University Hospital Balgrist + ETH Zurich; Reinhard Riener
- **disclosure citation:** Hocoma AG (Volketswil, Switzerland; founded 1996). Lokomat treadmill-mounted robot-driven gait orthosis commercial reveal 1999. Co-developed with University Hospital Balgrist (Zurich) and ETH Zurich (Reinhard Riener).
- **disclosed subsystems:** `exoskeleton-lower-limb`, `actuator-electric`, `control-gait-rehabilitation`

**Prior art notes:**

> Hocoma Lokomat (Hocoma AG Volketswil 1999+) is the foundational treadmill-mounted robotic gait-rehab orthosis. 26-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from treadmill-mounted lower-limb rehabilitation orthoses or robotic gait-rehabilitation. The Swiss anchor of medical exoskeletons.

**Sources:**

1. hocoma.com/us/solutions/lokomat/

---

### 1999-01 — VideoRay Pro / Mission Specialist (microROV market leader)

- **id:** `videoray-pro-1999`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** VideoRay LLC (Pottstown, PA, USA); Scott Bentley founder
- **disclosure citation:** VideoRay LLC (Pottstown, PA, USA; founded 1999). VideoRay Pro (1999) → Pro 4 → Mission Specialist (2017+) → Defender (US Navy EOD 2017+). Global volume leader in microROV; >3,000 units delivered.
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> VideoRay Pro / Mission Specialist (Pottstown PA 1999+) is the global volume leader in microROV. 26-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or ROV claim deriving from small-class portable observation/inspection ROVs.

**Sources:**

1. en.wikipedia.org/wiki/VideoRay_UROVs
2. videoray.com

---

### 2000-04 — Siasun Robotics (Chinese Academy of Sciences spinout)

- **id:** `siasun-robotics-cas-2000`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Siasun Robot & Automation Co., Ltd. (Shenyang, China; CAS Shenyang Institute of Automation spinout); Qu Daokui founder
- **disclosure citation:** Siasun Robot & Automation Co., Ltd. (Shenyang, China; founded 2000 from Shenyang Institute of Automation, Chinese Academy of Sciences). First China-based RIA (Robotic Industries Association) member. 100+ industry firsts in Chinese robotics.
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`

**Prior art notes:**

> Siasun Robotics (Shenyang 2000+; CAS spinout) is the Chinese Academy of Sciences industrial-robot spinout. 25-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from CAS-affiliated industrial arms or specialty Chinese semiconductor / vacuum robotics.

**Sources:**

1. en.wikipedia.org/wiki/Siasun_Robotics

---

### 2003-01 — Hercules + Argus (Ballard deep-archaeology two-body ROV)

- **id:** `hercules-argus-ballard-2003`
- **corpus:** private
- **ip status:** trade-secret (academic-publication for some systems)
- **creator:** Institute for Exploration + Inner Space Center + Ocean Exploration Trust (Bob Ballard); USA
- **disclosure citation:** Institute for Exploration / Inner Space Center / Ocean Exploration Trust (Bob Ballard) (USA). Hercules + Argus two-body deep-archaeology ROV system 2003+. Pair operates tethered: Argus (tow-sled providing lighting + 2nd-camera perspective) + Hercules (work-class ROV with manipulator + sample collection).
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-tethered`

**Prior art notes:**

> Hercules + Argus (Ballard 2003+) is the canonical deep-archaeology two-body ROV system. 22-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or ROV claim deriving from two-body cultural-heritage ROV operations.

**Sources:**

1. Ocean Exploration Trust + E/V Nautilus documentation.

---

### 2003-12 — KAIST KHR-2 / FX-2 humanoid (predecessor to HUBO)

- **id:** `kaist-fx-2-1995`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** KAIST; Jun-Ho Oh group
- **disclosure citation:** Korea Advanced Institute of Science and Technology (KAIST). KHR series of humanoids 1990s-2000s under Jun-Ho Oh group. KHR-1 (2002), KHR-2 (2003), KHR-3 / **HUBO** (2004) — the pre-HUBO lineage. Documented in: Park et al. 'Mechanical Design of the Humanoid Robot Platform, HUBO' Advanced Robotics 21(11) 2007.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric`, `control-zmp-balancing`

**Prior art notes:**

> The KAIST KHR series (1995-2004) is the foundational Korean academic humanoid lineage that produced HUBO. 22-year-deep public-domain prior art. Direct ancestor chain: KHR-1 → KHR-2 → KHR-3/HUBO → DRC-HUBO+. Together with HUBO (corpus entry) and DRC-HUBO+ (round-22), establishes the Korean humanoid academic lineage spanning 22+ years. Brings Korean entries to 8.

**Sources:**

1. Park et al. 'Mechanical Design of the Humanoid Robot Platform, HUBO' Advanced Robotics 21(11) 2007.
2. Jun-Ho Oh group publications (KAIST Humanoid Robot Research Center).

---

### 2006-04 — Sentry AUV (WHOI ABE successor; deep-search workhorse)

- **id:** `sentry-auv-whoi-2006`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Woods Hole Oceanographic Institution; Dana Yoerger group
- **disclosure citation:** Yoerger, D. et al. / Woods Hole Oceanographic Institution (USA). Sentry first deep-sea trials April 2006. Direct ABE successor; National Deep Submergence Facility workhorse for Deepwater Horizon (2010), hydrothermal-vent mapping, and deep-ocean exploration.
- **disclosed subsystems:** `auv`, `auv-hovering`, `actuator-electric`

**Prior art notes:**

> Sentry (WHOI 2006+) is the deep-search workhorse AUV — ABE successor. 19-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or AUV claim deriving from twin-hull hovering deep-search AUVs.

**Sources:**

1. en.wikipedia.org/wiki/Sentry_(AUV)

---

### 2006-09 — MAKO RIO orthopedic robot-arm-assisted surgery

- **id:** `mako-rio-stryker-2006`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** MAKO Surgical Corp. (Fort Lauderdale, FL, USA) → Stryker Corporation 2013
- **disclosure citation:** MAKO Surgical Corp. (Fort Lauderdale, FL, USA; founded 2004). RIO (Robotic-Arm Interactive Orthopedic) system FDA-cleared 2006 for partial knee. Acquired by Stryker Corporation December 2013 for USD 1.65B. Subsequent MAKO Total Knee 2017; MAKO 4 2025.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-haptic-boundary`, `actuator-electric`

**Prior art notes:**

> MAKO RIO (MAKO Surgical Fort Lauderdale 2006 → Stryker 2013) is the canonical robotic-arm-assisted orthopedic surgery system. 19-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from haptic-boundary-constrained surgical arms. Lineage descends from Barrett WAM Arm (round-45).

**Sources:**

1. en.wikipedia.org/wiki/MAKO_Surgical_Corp.

---

### 2007-07 — Modern multi-articulated prosthetic hands (i-LIMB / BeBionic / Michelangelo)

- **id:** `modern-multiarticulated-prosthetic-hands-2007-2012`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Touch Bionics (Edinburgh) → Össur (Iceland); RSL Steeper (UK) → Otto Bock (Germany); Otto Bock HealthCare (Duderstadt, Germany)
- **disclosure citation:** Touch Bionics Ltd. (Edinburgh, Scotland; founded 2003 by David Gow, NHS Lothian rehabilitation engineering spinout). i-LIMB myoelectric prosthetic hand product reveal July 2007. RSL Steeper Ltd. (UK) BeBionic hand 2010, acquired by Otto Bock HealthCare 2017. Otto Bock Michelangelo Hand reveal 2012. Touch Bionics acquired by Össur (Iceland) 2016; i-LIMB Quantum 2015.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-multi-articulated-finger`, `control-myoelectric`, `actuator-electric`

**Prior art notes:**

> Modern multi-articulated prosthetic hands (Touch Bionics i-LIMB 2007, RSL Steeper BeBionic 2010, Otto Bock Michelangelo 2012) are the defining commercial multi-articulated myoelectric prosthetic hand category. 13-19-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from individually-powered five-finger prosthetic hands or myoelectric multi-grip control. Lineage descends from Belgrade-USC Hand (round-42 belgrade-usc-tomovic-bekey-hand-1963) of foundational anthropomorphic prosthetics.

**Sources:**

1. ottobock.com/en-us/product/8E7----61161 (BeBionic).
2. Touch Bionics i-LIMB historical product page (Össur).

---

### 2008-01 — Robotiq Adaptive Grippers (2F-85, 2F-140, Hand-E, 3-Finger)

- **id:** `robotiq-adaptive-grippers-2008`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Robotiq Inc. (Lévis QC, Canada); Bouchard, Jobin, Duchaine; underactuated finger lineage from Laval University MARS hand
- **disclosure citation:** Robotiq Inc. (Lévis, Québec, Canada). Founded 2008 by Samuel Bouchard, Jean-Philippe Jobin, Vincent Duchaine. Adaptive Gripper product line 2008-2018: 2-Finger 85 (2F-85, 2014), 2-Finger 140 (2F-140, 2017), Hand-E (2018), 3-Finger Adaptive Gripper (2008). Underactuated finger mechanism descended from Laval University MARS hand (Laliberté, Birglen, Gosselin).
- **disclosed subsystems:** `mechanism-parallel-jaw-gripper`, `mechanism-underactuated-finger`, `actuator-electric`

**Prior art notes:**

> Robotiq Adaptive Grippers (Robotiq Lévis QC 2008+) are the canonical commercial cobot end-effector with 17+ years of deployment and 23,000+ units shipped. Direct shielding for any commercial humanoid claim deriving from underactuated parallel-jaw or three-finger adaptive grippers, or from cobot-tool plug-and-play architectures. Lineage descends from Laval University MARS hand (Laliberté / Birglen / Gosselin) underactuated mechanism.

**Sources:**

1. blog.robotiq.com/adaptive-robot-gripper-3-finger-history
2. robotiq.com/products/adaptive-grippers

---

### 2008-12 — Surena humanoid (Tehran University)

- **id:** `surena-tehran-university-2008`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Tehran University CAST + Iranian Ministry of Industry; Aghil Yousefi-Koma group
- **disclosure citation:** Tehran University Center of Advanced Systems and Technologies (CAST). Surena lineage: Surena (2008), Surena II (2010), Surena III (2015), Surena IV (December 2019). Yousefi-Koma, A. + Tehran University engineering team. Iran's flagship humanoid program.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `actuator-electric`, `control-zmp-balancing`

**Prior art notes:**

> The Surena lineage (Tehran University CAST, 2008-2020+) is Iran's flagship humanoid program. 17-year-deep public-domain academic prior art (Iran does not enforce most foreign patents; Iranian academic publications are public-domain by default). Establishes Iranian indigenous capability under sanctions for: 170 cm / 68 kg adult-class bipedal humanoid, 43-DoF whole-body, anthropomorphic 5-finger hands. Closes the Iran/Middle-East regional gap (corpus had 0 entries from Iran prior to this round).

**Sources:**

1. Tehran University CAST publications.
2. Yousefi-Koma, A. et al. — various IEEE / ASME conference papers.
3. Wikipedia 'Surena' (en.wikipedia.org/wiki/Surena_(robot)).
4. Iranian press coverage 2008-2020.

---

### 2008-12 — Universal Robots (Odense, Denmark)

- **id:** `universal-robots-denmark-2008`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Universal Robots A/S (Odense, Denmark; SDU spinout); Østergaard, Støy, Kassow founders
- **disclosure citation:** Universal Robots A/S (Odense, Denmark; founded 2005 by Esben Østergaard, Kasper Støy, Kristian Kassow as a University of Southern Denmark spinout). UR5 first commercial cobot reveal December 2008. Subsequently: UR3 (2015), UR10 (2012), UR16 (2019), e-Series (2018+), UR20/UR30 (2022+). Acquired by Teradyne 2015 for $285M. universal-robots.com.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-collaborative-robot`, `actuator-electric`, `control-impedance-control`

**Prior art notes:**

> Universal Robots is the canonical 2008+ commercial cobot anchor (Odense Denmark, SDU spinout). 17-year-deep public-disclosure prior art for: 6-DoF anthropomorphic cobot at the educational/industrial price point, ISO 10218 + ISO/TS 15066 collaborative-safety compliance, PolyScope teach-pendant programming model. **The architectural anchor of every subsequent commercial cobot** — Doosan (round-22 entry), Franka Emika, Aubo, Elite, Jaka, Universal Robots' own e-Series. The Odense Denmark cobot cluster (Robocluster consortium) is the Nordic robotics anchor. Direct shielding for any commercial humanoid claim that includes cobot-class collaborative-arm derivative applications. Closes the Denmark / Nordic gap (corpus had no Danish entries prior).

**Sources:**

1. Universal Robots corporate site (universal-robots.com).
2. Teradyne 10-K SEC filings (post-2015 acquisition).
3. Wikipedia 'Universal Robots' (en.wikipedia.org/wiki/Universal_Robots).

---

### 2009-04 — Honda Walking Assist Device / Stride Management Assist

- **id:** `honda-walking-assist-2009`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Honda Motor Co., Ltd. (Tokyo, Japan); ASIMO research lineage
- **disclosure citation:** Honda Motor Co., Ltd. (Tokyo, Japan). Walking Assist Device public demo April 2009 (R&D since 1999). Lease program 2015. Stride Management Assist variant. Pre-dates Samsung GEMS Hip (round-43) by 10 years for hip-only motor-on-belt assist.
- **disclosed subsystems:** `exoskeleton-lower-limb`, `exoskeleton-hip-only`, `actuator-electric`

**Prior art notes:**

> Honda Walking Assist Device (Honda Tokyo 2009+; R&D 1999+) is the foundational hip-only motor-on-belt walking-assist exo. 16-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from hip-only powered-belt exoskeletons. Lineage descends from Honda ASIMO (corpus asimo) bipedal-locomotion research.

**Sources:**

1. global.honda/en/newsroom/worldnews/2009/c090414Walking-Assist-Devices.html

---

### 2009-09 — Kinova Jaco / Gen3 (Canadian assistive 7-DoF arm)

- **id:** `kinova-jaco-2009`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Kinova Inc. (Montreal, Quebec, Canada); Charles Deguire founder
- **disclosure citation:** Kinova Inc. (Montreal, Quebec, Canada; founded 2006 by Charles Deguire). Jaco assistive arm reveal 2009 (originally for wheelchair-mounted disability use). Subsequent: Jaco2 (2014), Gen3 (2018) 7-DoF research-grade, Gen3 Lite (2020).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`

**Prior art notes:**

> Kinova Jaco / Gen3 (Montreal 2009+) is the Canadian assistive + research arm family. 16-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from wheelchair-mounted assistive arms or low-cost research-grade 7-DoF cobots.

**Sources:**

1. spectrum.ieee.org/startup-spotlight-kinova

---

### 2010-03 — TRIDENT (first major EU autonomous underwater intervention)

- **id:** `trident-eu-fp7-iauv-2010`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** UJI Spain (lead) + multi-EU consortium; EU FP7-funded
- **disclosure citation:** TRIDENT consortium (UJI Spain coordinated; multi-EU partners). EU FP7 project launched March 1, 2010; ended 2013. First major EU autonomous underwater intervention I-AUV with dexterous hand+arm system.
- **disclosed subsystems:** `auv`, `auv-iauv`, `manipulator-arm`, `end-effector-anthropomorphic-hand`, `actuator-electric`

**Prior art notes:**

> TRIDENT (EU FP7 / UJI Spain 2010-2013) is the first major EU autonomous underwater intervention I-AUV. 15-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or aquatic-robot claim deriving from autonomous underwater intervention with manipulator arm + dexterous hand.

**Sources:**

1. cordis.europa.eu/project/id/248497

---

### 2010-04 — Willow Garage PR2 (defining ROS mobile-manipulation platform)

- **id:** `willow-garage-pr2-2010`
- **corpus:** academic
- **ip status:** open-permissive (ROS-integrated; hardware open-spec)
- **creator:** Willow Garage Inc. (Menlo Park, CA, USA); Scott Hassan + Steve Cousins
- **disclosure citation:** Willow Garage Inc. (Menlo Park, CA, USA; founded 2006 by Scott Hassan + Steve Cousins). PR2 (Personal Robot 2) commercial reveal 2010 ('PR2 Beta Program'). Mobile manipulator with two 7-DoF arms on omnidirectional base. Defining open-source ROS mobile-manipulation platform.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-mobile`, `manipulator-dual-arm`, `actuator-electric`, `control-ros`

**Prior art notes:**

> Willow Garage PR2 (Menlo Park 2010-2014) is the defining open-source ROS mobile-manipulation platform. 15-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from dual-arm mobile manipulators or ROS-integrated platforms. Steve Cousins lineage continues to Savioke (corpus savioke-relay-2014).

**Sources:**

1. Willow Garage PR2 documentation (historical).

---

### 2010-07 — Rex Bionics REX self-supporting exoskeleton

- **id:** `rex-bionics-rex-2010`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Rex Bionics Ltd. (Auckland, New Zealand); Robert Irving + Richard Little
- **disclosure citation:** Rex Bionics Ltd. (Auckland, New Zealand; founded 2007 by Robert Irving + Richard Little). REX commercial reveal July 2010. First commercial self-supporting hands-free powered exoskeleton — the user is hands-free, no crutches, the exo balances itself.
- **disclosed subsystems:** `exoskeleton-lower-limb`, `exoskeleton-self-supporting`, `control-quasistatic-walking`, `actuator-electric`

**Prior art notes:**

> Rex Bionics REX (Auckland NZ 2010+) is the first commercial self-supporting hands-free powered exoskeleton. 15-year-deep public-disclosure prior art. Pre-dates Wandercraft Atalante (round-43) by 8 years for hands-free walking, though REX uses quasi-static-stable gait rather than dynamic-walking. Direct shielding for any commercial humanoid or Iron Man-class claim deriving from hands-free powered exoskeletons.

**Sources:**

1. rexbionics.com/

---

### 2010-08 — Jiaolong (China 7000 m HOV)

- **id:** `jiaolong-china-2010`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** China Ship Scientific Research Center / CSSRC (Wuxi, China)
- **disclosure citation:** China Ship Scientific Research Center (CSSRC) (Wuxi, China). Jiaolong first sea trial 2010; reached 7,062 m on June 27, 2012 in Mariana Trench. The first Chinese 7,000 m HOV; made China the fifth nation with deep-HOV capability.
- **disclosed subsystems:** `hov`, `actuator-electric`

**Prior art notes:**

> Jiaolong (CSSRC China 2010+) is the first Chinese 7,000 m HOV. 15-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from Chinese deep HOVs. Lineage: Jiaolong (7,000 m) → Shenhai Yongshi (4,500 m, 2017) → Fendouzhe (full-ocean-depth, 2020 round-47).

**Sources:**

1. en.wikipedia.org/wiki/Jiaolong_(submersible)

---

### 2010-09 — Girona 500 I-AUV (UdG/IRSLab reconfigurable)

- **id:** `girona-500-uji-iauv-2010`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** University of Girona (UdG) IRSLab (Spain); Pere Ridao group
- **disclosure citation:** Ribas, D., Palomeras, N., Ridao, P., Carreras, M., Mallios, A. / University of Girona (UdG) IRSLab (Spain). Girona 500 first trial 2010. Reconfigurable intervention AUV with arm; backbone of TRIDENT/MERBOTS/TWINBOT EU manipulation projects.
- **disclosed subsystems:** `auv`, `auv-iauv`, `manipulator-arm`, `actuator-electric`

**Prior art notes:**

> Girona 500 (UdG IRSLab Spain 2010+) is the reconfigurable intervention AUV — backbone of EU manipulation projects. 15-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or aquatic-robot claim deriving from reconfigurable hovering intervention AUVs.

**Sources:**

1. iqua.cat/products/sparus-ii-auv/

---

### 2011-01 — Mazor Renaissance / Stealth Spine guidance

- **id:** `mazor-renaissance-medtronic-2011`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Mazor Robotics Ltd. (Caesarea, Israel; Moshe Shoham Technion); → Medtronic 2018
- **disclosure citation:** Mazor Robotics Ltd. (Caesarea, Israel; founded 2000 by Moshe Shoham, Technion). SpineAssist FDA-cleared 2004; Renaissance FDA-cleared 2011 (1.5 mm accuracy bone-mounted spine guidance). Mazor X 2017. Acquired by Medtronic 2018 for USD 1.6B.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-parallel`, `actuator-electric`

**Prior art notes:**

> Mazor Robotics SpineAssist + Renaissance + Mazor X (Caesarea Israel 2004-2017+; Medtronic 2018) is the bone-mounted spine surgical guidance system. 21-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from bone-mounted parallel-mechanism surgical guidance arms.

**Sources:**

1. en.wikipedia.org/wiki/Mazor_Robotics

---

### 2012-01 — Estun Automation industrial robots (CN #1 by shipments)

- **id:** `estun-automation-1993`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Estun Automation Co., Ltd. (Nanjing, China); Wu Bo founder
- **disclosure citation:** Estun Automation Co., Ltd. (Nanjing, China; founded 1993 by Wu Bo). Industrial robotics product line launched 2012. The #1 domestic Chinese industrial-arm maker by shipments. Listed on Shenzhen Stock Exchange 2015.
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`

**Prior art notes:**

> Estun Automation (Nanjing 1993; robotics 2012+) is the #1 Chinese domestic industrial-arm maker by shipments. 13-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from Chinese-OEM industrial arms.

**Sources:**

1. en.wikipedia.org/wiki/Estun_Automation

---

### 2012-02 — Ekso Bionics Ekso / EksoNR overground rehab exoskeleton

- **id:** `ekso-bionics-eksonr-2012`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Ekso Bionics Holdings (Richmond CA, USA); Homayoon Kazerooni Berkeley lineage; founded 2005
- **disclosure citation:** Ekso Bionics Holdings, Inc. (Richmond, CA, USA; founded 2005 by Homayoon Kazerooni's group at Berkeley Bionics, renamed Ekso Bionics 2011). Ekso commercial reveal February 2012. EksoNR (Neural Rehabilitation) 2019; FDA clearance for stroke + spinal-cord-injury 2016, brain-injury 2020, multiple sclerosis 2021.
- **disclosed subsystems:** `exoskeleton-lower-limb`, `exoskeleton-upper-limb`, `actuator-electric`, `control-gait-rehabilitation`

**Prior art notes:**

> Ekso Bionics Ekso / EksoNR (Richmond CA 2012+) is the first broadly FDA-cleared overground rehabilitation exoskeleton. 13-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from FDA-cleared overground lower-limb rehab exos. Together with Hocoma Lokomat (round-43; treadmill-mounted) and Wandercraft Atalante (round-43; self-balancing), establishes the medical-exoskeleton prior-art chain. Lineage descends from BLEEX (corpus).

**Sources:**

1. en.wikipedia.org/wiki/Ekso_Bionics
2. ir.eksobionics.com/press-releases/detail/689/ekso-bionics-receives-fda-clearance-to-market-its

---

### 2012-03 — Deepsea Challenger (Cameron solo Challenger Deep)

- **id:** `deepsea-challenger-cameron-2012`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** James Cameron / Acheron Project Pty Ltd (Australia/USA)
- **disclosure citation:** James Cameron / Acheron Project Pty Ltd (Australia/USA). Solo Challenger Deep dive March 26, 2012 (10,908 m). First solo human descent to Challenger Deep; vertical 'torpedo' HOV architecture.
- **disclosed subsystems:** `hov`, `actuator-electric`

**Prior art notes:**

> Deepsea Challenger (Cameron / Acheron 2012) is the first solo human descent to Challenger Deep + the vertical 'torpedo' HOV architecture. 13-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from single-person vertical-configuration HOVs.

**Sources:**

1. en.wikipedia.org/wiki/Deepsea_Challenger

---

### 2012-08 — Sandia Hand modular 12-DoF gripper

- **id:** `sandia-hand-2012`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Sandia National Laboratories (Albuquerque, NM, USA); Curt Salisbury (PI); DARPA ARM-H program
- **disclosure citation:** Quigley, M., Salisbury, C., Ng, A.Y., Salisbury, J.K. 'Mechatronic design of an integrated robotic hand'. International Journal of Robotics Research 33(5), 2014. Sandia National Laboratories (Albuquerque, NM, USA) DARPA Autonomous Robotic Manipulation (ARM-H) program. Reveal August 2012; ~$10K modular hand target.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-modular-finger`, `actuator-electric`

**Prior art notes:**

> Sandia Hand (Sandia National Laboratories 2012, IJRR 2014) is the canonical cost-reduced modular anthropomorphic hand. 13-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from modular-interchangeable-finger architectures or low-cost (\$10k-class) anthropomorphic hands. DARPA ARM-H program lineage.

**Sources:**

1. sandia.gov/research/sandia-hand/
2. spectrum.ieee.org/sandia-labs-robotic-hand-
3. Quigley, M. et al. IJRR 33(5), 2014.

---

### 2013-04 — KUKA LBR iiwa (intelligent industrial work assistant)

- **id:** `kuka-lbr-iiwa-2013`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** KUKA AG (Augsburg, Germany); DLR LWR licensee
- **disclosure citation:** KUKA AG (Augsburg, Germany; founded 1898). LBR iiwa commercial reveal Hannover Messe April 2013. World's first series-produced HRC-compatible 7-DoF cobot with joint torque sensors. Direct descendant of DLR LWR III (round-45 dlr-lwr-1991-2003) via licensing agreement.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> KUKA LBR iiwa (KUKA Augsburg 2013+) is the world's first series-produced HRC 7-DoF cobot with joint torque sensors. 12-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from 7-DoF cobots with joint torque sensing. Lineage descends from DLR LWR III (round-45 dlr-lwr-1991-2003).

**Sources:**

1. kuka.com/en-us/products/robotics-systems/industrial-robots/lbr-iiwa

---

### 2014-01 — JAKA Robotics Zu cobots (wireless-teach)

- **id:** `jaka-robotics-zu-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** JAKA Robotics Co., Ltd. (Shanghai, China)
- **disclosure citation:** JAKA Robotics Co., Ltd. (Shanghai, China; founded 2014). Zu5 cobot launch ~2017; Zu7 / Zu12 / Pro variants subsequent. First commercially deployed wireless-teach cobot.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `control-wireless-teach`

**Prior art notes:**

> JAKA Robotics Zu (Shanghai 2014+) is the first commercially deployed wireless-teach cobot. 11-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from wireless-teach cobots or Shanghai-based Chinese cobot specialists.

**Sources:**

1. hannovermesse.de/apollo/hannover_messe_2022/obs/Binary/A1142167/Welcome%20to%20JAKA%20Robotics.pdf

---

### 2014-04 — Allegro Hand (Wonik / SimLab)

- **id:** `allegro-hand-wonik-simlab-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Wonik Robotics + SimLab Co., Ltd. (Seoul, South Korea)
- **disclosure citation:** Wonik Robotics + SimLab Co., Ltd. (Seoul, South Korea). Allegro Hand commercial reveal April 2014 via wonikrobotics.com / simlab.co.kr. **The de facto academic-deployment reference for 16-DoF 4-finger dexterous hands** — used in OpenAI Dactyl (corpus entry openai-dactyl) Rubik's-Cube manipulation 2019, and 100+ academic publications.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-driven`, `actuator-electric`

**Prior art notes:**

> Allegro Hand is the canonical academic-deployment reference 16-DoF 4-finger dexterous hand (Wonik / SimLab Korea, 2014+). 11-year-deep public-disclosure prior art. **Used in OpenAI Dactyl 2019 Rubik's-Cube manipulation (corpus entry openai-dactyl)** + 100+ academic publications. Direct architectural successor to BarrettHand (round-27 entry below). Direct shielding for any commercial humanoid claim on 16-DoF tendon-driven dexterous hand.

**Sources:**

1. Wonik Robotics corporate site (wonikrobotics.com).
2. SimLab Allegro Hand product page (simlab.co.kr/allegro-hand).
3. OpenAI Dactyl Rubik's Cube paper (corpus entry openai-dactyl) uses Allegro Hand as the simulated hand.

---

### 2014-05 — PAL Robotics TIAGo mobile manipulator

- **id:** `pal-robotics-tiago-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** PAL Robotics S.L. (Barcelona, Spain)
- **disclosure citation:** PAL Robotics S.L. (Barcelona, Spain). TIAGo product reveal May 2014. Subsequent product variants: TIAGo Pro (dual-arm), TIAGo OMNI (omnidirectional drive), TIAGo++ (research kit). pal-robotics.com. Sister product to REEM-C humanoid (corpus entry reem-c).
- **disclosed subsystems:** `mechanism-mobile-base`, `mechanism-manipulator-arm`, `mechanism-telescoping-mast`, `actuator-electric`

**Prior art notes:**

> PAL Robotics TIAGo (Barcelona Spain 2014+) is the canonical Spanish commercial mobile manipulator. 11-year-deep public-disclosure prior art. Sister product line to REEM-C (corpus). Together with REEM-C, brings Spanish commercial-robotics representation to 2 specific platform entries. Architectural sibling to Hello Robot Stretch (round-17), Fetch (round-35), BD Stretch warehouse (round-34). Direct shielding for any commercial humanoid claim deriving from telescoping-mast mobile-manipulator commercial deployments.

**Sources:**

1. PAL Robotics TIAGo product page (pal-robotics.com).
2. PAL Robotics corporate site.

---

### 2014-05 — DEKA / Mobius Bionics LUKE Arm

- **id:** `deka-mobius-luke-arm-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** DEKA Research and Development Corporation (Manchester, NH, USA); Dean Kamen; DARPA Revolutionizing Prosthetics; commercialized as Mobius Bionics
- **disclosure citation:** DEKA Research and Development Corporation (Manchester, NH, USA; Dean Kamen). DARPA Revolutionizing Prosthetics program 2006-2014. FDA clearance May 2014. Mobius Bionics commercial launch July 2016. Named 'LUKE' after Star Wars (Luke Skywalker's prosthetic arm).
- **disclosed subsystems:** `end-effector-anthropomorphic-hand`, `exoskeleton-upper-limb`, `actuator-electric`, `control-multi-modal-user-input`

**Prior art notes:**

> DEKA / Mobius Bionics LUKE Arm (DEKA Manchester NH 2014; Mobius Bionics 2016) is the first FDA-cleared integrated multi-joint upper-extremity prosthesis. 11-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from integrated multi-joint upper-extremity prostheses. DARPA RP outcome; sister to APL MPL (corpus apl-mpl-revolutionizing-prosthetics-2009).

**Sources:**

1. darpa.mil/news/2016/mobius-bionics-luke-arms-walter-reed
2. darpa.mil/about/innovation-timeline/revolutionizing-prosthetics

---

### 2014-08 — Blue Robotics BlueROV2 (affordable open-hardware ROV)

- **id:** `bluerov2-blue-robotics-2016`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Blue Robotics Inc. (Torrance, CA, USA); Rusty Jordan + Erin Riley
- **disclosure citation:** Blue Robotics Inc. (Torrance, CA, USA; founded 2014 by Rusty Jordan + Erin Riley). BlueROV1 Kickstarter 2014; BlueROV2 production 2016. ArduSub-based open-source firmware ecosystem.
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-open-source`

**Prior art notes:**

> Blue Robotics BlueROV1/2 (Torrance CA 2014/2016+) is the democratized affordable open-hardware ROV. 11-year-deep open-permissive prior art. Direct shielding for any commercial humanoid or ROV claim deriving from open-source-ArduSub-firmware ROVs or BlueRobotics-component ecosystems.

**Sources:**

1. en.wikipedia.org/wiki/BlueROV2
2. bluerobotics.com

---

### 2015-01 — OnRobot RG2 / RG6 / VGC10 cobot grippers

- **id:** `onrobot-rg-grippers-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** On Robot A/S (Odense, Denmark); Christiansen + Fuglsang; absorbed Perception Robotics + OptoForce 2018
- **disclosure citation:** On Robot A/S (Odense, Denmark). Founded 2015 by Bilge J. Christiansen + Ebbe O. Fuglsang. RG2 (2015) and RG6 (2016) electric parallel grippers; VG10 / VGC10 compressor-free electric vacuum grippers (2017-2019). Merged with Perception Robotics (NASA-JPL gecko-microhair-licensed) and OptoForce (Hungarian F/T sensor) 2018.
- **disclosed subsystems:** `mechanism-parallel-jaw-gripper`, `mechanism-vacuum-gripper`, `mechanism-gecko-microhair-adhesion`, `actuator-electric`

**Prior art notes:**

> OnRobot RG-line and VGC-line grippers (Odense Denmark 2015+) are the canonical 'cable-free cobot tool' commercial category. 11-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from plug-and-play electric parallel grippers, compressor-free electric vacuum grippers, or gecko-microhair dry-adhesion grippers. Together with Robotiq (round-42) and SCHUNK Co-act (round-42), establishes the global cobot-gripper prior-art chain across CA / DK / DE.

**Sources:**

1. onrobot.com/en/about
2. onrobot.com/en/products/gecko-gripper

---

### 2015-04 — ABB YuMi IRB 14000 dual-arm cobot

- **id:** `abb-yumi-irb-14000-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** ABB Asea Brown Boveri (Zurich + Västerås)
- **disclosure citation:** ABB Asea Brown Boveri (Zurich, Switzerland + Västerås, Sweden). YuMi IRB 14000 commercial reveal Hannover Fair April 2015. World's first truly collaborative dual-arm 7-DoF cobot.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-dual-arm`, `manipulator-cobot`, `actuator-electric`

**Prior art notes:**

> ABB YuMi IRB 14000 (ABB Zurich + Västerås 2015+) is the world's first truly collaborative dual-arm 7-DoF cobot. 10-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from collaborative dual-arm 7-DoF cobots. Lineage descends from ASEA IRB-6 (round-45).

**Sources:**

1. abb.com/global/en/areas/robotics/products/robots/collaborative-robots/dual-arm-yumi

---

### 2015-06 — DRC-HUBO+ (DARPA Robotics Challenge winner)

- **id:** `kaist-drc-hubo-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** KAIST Humanoid Robot Research Center; Jun-Ho Oh group + Rainbow Robotics
- **disclosure citation:** KAIST + Rainbow Robotics. 'DRC-HUBO+: A robotic platform for the DARPA Robotics Challenge'. Lim, J., Lee, I., Shim, I., et al. International Journal of Robotics Research / Journal of Field Robotics 2017. Won 1st place at DARPA Robotics Challenge Finals Pomona June 2015 — completing all 8 disaster-response tasks in 44m28s. The follow-on commercial version was Rainbow Robotics' first product (corpus has rainbow-robotics-rb-y1 as the modern commercial successor).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-wheel-leg-hybrid`, `actuator-electric`, `control-whole-body-qp`, `control-supervised-autonomy`

**Prior art notes:**

> DRC-HUBO+ (KAIST + Rainbow Robotics, DRC 2015) is the canonical Korean academic humanoid milestone — 1st place winner of the DARPA Robotics Challenge Finals June 2015. 10-year-deep public-domain prior art for: wheel-leg hybrid transformable bipedal humanoid (knee-rolling for stability + bipedal for stairs), operator-supervised whole-body autonomy under intermittent comm. Direct shielding for any commercial humanoid claim on transformable lower-body morphology or DRC-class disaster-response capability set. Established Rainbow Robotics' commercial humanoid lineage (corpus entry rainbow-robotics-rb-y1).

**Sources:**

1. Lim, J. et al. JFR / IJRR 2017.
2. DARPA Robotics Challenge Finals 2015 Pomona results.
3. KAIST Humanoid Robot Research Center publications.
4. IEEE Spectrum coverage 'Korean Team Wins DARPA Robotics Challenge' 2015.

---

### 2015-09 — AUBO Robotics i5 / i3 / i7 / i10 cobots

- **id:** `aubo-robotics-i5-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** AUBO Robotics (Beijing, China; Smokie Robotics origins)
- **disclosure citation:** AUBO Robotics (Beijing, China; founded 2015 from Smokie Robotics origins). i5 cobot launch September 2015. Subsequent i3 / i7 / i10 cobots 2017. Open-architecture cobot widely cloned.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`

**Prior art notes:**

> AUBO Robotics i5 (Beijing 2015+) is the open-architecture Chinese cobot reference design. 10-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from open-architecture ROS-integrated Chinese cobots.

**Sources:**

1. auborobotic.com/about-us/

---

### 2015-09 — Mecademic Meca500 micro-cobot (5-µm precision)

- **id:** `mecademic-meca500-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Mecademic Inc. (Montreal, Quebec, Canada); Ilian Bonev (ÉTS Montreal)
- **disclosure citation:** Mecademic Inc. (Montreal, Quebec, Canada; founded 2013 by Ilian Bonev, ÉTS Montreal). Meca500 reveal September 2015. Smallest 6-axis industrial arm in the world (5 µm repeatability).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-precision`, `actuator-electric`

**Prior art notes:**

> Mecademic Meca500 (Montreal 2015+) is the smallest 6-axis industrial arm in the world (5-µm repeatability). 10-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from precision micro-cobot arms.

**Sources:**

1. mecademic.com/products/meca500-industrial-robot-arm/

---

### 2015-09 — Eelume snake robot (NTNU AMOS spinout)

- **id:** `eelume-ntnu-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Eelume AS (Trondheim, Norway); NTNU AMOS spinout; Pål Liljebäck + Kristin Pettersen lineage
- **disclosure citation:** Eelume AS (Trondheim, Norway; NTNU AMOS spinout founded 2015). NTNU snake-robot research from 2004 (Pål Liljebäck, Kristin Pettersen). Eelume vehicle for IMR (Inspection-Maintenance-Repair) in confined offshore structures.
- **disclosed subsystems:** `biomimetic-aquatic`, `mechanism-articulated-snake`, `actuator-electric`

**Prior art notes:**

> Eelume (NTNU AMOS spinout Trondheim 2015+) is the canonical articulated subsea snake robot for IMR. 10-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or aquatic-robot claim deriving from articulated subsea snake robots or resident-vehicle IMR architectures.

**Sources:**

1. en.wikipedia.org/wiki/Eelume

---

### 2016-01 — Inovance Technology industrial robots ('Little Huawei')

- **id:** `inovance-shenzhen-2003`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Shenzhen Inovance Technology Co., Ltd. (Shenzhen, China); Zhu Xingming + ex-Huawei colleagues
- **disclosure citation:** Shenzhen Inovance Technology Co., Ltd. (Shenzhen, China; founded 2003 by Zhu Xingming + ex-Huawei colleagues, hence 'Little Huawei'). Entered industrial robotics 2016. #2 Chinese domestic robot maker by shipments after Estun (round-45).
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`

**Prior art notes:**

> Inovance Technology (Shenzhen 2003; robotics 2016+) is the 'Little Huawei' #2 Chinese domestic industrial-robot maker. 9-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from vertically-integrated Chinese-OEM industrial arms.

**Sources:**

1. en.wikipedia.org/wiki/Inovance

---

### 2016-01 — ZeroErr eRob (Chinese joint actuators for humanoids)

- **id:** `zeroerr-erob-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** ZeroErr (Guangdong, China)
- **disclosure citation:** ZeroErr (Guangdong, China; founded ~2016). Joint actuator + magnetic-encoder specialist for harmonic-reducer-based humanoid joints.
- **disclosed subsystems:** `actuator-component`, `actuator-electric`

**Prior art notes:**

> ZeroErr eRob (Guangdong 2016+) is the Chinese joint-actuator + magnetic-encoder component supplier for humanoid OEMs. 9-year-deep public-disclosure prior art.

**Sources:**

1. kr-asia.com/behind-the-robotics-boom-zeroerr-raises-funds-to-build-the-parts-that-power-it

---

### 2016-03 — Indego modular powered lower-limb exoskeleton

- **id:** `indego-vanderbilt-parker-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Vanderbilt University CIM (Michael Goldfarb) → Parker Hannifin → Ekso Bionics 2023
- **disclosure citation:** Vanderbilt University Center for Intelligent Mechatronics (Michael Goldfarb's group; prototype 2010). Parker Hannifin license 2012; Indego FDA clearance March 2016. Indego acquired by Ekso Bionics 2023.
- **disclosed subsystems:** `exoskeleton-lower-limb`, `exoskeleton-modular`, `actuator-electric`

**Prior art notes:**

> Indego (Vanderbilt + Parker Hannifin 2016+; → Ekso Bionics 2023) is the canonical modular split-at-hips lower-limb exoskeleton. 9-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from modular seated-don lower-limb exos.

**Sources:**

1. news.vumc.org/2016/03/10/fda-approves-vanderbilt-designed-indego-exoskeleton-for-clinical-and-personal-use/

---

### 2016-06 — Boston Dynamics SpotMini

- **id:** `boston-dynamics-spotmini-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics
- **disclosure citation:** Boston Dynamics. SpotMini public reveal June 2016 demo video; subsequent IEEE Spectrum coverage 2017-2018; capability demonstrations via Boston Dynamics YouTube. Discontinued in favor of Spot (the production quadruped) circa 2019.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric`, `control-rl-policy`, `control-teleoperation`

**Prior art notes:**

> SpotMini is the architectural predecessor to commercial Spot. ~9-year-deep public-disclosure prior art for: all-electric quadruped morphology (distinct from hydraulic BigDog/Spot ancestors), dorsal-mount manipulator on quadruped base, Velodyne+depth-camera quadruped sensor stack. Trade-secret control software, public capability surface. Direct shielding for any commercial humanoid-quadruped or quadruped-manipulator claim. Cited in cheetah-cub-epfl and black-mirror-metalhead-2017 prior_art_notes; round-14 backfill closes those citation chains.

**Sources:**

1. Boston Dynamics YouTube reveal videos June 2016 and 2018.
2. IEEE Spectrum 'Boston Dynamics' SpotMini Is All Electric, Agile, and Has a Capable Face-Arm', 2017.
3. Vision Systems Design coverage 2018.

---

### 2016-12 — Techman Robot TM5 (first cobot with built-in vision)

- **id:** `techman-robot-tm5-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Techman Robot Inc. (Taoyuan, Taiwan; Quanta Computer spinout)
- **disclosure citation:** Techman Robot Inc. (Taoyuan, Taiwan; founded 2015 as Quanta Computer spinout). TM5 cobot iREX 2015 debut → first commercial shipments end-2016. First cobot with built-in vision system. OMRON co-distribution partnership.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `sensing-integrated-vision`

**Prior art notes:**

> Techman Robot TM5 (Taoyuan Taiwan 2016+; Quanta spinout) is the first cobot with built-in vision system. 9-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from vision-integrated cobots or Taiwanese-OEM cobots.

**Sources:**

1. en.wikipedia.org/wiki/Techman

---

### 2017-01 — Samsung GEMS Hip + Korean industrial wearables

- **id:** `samsung-gems-hip-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Hyundai Motor Group + Samsung Electronics (Seoul, South Korea)
- **disclosure citation:** Hyundai Motor Group (Seoul, South Korea). H-MEX paraplegic medical exo CES January 2017; CEX chairless 1.6 kg passive sit-stand 2018; Vex upper-body overhead industrial vest 2018; X-ble MEX medical rehab 2024. Samsung Electronics GEMS Hip powered hip assist 2019.
- **disclosed subsystems:** `exoskeleton-lower-limb`, `exoskeleton-upper-limb`, `exoskeleton-hip-only`, `actuator-electric`

**Prior art notes:**

> Samsung GEMS Hip + Hyundai H-MEX / CEX / Vex / X-ble (Seoul South Korea 2017+) establish the Korean industrial-conglomerate wearable-robotics product family. 9-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or Iron Man-class claim deriving from Korean OEM wearable-robotics. Lineage descends from Honda Walking Assist (round-43) for Samsung GEMS Hip, and from BLEEX/HULC for Hyundai H-MEX. Geographic balance with Japanese (Honda, Cyberdyne HAL corpus) and US (Ekso, Indego) wearable-robotics OEMs.

**Sources:**

1. cnbc.com/2017/02/01/hyundai-debuts-a-miracle-device-that-can-help-paraplegics-walk.html

---

### 2017-04 — Franka Emika Panda 7-DoF research cobot

- **id:** `franka-emika-panda-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Franka Emika GmbH (Munich, Germany); Sami Haddadin (ex-DLR)
- **disclosure citation:** Franka Emika GmbH (Munich, Germany; founded 2016 by Sami Haddadin + colleagues, ex-DLR). Panda commercial reveal 2017. Successor: Franka Research 3 (2022 post-restructure as Franka Robotics).
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> Franka Emika Panda (Munich 2017+; Franka Research 3 2022) is the canonical sub-€10K research-grade torque-sensor 7-DoF cobot. 8-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from low-cost 7-DoF research cobots with joint torque sensing. Lineage descends from DLR LWR III (round-45 dlr-lwr-1991-2003).

**Sources:**

1. franka.de/

---

### 2017-05 — Denso COBOTTA compact desktop cobot

- **id:** `denso-cobotta-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Denso Wave Inc. (Aichi, Japan; Toyota Group)
- **disclosure citation:** Denso Wave Inc. (Aichi, Japan; Toyota Group). COBOTTA prototype reveal May 2017; productized 2018. Sub-1 kg desktop cobot prototype. Subsequent: COBOTTA Pro (2022) higher-payload industrial-grade variant.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `manipulator-desktop`, `actuator-electric`

**Prior art notes:**

> Denso COBOTTA (Denso Wave Aichi 2017+; COBOTTA Pro 2022) is the sub-1 kg desktop cobot reference. 8-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from sub-1-kg desktop-form-factor cobots.

**Sources:**

1. roboticsandautomationnews.com/2017/05/17/denso-unveils-collaborative-robot-prototype-it-calls-cobotta/12374/

---

### 2017-08 — Robotis OP3

- **id:** `robotis-op3-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Robotis Co., Ltd. (Seoul, South Korea)
- **disclosure citation:** Robotis Co., Ltd. (Seoul, South Korea). OP3 educational humanoid kit reveal August 2017 via robotis.com. Successor to DARwIn-OP (corpus entry darwin-op, ~2010 Virginia Tech / Robotis collaboration). The platform deployed by DeepMind for the Haarnoja humanoid soccer paper (Science Robotics 2024, corpus entry deepmind-humanoid-soccer-haarnoja-2024).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric`, `control-rl-policy`

**Prior art notes:**

> Robotis OP3 is the canonical Korean educational/research humanoid platform (Robotis 2017+). 8-year-deep public-disclosure prior art. **The platform DeepMind humanoid soccer (round-18 entry) ran on** — round-26 closes that hardware-platform citation. Direct shielding for any commercial humanoid claim on small-form-factor (Kid-Size) educational humanoid. Brings Korean entries to 7.

**Sources:**

1. Robotis OP3 product page (robotis.com).
2. DeepMind humanoid soccer paper Science Robotics 2024.

---

### 2017-08 — Han's Robot Elfin / EX / SCR cobot family

- **id:** `hans-robot-elfin-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Han's Robot Co., Ltd. (Shenzhen, China; subsidiary of Han's Laser Technology)
- **disclosure citation:** Han's Robot Co., Ltd. (Shenzhen, China; founded August 2017 as subsidiary of Han's Laser Technology). Elfin cobot series launch 2017. EX heavy-payload variant + SCR series. 30,000 cobots/year capacity in Foshan.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`

**Prior art notes:**

> Han's Robot Elfin (Shenzhen 2017+) is one of the largest Chinese cobot makers by volume. 8-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from large-volume Chinese-OEM cobots.

**Sources:**

1. linkedin.com/company/hansrobot

---

### 2017-09 — Doosan Robotics M-series cobots

- **id:** `doosan-robotics-cobots-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Doosan Robotics (Suwon, South Korea)
- **disclosure citation:** Doosan Robotics, Inc. (Suwon, South Korea; Doosan Group subsidiary, founded 2015). M-series cobot product reveal September 2017 via doosanrobotics.com. M0609, M1013, M1509, M1013 lineup. Subsequent A-series (2021), H-series (2022) commercial expansions. KOSDAQ IPO 2023.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-collaborative-robot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> Doosan Robotics M-series is the canonical Korean commercial collaborative-robot arm family (2017+). 8-year-deep public-disclosure prior art for: 6-axis joint-torque-sensing cobot, ISO 10218 + ISO/TS 15066 compliant collaborative robot. The Korean commercial cobot leader (vs. Universal Robots Denmark / Franka Emika Germany / Kuka Germany). Direct shielding for any commercial humanoid claim on collaborative-robot-arm derivative applications, particularly anthropomorphic-arm joint-torque sensing as deployed in Optimus Gen 3 / Apptronik Apollo.

**Sources:**

1. Doosan Robotics corporate site (doosanrobotics.com).
2. KOSDAQ IPO filings 2023.

---

### 2017-09 — Yaskawa Motoman HC10 cobot

- **id:** `yaskawa-motoman-hc10-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Yaskawa Electric Corporation (Kitakyushu, Japan)
- **disclosure citation:** Yaskawa Electric Corporation (Kitakyushu, Japan; founded 1915). Motoman HC10 commercial reveal September 2017. Yaskawa's first cobot. Yaskawa is the largest Japanese industrial-robot OEM by revenue.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-cobot`, `actuator-electric`

**Prior art notes:**

> Yaskawa Motoman HC10 (Kitakyushu 2017+) is Yaskawa's first cobot and the Japanese cobot answer to Universal Robots. 8-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from Japanese-OEM cobots.

**Sources:**

1. yaskawa-global.com/newsrelease/product/9036

---

### 2018-01 — German Bionic Cray X IoT-connected industrial exoskeleton

- **id:** `german-bionic-cray-x-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** German Bionic Systems GmbH (Augsburg, Germany)
- **disclosure citation:** German Bionic Systems GmbH (Augsburg, Germany; founded 2017 by Armin Schmidt + Eric Eitel + Norma Steller). Cray X first generation 2018; v5 launch 2021. First TÜV-certified powered industrial exo. First IoT-connected powered exo with cloud telemetry.
- **disclosed subsystems:** `exoskeleton-upper-limb`, `exoskeleton-iot-connected`, `actuator-electric`, `control-cloud-telemetry`

**Prior art notes:**

> German Bionic Cray X (Augsburg 2018+) is the first IoT-connected powered industrial exo with cloud telemetry. 7-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from cloud-connected wearable robotics or Industry-4.0 data-loop exoskeletons.

**Sources:**

1. germanbionic.com/en/solutions/exoskeletons/crayx/

---

### 2018-01 — Inspire-Robots RH56 5-finger 6-DoF dexterous hand

- **id:** `inspire-robots-rh56-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Inspire-Robots Co., Ltd. (Beijing, China)
- **disclosure citation:** Inspire-Robots Co., Ltd. (Beijing, China). RH56 series 5-finger 6-DoF dexterous hand commercial reveal ~2018. Used by Unitree G1 / H2, Fourier GR-1, and many other Chinese commercial humanoids.
- **disclosed subsystems:** `end-effector-anthropomorphic-hand`, `actuator-electric`, `sensing-tactile-distributed`

**Prior art notes:**

> Inspire-Robots RH56 (Beijing 2018+) is the widely-deployed Chinese 5-finger 6-DoF anthropomorphic hand used by Unitree, Fourier, and many other Chinese commercial humanoids. 7-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from 5-finger 6-DoF Chinese commercial dexterous hands. Together with Linkerbot Linker Hand (round-44), establishes the Chinese hand-supplier prior-art chain.

**Sources:**

1. en.inspire-robots.com/wp-content/uploads/2024/02/INSPIRE-ROBOTS-THE-DEXTEROUS-HAND-RH56-SERIES-USER-MANUAL.pdf

---

### 2018-04 — NAVER LABS AMBIDEX

- **id:** `naver-labs-ambidex-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** NAVER LABS Corp. (Seongnam, South Korea)
- **disclosure citation:** NAVER LABS Corp. (Seongnam, South Korea; AI research arm of Naver Corporation). AMBIDEX humanoid arm reveal April 2018 at ICRA 2018 demo + naverlabs.com. Subsequent academic publications: 'Cable-driven anthropomorphic robot arm' related papers from the Korea Institute of Science and Technology / KAIST collaborations.
- **disclosed subsystems:** `mechanism-anthropomorphic-arm`, `mechanism-tendon-driven`, `mechanism-cable-driven-transmission`, `actuator-electric`

**Prior art notes:**

> NAVER LABS AMBIDEX is the canonical Korean academic-commercial cable-driven anthropomorphic arm (NAVER LABS, 2018+). 7-year-deep public-disclosure prior art for: dual-wire-driven 7-DoF manipulator with proximal motor concentration, low-distal-inertia commercial collaborative robot arm. Distinct architectural branch from harmonic-drive arms (Honda P-series, DLR Hand-Arm) and quasi-direct-drive arms (Berkeley Humanoid, ToddlerBot). Direct shielding for any commercial humanoid claim on cable-driven transmission for arms. Particularly relevant for free-humanoid-platform's wrist + hand subsystem (which is tendon-driven) — AMBIDEX establishes that whole-arm tendon transmission is well-anticipated commercial Korean practice.

**Sources:**

1. NAVER LABS corporate site (naverlabs.com).
2. ICRA 2018 demonstration coverage.
3. AMBIDEX product page (Naver internal).

---

### 2018-04 — Robotis OpenManipulator

- **id:** `robotis-openmanipulator-2018`
- **corpus:** private
- **ip status:** open-permissive
- **creator:** Robotis Co., Ltd. (Seoul, South Korea)
- **disclosure citation:** Robotis Co., Ltd. (Seoul, South Korea). OpenMANIPULATOR-X commercial reveal April 2018 via robotis.com. Open-hardware design; CAD files + control firmware open-source under MIT license.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `actuator-electric`

**Prior art notes:**

> Robotis OpenMANIPULATOR (Robotis 2018+) is the canonical Korean open-hardware educational manipulator. 7-year-deep open-permissive prior art. The educational-manipulator counterpart to TurtleBot (round-35) and DARwIn-OP (corpus round-19 robotis-op3-2017 entry). Together with TurtleBot, establishes the Korean open-educational-robotics ecosystem.

**Sources:**

1. Robotis OpenMANIPULATOR product page (robotis.com).
2. GitHub: github.com/ROBOTIS-GIT/open_manipulator.

---

### 2018-09 — Sarcos Guardian XO

- **id:** `sarcos-guardian-xo-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Sarcos Robotics / Stephen Jacobsen (University of Utah Center for Engineering Design)
- **disclosure citation:** Sarcos Robotics / Sarcos Technology and Robotics Corporation (Salt Lake City, UT; founded 1983 by Stephen Jacobsen, University of Utah). Guardian XO commercial reveal 2018; subsequent deployments through 2023. Sarcos was a long-running DARPA exoskeleton recipient (XOS, XOS-2 hydraulic precursors). Acquired by Boeing 2024 + multiple subsequent restructurings.
- **disclosed subsystems:** `mechanism-exoskeleton`, `mechanism-full-body-exoskeleton`, `actuator-electric`, `control-sensitivity-amplification`

**Prior art notes:**

> Sarcos Guardian XO is the canonical 2018+ all-electric full-body industrial exoskeleton. 7-year-deep public-disclosure prior art for: 24-DoF whole-body industrial exoskeleton, all-electric (vs. hydraulic) heavy-lift exoskeleton. Architecturally extends Berkeley BLEEX (round-19) from lower-extremity-only to whole-body. Direct shielding for any commercial humanoid claim on full-body load-handling robotics — particularly for industrial-deployment commercial humanoid claims (Apptronik Apollo, Figure, Optimus all market industrial heavy-lift) which face 7-year-deep Sarcos commercial prior art.

**Sources:**

1. Sarcos corporate site (sarcos.com — historical, archived).
2. Boeing acquisition announcement 2024.
3. Wikipedia 'Sarcos' (en.wikipedia.org/wiki/Sarcos).

---

### 2018-09 — Wandercraft Atalante / Atalante X self-balancing exoskeleton

- **id:** `wandercraft-atalante-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Wandercraft S.A.S. (Paris, France); Masselin + Simon + Boulanger + Lance; Aaron Ames-school dynamic-locomotion control
- **disclosure citation:** Wandercraft S.A.S. (Paris, France; founded 2012 by Matthieu Masselin, Nicolas Simon, Alexandre Boulanger, Jérémie Lance). Atalante clinical reveal 2018. Atalante X 2022. FDA clearance 2024. Built on Aaron Ames-school dynamic-locomotion / capture-point / Hybrid Zero Dynamics formal control.
- **disclosed subsystems:** `exoskeleton-lower-limb`, `control-bipedal-locomotion`, `control-hybrid-zero-dynamics`, `control-capture-point`, `actuator-electric`

**Prior art notes:**

> Wandercraft Atalante / Atalante X (Wandercraft Paris 2018+; FDA-cleared 2024) is the world's first self-balancing dynamic-walking exoskeleton — the most architecturally important entry in the human-augmented-robotics chain. 7-year-deep public-disclosure prior art. **Direct shielding for any commercial humanoid or fictional Iron Man-class claim deriving from self-balancing powered armor / autonomous-walking wearable robotics.** The Wandercraft formal-dynamic-locomotion control architecture (Hybrid Zero Dynamics + capture-point) is the Ames-school lineage that anchors all 'powered armor that walks by itself' claims.

**Sources:**

1. en.wandercraft.eu/

---

### 2018-12 — DSV Limiting Factor (Triton 36000/2 full-ocean-depth HOV)

- **id:** `dsv-limiting-factor-vescovo-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Triton Submarines (Sebastian, FL, USA) for Caladan Oceanic / Victor Vescovo
- **disclosure citation:** Triton Submarines (Sebastian, FL, USA) for Caladan Oceanic / Victor Vescovo. Limiting Factor first dive December 19 2018; Challenger Deep April 28 2019. First commercial repeatable full-ocean-depth HOV (Triton 36000/2 design certified by DNV-GL).
- **disclosed subsystems:** `hov`, `actuator-electric`

**Prior art notes:**

> DSV Limiting Factor (Triton Submarines + Caladan Oceanic / Vescovo 2018+) is the first commercial repeatable full-ocean-depth HOV. 7-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from commercially-certified full-ocean-depth crewed vehicles.

**Sources:**

1. en.wikipedia.org/wiki/DSV_Limiting_Factor

---

### 2018-12 — OceanGate Titan (carbon-fiber experimental HOV; 2023 loss)

- **id:** `oceangate-titan-2018-2023`
- **corpus:** private
- **ip status:** trade-secret (OceanGate dissolved 2023)
- **creator:** OceanGate Inc. (Everett, WA, USA); Stockton Rush founder
- **disclosure citation:** OceanGate Inc. / Stockton Rush (Everett, WA, USA). Titan uncrewed test June 2018; first crewed 4,000 m dive December 10, 2018. Imploded near RMS Titanic wreck on June 18, 2023, killing all 5 aboard. Tragic but pivotal prior-art event for carbon-fiber-hull experimental HOV / full-ocean-depth tourism.
- **disclosed subsystems:** `hov`, `exoskeleton-fictional`, `actuator-electric`

**Prior art notes:**

> OceanGate Titan (Everett WA 2018-2023) is the carbon-fiber experimental HOV that tragically imploded June 2023 near the RMS Titanic wreck. 7-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from carbon-fiber composite pressure hulls — the canonical 'what not to do' for deep-pressure-cycling design.

**Sources:**

1. en.wikipedia.org/wiki/Titan_(submersible)

---

### 2019-02 — Pliant Energy Velox / C-Ray (multi-gait undulating-fin amphibious robot)

- **id:** `pliant-energy-velox-cray-2019`
- **corpus:** private
- **ip status:** trade-secret (commercial; with patents on hyperbolic-fin mechanism)
- **creator:** Pliant Energy Systems LLC (Brooklyn, NY, USA); Benjamin Filardo founder; ONR-funded; MIT Marine Autonomy Lab autonomy collaboration
- **disclosure citation:** Pliant Energy Systems LLC (Brooklyn, NY, USA; founded 2007 by Benjamin Filardo). Velox amphibious-robot public reveal February 2019 via Dezeen feature. C-Ray autonomous-variant developed with MIT Marine Autonomy Lab (Office of Naval Research funding under Dr. Tom McKenna). Both share the patented hyperbolic-geometry undulating-fin mechanism.
- **disclosed subsystems:** `auv-amphibious`, `mechanism-undulating-fin`, `mechanism-multi-gait-single-actuator`, `actuator-electric`, `control-autonomy-stack`

**Prior art notes:**

> Pliant Energy Velox + C-Ray (Pliant Energy Systems Brooklyn NY 2019+; ONR + MIT Marine Autonomy Lab) is the canonical multi-gait single-actuator amphibious robot. 6-year-deep public-disclosure prior art. **The architectural counter-thesis to multi-machine single-function design** — one hyperbolic-geometry undulating-fin pair drives the same mechanism through four animal gaits (ray-swim / millipede-crawl / squid-jet / snake-slide) across four environments (water / land / ice / snow / sand) without any mechanical reconfiguration. Direct shielding for any commercial humanoid or amphibious-robot claim deriving from: (1) hyperbolic-geometry undulating fins; (2) multi-gait single-mechanism amphibious propulsion; (3) biomimetic ray + cuttlefish + snake + millipede gait synthesis in a single platform; (4) ONR-funded amphibious-AUV beach-survey applications. Sister to corpus AUV/HOV entries (alvin-hov-1964, jason-rov-1989, nereus-hrov-2008, bluefin-21-auv, aquanaut-houston-2017, oceanone-stanford-2016, ocean-onek-stanford-2022) — distinct from all of them via the multi-gait single-actuator architecture vs. their propeller / ducted-thruster propulsion.

**Sources:**

1. pliantenergy.com/robotics
2. pliantenergy.com/new-page-2 (About).
3. oceanai.mit.edu/autonomylab/pmwiki/pmwiki.php?n=Robot.CRay (MIT Marine Autonomy Lab C-Ray page).
4. dezeen.com/2019/02/07/amphibious-velox-robot-technology/ (Velox feature Feb 2019).
5. interestingengineering.com/innovation/cuttlefish-like-robots-are-far-more-efficient-than-propeller-powered-machines

---

### 2019-04 — Stanford Pupper / Doggo open-source quadruped

- **id:** `stanford-pupper-doggo-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Student Robotics; Nathan Kau, Aaron Schultz et al.
- **disclosure citation:** Stanford Student Robotics. Stanford Doggo open-source quadruped reveal April 2019. Subsequent: Stanford Pupper (smaller variant). stanfordstudentrobotics.org / hands-on-robotics.stanford.edu. Open-hardware design under MIT license.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric`, `mechanism-3d-printed-platform`

**Prior art notes:**

> Stanford Pupper / Doggo (Stanford Student Robotics 2019+) is the canonical Stanford educational open-source quadruped. 6-year-deep open-permissive prior art. The Stanford academic counterpart to Unitree Go1/Go2 (corpus) for educational quadruped robotics. Direct shielding for any commercial quadruped claim deriving from low-cost open-hardware educational platforms.

**Sources:**

1. Stanford Student Robotics (stanfordstudentrobotics.org).
2. Hands-on-Robotics Stanford (hands-on-robotics.stanford.edu).
3. GitHub: github.com/Nate711/StanfordDoggoProject.

---

### 2019-04 — QYSEA FIFISH V6 (omnidirectional consumer ROV pioneer)

- **id:** `qysea-fifish-v6-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** QYSEA Technology Co., Ltd. (Shenzhen, China); Belinda Zhang founder
- **disclosure citation:** QYSEA Technology Co., Ltd. / Belinda Zhang (Shenzhen, China). FIFISH V6 mass production April 2019 (debut CES 2016). First omnidirectional consumer underwater drone. Chinese consumer ROV pioneer.
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-omnidirectional`

**Prior art notes:**

> QYSEA FIFISH V6 (Shenzhen 2019+) is the first omnidirectional consumer underwater drone. 6-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or ROV claim deriving from omnidirectional consumer underwater drones or VR-headset-teleoperated ROVs.

**Sources:**

1. qysea.com/about-us/company-profile/

---

### 2019-09 — FANUC CRX collaborative robot family

- **id:** `fanuc-crx-collaborative-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** FANUC Corporation (Yamanashi, Japan)
- **disclosure citation:** FANUC Corporation. CRX collaborative robot family commercial reveal September 2019. CRX-10iA (10 kg payload) initial product; subsequent CRX-25iA (25 kg payload) + CRX-5iA (5 kg payload). fanuc.com. The cobot variant of FANUC's industrial-arm family (corpus round-34 fanuc-industrial-robotics-1956).
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-collaborative-robot`, `actuator-electric`, `sensing-joint-torque`

**Prior art notes:**

> FANUC CRX (FANUC Yamanashi 2019+) is FANUC's cobot variant of the industrial-arm family (round-34 fanuc-industrial-robotics-1956). 6-year-deep public-disclosure prior art. The Japanese cobot answer to Universal Robots (Denmark) + Doosan (Korea) + Franka Emika (Germany). Together, the global cobot prior-art chain spans 4 distinct national-origin commercial cobot product lines.

**Sources:**

1. FANUC CRX product page (fanuc.com).

---

### 2019-09 — Open Source Leg (Rouse Michigan)

- **id:** `open-source-leg-rouse-2019`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** University of Michigan + Shirley Ryan AbilityLab; Elliott Rouse
- **disclosure citation:** Elliott Rouse (University of Michigan + Shirley Ryan AbilityLab). Open Source Leg announced 2018; public release 2019. CC-BY / MIT licensed open-hardware powered knee+ankle prosthesis platform. Deployed at 15+ institutions worldwide.
- **disclosed subsystems:** `end-effector-prosthetic`, `exoskeleton-lower-limb`, `actuator-electric`, `actuator-quasi-direct-drive`

**Prior art notes:**

> Open Source Leg (Rouse Michigan + Shirley Ryan AbilityLab 2019+) is the canonical open-hardware powered knee+ankle prosthesis platform. 6-year-deep open-permissive prior art (CC-BY / MIT). Direct shielding for any commercial humanoid claim deriving from open-source powered prosthesis platforms or quasi-direct-drive brushless-DC + ball-screw lower-limb actuators.

**Sources:**

1. neurobionics.robotics.umich.edu/research/wearable-robotics/open-source-leg/

---

### 2019-09 — CMR Surgical Versius modular soft-tissue surgical robot

- **id:** `cmr-versius-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** CMR Surgical Ltd. (Cambridge, UK)
- **disclosure citation:** Cambridge Medical Robotics Surgical Ltd. (Cambridge, UK; founded 2014). Versius commercial reveal September 2019. CE-mark 2019. FDA Versius Plus 510(k) clearance 2025. Modular small-footprint per-arm soft-tissue surgical robot.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-modular`, `actuator-electric`

**Prior art notes:**

> CMR Surgical Versius (Cambridge UK 2019+) is the canonical modular small-footprint soft-tissue surgical robot. 6-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from modular per-arm surgical robotics.

**Sources:**

1. en.wikipedia.org/wiki/CMR_Surgical

---

### 2020-07 — Hello Robot Stretch

- **id:** `hello-robot-stretch-2020`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Hello Robot, Inc.; Charles Kemp + Aaron Edsinger
- **disclosure citation:** Hello Robot, Inc. 'Stretch: A Versatile Mobile Manipulator'. Public reveal July 2020 via hello-robot.com. Founded by Charles Kemp (Georgia Tech Healthcare Robotics Lab spinout) and Aaron Edsinger. Subsequent product generations: Stretch RE1 (2020), RE2 (2021), Stretch 3 (2024). Used as the deployment platform in LEGS (round-15 entry legs-berkeley-2024) and many other academic mobile-manipulation projects.
- **disclosed subsystems:** `mechanism-mobile-base`, `mechanism-manipulator-arm`, `mechanism-telescoping-mast`, `actuator-electric`

**Prior art notes:**

> Hello Robot Stretch is the canonical sub-\$25k educational mobile manipulator (2020). 5-year-deep public-disclosure prior art with 100+ academic publications using Stretch as the deployment platform. Direct shielding for any commercial mobile-manipulator claim at the educational price point or with the telescoping-mast architectural pattern. Notably **the Berkeley LEGS round-15 entry deployed on Stretch** — the round-15 entry's prior_art_notes implicitly reference Stretch as the platform; round-17 now resolves that reference. Architecturally distinct from humanoid-form mobile manipulators (Apptronik, Figure, Optimus): Stretch is single-arm + mast + wheels, not bipedal + bimanual.

**Sources:**

1. Hello Robot corporate site (hello-robot.com).
2. Kemp, C., Edsinger, A. et al. 'Stretch: A Versatile Mobile Manipulator' company technical reports 2020+.
3. Wikipedia 'Hello Robot' (en.wikipedia.org/wiki/Hello_Robot).

---

### 2020-11 — Fendouzhe / Striver (China full-ocean-depth HOV)

- **id:** `fendouzhe-china-2020`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** CSSRC + Institute of Deep-sea Science and Engineering (China)
- **disclosure citation:** China Ship Scientific Research Center (CSSRC) + Institute of Deep-sea Science and Engineering (CAS) (China). Fendouzhe 10,909 m dive November 2020 in Mariana Trench. China's full-ocean-depth HOV; second nation-state (after USA via DSV Limiting Factor round-47) to repeatedly reach Challenger Deep.
- **disclosed subsystems:** `hov`, `actuator-electric`

**Prior art notes:**

> Fendouzhe / Striver (CSSRC + CAS IDSSE China 2020+) is China's full-ocean-depth HOV. 5-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or deep-submergence claim deriving from Chinese full-ocean-depth HOVs. Lineage descends from Jiaolong (round-47).

**Sources:**

1. english.cas.cn/Special_Reports/Highlights_of_2020_Top_12_Achievements_in_CAS/Submersible_Fendouzhe_Completing_10000_meter_Deep_diving_Trial/

---

### 2021-07 — UBTech Walker X

- **id:** `ubtech-walker-x-2021`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** UBTech Robotics (Shenzhen, China)
- **disclosure citation:** UBTech Robotics (Shenzhen, China). Walker X humanoid reveal July 2021. Successor variant to original Walker (corpus entry ubtech-walker). ubtrobot.com. UBTech IPO Hong Kong 2023.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `actuator-electric`

**Prior art notes:**

> UBTech Walker X (UBTech Shenzhen 2021+) is UBTech's adult-class successor humanoid. 4-year-deep public-disclosure prior art. Brings UBTech entries to 2 (with original ubtech-walker) tracking the multi-generation Chinese commercial humanoid lineage.

**Sources:**

1. UBTech corporate site (ubtrobot.com).
2. UBTech July 2021 Walker X announcement.

---

### 2021-09 — Medtronic Hugo RAS modular surgical platform

- **id:** `medtronic-hugo-ras-2021`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Medtronic plc (Dublin, Ireland; HQ Galway / Minneapolis)
- **disclosure citation:** Medtronic plc (Dublin, Ireland; HQ Galway / Minneapolis). Hugo RAS (Robotic-Assisted Surgery) commercial reveal September 2021. CE-mark 2021. FDA urology 510(k) clearance December 2025. Modular multi-arm soft-tissue surgical platform — Medtronic's answer to da Vinci.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-modular`, `actuator-electric`

**Prior art notes:**

> Medtronic Hugo RAS (Medtronic Dublin 2021+) is Medtronic's modular multi-arm soft-tissue surgical platform — the answer to da Vinci. 4-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from modular multi-arm surgical robotics.

**Sources:**

1. medtronic.com/en-us/healthcare-professionals/specialties/surgical-robotics/hugo-robotic-assisted-surgery.html

---

### 2022-01 — Boston Dynamics Stretch (warehouse robot)

- **id:** `boston-dynamics-stretch-warehouse-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics (Hyundai subsidiary)
- **disclosure citation:** Boston Dynamics. Stretch warehouse robot commercial reveal January 2022 via boston-dynamics.com. Distinct from Hello Robot Stretch (corpus entry hello-robot-stretch-2020). DHL Supply Chain partnership announced 2022 for case-handling deployment.
- **disclosed subsystems:** `mechanism-mobile-base`, `mechanism-manipulator-arm`, `mechanism-telescoping-mast`, `actuator-electric`

**Prior art notes:**

> Boston Dynamics Stretch (BD warehouse robot, 2022+) is a canonical industrial warehouse case-handling robot. 3-year-deep public-disclosure prior art. **Distinct from Hello Robot Stretch (round-17 entry hello-robot-stretch-2020)** — BD Stretch is industrial warehouse-deployment focused, Hello Robot Stretch is educational mobile-manipulator focused. Both use telescoping form factors. Direct shielding for any commercial humanoid claim on warehouse case-handling derivative applications.

**Sources:**

1. Boston Dynamics Stretch product page (bostondynamics.com/products/stretch).
2. DHL Supply Chain announcement 2022.

---

### 2022-02 — Anduril Dive-LD (affordable LDUUV)

- **id:** `anduril-dive-ld-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Anduril Industries (Costa Mesa, CA, USA); Dive Technologies acquisition Feb 2022
- **disclosure citation:** Anduril Industries (Costa Mesa, CA, USA). Acquired Dive Technologies February 2022. Dive-LD large-displacement UUV with affordability thesis (tenth-the-cost-of-competitors). Subsequent Dive-XL Ghost Shark for Royal Australian Navy (prototype delivered April 2024 under AUKUS Pillar 2).
- **disclosed subsystems:** `auv`, `auv-lduuv`, `actuator-electric`

**Prior art notes:**

> Anduril Dive-LD + Ghost Shark (Anduril 2022+; AUKUS Pillar 2 2024) are the affordable LDUUV market disruptor. 3-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or AUV claim deriving from affordable modular Anduril-class LDUUVs.

**Sources:**

1. defensenews.com/industry/2022/02/02/autonomy-specialist-anduril-buys-underwater-drone-maker-dive-technologies/

---

### 2022-08 — Xiaomi CyberOne

- **id:** `xiaomi-cyberone-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Xiaomi Corporation (Beijing, China)
- **disclosure citation:** Xiaomi Corporation. CyberOne humanoid reveal August 11 2022 at Xiaomi annual product launch event, Beijing. mi.com. The first major consumer-electronics-company humanoid commercial platform from China.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `actuator-electric`

**Prior art notes:**

> Xiaomi CyberOne (Xiaomi Beijing August 2022) is the first major Chinese consumer-electronics-company humanoid. 3-year-deep public-disclosure prior art. The architectural predecessor of the Chinese commercial humanoid wave 2023-2026. Brings Chinese commercial humanoid corpus entries to 14+ specific platforms.

**Sources:**

1. Xiaomi annual product launch announcement August 11 2022.
2. Wikipedia 'Xiaomi CyberOne'.

---

### 2023-01 — Linkerbot Linker Hand (Beijing)

- **id:** `linkerbot-linker-hand-beijing-2023`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Linkerbot Co., Ltd. (Beijing, China); Alex Zhou Yong (周永) founder
- **disclosure citation:** Linkerbot Co., Ltd. (Beijing, China). Founded 2023 by Alex Zhou Yong (周永). Linker Hand product family ranges 6-42 DoF across all three mainstream dexterous-hand actuation technologies (linkage transmission, tendon drive, direct drive). Series B+ closed early May 2026 at USD 3B valuation; next round targeting USD 6B (May 2026). Early backers: Ant Group, HongShan Group. Latest investors: Zhongguancun Science Park Fund, Bank of China Asset Management, Fosun Capital.
- **disclosed subsystems:** `end-effector-anthropomorphic-hand`, `mechanism-tendon-drive`, `mechanism-linkage-drive`, `mechanism-direct-drive`, `actuator-electric`

**Prior art notes:**

> Linkerbot Linker Hand (Beijing 2023+) is the global volume-leader in high-DoF dexterous hands per Reuters (>80% market share by volume). 2-3-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from high-DoF anthropomorphic hand product families spanning linkage / tendon / direct-drive actuation, or from dedicated-hand supplier business models. The Chinese hand-specialist complement to corpus humanoid-platform entries (Unitree, Fourier, AgiBot, Astribot, Galbot, etc.). Lineage descends from foundational anthropomorphic-hand prior art: Belgrade-USC Hand (round-42 belgrade-usc-tomovic-bekey-hand-1963), Shadow Dexterous Hand (corpus shadow-dexterous-hand), Allegro Hand (corpus allegro-hand-wonik-simlab-2014), DLR Hand II (corpus dlr-hand-ii).

**Sources:**

1. linkerbot.cn/index (corporate site).
2. thenextweb.com/news/linkerbot-china-robot-hand-6-billion-valuation
3. scmp.com/tech/tech-trends/article/3344242 (South China Morning Post).
4. interestingengineering.com/ai-robotics/china-linkerbot-robotic-hands-human-skills
5. Reuters market-share reporting (cited in TNW and SCMP).

---

### 2024-04 — Astribot S1

- **id:** `astribot-s1-stardust-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Stardust Intelligence (Shenzhen, China)
- **disclosure citation:** Stardust Intelligence (Shenzhen, China; founded December 2022). Astribot S1 reveal April 2024 via stardust-tech.com / astribot.com demo videos showing 10 m/s arm motion. Stardust Intelligence Astribot Suite paper July 2025 (peer-reviewed; teleop + DuoCore-WB imitation learning achieving 80% task success). Commercial availability late 2025+ in China.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `actuator-electric`, `control-imitation-learning`, `control-foundation-model-policy`

**Prior art notes:**

> Astribot S1 is one of the canonical 2024-2025 Chinese commercial humanoid platforms (Stardust Intelligence). 1.5-year-deep public-disclosure prior art for: ≥10 m/s anthropomorphic arm motion (claimed industry-leading), 36-DoF whole-body humanoid, DuoCore-WB whole-body IL framework. Direct shielding for any commercial humanoid claim on extreme arm-speed performance — Astribot's April 2024 viral demo set the public benchmark. Claim surface is peer-reviewed (Astribot Suite paper July 2025), unlike most Chinese commercial humanoid platforms.

**Sources:**

1. Stardust Intelligence corporate site (stardust-tech.com / astribot.com).
2. Astribot Suite paper July 2025 (peer-reviewed; venue TBV).
3. Humanoid Press product database (humanoid.press/database/database-astribot-s1).
4. Origin of Bots, RobotsLATAM, Mike Kalil coverage 2024-2026.

---

### 2024-04 — Atlas Electric (Boston Dynamics)

- **id:** `boston-dynamics-atlas-electric-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics (Hyundai subsidiary since 2021)
- **disclosure citation:** Boston Dynamics. 'An Electric New Era for Atlas' announcement April 17 2024 via boston-dynamics.com (replacing the hydraulic Atlas, which retired April 16 2024). Subsequent capability demonstrations 2024-2025 including Hyundai factory deployment preparation. Trade-secret commercial humanoid platform.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-super-human-range-of-motion`, `actuator-electric`, `actuator-electric-harmonic-drive`

**Prior art notes:**

> Atlas Electric is Boston Dynamics' canonical 2024+ commercial all-electric humanoid (succeeding the 11-year hydraulic Atlas lineage). 1.5-year-deep public-disclosure prior art for: super-human range-of-motion humanoid joint design, all-electric humanoid form factor at compact mass. Public capability surface (viral demo videos) is fully covered by deeper academic prior art chains: HRP-2/HRP-4/HRP-5P (full-size humanoid lineage); Berkeley Humanoid + ToddlerBot (round-11, all-electric humanoid); the Hwangbo ANYmal sim-to-real lineage for the RL training substrate. **Specific super-human-ROM joint kinematics** are the architectural distinction; corpus has Salisbury / DLR / Pisa-IIT joint mechanism prior art back to 1982 for kinematic ranges that exceed standard anthropomorphic humanoids.

**Sources:**

1. Boston Dynamics 'An Electric New Era for Atlas' April 17 2024 (bostondynamics.com/atlas/an-electric-new-era-for-atlas).
2. Boston Dynamics YouTube channel (Atlas Electric demonstration videos 2024-2025).
3. Hyundai partnership announcements.

---

### 2024-04 — Sanctuary AI Phoenix Carbon (Gen 7) *(draft)*

- **id:** `sanctuary-phoenix-carbon-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Sanctuary AI (Vancouver, Canada)
- **disclosure citation:** Sanctuary AI (Vancouver, Canada). Phoenix Generation 7 reveal April 2024 via sanctuary.ai. Successor to Phoenix Gen 6 (corpus entry sanctuary-phoenix-gen6) + original Phoenix (corpus entry sanctuary-phoenix). Carbon-fiber chassis variant.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `actuator-electric`

**Prior art notes:**

> Sanctuary AI Phoenix Carbon / Gen 7 is the latest in the Sanctuary humanoid lineage (Vancouver, 2024+). 1.5-year-deep public-disclosure prior art. Successor to Phoenix Gen 6 (corpus). Brings Sanctuary Phoenix family to 3 corpus entries spanning the lineage.

**Sources:**

1. Sanctuary AI corporate site (sanctuary.ai).

---

### 2024-08 — AgiBot X1 *(draft)*

- **id:** `agibot-x1-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** AgiBot (Shanghai, China; Zhihui Jun co-founder)
- **disclosure citation:** AgiBot (Shanghai-based; founded 2023 by Zhihui Jun + colleagues). X1 humanoid product reveal August 2024 via agibot.com. Successor variant beyond A1 + A2 (corpus entries) in the AgiBot product evolution.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `actuator-electric`

**Prior art notes:**

> AgiBot X1 (AgiBot Shanghai 2024+) is AgiBot's adult-class successor humanoid. ~1-year-deep public-disclosure prior art. Brings AgiBot corpus entries to 2 (with agibot-a1) tracking the multi-generation product evolution. Together with Xiaomi CyberOne (round-39) + UBTech Walker X (round-39) + Unitree H1/G1/R1 + Astribot S1 + Galbot + Galaxea G1 + Booster K1/T1 + EngineAI PM01/SE01 + Kepler K2 + LimX CL-1, brings Chinese commercial humanoid corpus representation to 17+ specific platform entries.

**Sources:**

1. AgiBot corporate site (agibot.com).

---

### 2024-09 — Galbot *(draft)*

- **id:** `galbot-galaxy-robotics-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Galaxy Robotics (Beijing, China)
- **disclosure citation:** Galaxy Robotics (Beijing, China). Galbot platform reveal 2024 via galaxy-robotics.com / WAIC 2024 demonstration. Wheeled humanoid with telescoping torso lift + dual 7-DoF arms. ~CNY 500k initial commercial price.
- **disclosed subsystems:** `mechanism-mobile-base`, `mechanism-anthropomorphic-arm`, `mechanism-telescoping-mast`, `actuator-electric`

**Prior art notes:**

> Galbot is the canonical 2024 Chinese wheeled-humanoid commercial platform (Galaxy Robotics). 1.5-year-deep public-disclosure prior art for: telescoping-torso wheeled humanoid commercial deployment, dual-arm wheeled mobile manipulator at the educational-to-commercial price tier. Architectural sibling of Hello Robot Stretch (round-17 entry) but with humanoid-form dual-arm + telescoping-torso vs. Stretch's single-arm + mast. Direct shielding for any commercial humanoid claim on wheeled-humanoid (non-bipedal) form factor with telescoping vertical adjustment. **Directly relevant to free-humanoid-wheeled** — Galbot is the closest commercial product to that morphology.

**Sources:**

1. Galaxy Robotics corporate site (galaxy-robotics.com).
2. WAIC 2024 demonstration coverage.
3. Humanoid Press product database.

---

### 2024-09 — Galaxea G1 *(draft)*

- **id:** `galaxea-g1-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Galaxea AI (Beijing, China)
- **disclosure citation:** Galaxea AI (Beijing, China). G1 commercial humanoid product reveal September 2024 via galaxea.ai. Wheel-based mobile humanoid; ~165 cm tall.
- **disclosed subsystems:** `mechanism-mobile-base`, `mechanism-anthropomorphic-arm`, `actuator-electric`

**Prior art notes:**

> Galaxea G1 (Galaxea AI Beijing 2024+) is one of the canonical Chinese wheeled-humanoid commercial platforms. ~1.5-year-deep public-disclosure prior art. Together with Galbot (round-22) and Promobot (round-22), establishes the wheeled-humanoid commercial-deployment landscape.

**Sources:**

1. Galaxea AI corporate site (galaxea.ai).

---

### 2025-03 — Booster K1

- **id:** `booster-k1-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Booster Robotics (Beijing, China)
- **disclosure citation:** Booster Robotics. K1 product page (booster.tech/booster-k1) and associated commercial brochures, public 2025+. RoboCup 2025 KidSize humanoid league winning platform (Boosted HTWK team, Salvador Brazil, July 20 2025).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric`, `control-rl-policy`

**Prior art notes:**

> Booster K1 is the canonical 2025 sub-$25k educational humanoid. 5-month-deep public-disclosure prior art for: KidSize-class (95cm) humanoid form factor, 22-DoF anthropomorphic kinematics, ROS 2 + Python developer-friendly stack at the educational price point. Public competition record (RoboCup 2025 KidSize win) demonstrates a working system. Direct shielding for any commercial humanoid claim on educational/sub-$25k pricing or RoboCup-competition-grade autonomous bipedal locomotion.

**Sources:**

1. Booster Robotics product page (booster.tech/booster-k1).
2. Generation Robots product listing (generationrobots.com).
3. Humanoid Guide product database entry (humanoid.guide/product/k1).
4. RoboCup 2025 results (Salvador, Brazil, July 2025).

---

### 2025-07 — Unitree R1

- **id:** `unitree-r1-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Unitree Robotics (Hangzhou, China; founded 2016 by Wang Xingxing)
- **disclosure citation:** Unitree Robotics (Hangzhou, China). R1 product reveal July 2025; global launch April 2026 via shop.unitree.com / AliExpress. unitree.com/R1. Multi-tier product line: R1 Air \$4.9k, R1 Basic \$5.9k-\$8.99k, R1 EDU Standard \$10-12k, R1 EDU Smart \$15-19k, R1 EDU Pro \$20-35k.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric`, `control-rl-policy`, `control-vla-vision-language-action`

**Prior art notes:**

> Unitree R1 is the canonical 2025+ low-cost consumer humanoid (Unitree Robotics, China). ~10-month-deep public-disclosure prior art at time of corpus entry. **Significantly disrupts the humanoid pricing claim space** — drops the entry price from Boston Dynamics Atlas (>\$1M) / Figure 02 (\$15k+) / Optimus Gen 3 (\$20-30k target) to \$4,900. Establishes 9 km/h running + cartwheels as commercially-deployed-not-academic capabilities. Direct shielding for any commercial humanoid claim on consumer-tier pricing or low-cost humanoid morphology.

**Sources:**

1. Unitree Robotics R1 page (unitree.com/R1).
2. Unitree shop (shop.unitree.com/products/unitree-r1).
3. Gizmochina, CnTechPost, Robohorizon coverage 2025-2026.
4. Association for Advancing Automation 'Industry Insights' coverage.

---

### 2025-09 — Booster T1 *(draft)*

- **id:** `booster-t1-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Booster Robotics (Beijing, China)
- **disclosure citation:** Booster Robotics. T1 product reveal Q3 2025 via booster.tech. Successor to K1 (round-16 entry booster-k1-2025) with adult-class form factor.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric`, `control-rl-policy`

**Prior art notes:**

> Booster T1 is Booster Robotics' adult-class commercial humanoid (2025+). 8-month-deep public-disclosure prior art at the time of this corpus entry. Inherits from K1 (round-16) the ROS 2 + Python developer-friendly stack pattern. Direct shielding for Booster's commercial product line as a coherent multi-platform humanoid family (KidSize K1 + AdultSize T1).

**Sources:**

1. Booster Robotics corporate site (booster.tech).

---

### 2025-09 — EngineAI SE01 *(draft)*

- **id:** `engineai-se01-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** EngineAI Robotics (Shenzhen, China)
- **disclosure citation:** EngineAI Robotics (Shenzhen, China). SE01 product reveal Q3 2025 via engineai.com. Successor to PM01 (corpus entry `engineai-pm01`). Adult-class commercial humanoid at the sub-\$30k tier.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric`, `control-rl-policy`

**Prior art notes:**

> EngineAI SE01 is EngineAI's adult-class commercial humanoid (2025+). Successor in the EngineAI product line after PM01 (round-9 entry `engineai-pm01`). Direct shielding for any commercial claim on the EngineAI multi-platform humanoid family. Together with Unitree R1, Astribot S1, Booster T1, Galbot, establishes the 2024-2026 Chinese commercial humanoid landscape.

**Sources:**

1. EngineAI corporate site (engineai.com).

---

### 2025-10 — Tesla Optimus Gen 3 *(draft)*

- **id:** `tesla-optimus-gen3-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Tesla, Inc.
- **disclosure citation:** Tesla, Inc. Optimus Gen 3 product disclosures via Tesla AI Day-class demonstrations + product page (tesla.com/we-robot) + Optimus blog/social-media posts October 2025+. Trade-secret commercial humanoid platform.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-driven`, `actuator-electric`, `control-vision-only-perception`, `control-foundation-model-policy`, `sensing-fingertip-tactile`

**Prior art notes:**

> Tesla Optimus Gen 3 is the dominant commercial humanoid product claim surface. Public-disclosure surface (Tesla product page + demos + social-media + investor decks) discloses dimensional specs and high-level architecture; withholds actuator architecture, specific neural-network policies, training-data composition, and on-device inference details. **The 22-DoF hand × 50-actuator claim is the most specific architectural claim** and directly engages prior-art chains in the corpus: Shadow Hand (24-DoF), DLR Hand-II (15-DoF), Pisa-IIT SoftHand (synergy reduction), Tactile SoftHand-A (antagonistic tendons + tactile fingertips, round-11 entry — directly anticipates the tactile-fingertip delicate-manipulation claim), Educational SoftHand-A (round-12 entry — clutch-gear synergy mechanism). Modern claims on tactile-fingertip dexterous manipulation face 2-year-deep tactile-softhand-a prior art and the deeper SoftHand chain back to 2014. Vision-only sensing is shielded by Tesla's own FSD patents (which Tesla cannot use offensively against an own-lineage humanoid claim) but separately by Levine's GPS PR2/BRETT (2016) for vision-driven manipulation. The full Optimus Gen 3 claim surface is therefore element-by-element anticipated by deep open academic chains plus prior commercial humanoids in the corpus.

**Sources:**

1. Tesla Optimus product page (tesla.com/we-robot).
2. Humanoid Press 'Optimus 3' database entry (humanoid.press/database/humanoid-press-database-tesla-optimus-3/).
3. Basenor explainer 'Tesla Optimus Gen 3 Hands: 22-DoF, 50 Actuators Explained'.
4. AI Robots Media coverage (airobots.media/technology/tesla-optimus-gen-3-everything-we-know-about-teslas-most-ambitious-product/).
5. Wikipedia 'Optimus (robot)' (en.wikipedia.org/wiki/Optimus_(robot)).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b980619`.*
