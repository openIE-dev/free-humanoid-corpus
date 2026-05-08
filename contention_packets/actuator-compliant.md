---
title: "actuator-compliant"
parent: "Invalidity Contentions"
nav_order: 3
layout: default
---

# Invalidity Contention Packet — `actuator-compliant`

**Generated:** 2026-05-08  
**Cross-cut tag:** `actuator-compliant`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1957-01  
**Most recent disclosure:** 2017-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-compliant`.

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

### 1957-01 — McKibben pneumatic artificial muscle

- **id:** `mckibben-pneumatic-muscle-1957`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Joseph L. McKibben (NIH, Bethesda)
- **disclosure citation:** McKibben, J. L. (1957). Pneumatic artificial muscle developed at the National Institutes of Health for an orthotic device for polio patients. The original technical reports describe the braided-shell pneumatic actuator that contracts when pressurized. Subsequently extensively studied — Daerden + Lefeber 'Pneumatic Artificial Muscles: actuators for robotics and automation' European Journal of Mechanical and Environmental Engineering 47(1) 2002 is a canonical academic survey.
- **disclosed subsystems:** `actuator-pneumatic-muscle`, `actuator-compliant`

**Prior art notes:**

> The McKibben pneumatic artificial muscle is the canonical compliant-actuator foundation of soft robotics. 68-year-deep public-domain prior art (1957). The architectural parent of: Festo Fluidic Muscle (round-16 entry below), Shadow Robot Air Muscle, Pisa-IIT McKibben-actuated humanoid platforms (e.g., Walk-Man's compliant-joint design), Pneubotics. Direct shielding for any commercial humanoid claim on pneumatic-actuated compliant motion or biologically-mimetic actuator design. Particularly relevant if free-humanoid-platform pivots toward a soft-humanoid v0.2 variant — the pneumatic-actuator branch is well-anticipated.

**Sources:**

1. McKibben, J. L. NIH technical reports 1957.
2. Daerden, F., Lefeber, D. 'Pneumatic Artificial Muscles' EJMEE 47(1) 2002 — canonical academic survey.
3. Tondu, B. 'Modelling of the McKibben artificial muscle' J. Intelligent Material Systems 23(3) 2012.

---

### 2005-04 — Variable Stiffness Actuator (Tonietti VSA)

- **id:** `tonietti-vsa-pisa-iit-2005`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Pisa University + IIT (Italian Institute of Technology); Giovanni Tonietti, Riccardo Schiavi, Antonio Bicchi
- **disclosure citation:** Tonietti, G., Schiavi, R., Bicchi, A. 'Design and Control of a Variable Stiffness Actuator for Safe and Fast Physical Human/Robot Interaction'. ICRA 2005. Pisa-IIT (later: IIT-Pisa joint lab; antecedent of Pisa-IIT SoftHand corpus entry).
- **disclosed subsystems:** `actuator-variable-stiffness`, `actuator-compliant`, `actuator-electric-series-elastic`

**Prior art notes:**

> The Pisa-IIT Tonietti VSA (ICRA 2005) is the canonical academic variable-stiffness actuator. 20-year-deep public-domain prior art for: mechanically-adjustable joint compliance, two-motor co-control of position + stiffness. Architectural cousin of Pratt-Williamson SEA (corpus entry, 1995, fixed compliance). Direct ancestor of: DLR Hand-Arm System variable-impedance joints (corpus entry dlr-hand-arm-system-2011); EPFL spring-driven exoskeletons; modern compliant-actuator commercial products. Direct shielding for any commercial humanoid claim on real-time-adjustable compliance or variable-stiffness joint control.

**Sources:**

1. Tonietti et al. ICRA 2005 IEEE.
2. Bicchi group publications (Pisa-IIT centroaesp.unipi.it).

---

### 2017-04 — Festo BionicSoftArm

- **id:** `festo-bionic-soft-arm-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Festo AG (Esslingen, Germany)
- **disclosure citation:** Festo AG. BionicSoftArm and predecessor BionicMotionRobot product demonstrations 2017+. Festo's Bionic Learning Network public research program produces an annual demonstration platform; BionicSoftArm is the continuum-manipulator entry. Hannover Messe 2018 reveal.
- **disclosed subsystems:** `actuator-pneumatic-bellows`, `mechanism-continuum-manipulator`, `actuator-compliant`

**Prior art notes:**

> Festo BionicSoftArm is the canonical commercial continuum-manipulator demonstrator (Festo Bionic Learning Network 2017+). 8-year-deep public-disclosure prior art for: 12-bellows continuum manipulator, pneumatic-actuated soft commercial robot. Festo's Bionic Learning Network is itself a notable defensive-publication model — Festo demonstrates novel mechanisms publicly each year, establishing prior art across the bionic / soft-robotics space without filing patents. Direct shielding for any commercial humanoid claim on continuum-manipulator or bellows-actuated compliant arms.

**Sources:**

1. Festo AG corporate site (festo.com/group/en/cms/12747.htm).
2. Hannover Messe 2018 demonstration coverage.
3. Festo Bionic Learning Network annual reports.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b80ce5d`.*
