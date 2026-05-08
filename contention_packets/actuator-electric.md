---
title: "actuator-electric"
parent: "Invalidity Contentions"
nav_order: 4
layout: default
---

# Invalidity Contention Packet — `actuator-electric`

**Generated:** 2026-05-08  
**Cross-cut tag:** `actuator-electric`  
**Entries:** 11 (7 commons-grade, 4 draft)  
**Earliest disclosure:** 2016-06  
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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf892af`.*
