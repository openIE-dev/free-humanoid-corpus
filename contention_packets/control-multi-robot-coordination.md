---
title: "control-multi-robot-coordination"
parent: "Invalidity Contentions"
nav_order: 89
layout: default
---

# Invalidity Contention Packet — `control-multi-robot-coordination`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-multi-robot-coordination`  
**Entries:** 4 (3 commons-grade, 1 draft)  
**Earliest disclosure:** 2000-01  
**Most recent disclosure:** 2025-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-multi-robot-coordination`.

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

### 2000-01 — Czech Technical University Prague (CVUT/CTU) robotics *(draft)*

- **id:** `cvut-prague-czech-robotics`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Czech Technical University in Prague (CVUT/CTU); Multi-Robot Systems group + Faculty of Electrical Engineering
- **disclosure citation:** České Vysoké Učení Technické v Praze / Czech Technical University in Prague (CVUT/CTU). Faculty of Electrical Engineering robotics group; Multi-Robot Systems (MRS) group led by Martin Saska — major contributor to multi-MAV (multi-Micro-Aerial-Vehicle) research and DARPA Subterranean Challenge (2nd place 2021 alongside CSIRO). cvut.cz.
- **disclosed subsystems:** `control-research-cluster`, `control-multi-robot-coordination`, `control-mav-flight`, `control-gps-denied-navigation`

**Prior art notes:**

> CVUT Prague is Czech Republic's leading robotics academic institution and a Central European robotics anchor. **First real (non-fictional) entry in the corpus from Czech Republic** — closes a regional gap (corpus had only the fictional R.U.R. entry from CZ). Notable for multi-MAV + DARPA SubT work. Aggregator-style; specific CVUT MRS papers should be added in future rounds.

**Sources:**

1. CVUT Prague corporate site (cvut.cz).
2. CTU Multi-Robot Systems group (mrs.felk.cvut.cz).
3. DARPA SubT 2021 participation documentation.

---

### 2017-09 — Saska multi-MAV systems (CTU Prague MRS group)

- **id:** `saska-cvut-multi-mav-2017`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Czech Technical University in Prague; Martin Saska + MRS group
- **disclosure citation:** Saska, M., Bačha, V., Krajník, T., Hert, D., Spurný, V., Petrlík, M., Báča, T. 'System for deployment of groups of unmanned micro aerial vehicles in GPS-denied environments using onboard visual relative localization'. Autonomous Robots 41(4) 2017. Czech Technical University in Prague, Multi-Robot Systems group.
- **disclosed subsystems:** `control-multi-robot-coordination`, `control-mav-flight`, `control-gps-denied-navigation`, `control-visual-relative-localization`

**Prior art notes:**

> Saska MRS (CTU Prague 2017+) is the canonical multi-MAV swarm-coordination academic work from Czech Republic. Anchors round-23 CVUT Prague aggregator with paper-level disclosure. 8-year-deep open-permissive prior art. Together with Saska's DARPA SubT 2021 results, establishes Czech academic multi-MAV robotics as recognizably world-class.

**Sources:**

1. Saska et al. Autonomous Robots 41(4) 2017.
2. CTU MRS group (mrs.felk.cvut.cz).
3. DARPA SubT 2021 results.

---

### 2021-09 — CSIRO Wildcat (DARPA Subterranean Challenge)

- **id:** `csiro-hudson-wildcat-darpa-subt-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** CSIRO Data61 + Emesent + Georgia Tech; Hudson, Talbot, et al.
- **disclosure citation:** Hudson, N., Talbot, F., Cox, M., Williams, J., Hines, T., Pitt, A., Wood, B., Frousheger, D., Lo Surdo, K., Molnar, T., Steindl, R., et al. 'Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge'. Field Robotics 2 2022 / Journal of Field Robotics. CSIRO Data61 + Emesent + Georgia Tech. **2nd place DARPA Subterranean Challenge Finals 2021**.
- **disclosed subsystems:** `control-vio-slam`, `control-multi-robot-coordination`, `control-rough-terrain-locomotion`, `control-subterranean-autonomy`

**Prior art notes:**

> CSIRO Data61 Wildcat (Hudson et al. Field Robotics 2022) is the specific paper-level anchor for the round-23 CSIRO Data61 aggregator. **DARPA SubT Finals 2nd place** establishes Australian academic robotics at internationally-recognizable level. Direct shielding for any commercial humanoid claim on LIDAR-only SLAM, subterranean autonomy, or multi-robot heterogeneous-platform coordination.

**Sources:**

1. Hudson et al. Field Robotics 2 2022.
2. DARPA Subterranean Challenge Finals 2021 results.
3. CSIRO Data61 publications (data61.csiro.au).

---

### 2025-02 — Figure Helix

- **id:** `figure-helix-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Figure AI Inc.
- **disclosure citation:** Figure AI Inc. 'Helix: A Vision-Language-Action Model for Generalist Humanoid Control'. Public reveal February 2025 via figure.ai/news/helix. Subsequent disclosures: 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics) and Hacker News + Robot Report coverage. No academic publication; trade-secret commercial VLA.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-dual-system-architecture`, `control-high-rate-continuous-control`, `control-bimanual-manipulation`, `control-multi-robot-coordination`

**Prior art notes:**

> Helix is Figure AI's canonical 2025 commercial humanoid VLA. Public-disclosure surface (corporate blog + demo videos + Hacker News + Robot Report coverage) reveals architecture (S1/S2 dual-system, 35-DoF/200Hz, ~500hr teleop training) but withholds neural-network specifics, training-data composition, fine-tuning recipe, and policy-evaluation metrics. The capability set claimed is fully covered by deep open academic prior art chains: (1) S1/S2 dual-system architecture is shared with NVIDIA GR00T N1 (round-15 entry, released within weeks; the cognitive-science S1/S2 pattern dates to Kahneman 'Thinking Fast and Slow' 2011); (2) high-rate continuous VLA control was demonstrated by π₀ (round-12, October 2024) and π₀.₅ (round-12, April 2025) in diffusion/flow-matching form; (3) onboard low-power VLA inference is anticipated by OpenVLA-OFT (round-12, parallel decoding + 26× throughput); (4) multi-robot collaboration is anticipated by ROS 2 (round-13, real-time multi-vehicle middleware) and the Mobile ALOHA / ACT bimanual lineage. Direct shielding for any Helix or Helix-derivative commercial-IP claim.

**Sources:**

1. Figure AI 'Helix' announcement (figure.ai/news/helix), February 2025.
2. Figure AI 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics), 2025.
3. Robot Report coverage (therobotreport.com/figure-humanoid-robots-demonstrate-helix-model-household-chores/).
4. Hacker News discussion thread (news.ycombinator.com/item?id=43115079).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2fbde5f`.*
