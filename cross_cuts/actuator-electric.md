---
title: actuator-electric
parent: Cross-cuts
layout: default
---

# Cross-cut: `actuator-electric`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 2016-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Boston Dynamics SpotMini (2016-06)

- **id**: `boston-dynamics-spotmini-2017`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: Boston Dynamics. SpotMini public reveal June 2016 demo video; subsequent IEEE Spectrum coverage 2017-2018; capability demonstrations via Boston Dynamics YouTube. Discontinued in favor of Spot (the production quadruped) circa 2019.
- **ip status**: trade-secret
- **prior art notes**: SpotMini is the architectural predecessor to commercial Spot. ~9-year-deep public-disclosure prior art for: all-electric quadruped morphology (distinct from hydraulic BigDog/Spot ancestors), dorsal-mount manipulator on quadruped base, Velodyne+depth-camera quadruped sensor stack. Trade-secret control software, public capability surface. Direct shielding for any commercial humanoid-quadruped or quadruped-manipulator claim. Cited in cheetah-cub-epfl and black-mirror-metalhead-2017 prior_art_notes; round-14 backfill closes those citation chains.

## Hello Robot Stretch (2020-07)

- **id**: `hello-robot-stretch-2020`
- **corpus**: private
- **creator**: Hello Robot, Inc.; Charles Kemp + Aaron Edsinger
- **disclosure**: Hello Robot, Inc. 'Stretch: A Versatile Mobile Manipulator'. Public reveal July 2020 via hello-robot.com. Founded by Charles Kemp (Georgia Tech Healthcare Robotics Lab spinout) and Aaron Edsinger. Subsequent product generations: Stretch RE1 (2020), RE2 (2021), Stretch 3 (2024). Used as the deployment platform in LEGS (round-15 entry legs-berkeley-2024) and many other academic mobile-manipulation projects.
- **ip status**: trade-secret
- **prior art notes**: Hello Robot Stretch is the canonical sub-\$25k educational mobile manipulator (2020). 5-year-deep public-disclosure prior art with 100+ academic publications using Stretch as the deployment platform. Direct shielding for any commercial mobile-manipulator claim at the educational price point or with the telescoping-mast architectural pattern. Notably **the Berkeley LEGS round-15 entry deployed on Stretch** — the round-15 entry's prior_art_notes implicitly reference Stretch as the platform; round-17 now resolves that reference. Architecturally distinct from humanoid-form mobile manipulators (Apptronik, Figure, Optimus): Stretch is single-arm + mast + wheels, not bipedal + bimanual.

## Astribot S1 (2024-04)

- **id**: `astribot-s1-stardust-2025`
- **corpus**: private
- **creator**: Stardust Intelligence (Shenzhen, China)
- **disclosure**: Stardust Intelligence (Shenzhen, China; founded December 2022). Astribot S1 reveal April 2024 via stardust-tech.com / astribot.com demo videos showing 10 m/s arm motion. Stardust Intelligence Astribot Suite paper July 2025 (peer-reviewed; teleop + DuoCore-WB imitation learning achieving 80% task success). Commercial availability late 2025+ in China.
- **ip status**: trade-secret
- **prior art notes**: Astribot S1 is one of the canonical 2024-2025 Chinese commercial humanoid platforms (Stardust Intelligence). 1.5-year-deep public-disclosure prior art for: ≥10 m/s anthropomorphic arm motion (claimed industry-leading), 36-DoF whole-body humanoid, DuoCore-WB whole-body IL framework. Direct shielding for any commercial humanoid claim on extreme arm-speed performance — Astribot's April 2024 viral demo set the public benchmark. Claim surface is peer-reviewed (Astribot Suite paper July 2025), unlike most Chinese commercial humanoid platforms.

## Atlas Electric (Boston Dynamics) (2024-04)

- **id**: `boston-dynamics-atlas-electric-2024`
- **corpus**: private
- **creator**: Boston Dynamics (Hyundai subsidiary since 2021)
- **disclosure**: Boston Dynamics. 'An Electric New Era for Atlas' announcement April 17 2024 via boston-dynamics.com (replacing the hydraulic Atlas, which retired April 16 2024). Subsequent capability demonstrations 2024-2025 including Hyundai factory deployment preparation. Trade-secret commercial humanoid platform.
- **ip status**: trade-secret
- **prior art notes**: Atlas Electric is Boston Dynamics' canonical 2024+ commercial all-electric humanoid (succeeding the 11-year hydraulic Atlas lineage). 1.5-year-deep public-disclosure prior art for: super-human range-of-motion humanoid joint design, all-electric humanoid form factor at compact mass. Public capability surface (viral demo videos) is fully covered by deeper academic prior art chains: HRP-2/HRP-4/HRP-5P (full-size humanoid lineage); Berkeley Humanoid + ToddlerBot (round-11, all-electric humanoid); the Hwangbo ANYmal sim-to-real lineage for the RL training substrate. **Specific super-human-ROM joint kinematics** are the architectural distinction; corpus has Salisbury / DLR / Pisa-IIT joint mechanism prior art back to 1982 for kinematic ranges that exceed standard anthropomorphic humanoids.

## Galbot (2024-09)

- **id**: `galbot-galaxy-robotics-2024`
- **corpus**: private
- **creator**: Galaxy Robotics (Beijing, China)
- **disclosure**: Galaxy Robotics (Beijing, China). Galbot platform reveal 2024 via galaxy-robotics.com / WAIC 2024 demonstration. Wheeled humanoid with telescoping torso lift + dual 7-DoF arms. ~CNY 500k initial commercial price.
- **ip status**: trade-secret
- **prior art notes**: Galbot is the canonical 2024 Chinese wheeled-humanoid commercial platform (Galaxy Robotics). 1.5-year-deep public-disclosure prior art for: telescoping-torso wheeled humanoid commercial deployment, dual-arm wheeled mobile manipulator at the educational-to-commercial price tier. Architectural sibling of Hello Robot Stretch (round-17 entry) but with humanoid-form dual-arm + telescoping-torso vs. Stretch's single-arm + mast. Direct shielding for any commercial humanoid claim on wheeled-humanoid (non-bipedal) form factor with telescoping vertical adjustment. **Directly relevant to free-humanoid-wheeled** — Galbot is the closest commercial product to that morphology.

## Booster K1 (2025-03)

- **id**: `booster-k1-2025`
- **corpus**: private
- **creator**: Booster Robotics (Beijing, China)
- **disclosure**: Booster Robotics. K1 product page (booster.tech/booster-k1) and associated commercial brochures, public 2025+. RoboCup 2025 KidSize humanoid league winning platform (Boosted HTWK team, Salvador Brazil, July 20 2025).
- **ip status**: trade-secret
- **prior art notes**: Booster K1 is the canonical 2025 sub-$25k educational humanoid. 5-month-deep public-disclosure prior art for: KidSize-class (95cm) humanoid form factor, 22-DoF anthropomorphic kinematics, ROS 2 + Python developer-friendly stack at the educational price point. Public competition record (RoboCup 2025 KidSize win) demonstrates a working system. Direct shielding for any commercial humanoid claim on educational/sub-$25k pricing or RoboCup-competition-grade autonomous bipedal locomotion.

## Booster T1 (2025-09)

- **id**: `booster-t1-2025`
- **corpus**: private
- **creator**: Booster Robotics (Beijing, China)
- **disclosure**: Booster Robotics. T1 product reveal Q3 2025 via booster.tech. Successor to K1 (round-16 entry booster-k1-2025) with adult-class form factor.
- **ip status**: trade-secret
- **prior art notes**: Booster T1 is Booster Robotics' adult-class commercial humanoid (2025+). 8-month-deep public-disclosure prior art at the time of this corpus entry. Inherits from K1 (round-16) the ROS 2 + Python developer-friendly stack pattern. Direct shielding for Booster's commercial product line as a coherent multi-platform humanoid family (KidSize K1 + AdultSize T1).

## Tesla Optimus Gen 3 (2025-10)

- **id**: `tesla-optimus-gen3-2025`
- **corpus**: private
- **creator**: Tesla, Inc.
- **disclosure**: Tesla, Inc. Optimus Gen 3 product disclosures via Tesla AI Day-class demonstrations + product page (tesla.com/we-robot) + Optimus blog/social-media posts October 2025+. Trade-secret commercial humanoid platform.
- **ip status**: trade-secret
- **prior art notes**: Tesla Optimus Gen 3 is the dominant commercial humanoid product claim surface. Public-disclosure surface (Tesla product page + demos + social-media + investor decks) discloses dimensional specs and high-level architecture; withholds actuator architecture, specific neural-network policies, training-data composition, and on-device inference details. **The 22-DoF hand × 50-actuator claim is the most specific architectural claim** and directly engages prior-art chains in the corpus: Shadow Hand (24-DoF), DLR Hand-II (15-DoF), Pisa-IIT SoftHand (synergy reduction), Tactile SoftHand-A (antagonistic tendons + tactile fingertips, round-11 entry — directly anticipates the tactile-fingertip delicate-manipulation claim), Educational SoftHand-A (round-12 entry — clutch-gear synergy mechanism). Modern claims on tactile-fingertip dexterous manipulation face 2-year-deep tactile-softhand-a prior art and the deeper SoftHand chain back to 2014. Vision-only sensing is shielded by Tesla's own FSD patents (which Tesla cannot use offensively against an own-lineage humanoid claim) but separately by Levine's GPS PR2/BRETT (2016) for vision-driven manipulation. The full Optimus Gen 3 claim surface is therefore element-by-element anticipated by deep open academic chains plus prior commercial humanoids in the corpus.
