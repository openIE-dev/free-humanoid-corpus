---
title: mechanism-underactuated-grasping
parent: Cross-cuts
layout: default
---

# Cross-cut: `mechanism-underactuated-grasping`

**9 corpus entries disclose this subsystem.**

Earliest disclosure: 1986

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Mason Mechanics of Manipulation (1986)

- **id**: `mason-mechanics-manipulation`
- **corpus**: academic
- **creator**: Matthew T. Mason, Carnegie Mellon University Robotics Institute
- **disclosure**: Mason, Matthew T. 'Mechanics and planning of manipulator pushing operations.' International Journal of Robotics Research 5(3): 53-71, Fall 1986. Textbook consolidation: Mason, M.T. Mechanics of Robotic Manipulation. MIT Press, 2001. ISBN 0-262-13396-2.
- **ip status**: public-domain
- **prior art notes**: Mason's pushing-mechanics work and 2001 textbook are the canonical academic disclosure of nonprehensile manipulation analysis. Anticipates with mathematical specificity: (1) the limit-surface formalism for pushing/sliding contact — directly relevant to modern claims on contact-rich manipulation (every push-to-grasp policy in modern foundation-model papers grounds in this); (2) friction-cone-constrained quasi-static planning — relevant to claims on sliding manipulation; (3) action-primitive planning grounded in contact mechanics — relevant to skill-library robotics IP. Mason 2001 is the standard graduate-level textbook for manipulation and is heavily cited (>3000 citations across the program). Modern 'learn-to-push' or 'learn-to-slide' manipulation patents face this 40-year-deep academic anchor.

## Cornell Universal Jamming Gripper (2010-10-25)

- **id**: `cornell-jamming-gripper`
- **corpus**: academic
- **creator**: Eric Brown, Nicholas Rodenberg, John Amend, Annan Mozeika, Erik Steltz, Mitchell R. Zakin, Hod Lipson, Heinrich M. Jaeger; Cornell University and University of Chicago
- **disclosure**: Brown, E., Rodenberg, N., Amend, J., Mozeika, A., Steltz, E., Zakin, M.R., Lipson, H., Jaeger, H.M. 'Universal robotic gripper based on the jamming of granular material'. PNAS 107(44): 18809-18814, October 25, 2010.
- **ip status**: open-permissive
- **prior art notes**: The Cornell jamming gripper introduces granular-jamming as a fundamental new class of robotic gripper. Anticipates: (1) jamming-based universal grippers with single-DOF actuation — relevant to modern claims on universal/adaptive grippers; (2) the principle that compliance during approach and rigidity during grasp can be combined in a single deformable structure — relevant to compliant-grasp IP across the soft robotics field. The 2010 PNAS paper is one of the most-cited soft-robotics papers and has been licensed/extended by Empire Robotics (commercial spinoff) and many academic labs. Modern universal-gripper claims face this 2010 anchor.

## DLR Hand-Arm System (2011-05)

- **id**: `dlr-hand-arm-system-2011`
- **corpus**: academic
- **creator**: Markus Grebenstein, Alin Albu-Schäffer, Antonio Bicchi (collaboration), Gerd Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen
- **disclosure**: Grebenstein, Markus; Albu-Schäffer, Alin; Bahls, Thomas; Chalon, Maxime; Eiberger, Oliver; Friedl, Werner; Gruber, Robin; Haddadin, Sami; Hagn, Ulrich; Haslinger, Robert; Höppner, Hannes; Jörg, Stefan; Nickl, Mathias; Nothhelfer, Alexander; Petit, Florian; Reill, Josef; Seitz, Norbert; Wimböck, Thomas; Wolf, Sebastian; Wüsthoff, Tilo; Hirzinger, Gerd. 'The DLR Hand Arm System.' IEEE International Conference on Robotics and Automation (ICRA), Shanghai, May 2011, pp. 3175-3182. DOI: 10.1109/ICRA.2011.5980371. Companion thesis: Grebenstein, M. 'Approaching Human Performance: The Functionality-Driven Awiwi Robot Hand.' PhD thesis, ETH Zurich, 2012; published Springer Tracts in Advanced Robotics 98, 2014. ISBN 978-3-319-03592-9.
- **ip status**: public-domain
- **prior art notes**: The DLR Hand-Arm System (Grebenstein et al. ICRA 2011, Grebenstein PhD/STAR 2014) is the canonical academic disclosure of variable-impedance antagonistically-tendon-driven anthropomorphic hand-arm hardware. Anticipates with element-by-element mechanism-level specificity: (1) mechanically programmable variable joint stiffness via antagonistic tendons with nonlinear elastic elements — directly relevant to commercial claims on variable-stiffness humanoid hand IP; (2) the 19-DoF, 38-tendon, 38-motor architecture with motors in the forearm — relevant to claims on tendon-driven hand-with-forearm-actuation humanoid IP (Tesla Optimus Gen-3, Figure-02, Apptronik Apollo, Sanctuary Phoenix all show variations of this topology); (3) impact-survival via mechanical compliance absorption — anticipates claims on collision-tolerant humanoid hand IP; (4) the biomimetic muscle-tendon co-contraction analogue — relevant to claims on biomimetic humanoid manipulation. Grebenstein's PhD thesis (200+ pages) provides the deepest single-source mechanism disclosure in dexterous robotic hand history. Modern variable-impedance anthropomorphic hand IP filings face this 15-year-deep academic anchor with mechanical-drawing-level specificity.

## InMoov (2012)

- **id**: `inmoov`
- **corpus**: open
- **creator**: Gaël Langevin
- **disclosure**: Langevin, Gaël. InMoov project launch, 2012.
- **ip status**: open-permissive
- **prior art notes**: InMoov has been replicated globally thousands of times since 2012; the design is among the most-built humanoid platforms in history. Anticipates: 3D-printed tendon-driven anthropomorphic hands, modular humanoid construction.

## CMU HERB (Home Exploring Robotic Butler) (2012-04)

- **id**: `cmu-herb-srinivasa-2012`
- **corpus**: academic
- **creator**: Siddhartha Srinivasa et al., Carnegie Mellon Personal Robotics Lab / Intel Labs Pittsburgh
- **disclosure**: Srinivasa, Siddhartha S., Berenson, Dmitry, Cakmak, Maya, Collet, Alvaro, Dogar, Mehmet R., Dragan, Anca D., Knepper, Ross A., Niemueller, Tim, Strabala, Kyle, Vande Weghe, Mike, Ziegler, Julius. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE 100(8): 2410-2428, August 2012. Original disclosure: Srinivasa, S. et al. 'HERB: a home exploring robotic butler.' Autonomous Robots 28(1): 5-20, January 2010.
- **ip status**: public-domain
- **prior art notes**: CMU HERB is one of the most extensively-published academic mobile-manipulator humanoid platforms (>50 papers across 2008-2018). Anticipates with full specificity: (1) claims on home-environment dual-arm humanoid manipulation — HERB's headline contribution including kitchen/office task suite, fridge/microwave/dishwasher manipulation; (2) claims on legible/predictable HRI motion synthesis — Dragan-Srinivasa 2013 'Legibility and Predictability of Robot Motion' is part of the HERB program and anticipates current humanoid social-motion IP; (3) claims on cable-driven backdrivable arms with underactuated 3-finger hands for home manipulation — Barrett WAM + BH-280 are the explicit instantiation; (4) claims on manipulation-among-movable-obstacles planning. Proceedings of IEEE article and Autonomous Robots paper provide deeply-cited timestamped disclosure. Modern home-humanoid IP filings (1X NEO Gamma, Figure 02 home demos) face this 14-year-deep academic anchor.

## CMU Personal Robotics Lab Andy / HERB-2 follow-on platform (2014-05)

- **id**: `cmu-andy-herb2-srinivasa-2014`
- **corpus**: academic
- **creator**: Siddhartha Srinivasa, Anca Dragan, J. Andrew Bagnell, and the CMU Personal Robotics Lab
- **disclosure**: Srinivasa, Siddhartha S. et al. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE, vol. 100, no. 8, 2012; subsequent Andy disclosures: Dragan, Anca and Srinivasa, S. 'A Policy-Blending Formalism for Shared Control.' IJRR 32(7), 2013; Bagnell et al. CHIMP/Andy whole-body manipulation reports 2013-2015.
- **ip status**: public-domain
- **prior art notes**: The Andy / HERB-2 generation extends HERB-1 with formal shared-autonomy theory and is the survey-of-record for bimanual mobile-manipulator home robots in 2012-2015. It anticipates with full specificity: (1) claims on shared-autonomy arbitration between operator and policy — Dragan-Srinivasa policy-blending IJRR 2013 publishes the closed-form linear arbitration in confidence space; (2) claims on task-space-region constraint encoding for manipulation planning — Berenson-Srinivasa-Kuffner ICRA 2009 publishes TSR formalism executed on this platform; (3) claims on underactuated cable-driven grasping for unstructured pick-and-place — Barrett BH-280 deployment is the canonical published baseline. Modern humanoid manipulation IP claiming shared-autonomy or constraint-region planning faces these timestamped CMU disclosures.

## Yale OpenHand / ReFlex Hand (2014-05)

- **id**: `yale-reflex-openhand-2014`
- **corpus**: academic
- **creator**: Lael Odhner, Aaron Dollar, Robert Howe; Yale GRAB Lab and Harvard BioRobotics; with RightHand Robotics, Inc. as the commercial spinout (ReFlex SF/TakkTile)
- **disclosure**: Odhner, Lael U.; Jentoft, Leif P.; Claffee, Mark R.; Corson, Nicholas; Tenzer, Yaroslav; Ma, Raymond R.; Buehler, Martin; Kohout, Robert; Howe, Robert D.; Dollar, Aaron M. 'A compliant, underactuated hand for robust manipulation.' International Journal of Robotics Research, Volume 33, Issue 5, April 2014, pp. 736-752. DOI: 10.1177/0278364913514466. Yale OpenHand Project release: Ma, R. R. and Dollar, A. M. 'Yale OpenHand Project: Optimizing Open-Source Hand Designs for Ease of Fabrication and Adoption.' IEEE Robotics & Automation Magazine, Volume 24, Issue 1, March 2017, pp. 32-40. DOI: 10.1109/MRA.2016.2639034. Open-hardware repository at https://www.eng.yale.edu/grablab/openhand/.
- **ip status**: open-permissive
- **prior art notes**: Yale OpenHand / ReFlex SF (Odhner-Dollar et al. IJRR 2014; Yale OpenHand Project IEEE RAM 2017) is the canonical open-hardware academic disclosure of underactuated tendon-driven robust grasping hands. Anticipates with full open-hardware specificity: (1) the three-finger underactuated tendon-driven gripper with passive compliance — directly relevant to claims on simple-grasp humanoid end-effectors; (2) the open-hardware design release pattern (CAD files, BOMs, fabrication instructions) for robotic hands — relevant to claims on 3D-printable robotic hand IP (predates and anticipates many late-2010s and 2020s open-hardware hand patents); (3) the compliant-grasp-without-perception paradigm as an alternative to dexterous-perception-driven manipulation — relevant to claims on perception-light humanoid grasping; (4) integration of barometric tactile sensors (TakkTile) into a robot hand — relevant to claims on humanoid tactile fingertip IP. Yale GRAB Lab has continuous publication record on underactuated hands since the early 2000s; the 2014 IJRR consolidates the design canon. Modern open-hardware humanoid hand IP filings face this 12-year-deep open-source academic anchor.

## Pisa-IIT SoftHand (2014-11-03)

- **id**: `pisa-iit-softhand`
- **corpus**: academic
- **creator**: Catalano, Grioli, Farnioli, Serio, Piazza, Bicchi; Centro 'E. Piaggio', Università di Pisa, and Italian Institute of Technology
- **disclosure**: Catalano, M.G., Grioli, G., Farnioli, E., Serio, A., Piazza, C., Bicchi, A. 'Adaptive synergies for the design and control of the Pisa/IIT SoftHand'. International Journal of Robotics Research 33(5): 768-782, November 3, 2014.
- **ip status**: open-permissive
- **prior art notes**: The Pisa-IIT SoftHand is the canonical academic disclosure of synergistic underactuated anthropomorphic hands. Anticipates: (1) the use of human-derived postural synergies (specifically the 'first synergy' from PCA on human grasping kinematics) as the actuation pattern for an anthropomorphic robot hand — directly relevant to modern claims on synergy-driven hand IP; (2) reducing 19 DOFs to a single motor via tendon-coupling — relevant to underactuated humanoid hand patents. Bicchi's group has extensive prior art back to the 1990s on underactuated grasping; the SoftHand 2014 paper is the consolidated reference. Heavily cited; commercial extensions exist (qb robotics).

## Pisa-IIT SoftHand 2 (2018-09)

- **id**: `pisa-iit-softhand-2`
- **corpus**: academic
- **creator**: Cosimo Della Santina, Cristina Piazza, Giorgio Grioli, Manuel G. Catalano, Antonio Bicchi; Centro 'E. Piaggio', Università di Pisa, and Italian Institute of Technology (IIT)
- **disclosure**: Della Santina, Cosimo; Piazza, Cristina; Grioli, Giorgio; Catalano, Manuel G.; Bicchi, Antonio. 'Toward Dexterous Manipulation With Augmented Adaptive Synergies: The Pisa/IIT SoftHand 2.' IEEE Transactions on Robotics, Volume 34, Issue 5, October 2018, pp. 1141-1156. DOI: 10.1109/TRO.2018.2830407. First public disclosure as a conference work in earlier 2017 venues; the consolidated T-RO paper is the canonical reference.
- **ip status**: open-permissive
- **prior art notes**: Pisa-IIT SoftHand 2 (Della Santina et al. T-RO 2018) is the canonical academic disclosure of multi-synergy augmented underactuated anthropomorphic hands, extending the 2014 SoftHand from one synergy to two. Anticipates with element-by-element specificity: (1) the augmented multi-synergy actuation pattern that enables 19-DoF hand operation with 2 motors and provides in-hand manipulation capability — directly relevant to claims on low-motor-count dexterous humanoid hand IP (Tesla Optimus claimed motor-counts in the 11-22 range, Figure-02 hand counts similar; the SoftHand 2 paradigm anticipates the underactuation-with-manipulation-capability angle of those claims); (2) the formal extension of synergy theory from grasping (one synergy) to grasping-plus-manipulation (two synergies) — relevant to claims on synergy-based humanoid manipulation IP; (3) compliant passive shape adaptation eliminating perception-driven grasp planning — relevant to claims on perception-light humanoid grasping IP. Heavily cited (>200); consolidates Bicchi-group underactuation lineage from the 1990s. Modern multi-synergy underactuated humanoid hand IP filings face this 8-year-deep academic anchor.
