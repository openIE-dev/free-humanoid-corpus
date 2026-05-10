---
title: "sensing-force-torque"
parent: "Invalidity Contentions"
nav_order: 239
layout: default
---

# Invalidity Contention Packet — `sensing-force-torque`

**Generated:** 2026-05-10  
**Cross-cut tag:** `sensing-force-torque`  
**Entries:** 45 (39 commons-grade, 6 draft)  
**Earliest disclosure:** 1969  
**Most recent disclosure:** 2024-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-force-torque`.

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

### 1969 — Vukobratović Zero Moment Point

- **id:** `vukobratovic-zmp`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Miomir Vukobratović and D. Juričić, Mihajlo Pupin Institute, Belgrade
- **disclosure citation:** Vukobratović, Miomir and Juričić, D. 'Contribution to the synthesis of biped gait.' IEEE Transactions on Bio-Medical Engineering BME-16(1): 1-6, January 1969. Earlier conference: Vukobratović, M. and Juričić, D. 'Contribution to the synthesis of biped gait.' Proc. IFAC Symposium on Technical and Biological Problems of Control, Yerevan, 1968.
- **disclosed subsystems:** `control-zmp-balancing`, `mechanism-bipedal-locomotion`, `sensing-force-torque`

**Prior art notes:**

> Vukobratović's 1969 ZMP formulation is the foundational academic disclosure of dynamic-stability criteria for bipedal walking. Predates Honda P2 (1996) by 27 years and predates every modern humanoid bipedal patent at extraordinary depth. Anticipates with mathematical specificity: (1) the ZMP constraint as a sufficient condition for non-tipping bipedal gait — directly relevant to virtually every bipedal walking patent filed since 1990 (Honda, Sony, Toyota, every Asian humanoid program); (2) gait synthesis by ZMP-trajectory planning — relevant to claims on humanoid walking pattern generators (HRP series, ASIMO, NAO all use ZMP-derived planners); (3) the support polygon as the safety region for COM projection — relevant to claims on bipedal balance recovery. Heavily cited (>5000 citations); the ZMP concept has 13 books and several hundred papers as direct extensions. 57-year-deep 102 anchor against any bipedal-stability patent.

**Sources:**

1. Vukobratović, M. and Juričić, D. 'Contribution to the synthesis of biped gait.' IEEE Trans. BME-16(1): 1-6, 1969.
2. Vukobratović, M. and Borovac, B. 'Zero-moment point — thirty five years of its life.' Int. J. Humanoid Robotics 1(1): 157-173, 2004 (retrospective).

---

### 1982 — Salisbury Stanford/JPL Hand

- **id:** `salisbury-stanford-jpl-hand`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** J. Kenneth Salisbury, Stanford University and JPL
- **disclosure citation:** Salisbury, J. Kenneth. 'Kinematic and Force Analysis of Articulated Hands.' PhD Thesis, Stanford University, May 1982. Companion paper: Salisbury, J.K. and Craig, J.J. 'Articulated hands: Force control and kinematic issues.' International Journal of Robotics Research 1(1): 4-17, March 1982.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `sensing-force-torque`

**Prior art notes:**

> Salisbury's 1982 thesis is the foundational academic disclosure of dexterous tendon-driven multi-finger hands with analytic grasp planning. Anticipates with mechanism-level specificity: (1) N+1 antagonistic tendon architecture for fingers — directly relevant to claims on tendon-driven humanoid hand actuators (Tesla Optimus hand, Figure hand, 1X hand); (2) the grasp matrix G and grip Jacobian formalism — anticipates virtually every modern grasp-planning patent; (3) force-closure analysis for grasp synthesis — relevant to grasp-search IP; (4) per-finger stiffness control — relevant to compliant-grasp claims. Salisbury later co-developed the PHANToM haptic device using the same kinematic framework. Thesis publicly available through Stanford Libraries; the IJRR companion paper has >2000 citations. 44-year-deep 102 anchor.

**Sources:**

1. Salisbury, J.K. PhD Thesis, Stanford University, 1982.
2. Salisbury, J.K. and Craig, J.J. 'Articulated hands.' IJRR 1(1): 4-17, 1982.
3. Mason, M.T. and Salisbury, J.K. Robot Hands and the Mechanics of Manipulation. MIT Press, 1985.

---

### 1987-02 — Khatib Operational Space Formulation

- **id:** `khatib-operational-space`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Oussama Khatib, Stanford Artificial Intelligence Laboratory
- **disclosure citation:** Khatib, Oussama. 'A unified approach for motion and force control of robot manipulators: The operational space formulation.' IEEE Journal of Robotics and Automation, RA-3(1): 43-53, February 1987. Earlier: Khatib, O. 'Dynamic control of manipulators in operational space.' 6th IFToMM Congress on Theory of Machines and Mechanisms, New Delhi, December 1983.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> Khatib's 1987 operational-space formulation is the canonical academic disclosure of task-space inverse-dynamics control with null-space projection. It anticipates with full mathematical specificity: (1) the operational-space inertia matrix Λ(x) and its closed-form expression — directly relevant to whole-body torque-control claims for humanoid platforms; (2) null-space projection for redundancy resolution and prioritized task hierarchies — anticipates virtually every whole-body humanoid controller filed since 2010 (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo all employ derivatives); (3) unified motion-and-force impedance control via task-space coordinates — anticipates compliant manipulation IP. Continuously cited (>10,000 citations); the IEEE J-RA paper is freely available through IEEE Xplore. Modern claims on task-space humanoid control face a 39-year-deep 102 anchor here.

**Sources:**

1. Khatib, O. 'A unified approach for motion and force control of robot manipulators.' IEEE J. Robotics and Automation 3(1): 43-53, 1987.
2. Khatib, O. 'Dynamic control of manipulators in operational space.' 6th IFToMM Congress, 1983.

---

### 1989-05-14 — Howe-Cutkosky tactile fingertip

- **id:** `howe-cutkosky-tactile-1989`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Robert D. Howe and Mark R. Cutkosky; Stanford University Center for Design Research
- **disclosure citation:** Howe, R.D. and Cutkosky, M.R. 'Sensing skin acceleration for slip and texture perception'. IEEE ICRA 1989, Scottsdale AZ, May 14-19, 1989. Extended in Howe, R.D. and Cutkosky, M.R. 'Dynamic tactile sensing: perception of fine surface features with stress rate sensing'. IEEE T-RO 9(2): 140-151, 1993.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-force-torque`

**Prior art notes:**

> Howe-Cutkosky 1989 is the deepest academic anchor for multimodal tactile fingertip sensing in the corpus. Anticipates with full mechanism specificity: (1) PVDF piezoelectric film as a slip-detection sensing layer — relevant to claims on slip-detection tactile IP (BioTac 2008, GelSight 2017, DIGIT 2020 all build on this lineage); (2) multimodal fingertip combining force, vibration, and thermal — relevant to multimodal tactile IP; (3) signal processing for texture classification from contact vibration — relevant to texture-recognition claims. The 1989 ICRA paper and 1993 T-RO paper are heavily cited; modern fingertip-sensing patents face this 35-year academic anchor as 102 prior art.

**Sources:**

1. Howe, R.D. and Cutkosky, M.R. 'Sensing skin acceleration for slip and texture perception'. IEEE ICRA 1989.
2. Howe, R.D. and Cutkosky, M.R. 'Dynamic tactile sensing'. IEEE T-RO 9(2), 1993.
3. Howe, R.D. 'Tactile sensing and control of robotic manipulation'. Advanced Robotics 8(3), 1994.

---

### 1990-01 — ATI Industrial Automation 6-axis F/T sensors (Mini40, Nano17, Gamma)

- **id:** `ati-industrial-ft-sensors-1990s`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** ATI Industrial Automation, Inc. (Apex, NC, USA; now Novanta)
- **disclosure citation:** ATI Industrial Automation, Inc. (Apex, NC, USA; founded 1989; now part of Novanta). 6-axis force/torque sensor product line from ~1990 onward. Mini40 (~2000), Nano17 (~2003), Gamma, Delta, Theta product variants. EDM-cut stainless-steel monolith with silicon strain gauges. The dominant commercial wrist F/T sensor in academic + industrial robotics.
- **disclosed subsystems:** `sensing-force-torque`, `sensing-6axis-ft`

**Prior art notes:**

> ATI Industrial Automation 6-axis F/T sensors (Apex NC ~1990+) are the dominant commercial 6-axis wrist F/T sensors. 30+-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from 6-axis wrist or fingertip F/T sensing. The default citation for commercial F/T sensing in academic literature.

**Sources:**

1. ati-ia.com/products/ft/ft_models.aspx?id=mini40
2. ATI Industrial Automation product line documentation.

---

### 1993 — Honda P1

- **id:** `honda-p1`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Honda Motor Co.
- **disclosure citation:** Hirose, M. and Ogawa, K. 'Honda humanoid robots development.' Phil. Trans. R. Soc. A 365, 11–19 (2007).
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Transition from legs-only to full humanoid in the Honda lineage. P1 is the architectural ancestor of ASIMO. Anticipates subsequent claims around full-humanoid actuated platforms with arms and legs.

**Sources:**

1. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).

---

### 1995-08 — Pratt-Williamson Series Elastic Actuator

- **id:** `pratt-williamson-sea`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Gill A. Pratt and Matthew M. Williamson, MIT Leg Laboratory and MIT AI Lab
- **disclosure citation:** Pratt, Gill A. and Williamson, Matthew M. 'Series elastic actuators.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Pittsburgh PA, August 5-9, 1995: 399-406.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> The Pratt-Williamson 1995 paper is the foundational academic disclosure of series-elastic actuators (SEA) — the dominant compliant-actuator architecture in legged and humanoid robotics. Anticipates with full specificity: (1) intentional series mechanical spring as the force-sensing element — directly relevant to claims on compliant humanoid actuators (Cassie, Digit, Apollo SEA derivatives); (2) spring-deflection-based force control without strain gauges — relevant to claims on encoder-only force feedback; (3) the bandwidth/stiffness tradeoff disclosure — anticipates SEA-design IP. Pratt's later commercial work (Yobotics, then Boston Dynamics' Atlas SEA) is grounded in this paper. Heavily cited (>3000 citations); SEA is now a textbook concept. 31-year-deep 102 anchor against any 'compliant humanoid actuator' patent.

**Sources:**

1. Pratt, G.A. and Williamson, M.M. 'Series elastic actuators.' IEEE/RSJ IROS 1995: 399-406.
2. Robinson, D.W. 'Design and analysis of series elasticity in closed-loop actuator force control.' PhD Thesis, MIT, 2000 (extension).

---

### 1996-12-20 — Honda P2

- **id:** `honda-p2`
- **corpus:** private
- **ip status:** patented
- **creator:** Honda Motor Co.
- **disclosure citation:** Honda Motor Co. press release, December 20, 1996, Tokyo. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> P2's December 1996 reveal is among the most significant single events in humanoid robotics history. Honda's ZMP-based dynamic balancing as publicly disclosed via P2 anticipates virtually all subsequent commercial bipedal locomotion claims using ZMP. Honda's 1990s patent filings, many of which have now expired, form the deepest commercial prior art chain in the field.

**Sources:**

1. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).
2. Hirai, K. et al. 'The development of Honda humanoid robot.' ICRA 1998.

---

### 1997-09 — Honda P3

- **id:** `honda-p3`
- **corpus:** private
- **ip status:** patented
- **creator:** Honda Motor Co.
- **disclosure citation:** Honda Motor Co. press materials, September 1997. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Final Honda P-series prototype before ASIMO. Refinements to the P2 architecture; key continuity in the Honda prior art chain.

**Sources:**

1. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).

---

### 1999-12 — Goswami Foot Rotation Indicator

- **id:** `goswami-fri`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Ambarish Goswami, INRIA Rhône-Alpes (later Honda Research Institute)
- **disclosure citation:** Goswami, Ambarish. 'Postural stability of biped robots and the foot-rotation indicator (FRI) point.' International Journal of Robotics Research 18(6): 523-533, June 1999.
- **disclosed subsystems:** `control-zmp-balancing`, `mechanism-bipedal-locomotion`, `sensing-force-torque`

**Prior art notes:**

> Goswami's FRI is the canonical academic disclosure of an extended-ZMP stability indicator capable of quantifying impending foot-rotation. Anticipates: (1) graded stability metrics for bipedal walking that go beyond binary ZMP-inside/outside checks — relevant to claims on bipedal balance estimators in modern humanoids; (2) FRI as a continuous early-warning signal for tipping-onset — relevant to fall-prediction IP (every academic and commercial humanoid claiming 'fall prediction' or 'stability margin estimation' faces this); (3) the formal distinction between ZMP and FRI in non-quasi-static gaits — relevant to dynamic-walking control claims. Highly cited (>1000 citations); Goswami's later work at Honda Research Institute (Asimo group) extended this. 27-year-deep 102 anchor against bipedal-stability-monitoring IP.

**Sources:**

1. Goswami, A. 'Postural stability of biped robots and the FRI point.' IJRR 18(6): 523-533, 1999.
2. Sardain, P. and Bessonnet, G. 'Forces acting on a biped robot. Center of pressure-zero moment point.' IEEE Trans. SMC-A 34(5): 630-637, 2004 (clarifies FRI vs ZMP).

---

### 2000-10-31 — ASIMO

- **id:** `asimo`
- **corpus:** private
- **ip status:** patented
- **creator:** Honda Motor Co.
- **disclosure citation:** Honda Motor Co. press conference, Tokyo, October 31, 2000.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> ASIMO's public disclosures and Honda's published papers anticipate most claimed innovations in modern bipedal humanoids. The Hirose/Ogawa 2007 Phil. Trans. paper is a particularly comprehensive disclosure that should be referenced when reading current humanoid patent claims.

**Sources:**

1. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).
2. Sakagami, Y. et al. 'The intelligent ASIMO: System overview and integration.' IROS 2002.

---

### 2002 — HRP-2

- **id:** `hrp-2`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** AIST (National Institute of Advanced Industrial Science and Technology), Kawada Industries
- **disclosure citation:** Kaneko, K. et al. 'Design of prototype humanoid robotics platform for HRP.' IROS 2002.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `software-openhrp`, `software-ros1`

**Prior art notes:**

> OpenHRP is itself foundational prior art for open robotics simulation frameworks. HRP-2 was among the first humanoids to publicly demonstrate falling-and-recovering behaviors.

**Sources:**

1. Kaneko, K. et al. IROS 2002.
2. Kanehiro, F. et al. 'OpenHRP: Open Architecture Humanoid Robotics Platform.' IJRR 23(2), 2004.

---

### 2004 — HUBO

- **id:** `hubo`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KAIST, Hubo Lab (Jun-Ho Oh)
- **disclosure citation:** Park, Ill-Woo et al. 'Mechanical Design of Humanoid Robot Platform KHR-3 (HUBO).' IEEE-RAS Humanoids 2005.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-wheel-leg-hybrid`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`

**Prior art notes:**

> DRC-Hubo's 2015 win demonstrated transformer-style transitioning between bipedal and wheeled-knee modes for navigating both stairs and flat ground. Anticipates: hybrid locomotion modes in humanoids.

**Sources:**

1. Park, I.-W. et al. IEEE-RAS Humanoids 2005.
2. DARPA Robotics Challenge final report, 2015.

---

### 2004 — DLR Hand-II

- **id:** `dlr-hand-ii`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Butterfass, Grebenstein, Liu, Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen, Germany
- **disclosure citation:** Butterfass, J., Grebenstein, M., Liu, H., Hirzinger, G. 'DLR-Hand II: next generation of a dextrous robot hand'. IEEE ICRA, 2001 (early disclosure); Butterfass, J. et al. 'Design and Experiences with DLR Hand II'. World Automation Congress, 2004.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-harmonic-drive`, `actuator-electric-tendon-driven`, `sensing-tactile-fingertip`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> DLR Hand-II is the canonical academic disclosure of joint-torque-sensing dexterous hands with compact actuator integration. Anticipates: (1) impedance-controlled dexterous manipulation with proprioceptive sensing — directly relevant to claims on torque-controlled humanoid hands (every modern humanoid hand IP); (2) cable-tendon transmission with harmonic-drive primary reducer — relevant to combined-mechanism actuator claims; (3) per-joint integrated torque sensor with calibrated absolute position — anticipates proprioceptive-actuator IP. The DLR series (Hand-II, then Hand-III, then Hand Arm System) is one of the deepest academic technical lineages in dexterous manipulation. Continuously published in IEEE proceedings since 2001.

**Sources:**

1. Butterfass, J. et al. 'DLR-Hand II: next generation of a dextrous robot hand'. IEEE ICRA 2001.
2. Butterfass, J. et al. 'Design and Experiences with DLR Hand II'. World Automation Congress 2004.

---

### 2005 — Sentis-Khatib Whole-Body Prioritized Task Control

- **id:** `sentis-khatib-whole-body`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Luis Sentis and Oussama Khatib, Stanford AI Laboratory
- **disclosure citation:** Sentis, Luis and Khatib, Oussama. 'Synthesis of whole-body behaviors through hierarchical control of behavioral primitives.' International Journal of Humanoid Robotics 2(4): 505-518, December 2005. Extended in: Sentis, L. and Khatib, O. 'A whole-body control framework for humanoids operating in human environments.' IEEE ICRA, May 2006: 2641-2648.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`, `sensing-proprioceptive-actuator`, `sensing-force-torque`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Sentis-Khatib whole-body operational-space control extends Khatib 1987 to free-floating humanoids with constraint-aware prioritized task stacks. Anticipates with full specificity: (1) whole-body humanoid task-priority controllers — every modern humanoid (Atlas, TORO, HRP-5P, Optimus, Figure 02) executes a derivative of this stack; (2) contact-consistent dynamics where stance-foot constraints are projected out of the task space — directly relevant to claims on multi-contact humanoid balancing; (3) the formal hierarchical-stack structure (high > mid > low priority via null-space chaining) used in essentially every whole-body humanoid controller since 2010. Sentis's 2007 PhD thesis and the IJHR/ICRA papers are heavily cited (>4000 citations combined). Modern whole-body humanoid IP filings face this academic anchor at 21 years' depth.

**Sources:**

1. Sentis, L. and Khatib, O. 'Synthesis of whole-body behaviors.' Int. J. Humanoid Robotics 2(4): 505-518, 2005.
2. Sentis, L. and Khatib, O. 'A whole-body control framework for humanoids.' IEEE ICRA 2006: 2641-2648.
3. Sentis, L. PhD Thesis: 'Synthesis and control of whole-body behaviors in humanoid systems.' Stanford University, 2007.

---

### 2006 — WABIAN-2

- **id:** `wabian-2`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Waseda University, Takanishi Laboratory
- **disclosure citation:** Ogura, Y. et al. 'Development of a New Humanoid Robot WABIAN-2.' ICRA 2006.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `control-zmp-balancing`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`, `power-tethered`

**Prior art notes:**

> WABIAN-2's stretched-knee gait disclosure is significant prior art for any humanoid walking control claim aiming at more human-like locomotion (less crouched, more upright knees during stance). Distinct from ASIMO's bent-knee paradigm. The Takanishi laboratory's continued publication makes this a well-anchored academic disclosure.

**Sources:**

1. Ogura, Y. et al. ICRA 2006.
2. Takanishi laboratory humanoid robot publications.

---

### 2007 — Toyota Partner Robot (Violin)

- **id:** `toyota-partner-robot-violin`
- **corpus:** private
- **ip status:** patented
- **creator:** Toyota Motor Corporation Partner Robot Division
- **disclosure citation:** Toyota Motor Corporation public reveal, 2007.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `sensing-stereo-camera`, `sensing-force-torque`, `power-li-ion`

**Prior art notes:**

> Toyota's high-precision finger control disclosures are significant prior art for fine motor control humanoid claims.

**Sources:**

1. Toyota Partner Robot press materials, 2007.

---

### 2008 — iCub

- **id:** `icub`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Italian Institute of Technology (IIT) and the RobotCub Consortium
- **disclosure citation:** Metta, G. et al. 'The iCub humanoid robot: an open platform for research in embodied cognition.' PerMIS 2008.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `actuator-electric-tendon-driven`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-tactile-whole-body`, `software-yarp`

**Prior art notes:**

> Among the earliest fully open-source humanoid platforms with hardware design released. Anticipates: tendon-driven anthropomorphic hands, full-body artificial skin, open robotics middleware.

**Sources:**

1. Metta, G. et al. PerMIS 2008.
2. iCub.org documentation.

---

### 2008 — HRP-3

- **id:** `hrp-3`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** AIST and Kawada Industries
- **disclosure citation:** Kaneko, K. et al. 'Humanoid Robot HRP-3.' IROS 2008.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> HRP-3's environmental sealing disclosures anticipate subsequent IP-rated humanoid claims. The HRP series is a deep commons asset because of consistent open academic disclosure across generations.

**Sources:**

1. Kaneko, K. et al. IROS 2008.

---

### 2008 — Willow Garage PR1

- **id:** `willow-pr1`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Willow Garage / Stanford (Ken Salisbury group)
- **disclosure citation:** Wyrobek, K.A. et al. 'Towards a Personal Robotics Development Platform: Rationale and Design of an Intrinsically Safe Personal Robot.' ICRA 2008.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `power-tethered`, `safety-hard-constraint`

**Prior art notes:**

> PR1 is significant prior art for safety-by-design humanoid robotics. Cable-driven intrinsically-safe architecture anticipates several modern compliant-actuator humanoid claims.

**Sources:**

1. Wyrobek, K.A. et al. ICRA 2008.
2. Willow Garage technical materials.

---

### 2008 — BioTac

- **id:** `biotac-syntouch`
- **corpus:** academic
- **ip status:** patented
- **creator:** Wettels, Santos, Fishel, Johansson, Loeb; University of Southern California; commercial: SynTouch
- **disclosure citation:** Lin, C.H., Erickson, T.W., Fishel, J.A., Wettels, N., Loeb, G.E. 'Signal processing and fabrication of a biomimetic tactile sensor array with thermal, force and microvibration modalities'. IEEE ROBIO 2009; commercial release by SynTouch (USC spinoff) 2008. Foundational biomimetic concepts in Wettels, N., Santos, V.J., Johansson, R.S., Loeb, G.E. 'Biomimetic tactile sensor array'. Advanced Robotics 22(8): 829-849, 2008.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-force-torque`

**Prior art notes:**

> BioTac is the bridge between Howe-Cutkosky 1989 multimodal academic concept and modern commercial multimodal fingertip sensors. Anticipates: (1) commercial biomimetic multimodal fingertip — relevant to claims on integrated tactile fingertips for humanoids; (2) thermal-flux sensing as a material classification modality — relevant to material-identification claims; (3) hydroacoustic vibration sensing — relevant to dynamic-tactile-perception claims. Patented (US7878075) but the academic disclosure (Wettels et al. 2008) precedes the patent and is itself prior art. Widely deployed in research labs and modern humanoid platforms; canonical reference for 'biotac-class' multimodal fingertip.

**Sources:**

1. Wettels, N. et al. 'Biomimetic tactile sensor array'. Advanced Robotics 22(8), 2008.
2. Lin, C.H. et al. IEEE ROBIO 2009.
3. US Patent 7878075 (SynTouch).

---

### 2010 — PR2

- **id:** `pr2`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Willow Garage
- **disclosure citation:** Willow Garage. PR2 platform release, 2010.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `actuator-electric-series-elastic`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> PR2 was the platform around which ROS was originally built. Its hardware is significant prior art for omnidirectional wheeled mobile manipulation. ROS itself is even more significant prior art for robotics middleware.

**Sources:**

1. Willow Garage technical materials.
2. Quigley, M. et al. 'ROS: an open-source Robot Operating System.' ICRA Workshop 2009.

---

### 2010 — HRP-4

- **id:** `hrp-4`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** AIST and Kawada Industries
- **disclosure citation:** Kaneko, K. et al. 'Humanoid Robot HRP-4: Humanoid Robotics Platform with Lightweight and Slim Body.' IROS 2010.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> HRP-4 lightweight design anticipates subsequent slim-form humanoid claims. The 2010 IROS paper provides full mechanical specifications openly.

**Sources:**

1. Kaneko, K. et al. IROS 2010.

---

### 2010-02 — Robonaut 2

- **id:** `robonaut-2`
- **corpus:** academic
- **ip status:** patented
- **creator:** NASA Johnson Space Center, in partnership with General Motors
- **disclosure citation:** Diftler, M.A. et al. 'Robonaut 2 — The First Humanoid Robot in Space.' ICRA 2011.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `actuator-electric-series-elastic`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-tactile-fingertip`, `power-tethered`

**Prior art notes:**

> Robonaut 2's hand design, with 12 DoF per hand and tendon routing through the forearm, is foundational prior art for high-DoF tendon-driven humanoid hands. The NASA-GM patent portfolio has been extensively cited.

**Sources:**

1. Diftler, M.A. et al. ICRA 2011.
2. Bridgwater, L.B. et al. 'The Robonaut 2 Hand — Designed To Do Work With Tools.' ICRA 2012.

---

### 2011-05 — DLR Hand-Arm System

- **id:** `dlr-hand-arm-system-2011`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Markus Grebenstein, Alin Albu-Schäffer, Antonio Bicchi (collaboration), Gerd Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen
- **disclosure citation:** Grebenstein, Markus; Albu-Schäffer, Alin; Bahls, Thomas; Chalon, Maxime; Eiberger, Oliver; Friedl, Werner; Gruber, Robin; Haddadin, Sami; Hagn, Ulrich; Haslinger, Robert; Höppner, Hannes; Jörg, Stefan; Nickl, Mathias; Nothhelfer, Alexander; Petit, Florian; Reill, Josef; Seitz, Norbert; Wimböck, Thomas; Wolf, Sebastian; Wüsthoff, Tilo; Hirzinger, Gerd. 'The DLR Hand Arm System.' IEEE International Conference on Robotics and Automation (ICRA), Shanghai, May 2011, pp. 3175-3182. DOI: 10.1109/ICRA.2011.5980371. Companion thesis: Grebenstein, M. 'Approaching Human Performance: The Functionality-Driven Awiwi Robot Hand.' PhD thesis, ETH Zurich, 2012; published Springer Tracts in Advanced Robotics 98, 2014. ISBN 978-3-319-03592-9.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `mechanism-underactuated-grasping`, `actuator-electric-tendon-driven`, `sensing-tactile-fingertip`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> The DLR Hand-Arm System (Grebenstein et al. ICRA 2011, Grebenstein PhD/STAR 2014) is the canonical academic disclosure of variable-impedance antagonistically-tendon-driven anthropomorphic hand-arm hardware. Anticipates with element-by-element mechanism-level specificity: (1) mechanically programmable variable joint stiffness via antagonistic tendons with nonlinear elastic elements — directly relevant to commercial claims on variable-stiffness humanoid hand IP; (2) the 19-DoF, 38-tendon, 38-motor architecture with motors in the forearm — relevant to claims on tendon-driven hand-with-forearm-actuation humanoid IP (Tesla Optimus Gen-3, Figure-02, Apptronik Apollo, Sanctuary Phoenix all show variations of this topology); (3) impact-survival via mechanical compliance absorption — anticipates claims on collision-tolerant humanoid hand IP; (4) the biomimetic muscle-tendon co-contraction analogue — relevant to claims on biomimetic humanoid manipulation. Grebenstein's PhD thesis (200+ pages) provides the deepest single-source mechanism disclosure in dexterous robotic hand history. Modern variable-impedance anthropomorphic hand IP filings face this 15-year-deep academic anchor with mechanical-drawing-level specificity.

**Sources:**

1. Grebenstein, M. et al. 'The DLR Hand Arm System.' IEEE ICRA 2011: 3175-3182. DOI: 10.1109/ICRA.2011.5980371.
2. Grebenstein, M. 'Approaching Human Performance: The Functionality-Driven Awiwi Robot Hand.' Springer Tracts in Advanced Robotics 98, 2014. ISBN 978-3-319-03592-9.
3. Wolf, S. et al. 'The DLR FSJ: Energy based design of a variable stiffness joint.' IEEE ICRA 2011 (companion paper on the variable-stiffness joint mechanism).

---

### 2012-04 — CMU HERB (Home Exploring Robotic Butler)

- **id:** `cmu-herb-srinivasa-2012`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Siddhartha Srinivasa et al., Carnegie Mellon Personal Robotics Lab / Intel Labs Pittsburgh
- **disclosure citation:** Srinivasa, Siddhartha S., Berenson, Dmitry, Cakmak, Maya, Collet, Alvaro, Dogar, Mehmet R., Dragan, Anca D., Knepper, Ross A., Niemueller, Tim, Strabala, Kyle, Vande Weghe, Mike, Ziegler, Julius. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE 100(8): 2410-2428, August 2012. Original disclosure: Srinivasa, S. et al. 'HERB: a home exploring robotic butler.' Autonomous Robots 28(1): 5-20, January 2010.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-anthropomorphic-hand`, `mechanism-underactuated-grasping`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `software-ros1`

**Prior art notes:**

> CMU HERB is one of the most extensively-published academic mobile-manipulator humanoid platforms (>50 papers across 2008-2018). Anticipates with full specificity: (1) claims on home-environment dual-arm humanoid manipulation — HERB's headline contribution including kitchen/office task suite, fridge/microwave/dishwasher manipulation; (2) claims on legible/predictable HRI motion synthesis — Dragan-Srinivasa 2013 'Legibility and Predictability of Robot Motion' is part of the HERB program and anticipates current humanoid social-motion IP; (3) claims on cable-driven backdrivable arms with underactuated 3-finger hands for home manipulation — Barrett WAM + BH-280 are the explicit instantiation; (4) claims on manipulation-among-movable-obstacles planning. Proceedings of IEEE article and Autonomous Robots paper provide deeply-cited timestamped disclosure. Modern home-humanoid IP filings (1X NEO Gamma, Figure 02 home demos) face this 14-year-deep academic anchor.

**Sources:**

1. Srinivasa, S. et al. 'HERB 2.0.' Proc. IEEE 100(8): 2410-2428, 2012.
2. Srinivasa, S. et al. 'HERB: a home exploring robotic butler.' Autonomous Robots 28(1): 5-20, 2010.
3. Dragan, A., Lee, K., Srinivasa, S. 'Legibility and Predictability of Robot Motion.' HRI 2013.

---

### 2013 — NASA Valkyrie

- **id:** `nasa-valkyrie`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NASA Johnson Space Center, in collaboration with University of Texas at Austin and others
- **disclosure citation:** NASA Johnson Space Center, DARPA Robotics Challenge entry, 2013.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`, `sensing-imu`, `software-ros1`, `power-li-ion`, `power-tethered`

**Prior art notes:**

> NASA Valkyrie's series-elastic actuator implementations and the IHMC-derived whole-body control work are foundational prior art. The robot was distributed to multiple universities and produced extensive open publications.

**Sources:**

1. Radford, N. et al. 'Valkyrie: NASA's First Bipedal Humanoid Robot.' Journal of Field Robotics 32(3), 2015.
2. NASA technical reports.

---

### 2013 — REEM-C

- **id:** `reem-c`
- **corpus:** private
- **ip status:** patented
- **creator:** PAL Robotics
- **disclosure citation:** PAL Robotics REEM-C release, 2013.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> REEM-C distributed to multiple research labs; design characteristics openly published.

**Sources:**

1. PAL Robotics company materials.
2. Academic publications by REEM-C users.

---

### 2014-05 — CMU Personal Robotics Lab Andy / HERB-2 follow-on platform

- **id:** `cmu-andy-herb2-srinivasa-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Siddhartha Srinivasa, Anca Dragan, J. Andrew Bagnell, and the CMU Personal Robotics Lab
- **disclosure citation:** Srinivasa, Siddhartha S. et al. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE, vol. 100, no. 8, 2012; subsequent Andy disclosures: Dragan, Anca and Srinivasa, S. 'A Policy-Blending Formalism for Shared Control.' IJRR 32(7), 2013; Bagnell et al. CHIMP/Andy whole-body manipulation reports 2013-2015.
- **disclosed subsystems:** `mechanism-underactuated-grasping`, `actuator-electric-tendon-driven`, `sensing-force-torque`, `sensing-stereo-camera`, `control-teleoperation`, `software-ros1`

**Prior art notes:**

> The Andy / HERB-2 generation extends HERB-1 with formal shared-autonomy theory and is the survey-of-record for bimanual mobile-manipulator home robots in 2012-2015. It anticipates with full specificity: (1) claims on shared-autonomy arbitration between operator and policy — Dragan-Srinivasa policy-blending IJRR 2013 publishes the closed-form linear arbitration in confidence space; (2) claims on task-space-region constraint encoding for manipulation planning — Berenson-Srinivasa-Kuffner ICRA 2009 publishes TSR formalism executed on this platform; (3) claims on underactuated cable-driven grasping for unstructured pick-and-place — Barrett BH-280 deployment is the canonical published baseline. Modern humanoid manipulation IP claiming shared-autonomy or constraint-region planning faces these timestamped CMU disclosures.

**Sources:**

1. Srinivasa, S. et al. 'HERB 2.0' Proc. IEEE 100(8), 2012.
2. Dragan, A. and Srinivasa, S. 'A Policy-Blending Formalism for Shared Control.' IJRR 32(7), 2013.
3. Berenson, D., Srinivasa, S., Kuffner, J. 'Task Space Regions: A Framework for Pose-Constrained Manipulation Planning.' IJRR 2011.

---

### 2014-06 — Atlas academic publications (Kuindersma et al., DRC era)

- **id:** `atlas-academic-disclosures`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Scott Kuindersma, Russ Tedrake, Robin Deits, Maurice Fallon, Andrés Valenzuela, Hongkai Dai, Frank Permenter, Twan Koolen, Pat Marion; MIT CSAIL Robot Locomotion Group (DRC Atlas team)
- **disclosure citation:** Kuindersma, Scott; Permenter, Frank; Tedrake, Russ. 'An efficiently solvable quadratic program for stabilizing dynamic locomotion.' IEEE International Conference on Robotics and Automation (ICRA), Hong Kong, June 2014, pp. 2589-2594. DOI: 10.1109/ICRA.2014.6907230. Consolidated Atlas-on-DRC paper: Kuindersma, S.; Deits, R.; Fallon, M.; Valenzuela, A.; Dai, H.; Permenter, F.; Koolen, T.; Marion, P.; Tedrake, R. 'Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot.' Autonomous Robots 40(3): 429-455, March 2016. DOI: 10.1007/s10514-015-9479-3.
- **disclosed subsystems:** `actuator-hydraulic`, `mechanism-bipedal-locomotion`, `control-mpc`, `control-zmp-balancing`, `control-reduced-order-model`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `sensing-force-torque`

**Prior art notes:**

> The MIT DRC Atlas academic publication trail (Kuindersma-Tedrake et al. 2014-2016) is distinct from the Boston Dynamics Atlas product entry (atlas-boston-dynamics) and from the Sentis-Khatib WBOSC entry: it is the canonical academic disclosure of the actually-deployed Atlas controller stack as fielded at the DARPA Robotics Challenge Finals (June 2015). Anticipates with element-by-element specificity: (1) whole-body QP-based inverse-dynamics control on a hydraulically-actuated humanoid platform — directly relevant to commercial claims on QP-based humanoid IP (every modern humanoid runs a derivative); (2) the IRIS-regions mixed-integer convex footstep planner — relevant to claims on footstep-planning humanoid IP; (3) iterative SQP trajectory optimization with contact schedule — anticipates claims overlapping Crocoddyl (mastalli-crocoddyl-2020) and DDP approaches; (4) the consolidated end-to-end stack documentation in AURO 2016 — the most complete public disclosure of a working DRC-class humanoid control architecture. Drake source code accompanies the publications under BSD license. Modern QP-IDC-based humanoid IP filings face this 12-year-deep academic anchor with full implementation disclosure.

**Sources:**

1. Kuindersma, S.; Permenter, F.; Tedrake, R. 'An efficiently solvable quadratic program for stabilizing dynamic locomotion.' ICRA 2014: 2589-2594. DOI: 10.1109/ICRA.2014.6907230.
2. Kuindersma, S. et al. 'Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot.' Autonomous Robots 40(3): 429-455, 2016. DOI: 10.1007/s10514-015-9479-3.
3. Deits, R. and Tedrake, R. 'Footstep planning on uneven terrain with mixed-integer convex optimization.' IEEE-RAS Humanoids 2014.
4. Drake source code: https://drake.mit.edu, BSD-3-Clause license (companion to the Atlas papers).

---

### 2015-04 — Levine Guided Policy Search end-to-end manipulation on PR2/BRETT

- **id:** `levine-gps-pr2-2016`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Sergey Levine, Chelsea Finn, Trevor Darrell, Pieter Abbeel, UC Berkeley
- **disclosure citation:** Levine, Sergey, Finn, Chelsea, Darrell, Trevor, Abbeel, Pieter. 'End-to-End Training of Deep Visuomotor Policies.' Journal of Machine Learning Research 17(39): 1-40, 2016 (received April 2015; published 2016). Earlier: Levine, S., Wagener, N., Abbeel, P. 'Learning Contact-Rich Manipulation Skills with Guided Policy Search.' ICRA 2015.
- **disclosed subsystems:** `control-rl-policy`, `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-force-torque`, `software-ros1`

**Prior art notes:**

> Levine et al. 2016 JMLR is the canonical academic disclosure of end-to-end pixels-to-torques visuomotor policies for humanoid manipulation, learned via guided policy search on a PR2 (BRETT). Anticipates with full specificity: (1) claims on end-to-end neural-network policies mapping camera observations directly to humanoid actuator commands — Levine's CNN architecture, training pipeline, and on-robot evaluation are explicitly disclosed; (2) claims on trajectory-optimization-supervised distillation as a sample-efficient alternative to model-free RL on physical humanoids — GPS is the headline contribution; (3) claims on multi-task generalization of a single visuomotor network across contact-rich manipulation tasks (coat-hanger, plastic-bottle, hammer, screw insertion). >3500 citations; JMLR open access; arXiv preprint 2015. The lineage runs directly forward to RT-1, RT-2, OpenVLA, and modern humanoid VLA systems. Modern humanoid end-to-end visuomotor IP filings face this 11-year-deep anchor with full architecture disclosure.

**Sources:**

1. Levine, S., Finn, C., Darrell, T., Abbeel, P. 'End-to-End Training of Deep Visuomotor Policies.' JMLR 17(39): 1-40, 2016.
2. Levine, S., Wagener, N., Abbeel, P. 'Learning Contact-Rich Manipulation Skills with Guided Policy Search.' ICRA 2015.
3. BRETT video archive, UC Berkeley RAIL Lab, 2015.

---

### 2017 — PAL TALOS

- **id:** `pal-talos`
- **corpus:** private
- **ip status:** patented
- **creator:** PAL Robotics, in collaboration with LAAS-CNRS
- **disclosure citation:** Stasse, O. et al. 'TALOS: A new humanoid research platform targeted for industrial applications.' IEEE Humanoids 2017.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> TALOS is among the better-published European industrial humanoids. Stasse 2017 IEEE Humanoids paper provides comprehensive design disclosure.

**Sources:**

1. Stasse, O. et al. IEEE Humanoids 2017.
2. PAL Robotics company materials.

---

### 2017-11 — Toyota T-HR3

- **id:** `toyota-thr3`
- **corpus:** private
- **ip status:** patented
- **creator:** Toyota Motor Corporation Partner Robot Division
- **disclosure citation:** Toyota Motor Corporation public reveal, November 2017.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `control-teleoperation`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-tethered`

**Prior art notes:**

> T-HR3 is significant prior art for whole-body teleoperated humanoids with force feedback. The Master Maneuvering System teleoperation interface anticipates many modern humanoid teleop claims.

**Sources:**

1. Toyota press materials.
2. Toyota Partner Robot publications.

---

### 2017-11 — Kawasaki Kaleido

- **id:** `kawasaki-kaleido`
- **corpus:** private
- **ip status:** patented
- **creator:** Kawasaki Heavy Industries
- **disclosure citation:** Kawasaki Heavy Industries public reveal of Kaleido, iREX November 2017.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Kawasaki's deep industrial robotics IP base means much of their humanoid claims are anticipated by their own prior industrial robotics disclosures, plus AIST HRP series prior art.

**Sources:**

1. Kawasaki Heavy Industries materials.
2. iREX 2017 demonstration coverage.

---

### 2018-01 — UBTech Walker

- **id:** `ubtech-walker`
- **corpus:** private
- **ip status:** patented
- **creator:** UBTech Robotics
- **disclosure citation:** UBTech public reveal of Walker, CES January 2018.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> UBTech's bipedal locomotion claims anticipated by Honda P-series and ASIMO disclosures.

**Sources:**

1. UBTech company materials.
2. CES 2018 demonstration coverage.

---

### 2018-09 — HRP-5P

- **id:** `hrp-5p`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** AIST and Kawada Industries
- **disclosure citation:** Kaneko, K. et al. 'Humanoid Robot HRP-5P: An Electrically Actuated Humanoid Robot With High-Power and Wide-Range Joints.' IEEE Robotics and Automation Letters 4(2), 2019.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> HRP-5P's construction-task demonstrations and high-power actuator disclosures are among the most thoroughly published examples of humanoid construction work. Anticipates many subsequent industrial humanoid claims.

**Sources:**

1. Kaneko, K. et al. IEEE RA-L 4(2), 2019.

---

### 2022 — Sanctuary Phoenix Gen 6 *(draft)*

- **id:** `sanctuary-phoenix-gen6`
- **corpus:** private
- **ip status:** patented
- **creator:** Sanctuary AI
- **disclosure citation:** Sanctuary AI public reveals of Phoenix predecessors, 2020-2022.
- **disclosed subsystems:** `actuator-hydraulic`, `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `control-teleoperation`, `sensing-stereo-camera`, `sensing-force-torque`

**Prior art notes:**

> Sanctuary's hybrid hydraulic-electric actuation faces extensive prior art from Boston Dynamics Atlas (hydraulic), Honda (electric), and academic hybrid actuation literature.

**Sources:**

1. Sanctuary AI public materials, 2020-2022.

---

### 2023-05 — Sanctuary AI Phoenix *(draft)*

- **id:** `sanctuary-phoenix`
- **corpus:** private
- **ip status:** patented
- **creator:** Sanctuary AI
- **disclosure citation:** Sanctuary AI public reveal, May 2023.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `control-teleoperation`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-force-torque`, `power-li-ion`

**Prior art notes:**

> Sanctuary's high-DoF hand claims face Shadow Hand (2003) and iCub (2008) as deep prior art for tendon-driven anthropomorphic hands with high finger DoF.

**Sources:**

1. sanctuary.ai
2. Sanctuary AI press materials and demonstration videos.

---

### 2023-07 — RH20T heterogeneous robot trajectory dataset

- **id:** `rh20t-fang-2024`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Hao-Shu Fang et al., Shanghai Jiao Tong University Machine Vision and Intelligence Group
- **disclosure citation:** Fang, Hao-Shu, Fang, Hongjie, Tang, Zhenyu, Liu, Jirong, Wang, Junbo, Zhu, Haoyi, Lu, Cewu. 'RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot.' arXiv:2307.00595, July 2023; ICRA 2024 workshop and project release.
- **disclosed subsystems:** `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-tactile-fingertip`

**Prior art notes:**

> RH20T is one of the largest publicly-released heterogeneous robot trajectory datasets prior to OpenX-Embodiment. It anticipates with full specificity: (1) claims on multi-embodiment imitation learning where a single policy is trained across robots with differing kinematics — RH20T explicitly demonstrates and releases the data substrate; (2) claims on language-annotated demonstration corpora paired with sensor-rich teleoperation — RH20T pairs RGB-D, force-torque, tactile, audio, and matched human-video for each episode; (3) claims on one-shot/few-shot skill acquisition from teleoperated data — the dataset's headline benchmark. Released CC-BY 4.0 with timestamped arXiv and project page; broadly indexed. Modern humanoid imitation-learning IP claims to multi-embodiment trajectory corpora face this 2023 anchor.

**Sources:**

1. Fang, H.-S. et al. 'RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot.' arXiv:2307.00595, 2023.
2. RH20T project page: rh20t.github.io

---

### 2023-08 — Apptronik Apollo *(draft)*

- **id:** `apptronik-apollo`
- **corpus:** private
- **ip status:** patented
- **creator:** Apptronik
- **disclosure citation:** Apptronik public reveal of Apollo, August 2023.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-planetary`, `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`, `power-hot-swap`

**Prior art notes:**

> Apptronik's actuator IP has lineage from UT Austin Human-Centered Robotics Lab (Sentis) and from NASA Valkyrie work; both sources constitute substantial prior art that limits the patentable surface area of Apptronik's own claims.

**Sources:**

1. apptronik.com
2. Apptronik technical materials.

---

### 2023-08 — AgiBot A1 *(draft)*

- **id:** `agibot-a1`
- **corpus:** private
- **ip status:** patented
- **creator:** AgiBot (Shanghai Zhiyuan New Technology Co.)
- **disclosure citation:** AgiBot (Shanghai Zhiyuan New Technology) public reveal, August 2023.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-imu`, `sensing-force-torque`, `power-li-ion`

**Prior art notes:**

> AgiBot's actuator IP heavily anticipated by Honda P-series harmonic drive work and MIT Cheetah QDD lineage. Chinese-language patent filings should be enumerated in strengthening pass.

**Sources:**

1. AgiBot company materials.
2. Chinese-language tech press coverage.

---

### 2023-08 — Apptronik Apollo academic and technical disclosures (2023-2024)

- **id:** `apptronik-apollo-publications-2024`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Apptronik Inc. (Jeff Cardenas, Nick Paine, Luis Sentis lineage from UT Austin Human-Centered Robotics Lab)
- **disclosure citation:** Apptronik. 'Apollo: A Commercial Humanoid Robot for the Workforce.' Apptronik whitepaper, August 2023; Knabe, Coleman et al. 'Designing a Force-Controlled Linear Series Elastic Actuator.' (NASA Valkyrie / Apptronik lineage) IROS 2014; Apptronik-NASA JSC disclosures 2023-2024 including SAFFiR/Valkyrie genealogy white-papers.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `actuator-electric-series-elastic`, `actuator-electric-planetary`, `sensing-imu`, `sensing-force-torque`, `sensing-stereo-camera`, `control-zmp-balancing`, `control-teleoperation`, `power-hot-swap`, `power-li-ion`

**Prior art notes:**

> This entry isolates the academic-publication and technical-disclosure trail behind Apptronik Apollo (distinct from the Apollo product seed entry). It anticipates with full specificity: (1) claims on humanoid SEA actuator topology — Knabe-Paine et al. IROS 2014 publishes the linear-SEA design that lineally seeds Apollo; (2) claims on whole-body operational-space control for force-interactive humanoid manipulation — Sentis-Khatib WBOSC 2007/2010 papers (UT Austin lineage carried into Apptronik) are foundational and timestamped; (3) claims on hot-swap-battery torso integration with regenerative power electronics on humanoid platforms — Apollo whitepaper August 2023 discloses publicly. Modern humanoid commercial-platform IP claims to SEA torque control or WBOSC face this Apptronik publication trail at element-by-element specificity.

**Sources:**

1. Apptronik. 'Apollo: A Commercial Humanoid Robot for the Workforce.' Whitepaper, 2023.
2. Knabe, C., Paine, N. et al. 'Designing a Force-Controlled Linear Series Elastic Actuator.' IROS 2014.
3. Sentis, L. and Khatib, O. 'Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives.' IJHR 2(4), 2005.

---

### 2024-03-19 — DROID Dataset

- **id:** `droid-dataset`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** DROID Consortium (Khazatsky et al., 18 academic + industry institutions)
- **disclosure citation:** Khazatsky, Alexander et al. 'DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset.' arXiv:2403.12945, March 19, 2024. Robotics: Science and Systems (RSS) 2024. Authors: Khazatsky, A., Pertsch, K., Nair, S., Balakrishna, A., Dasari, S., Karamcheti, S., Nasiriany, S., Srirama, M.K., Chen, L.Y., Ellis, K., Fagan, P.D., Hejna, J., Itkina, M., Lepert, M., Ma, Y.J., Miller, P.T., Wu, J., Belkhale, S., Dass, S., Ha, H., Jain, A., Lee, A., Lee, Y., Memmel, M., Park, S., Radosavovic, I., Wang, K., Zhan, A., Black, K., Chi, C., Hatch, K.B., Lin, S., Lu, J., Mercat, J., Rehman, A., Sanketi, P.R., Sharma, A., Simpson, C., Vuong, Q., Walke, H.R., Wulfe, B., Xiao, T., Yang, J.H., Yavary, A., Zhao, T.Z., Agia, C., Baijal, R., Castro, M.G., Chen, D., Chen, Q., Chung, T., Drake, J., Foster, E.P., Gao, J., Garcia Herrera, D.A., Heo, M., Hsu, K., Hu, J., Jackson, D., Le, C., Li, Y., Lin, K., Lin, R., Ma, Z., Maddukuri, A., Mirchandani, S., Morton, D., Nguyen, T., O'Neill, A., Scalise, R., Seale, D., Son, V., Tian, S., Tran, E., Wang, A.E., Wu, Y., Xie, A., Yang, J., Yin, P., Zhang, Y., Bastani, O., Berseth, G., Bohg, J., Goldberg, K., Gupta, A., Gupta, A., Jayaraman, D., Lim, J.J., Malik, J., Martín-Martín, R., Ramamoorthy, S., Sadigh, D., Song, S., Wu, J., Yip, M.C., Zhu, Y., Kollar, T., Levine, S., Finn, C. (Stanford / Berkeley / TRI / GoogleDeepMind / 18-institution academic consortium).
- **disclosed subsystems:** `control-teleoperation`, `sensing-stereo-camera`, `sensing-force-torque`

**Prior art notes:**

> DROID is the canonical academic disclosure of large-scale standardized robot manipulation data collection across diverse environments. Anticipates: (1) standardized hardware-stack-based data collection at multi-institutional scale — directly relevant to claims on 'data-flywheel' humanoid programs (Tesla Optimus operator floor, Figure data pipeline, 1X data-collection program); (2) teleoperated demonstration data as the substrate for VLA training — relevant to claims on imitation-learning-based humanoid IP; (3) the open data + open hardware spec combination — establishes prior art for any 'standardized fleet for robot data' patent claim. Released under permissive license (CC-BY 4.0 for data); 76k trajectories, 564 scenes, full hardware spec. Modern humanoid data-collection patent claims face this 2-year-deep anchor.

**Sources:**

1. Khazatsky, A. et al. 'DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset.' RSS 2024; arXiv:2403.12945.
2. Project page and dataset: https://droid-dataset.github.io/

---

### 2024-05 — Neura 4NE-1 *(draft)*

- **id:** `neura-4ne1`
- **corpus:** private
- **ip status:** patented
- **creator:** Neura Robotics
- **disclosure citation:** Neura Robotics public reveal of 4NE-1, May 2024.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-vla-vision-language-action`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Neura's cognitive-AI claims overlap with academic VLA literature.

**Sources:**

1. Neura Robotics website.
2. Industry press coverage.

---

### 2024-07 — Kepler K2 *(draft)*

- **id:** `kepler-k2`
- **corpus:** private
- **ip status:** patented
- **creator:** Kepler Exploration Robotics
- **disclosure citation:** Kepler Exploration Robotics public reveal, July 2024.
- **disclosed subsystems:** `actuator-electric-planetary`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-imu`, `sensing-force-torque`, `power-li-ion`

**Prior art notes:**

> Kepler's planetary-reducer actuator claims are anticipated by extensive prior art in industrial robotics planetary-gearing literature.

**Sources:**

1. Kepler company materials.

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
