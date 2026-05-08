---
title: "mechanism-tendon-driven"
parent: "Invalidity Contentions"
nav_order: 93
layout: default
---

# Invalidity Contention Packet — `mechanism-tendon-driven`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-tendon-driven`  
**Entries:** 2 (1 commons-grade, 1 draft)  
**Earliest disclosure:** 2000-07  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-tendon-driven`.

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
