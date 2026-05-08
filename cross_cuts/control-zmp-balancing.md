---
title: control-zmp-balancing
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-zmp-balancing`

**23 corpus entries disclose this subsystem.**

Earliest disclosure: 1969

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Vukobratović Zero Moment Point (1969)

- **id**: `vukobratovic-zmp`
- **corpus**: academic
- **creator**: Miomir Vukobratović and D. Juričić, Mihajlo Pupin Institute, Belgrade
- **disclosure**: Vukobratović, Miomir and Juričić, D. 'Contribution to the synthesis of biped gait.' IEEE Transactions on Bio-Medical Engineering BME-16(1): 1-6, January 1969. Earlier conference: Vukobratović, M. and Juričić, D. 'Contribution to the synthesis of biped gait.' Proc. IFAC Symposium on Technical and Biological Problems of Control, Yerevan, 1968.
- **ip status**: public-domain
- **prior art notes**: Vukobratović's 1969 ZMP formulation is the foundational academic disclosure of dynamic-stability criteria for bipedal walking. Predates Honda P2 (1996) by 27 years and predates every modern humanoid bipedal patent at extraordinary depth. Anticipates with mathematical specificity: (1) the ZMP constraint as a sufficient condition for non-tipping bipedal gait — directly relevant to virtually every bipedal walking patent filed since 1990 (Honda, Sony, Toyota, every Asian humanoid program); (2) gait synthesis by ZMP-trajectory planning — relevant to claims on humanoid walking pattern generators (HRP series, ASIMO, NAO all use ZMP-derived planners); (3) the support polygon as the safety region for COM projection — relevant to claims on bipedal balance recovery. Heavily cited (>5000 citations); the ZMP concept has 13 books and several hundred papers as direct extensions. 57-year-deep 102 anchor against any bipedal-stability patent.

## AV-98 Ingram (1988-04)

- **id**: `patlabor-av-98`
- **corpus**: fictional
- **creator**: Headgear (Masami Yuki, Yutaka Izubuchi, Mamoru Oshii, Kazunori Itō, Akemi Takada)
- **disclosure**: Yuki, Masami; Headgear collective (Yuki, Yutaka Izubuchi, Mamoru Oshii, Kazunori Itō, Akemi Takada). Mobile Police Patlabor. Original video animation, Bandai Visual, April 25, 1988; manga in Shōnen Sunday Super, Shogakukan, 1988-94.
- **ip status**: fictional
- **prior art notes**: Patlabor's 'Labor' family is an unusually engineering-grounded fictional disclosure of bipedal civilian humanoid robotics. The 1988 OVA explicitly names the 'OS' that handles balance (anticipating ZMP balance controllers years before Honda P2 1996), discloses runtime of ~15 minutes per battery, and depicts limp-on-shutdown safety. Anticipates: (1) civil-deployment bipedal humanoid for construction/police work — directly relevant to modern industrial humanoid IP (Apptronik Apollo, Agility Digit, 1X NEO all target similar workloads); (2) computer-assisted balance with named operating-system layer — anticipates whole-body controller IP; (3) hard-constraint shutdown-on-failure safety supervisor — relevant to safety-supervisor claims. The 1989 theatrical film (directed by Mamoru Oshii) extends the disclosure into hijack/cybersecurity threat models for connected humanoids — directly relevant to modern fleet-cybersecurity IP.

## Honda P2 (1996-12-20)

- **id**: `honda-p2`
- **corpus**: private
- **creator**: Honda Motor Co.
- **disclosure**: Honda Motor Co. press release, December 20, 1996, Tokyo. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).
- **ip status**: patented
- **prior art notes**: P2's December 1996 reveal is among the most significant single events in humanoid robotics history. Honda's ZMP-based dynamic balancing as publicly disclosed via P2 anticipates virtually all subsequent commercial bipedal locomotion claims using ZMP. Honda's 1990s patent filings, many of which have now expired, form the deepest commercial prior art chain in the field.

## Honda P3 (1997-09)

- **id**: `honda-p3`
- **corpus**: private
- **creator**: Honda Motor Co.
- **disclosure**: Honda Motor Co. press materials, September 1997. Hirose, M. and Ogawa, K. Phil. Trans. R. Soc. A 365, 11–19 (2007).
- **ip status**: patented
- **prior art notes**: Final Honda P-series prototype before ASIMO. Refinements to the P2 architecture; key continuity in the Honda prior art chain.

## Goswami Foot Rotation Indicator (1999-12)

- **id**: `goswami-fri`
- **corpus**: academic
- **creator**: Ambarish Goswami, INRIA Rhône-Alpes (later Honda Research Institute)
- **disclosure**: Goswami, Ambarish. 'Postural stability of biped robots and the foot-rotation indicator (FRI) point.' International Journal of Robotics Research 18(6): 523-533, June 1999.
- **ip status**: public-domain
- **prior art notes**: Goswami's FRI is the canonical academic disclosure of an extended-ZMP stability indicator capable of quantifying impending foot-rotation. Anticipates: (1) graded stability metrics for bipedal walking that go beyond binary ZMP-inside/outside checks — relevant to claims on bipedal balance estimators in modern humanoids; (2) FRI as a continuous early-warning signal for tipping-onset — relevant to fall-prediction IP (every academic and commercial humanoid claiming 'fall prediction' or 'stability margin estimation' faces this); (3) the formal distinction between ZMP and FRI in non-quasi-static gaits — relevant to dynamic-walking control claims. Highly cited (>1000 citations); Goswami's later work at Honda Research Institute (Asimo group) extended this. 27-year-deep 102 anchor against bipedal-stability-monitoring IP.

## ASIMO (2000-10-31)

- **id**: `asimo`
- **corpus**: private
- **creator**: Honda Motor Co.
- **disclosure**: Honda Motor Co. press conference, Tokyo, October 31, 2000.
- **ip status**: patented
- **prior art notes**: ASIMO's public disclosures and Honda's published papers anticipate most claimed innovations in modern bipedal humanoids. The Hirose/Ogawa 2007 Phil. Trans. paper is a particularly comprehensive disclosure that should be referenced when reading current humanoid patent claims.

## Kajita Linear Inverted Pendulum Model (2001-10)

- **id**: `kajita-lipm`
- **corpus**: academic
- **creator**: Shuuji Kajita, Fumio Kanehiro, Kenji Kaneko, Kazuhito Yokoi, Hirohisa Hirukawa; AIST National Institute of Advanced Industrial Science and Technology, Japan
- **disclosure**: Kajita, Shuuji, Kanehiro, F., Kaneko, K., Yokoi, K., Hirukawa, H. 'The 3D Linear Inverted Pendulum Mode: A simple modeling for a biped walking pattern generation.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Maui HI, October 29-November 3, 2001: 239-246.
- **ip status**: public-domain
- **prior art notes**: Kajita's 3D-LIPM is the canonical academic disclosure of real-time humanoid walking pattern generation via reduced-order model. Anticipates: (1) the LIPM ẍ = (g/h)(x - p) reduction — directly relevant to claims on real-time bipedal pattern generation in essentially every academic and commercial humanoid since 2001 (HRP series, NAO, ASIMO derivatives, Atlas-class, Optimus, Figure 02 all use LIPM-derivative real-time planners); (2) preview-control-based ZMP tracking (Kajita-Kanehiro 2003 ICRA paper extending this) — relevant to model-predictive bipedal walking IP; (3) the constant-height constraint as a real-time-tractable simplification — relevant to humanoid walking-controller claims. Heavily cited (>4000 citations between LIPM 2001 and preview-control 2003 papers). Basis for the textbook Kajita et al. 'Introduction to Humanoid Robotics' (Springer 2014).

## HRP-2 (2002)

- **id**: `hrp-2`
- **corpus**: academic
- **creator**: AIST (National Institute of Advanced Industrial Science and Technology), Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Design of prototype humanoid robotics platform for HRP.' IROS 2002.
- **ip status**: open-permissive
- **prior art notes**: OpenHRP is itself foundational prior art for open robotics simulation frameworks. HRP-2 was among the first humanoids to publicly demonstrate falling-and-recovering behaviors.

## Sony QRIO (2003-03)

- **id**: `sony-qrio`
- **corpus**: private
- **creator**: Sony Corporation
- **disclosure**: Sony Corporation public reveal of QRIO, March 2003.
- **ip status**: patented
- **prior art notes**: QRIO's intelligent servo actuator architecture (embedded control in each joint module) is significant prior art for distributed-control humanoid actuator claims. Sony's now-expiring patents are a deep prior art well.

## HUBO (2004)

- **id**: `hubo`
- **corpus**: academic
- **creator**: KAIST, Hubo Lab (Jun-Ho Oh)
- **disclosure**: Park, Ill-Woo et al. 'Mechanical Design of Humanoid Robot Platform KHR-3 (HUBO).' IEEE-RAS Humanoids 2005.
- **ip status**: open-permissive
- **prior art notes**: DRC-Hubo's 2015 win demonstrated transformer-style transitioning between bipedal and wheeled-knee modes for navigating both stairs and flat ground. Anticipates: hybrid locomotion modes in humanoids.

## NAO (2006)

- **id**: `nao`
- **corpus**: private
- **creator**: Aldebaran Robotics (later SoftBank Robotics, then UBT)
- **disclosure**: Gouaillier, D. et al. 'Mechatronic design of NAO humanoid.' ICRA 2009.
- **ip status**: patented
- **prior art notes**: NAO's mechatronic design publication is well-cited prior art. The platform's wide academic distribution since 2006 makes its design choices broadly disclosed.

## WABIAN-2 (2006)

- **id**: `wabian-2`
- **corpus**: academic
- **creator**: Waseda University, Takanishi Laboratory
- **disclosure**: Ogura, Y. et al. 'Development of a New Humanoid Robot WABIAN-2.' ICRA 2006.
- **ip status**: open-permissive
- **prior art notes**: WABIAN-2's stretched-knee gait disclosure is significant prior art for any humanoid walking control claim aiming at more human-like locomotion (less crouched, more upright knees during stance). Distinct from ASIMO's bent-knee paradigm. The Takanishi laboratory's continued publication makes this a well-anchored academic disclosure.

## Capture Point (Pratt humanoid balance) (2006-12)

- **id**: `pratt-capture-point-2007`
- **corpus**: academic
- **creator**: IHMC + Honda Research Institute; Jerry Pratt + collaborators (Twan Koolen, Tomas de Boer, et al.)
- **disclosure**: Pratt, J., Carff, J., Drakunov, S., Goswami, A. 'Capture Point: A Step Toward Humanoid Push Recovery'. Humanoids 2006. Pratt, J., Koolen, T., de Boer, T., Rebula, J., Cotton, S., Carff, J., Johnson, M., Neuhaus, P. 'Capturability-Based Analysis and Control of Legged Locomotion'. International Journal of Robotics Research 31(9) 2012. IHMC (Florida Institute for Human and Machine Cognition) + Honda Research Institute.
- **ip status**: public-domain
- **prior art notes**: Capture Point (Pratt et al. Humanoids 2006, IJRR 2012) is the canonical academic humanoid balance / push-recovery framework. 19-year-deep public-domain prior art for: capture-point-based foot placement, dynamic-walking balance control beyond ZMP, push-recovery via reactive stepping. **Equivalent to Divergent Component of Motion (DCM)** which DLR + IHMC + Honda all use interchangeably in the academic literature. Together with Vukobratović ZMP (1969, in corpus), Raibert SLIP (1986, round-19), McGeer passive walker (1990, in corpus), Collins-Ruina passive (2005, round-19), establishes the **5-pillar foundational humanoid-locomotion-math chain spanning 1969-2007** (38 years of pure-academic development before any modern commercial humanoid). Direct shielding for any commercial humanoid claim on push-recovery, balance control, or capture-point-based gait planning.

## HRP-3 (2008)

- **id**: `hrp-3`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-3.' IROS 2008.
- **ip status**: open-permissive
- **prior art notes**: HRP-3's environmental sealing disclosures anticipate subsequent IP-rated humanoid claims. The HRP series is a deep commons asset because of consistent open academic disclosure across generations.

## Surena humanoid (Tehran University) (2008-12)

- **id**: `surena-tehran-university-2008`
- **corpus**: academic
- **creator**: Tehran University CAST + Iranian Ministry of Industry; Aghil Yousefi-Koma group
- **disclosure**: Tehran University Center of Advanced Systems and Technologies (CAST). Surena lineage: Surena (2008), Surena II (2010), Surena III (2015), Surena IV (December 2019). Yousefi-Koma, A. + Tehran University engineering team. Iran's flagship humanoid program.
- **ip status**: public-domain
- **prior art notes**: The Surena lineage (Tehran University CAST, 2008-2020+) is Iran's flagship humanoid program. 17-year-deep public-domain academic prior art (Iran does not enforce most foreign patents; Iranian academic publications are public-domain by default). Establishes Iranian indigenous capability under sanctions for: 170 cm / 68 kg adult-class bipedal humanoid, 43-DoF whole-body, anthropomorphic 5-finger hands. Closes the Iran/Middle-East regional gap (corpus had 0 entries from Iran prior to this round).

## DARwIn-OP (2010)

- **id**: `darwin-op`
- **corpus**: open
- **creator**: Robotis Co. with University of Pennsylvania, Virginia Tech, Purdue
- **disclosure**: Ha, I. et al. 'Development of Open Humanoid Platform DARwIn-OP.' SICE 2011.
- **ip status**: open-permissive
- **prior art notes**: DARwIn-OP is foundational prior art for fully-open small-scale humanoid platforms. Predates Poppy by several years for the academic-open category.

## HRP-4 (2010)

- **id**: `hrp-4`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-4: Humanoid Robotics Platform with Lightweight and Slim Body.' IROS 2010.
- **ip status**: open-permissive
- **prior art notes**: HRP-4 lightweight design anticipates subsequent slim-form humanoid claims. The 2010 IROS paper provides full mechanical specifications openly.

## REEM-C (2013)

- **id**: `reem-c`
- **corpus**: private
- **creator**: PAL Robotics
- **disclosure**: PAL Robotics REEM-C release, 2013.
- **ip status**: patented
- **prior art notes**: REEM-C distributed to multiple research labs; design characteristics openly published.

## Atlas academic publications (Kuindersma et al., DRC era) (2014-06)

- **id**: `atlas-academic-disclosures`
- **corpus**: academic
- **creator**: Scott Kuindersma, Russ Tedrake, Robin Deits, Maurice Fallon, Andrés Valenzuela, Hongkai Dai, Frank Permenter, Twan Koolen, Pat Marion; MIT CSAIL Robot Locomotion Group (DRC Atlas team)
- **disclosure**: Kuindersma, Scott; Permenter, Frank; Tedrake, Russ. 'An efficiently solvable quadratic program for stabilizing dynamic locomotion.' IEEE International Conference on Robotics and Automation (ICRA), Hong Kong, June 2014, pp. 2589-2594. DOI: 10.1109/ICRA.2014.6907230. Consolidated Atlas-on-DRC paper: Kuindersma, S.; Deits, R.; Fallon, M.; Valenzuela, A.; Dai, H.; Permenter, F.; Koolen, T.; Marion, P.; Tedrake, R. 'Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot.' Autonomous Robots 40(3): 429-455, March 2016. DOI: 10.1007/s10514-015-9479-3.
- **ip status**: public-domain
- **prior art notes**: The MIT DRC Atlas academic publication trail (Kuindersma-Tedrake et al. 2014-2016) is distinct from the Boston Dynamics Atlas product entry (atlas-boston-dynamics) and from the Sentis-Khatib WBOSC entry: it is the canonical academic disclosure of the actually-deployed Atlas controller stack as fielded at the DARPA Robotics Challenge Finals (June 2015). Anticipates with element-by-element specificity: (1) whole-body QP-based inverse-dynamics control on a hydraulically-actuated humanoid platform — directly relevant to commercial claims on QP-based humanoid IP (every modern humanoid runs a derivative); (2) the IRIS-regions mixed-integer convex footstep planner — relevant to claims on footstep-planning humanoid IP; (3) iterative SQP trajectory optimization with contact schedule — anticipates claims overlapping Crocoddyl (mastalli-crocoddyl-2020) and DDP approaches; (4) the consolidated end-to-end stack documentation in AURO 2016 — the most complete public disclosure of a working DRC-class humanoid control architecture. Drake source code accompanies the publications under BSD license. Modern QP-IDC-based humanoid IP filings face this 12-year-deep academic anchor with full implementation disclosure.

## DLR TORO (2014-07)

- **id**: `dlr-toro`
- **corpus**: academic
- **creator**: Englsberger, Werner, Ott, Henze, Roa, Garofalo, Burger, Beyer, Eiberger, Schmid, Albu-Schäffer; DLR Institute of Robotics and Mechatronics
- **disclosure**: Englsberger, J., Werner, A., Ott, C., Henze, B., Roa, M.A., Garofalo, G., Burger, R., Beyer, A., Eiberger, O., Schmid, K., Albu-Schäffer, A. 'Overview of the torque-controlled humanoid robot TORO'. IEEE-RAS Humanoids, July 2014.
- **ip status**: open-permissive
- **prior art notes**: TORO is the canonical academic disclosure of full-body torque-controlled bipedal humanoid with DCM (Divergent Component of Motion) walking control. Anticipates: (1) torque-controlled whole-body bipedal walking — directly relevant to claims on whole-body torque-controlled humanoid platforms; (2) DCM walking as an alternative to ZMP — relevant to walking-control IP; (3) impedance-control whole-body interaction with humans — relevant to safe-human-interaction humanoid claims. DLR's Englsberger paper introduced the DCM formulation that subsequent humanoids (HRP-5P, several private platforms) adopted. Publicly funded research with extensive IEEE-proceedings publication.

## UBTech Walker (2018-01)

- **id**: `ubtech-walker`
- **corpus**: private
- **creator**: UBTech Robotics
- **disclosure**: UBTech public reveal of Walker, CES January 2018.
- **ip status**: patented
- **prior art notes**: UBTech's bipedal locomotion claims anticipated by Honda P-series and ASIMO disclosures.

## Caltech CAST Hank bipedal platform (2019-05)

- **id**: `caltech-hank-cast-2019`
- **corpus**: academic
- **creator**: Aaron D. Ames and the Caltech AMBER Lab / CAST
- **disclosure**: Reher, Jenna and Ames, Aaron D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021; Csomay-Shanklin, Noel et al. 'Episodic Learning for Safe Bipedal Locomotion with Control Barrier Functions and Projection-to-State Safety.' L4DC 2021; CAST (Center for Autonomous Systems and Technologies) Caltech Hank reveal 2019.
- **ip status**: public-domain
- **prior art notes**: Hank is the Caltech CAST flagship humanoid biped of the late-2010s and is the canonical platform for HZD + CBF formal-method bipedal locomotion publications by the Ames group. It anticipates with full specificity: (1) claims on hybrid-zero-dynamics low-dimensional gait manifolds for humanoids — Reher-Ames ICRA 2021 publishes the formal HZD+ID-CLF-QP stack on Hank; (2) claims on control-barrier-function safety supervision for legged locomotion — Csomay-Shanklin L4DC 2021 publishes episodic CBF learning on Hank; (3) claims on quasi-direct-drive proprioceptive humanoid biped hardware — Hank's actuator topology predates and parallels Tesla Optimus and Apptronik Apollo public claims. All Hank publications are open-access with timestamped arXiv.

## Apptronik Apollo academic and technical disclosures (2023-2024) (2023-08)

- **id**: `apptronik-apollo-publications-2024`
- **corpus**: academic
- **creator**: Apptronik Inc. (Jeff Cardenas, Nick Paine, Luis Sentis lineage from UT Austin Human-Centered Robotics Lab)
- **disclosure**: Apptronik. 'Apollo: A Commercial Humanoid Robot for the Workforce.' Apptronik whitepaper, August 2023; Knabe, Coleman et al. 'Designing a Force-Controlled Linear Series Elastic Actuator.' (NASA Valkyrie / Apptronik lineage) IROS 2014; Apptronik-NASA JSC disclosures 2023-2024 including SAFFiR/Valkyrie genealogy white-papers.
- **ip status**: public-domain
- **prior art notes**: This entry isolates the academic-publication and technical-disclosure trail behind Apptronik Apollo (distinct from the Apollo product seed entry). It anticipates with full specificity: (1) claims on humanoid SEA actuator topology — Knabe-Paine et al. IROS 2014 publishes the linear-SEA design that lineally seeds Apollo; (2) claims on whole-body operational-space control for force-interactive humanoid manipulation — Sentis-Khatib WBOSC 2007/2010 papers (UT Austin lineage carried into Apptronik) are foundational and timestamped; (3) claims on hot-swap-battery torso integration with regenerative power electronics on humanoid platforms — Apollo whitepaper August 2023 discloses publicly. Modern humanoid commercial-platform IP claims to SEA torque control or WBOSC face this Apptronik publication trail at element-by-element specificity.
