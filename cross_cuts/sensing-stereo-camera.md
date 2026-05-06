---
title: sensing-stereo-camera
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-stereo-camera`

**61 corpus entries disclose this subsystem.**

Earliest disclosure: 1973

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## WABOT-1 (1973)

- **id**: `wabot-1`
- **corpus**: academic
- **creator**: Waseda University, Kato Laboratory
- **disclosure**: Kato, Ichiro et al. 'Information-Power Machine with Senses and Limbs (WABOT-1).' Proceedings of First CISM-IFToMM Symposium on Theory and Practice of Robots and Manipulators, 1973.
- **ip status**: public-domain
- **prior art notes**: First full-scale humanoid in academic record. Anticipates virtually every subsystem of modern humanoids at concept level: bipedal locomotion, bimanual manipulation, multimodal sensing, natural language interface. Specific implementations are crude by modern standards but the architectural decomposition is foundational.

## RoboCop (Alex Murphy) (1987-07-17)

- **id**: `robocop-1987`
- **corpus**: fictional
- **creator**: Paul Verhoeven; Edward Neumeier and Michael Miner (writers); Omni Consumer Products (in-fiction)
- **disclosure**: Verhoeven, Paul (dir.); Neumeier, Edward and Miner, Michael (writers). RoboCop. Orion Pictures, July 17, 1987.
- **ip status**: fictional
- **prior art notes**: RoboCop's Prime Directives architecture is a foundational fictional disclosure of *enumerated, prioritized, hard-constraint safety supervisors with disclosed backdoors*. Anticipates with notable specificity: (1) explicit prioritized list of safety directives operating as hard constraints — relevant to modern Simplex/CBF/RTA-style safety supervisor IP; (2) the *failure mode* of operator-installed backdoors in safety supervisors (Directive 4 prevents arrest of OCP senior staff) — directly relevant to claims on tamper-resistant safety policies; this is the single most prescient pre-2010 fictional disclosure of the alignment-failure modes that modern safety-supervisor IP attempts to address; (3) integrated armed humanoid for civic deployment — relevant to law-enforcement humanoid IP. Continuously available since 1987; the Prime Directives sequence is widely cited in safety-architecture pedagogy.

## ALVINN (Autonomous Land Vehicle in a Neural Network) (1989)

- **id**: `pomerleau-alvinn`
- **corpus**: academic
- **creator**: Dean Pomerleau; Carnegie Mellon University Robotics Institute
- **disclosure**: Pomerleau, Dean A. 'ALVINN: An Autonomous Land Vehicle in a Neural Network'. NIPS 1988 (December 1988); published in Touretzky, D.S. (ed.), Advances in Neural Information Processing Systems 1: 305-313, Morgan Kaufmann, 1989.
- **ip status**: public-domain
- **prior art notes**: Pomerleau's ALVINN is the foundational academic disclosure of end-to-end vision-to-action neural network policies — the architectural pattern that modern VLA models implement at scale. Anticipates: (1) end-to-end vision-to-action neural policy as a deployable control architecture — directly relevant to RT-1, RT-2, OpenVLA, Octo, and every subsequent foundation-model-policy claim; (2) training data augmentation via simulated variation — relevant to sim-to-real claims; (3) deploying neural policies on real-world hardware — relevant to deployment-on-robot patents. The 1989 NIPS paper and subsequent CMU technical reports establish the lineage that culminates in modern VLA systems. Modern VLA claims face this 35-year academic anchor as 102 prior art.

## Robonaut 1 (1996)

- **id**: `robonaut-1`
- **corpus**: academic
- **creator**: Robert O. Ambrose, Myron A. Diftler, et al.; NASA Johnson Space Center, with DARPA
- **disclosure**: Diftler, M.A., Ambrose, R.O. 'Robonaut: A Robotic Astronaut Assistant'. International Symposium on Artificial Intelligence, Robotics and Automation in Space (i-SAIRAS) 2001 (consolidated paper); earlier disclosures NASA JSC 1996 onwards.
- **ip status**: public-domain
- **prior art notes**: Robonaut 1 is the academic predecessor to Robonaut 2 and the deepest NASA-side disclosure of humanoid platform IP for space applications. Anticipates: (1) torso-only humanoid form factor for collaborative work with humans — relevant to current commercial torso-only humanoid claims; (2) VR teleoperation with force-feedback gloves as the operator interface — relevant to teleoperation IP; (3) tendon-driven anthropomorphic hands integrated with harmonic-drive arms — relevant to integrated-hand-arm claims. NASA JSC publications and i-SAIRAS proceedings are publicly accessible. Modern humanoid hand claims face this 1996 academic anchor.

## Sony AIBO (1999-05-11)

- **id**: `sony-aibo`
- **corpus**: private
- **creator**: Sony Corporation
- **disclosure**: Sony Corporation announcement of AIBO ERS-110, May 11, 1999.
- **ip status**: patented
- **prior art notes**: AIBO is foundational prior art for consumer quadruped robots. Sony's 1990s-2000s patents cover quadruped behavior architecture, learning systems, and small-form-factor actuators. Many expired or near expiration.

## ASIMO (2000-10-31)

- **id**: `asimo`
- **corpus**: private
- **creator**: Honda Motor Co.
- **disclosure**: Honda Motor Co. press conference, Tokyo, October 31, 2000.
- **ip status**: patented
- **prior art notes**: ASIMO's public disclosures and Honda's published papers anticipate most claimed innovations in modern bipedal humanoids. The Hirose/Ogawa 2007 Phil. Trans. paper is a particularly comprehensive disclosure that should be referenced when reading current humanoid patent claims.

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

## Toyota Partner Robot (Violin) (2007)

- **id**: `toyota-partner-robot-violin`
- **corpus**: private
- **creator**: Toyota Motor Corporation Partner Robot Division
- **disclosure**: Toyota Motor Corporation public reveal, 2007.
- **ip status**: patented
- **prior art notes**: Toyota's high-precision finger control disclosures are significant prior art for fine motor control humanoid claims.

## iCub (2008)

- **id**: `icub`
- **corpus**: academic
- **creator**: Italian Institute of Technology (IIT) and the RobotCub Consortium
- **disclosure**: Metta, G. et al. 'The iCub humanoid robot: an open platform for research in embodied cognition.' PerMIS 2008.
- **ip status**: open-permissive
- **prior art notes**: Among the earliest fully open-source humanoid platforms with hardware design released. Anticipates: tendon-driven anthropomorphic hands, full-body artificial skin, open robotics middleware.

## HRP-3 (2008)

- **id**: `hrp-3`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-3.' IROS 2008.
- **ip status**: open-permissive
- **prior art notes**: HRP-3's environmental sealing disclosures anticipate subsequent IP-rated humanoid claims. The HRP series is a deep commons asset because of consistent open academic disclosure across generations.

## Willow Garage PR1 (2008)

- **id**: `willow-pr1`
- **corpus**: academic
- **creator**: Willow Garage / Stanford (Ken Salisbury group)
- **disclosure**: Wyrobek, K.A. et al. 'Towards a Personal Robotics Development Platform: Rationale and Design of an Intrinsically Safe Personal Robot.' ICRA 2008.
- **ip status**: open-permissive
- **prior art notes**: PR1 is significant prior art for safety-by-design humanoid robotics. Cable-driven intrinsically-safe architecture anticipates several modern compliant-actuator humanoid claims.

## DLR Justin (Rollin' Justin) (2009-05)

- **id**: `dlr-justin`
- **corpus**: academic
- **creator**: Borst, Wimboeck, Schmidt, Fuchs, Brunner, Zacharias, Giordano, Konietschke, Sepp, Fuchs, Rink, Albu-Schäffer, Hirzinger; DLR Institute of Robotics and Mechatronics
- **disclosure**: Borst, C., Wimboeck, T., Schmidt, F., Fuchs, M., Brunner, B., Zacharias, F., Giordano, P. R., Konietschke, R., Sepp, W., Fuchs, S., Rink, C., Albu-Schäffer, A., Hirzinger, G. 'Rollin' Justin — Mobile platform with variable base'. IEEE ICRA, May 2009.
- **ip status**: open-permissive
- **prior art notes**: Justin is the canonical academic disclosure of wheeled humanoid mobile manipulation with full impedance control. Anticipates and provides extensive prior art for: (1) wheeled humanoid platform for service tasks — relevant to claims on wheeled humanoid IP (Diligent Moxi, NEXTAGE follow this paradigm); (2) torque-controlled dual-arm coordination — relevant to bimanual humanoid manipulation IP; (3) variable-wheelbase mobile base — relevant to morphology-changing wheeled platform claims. DLR has published Justin disclosures in ICRA, IROS, Humanoids continuously since 2009. Modern wheeled humanoid claims face this deep academic anchor.

## DARwIn-OP (2010)

- **id**: `darwin-op`
- **corpus**: open
- **creator**: Robotis Co. with University of Pennsylvania, Virginia Tech, Purdue
- **disclosure**: Ha, I. et al. 'Development of Open Humanoid Platform DARwIn-OP.' SICE 2011.
- **ip status**: open-permissive
- **prior art notes**: DARwIn-OP is foundational prior art for fully-open small-scale humanoid platforms. Predates Poppy by several years for the academic-open category.

## PR2 (2010)

- **id**: `pr2`
- **corpus**: open
- **creator**: Willow Garage
- **disclosure**: Willow Garage. PR2 platform release, 2010.
- **ip status**: open-permissive
- **prior art notes**: PR2 was the platform around which ROS was originally built. Its hardware is significant prior art for omnidirectional wheeled mobile manipulation. ROS itself is even more significant prior art for robotics middleware.

## HRP-4 (2010)

- **id**: `hrp-4`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-4: Humanoid Robotics Platform with Lightweight and Slim Body.' IROS 2010.
- **ip status**: open-permissive
- **prior art notes**: HRP-4 lightweight design anticipates subsequent slim-form humanoid claims. The 2010 IROS paper provides full mechanical specifications openly.

## Robonaut 2 (2010-02)

- **id**: `robonaut-2`
- **corpus**: academic
- **creator**: NASA Johnson Space Center, in partnership with General Motors
- **disclosure**: Diftler, M.A. et al. 'Robonaut 2 — The First Humanoid Robot in Space.' ICRA 2011.
- **ip status**: patented
- **prior art notes**: Robonaut 2's hand design, with 12 DoF per hand and tendon routing through the forearm, is foundational prior art for high-DoF tendon-driven humanoid hands. The NASA-GM patent portfolio has been extensively cited.

## Toyota HSR (2012)

- **id**: `toyota-hsr`
- **corpus**: private
- **creator**: Toyota Motor Corporation Partner Robot Division
- **disclosure**: Yamamoto, T. et al. 'Development of Human Support Robot as the research platform of a domestic mobile manipulator.' ROBOMECH Journal 6:4, 2019. Earlier 2012 disclosure.
- **ip status**: patented
- **prior art notes**: HSR's telescoping torso with whole-body control is significant prior art for domestic-context wheeled humanoid claims.

## NASA Valkyrie (2013)

- **id**: `nasa-valkyrie`
- **corpus**: academic
- **creator**: NASA Johnson Space Center, in collaboration with University of Texas at Austin and others
- **disclosure**: NASA Johnson Space Center, DARPA Robotics Challenge entry, 2013.
- **ip status**: open-permissive
- **prior art notes**: NASA Valkyrie's series-elastic actuator implementations and the IHMC-derived whole-body control work are foundational prior art. The robot was distributed to multiple universities and produced extensive open publications.

## REEM-C (2013)

- **id**: `reem-c`
- **corpus**: private
- **creator**: PAL Robotics
- **disclosure**: PAL Robotics REEM-C release, 2013.
- **ip status**: patented
- **prior art notes**: REEM-C distributed to multiple research labs; design characteristics openly published.

## Atlas (2013-07)

- **id**: `atlas-boston-dynamics`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: DARPA press release, July 2013, announcing Atlas as DRC platform.
- **ip status**: patented
- **prior art notes**: Boston Dynamics' patents are among the most-cited in the humanoid space and also among the most likely to be challenged on 102/103 grounds given the long academic prior art chain (Honda, AIST, KAIST, MIT). Worth dedicated patent-by-patent analysis.

## Poppy Humanoid (2014)

- **id**: `poppy-humanoid`
- **corpus**: open
- **creator**: Inria Flowers Team / Poppy Project
- **disclosure**: Lapeyre, Matthieu et al. 'Poppy Humanoid Platform: Experimental Evaluation of the Role of a Bio-inspired Thigh Shape.' IEEE Humanoids 2013.
- **ip status**: open-permissive
- **prior art notes**: Among the earliest fully-open 3D-printable humanoids. Anticipates open-source educational humanoid platforms broadly.

## Pepper (2014-06)

- **id**: `pepper-softbank`
- **corpus**: private
- **creator**: SoftBank Robotics (formerly Aldebaran)
- **disclosure**: SoftBank Robotics public reveal of Pepper, June 2014.
- **ip status**: patented
- **prior art notes**: Pepper is foundational prior art for wheeled-base humanoid social robots. The omnidirectional wheeled base design has been widely cited.

## Boston Dynamics Spot (2015-02)

- **id**: `hyundai-boston-dynamics-spot`
- **corpus**: private
- **creator**: Boston Dynamics (now Hyundai Motor Group subsidiary)
- **disclosure**: Boston Dynamics public reveal of Spot, February 2015.
- **ip status**: patented
- **prior art notes**: Spot is the most commercially deployed quadruped robot. BD's Spot patents face deep prior art from MIT Cheetah series, ANYmal lineage, and academic quadruped literature.

## ANYmal (2016)

- **id**: `anymal`
- **corpus**: private
- **creator**: ANYbotics, ETH Zurich Robotic Systems Lab
- **disclosure**: Hutter, M. et al. 'ANYmal — a highly mobile and dynamic quadrupedal robot.' IROS 2016.
- **ip status**: patented
- **prior art notes**: ANYbotics SEA design heavily anticipated by NASA Valkyrie and Robonaut SEA work. ETH RSL academic publications provide open prior art for many control claims.

## Sophia (2016-04)

- **id**: `hanson-sophia`
- **corpus**: private
- **creator**: Hanson Robotics
- **disclosure**: Hanson Robotics public reveal of Sophia, April 2016.
- **ip status**: patented
- **prior art notes**: Hanson's Frubber synthetic skin material and facial actuation prior art is significant for any claim around expressive humanoid faces. Disney Imagineering's earlier work is the deeper prior art.

## PAL TALOS (2017)

- **id**: `pal-talos`
- **corpus**: private
- **creator**: PAL Robotics, in collaboration with LAAS-CNRS
- **disclosure**: Stasse, O. et al. 'TALOS: A new humanoid research platform targeted for industrial applications.' IEEE Humanoids 2017.
- **ip status**: patented
- **prior art notes**: TALOS is among the better-published European industrial humanoids. Stasse 2017 IEEE Humanoids paper provides comprehensive design disclosure.

## Toyota T-HR3 (2017-11)

- **id**: `toyota-thr3`
- **corpus**: private
- **creator**: Toyota Motor Corporation Partner Robot Division
- **disclosure**: Toyota Motor Corporation public reveal, November 2017.
- **ip status**: patented
- **prior art notes**: T-HR3 is significant prior art for whole-body teleoperated humanoids with force feedback. The Master Maneuvering System teleoperation interface anticipates many modern humanoid teleop claims.

## Kawasaki Kaleido (2017-11)

- **id**: `kawasaki-kaleido`
- **corpus**: private
- **creator**: Kawasaki Heavy Industries
- **disclosure**: Kawasaki Heavy Industries public reveal of Kaleido, iREX November 2017.
- **ip status**: patented
- **prior art notes**: Kawasaki's deep industrial robotics IP base means much of their humanoid claims are anticipated by their own prior industrial robotics disclosures, plus AIST HRP series prior art.

## Ghost Robotics Vision 60 (2018)

- **id**: `ghost-robotics-vision-60`
- **corpus**: private
- **creator**: Ghost Robotics
- **disclosure**: Ghost Robotics Vision 60 release, 2018.
- **ip status**: patented
- **prior art notes**: Ghost Robotics derives from Penn's Kod*lab academic quadruped work. The legged-robot patents face the same MIT Cheetah / ANYmal / Penn Kod*lab prior art chain as other quadrupeds.

## UBTech Walker (2018-01)

- **id**: `ubtech-walker`
- **corpus**: private
- **creator**: UBTech Robotics
- **disclosure**: UBTech public reveal of Walker, CES January 2018.
- **ip status**: patented
- **prior art notes**: UBTech's bipedal locomotion claims anticipated by Honda P-series and ASIMO disclosures.

## HRP-5P (2018-09)

- **id**: `hrp-5p`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-5P: An Electrically Actuated Humanoid Robot With High-Power and Wide-Range Joints.' IEEE Robotics and Automation Letters 4(2), 2019.
- **ip status**: open-permissive
- **prior art notes**: HRP-5P's construction-task demonstrations and high-power actuator disclosures are among the most thoroughly published examples of humanoid construction work. Anticipates many subsequent industrial humanoid claims.

## Digit (2019-01)

- **id**: `agility-digit`
- **corpus**: private
- **creator**: Agility Robotics
- **disclosure**: Agility Robotics public reveal, CES January 2019.
- **ip status**: patented
- **prior art notes**: Cassie/Digit derive from Oregon State University academic work (Hurst lab); the academic publications constitute substantial prior art for the bipedal control claims.

## Diligent Moxi (2019-09)

- **id**: `diligent-moxi`
- **corpus**: private
- **creator**: Diligent Robotics
- **disclosure**: Diligent Robotics public reveal of Moxi, September 2019.
- **ip status**: patented
- **prior art notes**: Diligent's claims around mobile manipulation in healthcare environments face extensive prior art from PR2, HSR, and academic mobile manipulation literature.

## Reachy (2020)

- **id**: `reachy`
- **corpus**: open
- **creator**: Pollen Robotics
- **disclosure**: Pollen Robotics. Reachy public release, 2020.
- **ip status**: open-permissive
- **prior art notes**: Reachy's Orbita 3-DoF spherical actuator is novel-ish but anticipated by extensive academic spherical-motor literature. Open hardware files constitute prior art for the specific implementation.

## Boston Dynamics Spot (fuel-cell variant) (2020)

- **id**: `spot-fuel-cell`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: Boston Dynamics partnership announcements with fuel cell vendors, 2020.
- **ip status**: patented
- **prior art notes**: Demonstrates fuel-cell-powered legged robotics at commercial scale. Anticipates fuel-cell power claims in field robotics applications.

## Tesla Optimus (2021-08-19)

- **id**: `tesla-optimus`
- **corpus**: private
- **creator**: Tesla, Inc.
- **disclosure**: Tesla AI Day 1, August 19, 2021, Palo Alto.
- **ip status**: patented
- **prior art notes**: Tesla's claims around vision-only humanoid perception are heavily anticipated by academic vision-based humanoid work. Actuator IP claims should be examined against Honda harmonic drive prior art.

## Ameca (2021-12)

- **id**: `ameca`
- **corpus**: private
- **creator**: Engineered Arts
- **disclosure**: Engineered Arts public reveal, December 2021.
- **ip status**: patented
- **prior art notes**: Engineered Arts' animatronic facial expression IP is heavily anticipated by Disney Imagineering work and by academic facial-animation robotics.

## Sanctuary Phoenix Gen 6 (2022)

- **id**: `sanctuary-phoenix-gen6`
- **corpus**: private
- **creator**: Sanctuary AI
- **disclosure**: Sanctuary AI public reveals of Phoenix predecessors, 2020-2022.
- **ip status**: patented
- **prior art notes**: Sanctuary's hybrid hydraulic-electric actuation faces extensive prior art from Boston Dynamics Atlas (hydraulic), Honda (electric), and academic hybrid actuation literature.

## RT-1 (Robotics Transformer 1) (2022-12-13)

- **id**: `rt-1`
- **corpus**: academic
- **creator**: Google Robotics (Brohan et al.)
- **disclosure**: Brohan, Anthony et al. 'RT-1: Robotics Transformer for Real-World Control at Scale.' arXiv:2212.06817, December 13, 2022. Authors: Brohan, A., Brown, N., Carbajal, J., Chebotar, Y., Dabis, J., Finn, C., Gopalakrishnan, K., Hausman, K., Herzog, A., Hsu, J., Ibarz, J., Ichter, B., Irpan, A., Jackson, T., Jesmonth, S., Joshi, N.J., Julian, R., Kalashnikov, D., Kuang, Y., Leal, I., Lee, K-H., Levine, S., Lu, Y., Malla, U., Manjunath, D., Mordatch, I., Nachum, O., Parada, C., Peralta, J., Perez, E., Pertsch, K., Quiambao, J., Rao, K., Ryoo, M., Salazar, G., Sanketi, P., Sayed, K., Singh, J., Sontakke, S., Stewart, A., Tan, J., Tompson, J., Vanhoucke, V., Vuong, Q., Wahid, A., Welker, S., Wohlhart, P., Wu, J., Xia, F., Xiao, T., Xu, P., Xu, S., Yu, T., Zitkovich, B. (Google).
- **ip status**: open-permissive
- **prior art notes**: RT-1 is the foundational academic disclosure of large-scale Transformer-based vision-language-action policy for real robot control, predating RT-2 (2023) and OpenVLA (2024). Anticipates with full architectural specificity: (1) tokenized action space for cross-task transformer policies — directly relevant to claims on action-tokenization in modern VLAs (Tesla Optimus, Figure 02, 1X NEO, Physical Intelligence π-zero all employ derivatives); (2) language-conditioned manipulation policy with multi-image history — relevant to instruction-following manipulation IP; (3) the data-scaling law showing performance vs. dataset size for robot policies — relevant to claims on data-driven policy training. Code and data partially released under permissive licenses; arXiv preprint available since December 2022. Brohan et al. paper foundational for the entire VLA lineage.

## Sanctuary AI Phoenix (2023-05)

- **id**: `sanctuary-phoenix`
- **corpus**: private
- **creator**: Sanctuary AI
- **disclosure**: Sanctuary AI public reveal, May 2023.
- **ip status**: patented
- **prior art notes**: Sanctuary's high-DoF hand claims face Shadow Hand (2003) and iCub (2008) as deep prior art for tendon-driven anthropomorphic hands with high finger DoF.

## Fourier GR-1 (2023-07)

- **id**: `fourier-gr1`
- **corpus**: private
- **creator**: Fourier Intelligence
- **disclosure**: Fourier Intelligence public reveal of GR-1, July 2023, World AI Conference Shanghai.
- **ip status**: patented
- **prior art notes**: Fourier transitions from rehabilitation exoskeletons to humanoids; actuator IP from exoskeleton work potentially anticipates some humanoid actuator claims by other companies.

## Unitree H1 (2023-08)

- **id**: `unitree-h1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics public reveal, August 2023.
- **ip status**: patented
- **prior art notes**: Unitree's actuator IP largely derives from quadruped work (Go1, Aliengo) which is itself heavily anticipated by MIT Mini Cheetah QDD lineage.

## Apptronik Apollo (2023-08)

- **id**: `apptronik-apollo`
- **corpus**: private
- **creator**: Apptronik
- **disclosure**: Apptronik public reveal of Apollo, August 2023.
- **ip status**: patented
- **prior art notes**: Apptronik's actuator IP has lineage from UT Austin Human-Centered Robotics Lab (Sentis) and from NASA Valkyrie work; both sources constitute substantial prior art that limits the patentable surface area of Apptronik's own claims.

## AgiBot A1 (2023-08)

- **id**: `agibot-a1`
- **corpus**: private
- **creator**: AgiBot (Shanghai Zhiyuan New Technology Co.)
- **disclosure**: AgiBot (Shanghai Zhiyuan New Technology) public reveal, August 2023.
- **ip status**: patented
- **prior art notes**: AgiBot's actuator IP heavily anticipated by Honda P-series harmonic drive work and MIT Cheetah QDD lineage. Chinese-language patent filings should be enumerated in strengthening pass.

## Figure 01 (2023-10)

- **id**: `figure-01`
- **corpus**: private
- **creator**: Figure AI
- **disclosure**: Figure AI public reveal, October 2023.
- **ip status**: patented
- **prior art notes**: Figure's claimed innovations in electric humanoid actuation are heavily anticipated by Honda's E-series and ASIMO publications, by KAIST HUBO papers, and by the entire academic literature.

## LimX Dynamics CL-1 (2023-12)

- **id**: `limx-cl1`
- **corpus**: private
- **creator**: LimX Dynamics
- **disclosure**: LimX Dynamics public reveal, December 2023.
- **ip status**: patented
- **prior art notes**: LimX QDD actuation derives from MIT Cheetah lineage; bipedal control claims anticipated by Cassie/ATRIAS work.

## 1X NEO (2024)

- **id**: `1x-neo`
- **corpus**: private
- **creator**: 1X Technologies (formerly Halodi Robotics)
- **disclosure**: 1X Technologies public reveal, 2024.
- **ip status**: patented
- **prior art notes**: Tendon-driven compliant actuation is heavily anticipated by iCub, by Shadow Robot Hand work, and by decades of academic compliant-actuation literature.

## K-Scale Labs Open Source Humanoid (2024)

- **id**: `k-scale-os`
- **corpus**: open
- **creator**: K-Scale Labs
- **disclosure**: K-Scale Labs project launch, 2024.
- **ip status**: open-permissive
- **prior art notes**: Among the most ambitious recent fully-open humanoid efforts. Direct peer to Free Humanoid in scope.

## Berkeley Humanoid (2024)

- **id**: `berkeley-humanoid`
- **corpus**: academic
- **creator**: UC Berkeley, Hybrid Robotics Lab
- **disclosure**: Liao, Q. et al. 'Berkeley Humanoid: A Research Platform for Learning-based Control.' arXiv 2024.
- **ip status**: open-permissive
- **prior art notes**: Berkeley quasi-direct-drive lineage (predates the humanoid; comes from the Mini Cheetah / leg work) anticipates many actuator architecture claims.

## Persona AI Mentee (2024)

- **id**: `persona-ai-mentee`
- **corpus**: private
- **creator**: Persona AI
- **disclosure**: Persona AI public reveal, 2024.
- **ip status**: trade-secret
- **prior art notes**: Public technical disclosure is thin; strengthening pass needed.

## Universal Manipulation Interface (UMI) (2024-02-15)

- **id**: `umi-stanford`
- **corpus**: academic
- **creator**: Stanford + TRI + Columbia (Chi, Xu, Pan, Cousineau, Burchfiel, Feng, Tedrake, Song)
- **disclosure**: Chi, Cheng, Xu, Zhenjia, Pan, Chuer, Cousineau, Eric, Burchfiel, Benjamin, Feng, Siyuan, Tedrake, Russ, Song, Shuran. 'Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots.' arXiv:2402.10329, February 15, 2024. Robotics: Science and Systems (RSS) 2024. Stanford University + Toyota Research Institute + Columbia University.
- **ip status**: open-permissive
- **prior art notes**: UMI is the canonical academic disclosure of embodiment-decoupled manipulation data collection via hand-held wrist-camera devices. Anticipates: (1) data collection with a portable hand-held gripper-replica without the robot present — directly relevant to claims on low-cost humanoid data collection (this paradigm is now used by Stanford ALOHA's portable variants, Tesla operator-glove proposals, several other commercial programs); (2) wrist-camera SLAM as the substrate for trajectory reconstruction — relevant to vision-based teleoperation IP; (3) embodiment-matching gripper geometry between collection rig and deployment robot — relevant to claims on cross-embodiment manipulation training. Open-source hardware (3D print files), software, and data under permissive license. Modern humanoid 'in-the-wild data' patent claims face this 2-year-deep anchor with full DIY-buildable defensibility.

## Rainbow Robotics RB-Y1 (2024-03)

- **id**: `rainbow-robotics-rb-y1`
- **corpus**: private
- **creator**: Rainbow Robotics
- **disclosure**: Rainbow Robotics public reveal of RB-Y1, March 2024.
- **ip status**: patented
- **prior art notes**: Rainbow Robotics has direct lineage from KAIST HUBO program; HUBO academic publications constitute prior art for many of their humanoid claims.

## DROID Dataset (2024-03-19)

- **id**: `droid-dataset`
- **corpus**: academic
- **creator**: DROID Consortium (Khazatsky et al., 18 academic + industry institutions)
- **disclosure**: Khazatsky, Alexander et al. 'DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset.' arXiv:2403.12945, March 19, 2024. Robotics: Science and Systems (RSS) 2024. Authors: Khazatsky, A., Pertsch, K., Nair, S., Balakrishna, A., Dasari, S., Karamcheti, S., Nasiriany, S., Srirama, M.K., Chen, L.Y., Ellis, K., Fagan, P.D., Hejna, J., Itkina, M., Lepert, M., Ma, Y.J., Miller, P.T., Wu, J., Belkhale, S., Dass, S., Ha, H., Jain, A., Lee, A., Lee, Y., Memmel, M., Park, S., Radosavovic, I., Wang, K., Zhan, A., Black, K., Chi, C., Hatch, K.B., Lin, S., Lu, J., Mercat, J., Rehman, A., Sanketi, P.R., Sharma, A., Simpson, C., Vuong, Q., Walke, H.R., Wulfe, B., Xiao, T., Yang, J.H., Yavary, A., Zhao, T.Z., Agia, C., Baijal, R., Castro, M.G., Chen, D., Chen, Q., Chung, T., Drake, J., Foster, E.P., Gao, J., Garcia Herrera, D.A., Heo, M., Hsu, K., Hu, J., Jackson, D., Le, C., Li, Y., Lin, K., Lin, R., Ma, Z., Maddukuri, A., Mirchandani, S., Morton, D., Nguyen, T., O'Neill, A., Scalise, R., Seale, D., Son, V., Tian, S., Tran, E., Wang, A.E., Wu, Y., Xie, A., Yang, J., Yin, P., Zhang, Y., Bastani, O., Berseth, G., Bohg, J., Goldberg, K., Gupta, A., Gupta, A., Jayaraman, D., Lim, J.J., Malik, J., Martín-Martín, R., Ramamoorthy, S., Sadigh, D., Song, S., Wu, J., Yip, M.C., Zhu, Y., Kollar, T., Levine, S., Finn, C. (Stanford / Berkeley / TRI / GoogleDeepMind / 18-institution academic consortium).
- **ip status**: open-permissive
- **prior art notes**: DROID is the canonical academic disclosure of large-scale standardized robot manipulation data collection across diverse environments. Anticipates: (1) standardized hardware-stack-based data collection at multi-institutional scale — directly relevant to claims on 'data-flywheel' humanoid programs (Tesla Optimus operator floor, Figure data pipeline, 1X data-collection program); (2) teleoperated demonstration data as the substrate for VLA training — relevant to claims on imitation-learning-based humanoid IP; (3) the open data + open hardware spec combination — establishes prior art for any 'standardized fleet for robot data' patent claim. Released under permissive license (CC-BY 4.0 for data); 76k trajectories, 564 scenes, full hardware spec. Modern humanoid data-collection patent claims face this 2-year-deep anchor.

## Neura 4NE-1 (2024-05)

- **id**: `neura-4ne1`
- **corpus**: private
- **creator**: Neura Robotics
- **disclosure**: Neura Robotics public reveal of 4NE-1, May 2024.
- **ip status**: patented
- **prior art notes**: Neura's cognitive-AI claims overlap with academic VLA literature.

## Kepler K2 (2024-07)

- **id**: `kepler-k2`
- **corpus**: private
- **creator**: Kepler Exploration Robotics
- **disclosure**: Kepler Exploration Robotics public reveal, July 2024.
- **ip status**: patented
- **prior art notes**: Kepler's planetary-reducer actuator claims are anticipated by extensive prior art in industrial robotics planetary-gearing literature.

## Figure 02 (2024-08)

- **id**: `figure-02`
- **corpus**: private
- **creator**: Figure AI
- **disclosure**: Figure AI public reveal of Figure 02, August 2024.
- **ip status**: patented
- **prior art notes**: Figure 02 actuator and hand claims are heavily anticipated by Honda P-series, Robonaut 2, Shadow Hand, and iCub work. The 16-DoF hand is in the same design space as Robonaut 2's 12-DoF and Sanctuary's 21-DoF.

## Robot Era STAR1 (2024-10)

- **id**: `robot-era-star1`
- **corpus**: private
- **creator**: Robot Era
- **disclosure**: Robot Era public reveal of STAR1, October 2024.
- **ip status**: patented
- **prior art notes**: Bipedal running speed claims anticipated by Cassie's Guinness record work.

## XPeng Iron (2024-11)

- **id**: `xpeng-iron`
- **corpus**: private
- **creator**: XPeng Motors (Robotics division)
- **disclosure**: XPeng AeroHT and XPeng Robotics reveal, November 2024.
- **ip status**: patented
- **prior art notes**: XPeng's leveraging of automotive ML stack for humanoid perception is heavily anticipated by Tesla Optimus's same approach (which is itself anticipated by academic vision-based humanoid work).
