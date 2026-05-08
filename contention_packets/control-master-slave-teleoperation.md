---
title: "control-master-slave-teleoperation"
parent: "Invalidity Contentions"
nav_order: 58
layout: default
---

# Invalidity Contention Packet — `control-master-slave-teleoperation`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-master-slave-teleoperation`  
**Entries:** 6 (5 commons-grade, 1 draft)  
**Earliest disclosure:** 1989-01  
**Most recent disclosure:** 2021-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-master-slave-teleoperation`.

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

### 1989-01 — Taylor JHU surgical robotics (foundational) *(draft)*

- **id:** `taylor-jhu-surgical-robotics-1990s`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** JHU Computer Integrated Surgery Lab; Russell Taylor + collaborators
- **disclosure citation:** Taylor, R. H. et al. 'Robotic technology in surgery: past, present, and future'. American Journal of Surgery 188(4) 2004 (survey); foundational papers from 1989+: 'A Telerobotic Assistant for Laparoscopic Surgery' IEEE EMBC 1995; 'Steady-Hand robotic system for microsurgical augmentation' IJRR 1999. Johns Hopkins University Computer Integrated Surgery Lab. Russell Taylor + collaborators (Marcel Brett, Allison Okamura, Peter Kazanzides).
- **disclosed subsystems:** `mechanism-manipulator-arm`, `control-cooperative-control`, `control-master-slave-teleoperation`, `mechanism-surgical-robot`

**Prior art notes:**

> Russell Taylor's JHU CISST academic surgical robotics program (1989+) is the foundational academic counterpart to commercial surgical robotics (Intuitive Surgical da Vinci, Vicarious Surgical, Memic Hominis — all round-16 entries). 36-year-deep public-domain academic prior art for: cooperative-control surgical augmentation, master-slave surgical teleoperation, robotic orthopedic bone-cutting. ROBODOC (FDA 2008 / European 1992) and AESOP (Taylor co-developed) predate Intuitive Surgical da Vinci (FDA 2000) by years. Direct shielding for any commercial humanoid claim that derives from surgical-robot manipulator architectures. **Together with Salisbury Stanford-JPL hand (1982), establishes the two foundational academic lineages underpinning all modern surgical-and-humanoid manipulator IP.**

**Sources:**

1. Taylor, R. H. American Journal of Surgery 188(4) 2004.
2. JHU LCSR Computer Integrated Surgery Lab (cisst.org).
3. Taylor, R. H. + Stoianovici 'Medical robotics in computer-integrated surgery' IEEE T-RA 2003.

---

### 2000-07 — Intuitive Surgical da Vinci

- **id:** `intuitive-surgical-da-vinci-2000`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Intuitive Surgical, Inc.; SRI International + Stanford JPL Salisbury lineage roots
- **disclosure citation:** Intuitive Surgical, Inc. (Sunnyvale, CA). da Vinci Surgical System FDA approval July 11, 2000. SRI International / Stanford telesurgical lineage; Salisbury Stanford-JPL hand era roots. Subsequent product generations: da Vinci S (2006), Si (2009), Xi (2014), X (2017), SP single-port (2018), Ion bronchoscopy (2019), da Vinci 5 (2024).
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-tendon-driven`, `mechanism-wristed-instrument`, `control-master-slave-teleoperation`, `control-tremor-filtering`, `sensing-stereoscopic-camera`

**Prior art notes:**

> The Intuitive Surgical da Vinci system is the canonical commercial surgical-robot platform (FDA approval July 2000). 25-year-deep public-disclosure prior art for: master-slave teleoperated manipulator + console architecture, EndoWrist tendon-driven wristed-instrument design (architecturally descended from Salisbury's Stanford-JPL hand 1982 — corpus entry `salisbury-stanford-jpl-hand-1982`), tremor filtering + motion scaling for telerobotic precision. Direct shielding for any commercial humanoid claim on bimanual fine-manipulation with wristed end-effectors and tremor-filtered teleoperation. The 25-year commercial deployment + 7,500+ systems + 10M+ procedures establishes a deeply-anticipated prior-art cushion for any humanoid manipulation claim.

**Sources:**

1. Intuitive Surgical corporate site (intuitive.com).
2. FDA premarket approval (PMA) database, da Vinci System (P000004).
3. Wikipedia 'Da Vinci Surgical System'.

---

### 2007-08 — Hansen Medical Sensei catheter robotic system

- **id:** `sensei-hansen-medical-2009`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Hansen Medical (Mountain View, CA); now Auris Health / Johnson & Johnson
- **disclosure citation:** Hansen Medical, Inc. (Mountain View, CA). Sensei catheter robotic system FDA cleared August 2007. Subsequent: Magellan vascular system. Acquired by Auris Health 2016 → Johnson & Johnson 2019.
- **disclosed subsystems:** `mechanism-surgical-robot`, `mechanism-catheter-robot`, `control-master-slave-teleoperation`

**Prior art notes:**

> Hansen Medical Sensei (FDA cleared August 2007) is the canonical robotic catheter system for cardiac electrophysiology. 18-year-deep public-disclosure prior art. Distinct architectural branch from Intuitive da Vinci by application + kinematics. The Hansen→Auris→J&J lineage is the major intravascular robotic-surgery commercial platform.

**Sources:**

1. Hansen Medical / Auris Health / Johnson & Johnson corporate history.
2. FDA 510(k) Sensei clearance 2007.

---

### 2012-07 — CorPath GRX (Corindus / Siemens Healthineers)

- **id:** `corpath-grx-corindus-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Corindus Vascular Robotics (Waltham, MA); acquired by Siemens Healthineers 2019
- **disclosure citation:** Corindus Vascular Robotics, Inc. CorPath 200 FDA cleared July 2012; CorPath GRX FDA cleared October 2016. Acquired by Siemens Healthineers 2019.
- **disclosed subsystems:** `mechanism-surgical-robot`, `mechanism-catheter-robot`, `control-master-slave-teleoperation`

**Prior art notes:**

> Corindus CorPath GRX (FDA 2012/2016, Siemens Healthineers 2019) is the canonical robotic-PCI commercial platform. 13-year-deep public-disclosure prior art. Together with Hansen Medical Sensei (round-33 entry above), establishes the intravascular surgical-robot prior-art chain.

**Sources:**

1. Corindus / Siemens Healthineers corporate history.
2. FDA 510(k) CorPath 200 clearance 2012; CorPath GRX 2016.

---

### 2014-04 — Skybot F-850 / FEDOR

- **id:** `skybot-fedor-russia-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Roscosmos + NPO Android Technics (Magnitogorsk, Russia); also Russian Foundation for Advanced Research Projects
- **disclosure citation:** Roscosmos + NPO Android Technics (Russia). FEDOR (Final Experimental Demonstration Object Research) humanoid robot project announced 2014. Skybot F-850 variant launched to International Space Station August 22 2019 aboard Soyuz MS-14, uncrewed test mission; spent 16 days at ISS performing supervised tasks before returning to Earth September 7 2019. Subsequent FEDOR work continues at Magnitogorsk-based NPO Android Technics.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `control-master-slave-teleoperation`, `control-cabin-environment`

**Prior art notes:**

> Skybot F-850 / FEDOR is the canonical Russian humanoid robotics platform (2014+; ISS deployment 2019). 11-year-deep public-disclosure prior art for: ISS-deployable humanoid (second after NASA Robonaut 2), 180 cm / 160 kg anthropomorphic with bimanual tool-use, exoskeleton-glove master-slave teleoperation. Direct shielding for any commercial humanoid claim on space-deployable humanoid form factor. Closes the Russian regional gap — corpus previously had only 1 RU-tagged entry.

**Sources:**

1. Roscosmos public statements 2014-2019.
2. NPO Android Technics corporate page (npo-at.com).
3. Soyuz MS-14 mission documentation.
4. Wikipedia 'Skybot F-850' (en.wikipedia.org/wiki/Skybot_F-850).

---

### 2021-03 — Memic Hominis

- **id:** `memic-hominis-2020`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Memic Innovative Surgery / Momentis Surgical (Israel)
- **disclosure citation:** Memic Innovative Surgery, Ltd. (Tel Aviv, Israel; now Momentis Surgical). FDA De Novo authorization March 1 2021 for transvaginal hysterectomy and salpingectomy/oophorectomy. memicmed.com / momentissurgical.com.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `control-master-slave-teleoperation`

**Prior art notes:**

> Memic Hominis (FDA De Novo March 2021) is a canonical anthropomorphic-arm-kinematics surgical robotic system. 4-year-deep public-disclosure prior art for: humanoid-style (shoulder+elbow+wrist) surgical-arm kinematics, natural-orifice robotic surgery. Direct shielding for any commercial humanoid claim on anthropomorphic-arm-derivative surgical applications or natural-orifice manipulation. Together with da Vinci and Vicarious Surgical, establishes a 25-year commercial robotic-surgery prior-art chain that anticipates humanoid-form manipulator architectures from a different industrial vertical.

**Sources:**

1. Memic Innovative Surgery (memicmed.com / momentissurgical.com).
2. FDA De Novo authorization (DEN200067) March 1 2021.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `a27a0cf`.*
