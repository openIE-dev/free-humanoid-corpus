---
title: Home
layout: home
nav_order: 1
description: "A public-domain prior art commons for humanoid robotics. CC0."
permalink: /
---

# Free Humanoid Corpus
{: .fs-9 }

A public-domain prior art commons covering robots, humanoids, and humanoid-adjacent entities from private companies, open source repositories, science fiction, and academia.
{: .fs-6 .fw-300 }

[Browse the corpus](browse/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Cross-cuts](cross_cuts/){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[GitHub](https://github.com/openIE-dev/free-humanoid-corpus){: .btn .fs-5 .mb-4 .mb-md-0 }

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20049531.svg)](https://doi.org/10.5281/zenodo.20049531)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](https://github.com/openIE-dev/free-humanoid-corpus/blob/main/LICENSE)

---

**The corpus IS the prior art commons.** Every entry, at the moment of timestamped commit and quarterly release, is a defensive publication. There is no separate commons layer above this catalog — the structured data here, combined with the cryptographic timestamping in `releases/`, is itself the invalidity-contention material.

---

## What it covers

| Corpus | Count | Role |
|:---|---:|:---|
| Private | 57 | Patent-thicket holders. Reference points for what's been claimed. |
| Academic | 27 | Peer-reviewed disclosures. Already prior art automatically. |
| Fictional | 11 | Science fiction. Cited successfully as 102 prior art when specific. |
| Open | 11 | Existing open hardware. Already public-domain or permissive. |
| **Total** | **106** | (77 commons-grade, 29 draft) |

Entries span **1920** (Karel Čapek's R.U.R.) through **2025**.

---

## The 48 cross-cuts are the working tool

Each [subsystem cross-cut](cross_cuts/) is a chronologically-ordered list of every disclosing entry, with `prior_art_notes` and `disclosure_citation` ready to drop into an invalidity contention.

| Cross-cut | Earliest | Entries |
|:---|---:|---:|
| [Bipedal locomotion](cross_cuts/mechanism-bipedal-locomotion.html) | 1956 | 57 |
| [Anthropomorphic hand](cross_cuts/mechanism-anthropomorphic-hand.html) | 1973 | 42 |
| [Direct-drive electric actuator](cross_cuts/actuator-electric-direct-drive.html) | 1987 | 44 |
| [Harmonic-drive electric actuator](cross_cuts/actuator-electric-harmonic-drive.html) | 1986 | 14 |
| [ZMP balancing](cross_cuts/control-zmp-balancing.html) | 1996 | 13 |
| [RL policy](cross_cuts/control-rl-policy.html) | 2016 | 30 |
| [VLA (vision-language-action)](cross_cuts/control-vla-vision-language-action.html) | 2023 | 9 |
| [Safety hard-constraint supervisor](cross_cuts/safety-hard-constraint.html) | 1940 | 11 |

→ [All 48 cross-cuts](cross_cuts/)

---

## Provenance

Quarterly releases carry three independent cryptographic timestamps attesting pre-existence:

- **FreeTSA** (RFC 3161)
- **DigiCert** (RFC 3161)
- **OpenTimestamps** (Bitcoin-anchored)

The current release tarball, `corpus-2026.Q2.tar.gz` (SHA-256 `aa9430c6e785a409e3dbb10042b16e0e5677752c85eeffcba2c6b5605cde27ce`), is anchored to Bitcoin blocks **948142**, **948151**, and **948161**.

→ [Release runbook](RELEASE_RUNBOOK.html) · [Timestamping ceremony](TIMESTAMPING.html)

---

## Use it from the command line

```bash
git clone https://github.com/openIE-dev/free-humanoid-corpus.git
cd free-humanoid-corpus

# Validate the corpus and your local edits
python3 tools/validate.py corpus.jsonl --strict

# Look up prior art for a patent-claim phrase
python3 tools/lookup.py "harmonic drive reducer with output torque sensor"

# Scaffold a new entry interactively (then submit as a PR)
python3 tools/new_entry.py
```

---

## License

CC0 1.0. Public domain dedication. The corpus exists to be cited, copied, indexed, mirrored, embedded, ingested, and built upon. No usage license required.
