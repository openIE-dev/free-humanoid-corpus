---
title: "control-tree-search"
parent: "Invalidity Contentions"
nav_order: 136
layout: default
---

# Invalidity Contention Packet — `control-tree-search`

**Generated:** 2026-05-11  
**Cross-cut tag:** `control-tree-search`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2016-01  
**Most recent disclosure:** 2017-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-tree-search`.

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

### 2016-01 — AlphaGo (DeepMind Silver et al. 2016)

- **id:** `alphago-deepmind-2016`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** DeepMind (London); David Silver lead author + Demis Hassabis + 18 co-authors
- **disclosure citation:** Silver, D., Huang, A., Maddison, C.J., Guez, A., Sifre, L., van den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., Dieleman, S., Grewe, D., Nham, J., Kalchbrenner, N., Sutskever, I., Lillicrap, T., Leach, M., Kavukcuoglu, K., Graepel, T., Hassabis, D. 'Mastering the game of Go with deep neural networks and tree search'. Nature 529(7587):484-489, January 2016. DeepMind.
- **disclosed subsystems:** `ai-foundation-model`, `control-tree-search`

**Prior art notes:**

> AlphaGo (DeepMind Silver et al. Nature 2016) is the cultural-inflection AI moment for deep RL. 9-year-deep academic-publication prior art.

**Sources:**

1. Nature 529(7587):484-489, January 2016.

---

### 2017-12 — AlphaZero (DeepMind 2017; tabula-rasa self-play)

- **id:** `alphazero-deepmind-2017`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** DeepMind (London)
- **disclosure citation:** Silver, D., Hubert, T., Schrittwieser, J., et al. 'Mastering chess and shogi by self-play with a general reinforcement learning algorithm'. arXiv:1712.01815, December 2017. Published Science 362(6419):1140-1144, December 2018. DeepMind.
- **disclosed subsystems:** `ai-foundation-model`, `control-tree-search`, `control-self-play`

**Prior art notes:**

> AlphaZero (DeepMind Silver et al. arXiv 1712.01815, Science 2018) is the tabula-rasa self-play foundational result. 8-year-deep academic-publication prior art.

**Sources:**

1. arxiv.org/abs/1712.01815

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
