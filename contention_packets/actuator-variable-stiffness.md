---
title: "actuator-variable-stiffness"
parent: "Invalidity Contentions"
nav_order: 22
layout: default
---

# Invalidity Contention Packet — `actuator-variable-stiffness`

**Generated:** 2026-05-12  
**Cross-cut tag:** `actuator-variable-stiffness`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2005-04  
**Most recent disclosure:** 2015-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-variable-stiffness`.

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

### 2015-06 — IIT WALK-MAN + R1 personal humanoid (Italy)

- **id:** `iit-walk-man-r1-italy-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Istituto Italiano di Tecnologia (IIT, Genoa); Nikos Tsagarakis + Darwin Caldwell groups
- **disclosure citation:** Istituto Italiano di Tecnologia (IIT), Genoa, Italy. WALK-MAN humanoid reveal June 2015 for DARPA Robotics Challenge competition (5th place). Subsequent: COMAN+ (Compliant Humanoid), **R1 personal humanoid** (2017-2020) targeted at home + service applications. iit.it. Tsagarakis + Caldwell + Bicchi groups.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `actuator-electric-series-elastic`, `actuator-variable-stiffness`

**Prior art notes:**

> IIT WALK-MAN + R1 are the canonical Italian academic humanoid platforms (IIT Genoa, 2015-2020+). 10-year-deep public-domain prior art for: SEA + VSA-actuated compliant whole-body humanoid, personal humanoid form factor (130cm/50kg/sub-€30k), DARPA-class disaster-response humanoid. Direct architectural descendant of: Pratt-Williamson SEA (1995, in corpus), Tonietti VSA (2005, round-21), Pisa-IIT SoftHand (in corpus). Together with iCub (corpus entry), establishes the Italian academic humanoid + compliant-actuator prior-art chain. Brings Italian depth from 5 to 6 entries.

**Sources:**

1. IIT corporate site (iit.it).
2. Tsagarakis + Caldwell publications (iit.it/research/lines/humanoid-and-human-centred-mechatronics).
3. WALK-MAN DRC 2015 documentation.
4. IIT R1 product page.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4e68247`.*
