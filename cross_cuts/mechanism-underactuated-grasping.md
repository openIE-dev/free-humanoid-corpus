---
title: mechanism-underactuated-grasping
parent: Cross-cuts
layout: default
---

# Cross-cut: `mechanism-underactuated-grasping`

**6 corpus entries disclose this subsystem.**

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

## Pisa-IIT SoftHand (2014-11-03)

- **id**: `pisa-iit-softhand`
- **corpus**: academic
- **creator**: Catalano, Grioli, Farnioli, Serio, Piazza, Bicchi; Centro 'E. Piaggio', Università di Pisa, and Italian Institute of Technology
- **disclosure**: Catalano, M.G., Grioli, G., Farnioli, E., Serio, A., Piazza, C., Bicchi, A. 'Adaptive synergies for the design and control of the Pisa/IIT SoftHand'. International Journal of Robotics Research 33(5): 768-782, November 3, 2014.
- **ip status**: open-permissive
- **prior art notes**: The Pisa-IIT SoftHand is the canonical academic disclosure of synergistic underactuated anthropomorphic hands. Anticipates: (1) the use of human-derived postural synergies (specifically the 'first synergy' from PCA on human grasping kinematics) as the actuation pattern for an anthropomorphic robot hand — directly relevant to modern claims on synergy-driven hand IP; (2) reducing 19 DOFs to a single motor via tendon-coupling — relevant to underactuated humanoid hand patents. Bicchi's group has extensive prior art back to the 1990s on underactuated grasping; the SoftHand 2014 paper is the consolidated reference. Heavily cited; commercial extensions exist (qb robotics).
