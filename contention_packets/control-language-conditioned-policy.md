---
title: "control-language-conditioned-policy"
parent: "Invalidity Contentions"
nav_order: 76
layout: default
---

# Invalidity Contention Packet — `control-language-conditioned-policy`

**Generated:** 2026-05-11  
**Cross-cut tag:** `control-language-conditioned-policy`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2021-12  
**Most recent disclosure:** 2021-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-language-conditioned-policy`.

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

### 2021-12 — CALVIN

- **id:** `calvin-mees-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Freiburg AIS Lab; Oier Mees, Lukas Hermann, Wolfram Burgard
- **disclosure citation:** Mees, O., Hermann, L., Rosete-Beas, E., Burgard, W. 'CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks'. IEEE Robotics and Automation Letters 7(3) 2022. arXiv:2112.03227. University of Freiburg.
- **disclosed subsystems:** `control-language-conditioned-policy`, `control-imitation-learning`, `control-long-horizon-manipulation`, `control-benchmarking`

**Prior art notes:**

> CALVIN is the canonical long-horizon language-conditioned manipulation benchmark (Mees + Burgard Freiburg, RA-L 2022). 4-year-deep open-permissive prior art for: language-conditioned robot manipulation benchmark, teleoperated 'play data' as training distribution, hour-scale unstructured play datasets for language grounding. Direct shielding for any commercial humanoid claim on language-conditioned manipulation training data + benchmarks. Together with LIBERO (round-17), RoboCasa (round-16), robomimic (round-16), establishes the language-conditioned-VLA evaluation substrate.

**Sources:**

1. Mees et al. arXiv:2112.03227 IEEE RA-L 2022.
2. Project page (calvin.cs.uni-freiburg.de).
3. GitHub: github.com/mees/calvin.

---

### 2021-12 — BC-Z

- **id:** `bc-z-jang-2021`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Research + Stanford + Everyday Robots; Eric Jang, Sergey Levine, Chelsea Finn et al.
- **disclosure citation:** Jang, E., Irpan, A., Khansari, M., Kappler, D., Ebert, F., Lynch, C., Levine, S., Finn, C. 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'. CoRL 2021. arXiv:2202.02005. Google Research + Stanford + Everyday Robots.
- **disclosed subsystems:** `control-imitation-learning`, `control-language-conditioned-policy`, `control-foundation-model-policy`

**Prior art notes:**

> BC-Z (Jang et al. CoRL 2021) is the foundational language-conditioned manipulation policy paper at Google scale. 4-year-deep public-domain prior art. **Direct architectural ancestor of RT-1** (corpus entry) which transformerized BC-Z's framework. Established the 'large-scale demonstrations + language conditioning' pattern that the entire RT-X lineage descends from. Direct shielding for any commercial humanoid VLA claim on 'large-scale teleop + language conditioning'.

**Sources:**

1. Jang et al. arXiv:2202.02005 CoRL 2021.
2. Project page (sites.google.com/view/bc-z).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `934776f`.*
