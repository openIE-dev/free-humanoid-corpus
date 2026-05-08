---
title: "control-whole-body-qp"
parent: "Invalidity Contentions"
nav_order: 105
layout: default
---

# Invalidity Contention Packet — `control-whole-body-qp`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-whole-body-qp`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2003-09  
**Most recent disclosure:** 2015-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-whole-body-qp`.

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

### 2003-09 — LAAS-CNRS Toulouse humanoid robotics

- **id:** `laas-cnrs-toulouse-humanoid-2003`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** LAAS-CNRS Toulouse; Jean-Paul Laumond, Olivier Stasse, Florent Lamiraux et al.
- **disclosure citation:** Laboratoire d'Analyse et d'Architecture des Systèmes (LAAS-CNRS), Toulouse, France. Founded 1968; one of CNRS's largest joint research units. **HRP-2 humanoid deployed at LAAS 2003** as the first European HRP-2 unit (under joint Japanese-French research agreement). Subsequent: HRP-2 then HRP-4 deployments. Notable researchers: Jean-Paul Laumond (motion planning), Olivier Stasse (humanoid manipulation), Florent Lamiraux.
- **disclosed subsystems:** `control-research-cluster`, `control-whole-body-qp`, `control-motion-planning`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> LAAS-CNRS Toulouse is the foundational European humanoid research lab (HRP-2 deployment 2003+). 22-year-deep public-domain academic prior art. **The origin of the Pinocchio rigid-body dynamics library** that underlies OCS2 and Crocoddyl (corpus entry mastalli-crocoddyl-2020). Direct shielding for any commercial humanoid claim on whole-body dynamics computation or motion-planning theory. Brings French-academic robotics depth in the corpus from 13 to 14 entries.

**Sources:**

1. LAAS-CNRS corporate site (laas.fr).
2. Pinocchio library (github.com/stack-of-tasks/pinocchio).
3. Laumond + Stasse + Lamiraux publications.

---

### 2015-06 — DRC-HUBO+ (DARPA Robotics Challenge winner)

- **id:** `kaist-drc-hubo-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** KAIST Humanoid Robot Research Center; Jun-Ho Oh group + Rainbow Robotics
- **disclosure citation:** KAIST + Rainbow Robotics. 'DRC-HUBO+: A robotic platform for the DARPA Robotics Challenge'. Lim, J., Lee, I., Shim, I., et al. International Journal of Robotics Research / Journal of Field Robotics 2017. Won 1st place at DARPA Robotics Challenge Finals Pomona June 2015 — completing all 8 disaster-response tasks in 44m28s. The follow-on commercial version was Rainbow Robotics' first product (corpus has rainbow-robotics-rb-y1 as the modern commercial successor).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-wheel-leg-hybrid`, `actuator-electric`, `control-whole-body-qp`, `control-supervised-autonomy`

**Prior art notes:**

> DRC-HUBO+ (KAIST + Rainbow Robotics, DRC 2015) is the canonical Korean academic humanoid milestone — 1st place winner of the DARPA Robotics Challenge Finals June 2015. 10-year-deep public-domain prior art for: wheel-leg hybrid transformable bipedal humanoid (knee-rolling for stability + bipedal for stairs), operator-supervised whole-body autonomy under intermittent comm. Direct shielding for any commercial humanoid claim on transformable lower-body morphology or DRC-class disaster-response capability set. Established Rainbow Robotics' commercial humanoid lineage (corpus entry rainbow-robotics-rb-y1).

**Sources:**

1. Lim, J. et al. JFR / IJRR 2017.
2. DARPA Robotics Challenge Finals 2015 Pomona results.
3. KAIST Humanoid Robot Research Center publications.
4. IEEE Spectrum coverage 'Korean Team Wins DARPA Robotics Challenge' 2015.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b2db4c5`.*
