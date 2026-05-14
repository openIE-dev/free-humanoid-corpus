---
title: "mechanism-soft-pneumatic-gripper"
parent: "Invalidity Contentions"
nav_order: 221
layout: default
---

# Invalidity Contention Packet — `mechanism-soft-pneumatic-gripper`

**Generated:** 2026-05-14  
**Cross-cut tag:** `mechanism-soft-pneumatic-gripper`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2014-04  
**Most recent disclosure:** 2017-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-soft-pneumatic-gripper`.

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

### 2014-04 — Soft Robotics Inc mGrip food-handling gripper

- **id:** `soft-robotics-mgrip-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Soft Robotics Inc. (Bedford, MA, USA); Harvard / Whitesides-group spinout; Carl Vause CEO
- **disclosure citation:** Soft Robotics Inc. (Bedford, MA, USA). Founded 2013 by Carl Vause + Harvard / Whitesides-group spinout. mGrip elastomer soft-gripper product line 2014+. FDA / USDA / 3A-compliant materials for food handling. Asset acquisition by J. Schmalz GmbH August 2024 (Soft Robotics Inc. wound down).
- **disclosed subsystems:** `mechanism-soft-pneumatic-gripper`, `mechanism-elastomer-finger`, `actuator-pneumatic`

**Prior art notes:**

> Soft Robotics Inc. mGrip (Bedford MA 2014-2024; assets to Schmalz 2024) is the defining commercial soft-elastomer food-handling gripper. 11-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from pneumatic-elastomer finger-array grippers, FDA-grade soft food-handling end-effectors, or Whitesides-lineage soft-robotics commercial deployment. Lineage descends from Harvard Soft Robotics Toolkit (corpus harvard-soft-robotics-toolkit-2017) and McKibben pneumatic muscle (corpus mckibben-pneumatic-muscle-1957).

**Sources:**

1. businesswire.com/news/home/20240807157208 (Schmalz acquires mGrip).
2. Soft Robotics Inc. corporate site (historical).

---

### 2014-07 — RBO Hand 2 (TU Berlin Brock)

- **id:** `rbo-hand-2-brock-tu-berlin-2014`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** TU Berlin Robotics and Biology Laboratory (RBO); Raphael Deimel + Oliver Brock
- **disclosure citation:** Deimel, R., Brock, O. 'A novel type of compliant, underactuated robotic hand for dexterous grasping'. Robotics: Science and Systems (RSS) 2014. Extended journal version: International Journal of Robotics Research 35(1-3), 2016. TU Berlin Robotics and Biology Laboratory (RBO) under Oliver Brock.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-soft-pneumatic-gripper`, `actuator-pneumatic`

**Prior art notes:**

> RBO Hand 2 (Deimel + Brock TU Berlin RSS 2014, IJRR 2016) is the canonical soft-pneumatic anthropomorphic hand. 11-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from soft-pneumatic anthropomorphic hands or fiber-reinforced silicone-rubber actuator hands. Lineage descends from McKibben pneumatic muscle (corpus mckibben-pneumatic-muscle-1957) and Pisa-IIT SoftHand (corpus pisa-iit-softhand).

**Sources:**

1. Deimel, R. + Brock, O. RSS 2014.
2. Deimel, R. + Brock, O. IJRR 35(1-3), 2016.
3. static.tu.berlin/fileadmin/www/10002220/Research/publications/Puhlmann__Harris__Brock_-_RBO_Hand_3_A_Platform_for_Soft_Dexterous_Manipulation.pdf (RBO Hand 3 follow-on)

---

### 2017-04 — Festo OctopusGripper continuum bionic gripper

- **id:** `festo-octopus-gripper-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Festo AG & Co. KG Bionic Learning Network (Esslingen, Germany)
- **disclosure citation:** Festo AG & Co. KG Bionic Learning Network (Esslingen, Germany). OctopusGripper reveal Hannover Messe April 2017. Soft pneumatic silicone tentacle inspired by octopus tentacle morphology. Sister product to FlexShapeGripper (2015) and MultiChoiceGripper (2014) in the Festo Bionic Learning Network gripper portfolio.
- **disclosed subsystems:** `mechanism-continuum-manipulator`, `mechanism-soft-pneumatic-gripper`, `mechanism-suction-cup-array`, `actuator-pneumatic`

**Prior art notes:**

> Festo OctopusGripper (Festo Esslingen 2017) is the defining bionic continuum-tentacle gripper. 8-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from continuum-tentacle end-effectors, octopus-inspired soft grippers, or pneumatic suction-cup-array tentacle hybrids. Sister entries to festo-bionic-soft-arm-2017 (corpus) and festo-finray-fingripper-2009 (round-42).

**Sources:**

1. newatlas.com/festo-octopusgripper-details/48721/
2. festo.com/us/en/e/about-festo/research-and-development/bionic-learning-network/

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4abb724`.*
