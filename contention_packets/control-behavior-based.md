---
title: "control-behavior-based"
parent: "Invalidity Contentions"
nav_order: 43
layout: default
---

# Invalidity Contention Packet — `control-behavior-based`

**Generated:** 2026-05-15  
**Cross-cut tag:** `control-behavior-based`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1993-01  
**Most recent disclosure:** 2007-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-behavior-based`.

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

### 1993-01 — Cog (Rodney Brooks MIT 1993; behavior-based humanoid)

- **id:** `cog-brooks-mit-1993`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** MIT Artificial Intelligence Laboratory; Rodney Brooks (PI) + Cynthia Breazeal + Brian Scassellati + Matthew Marjanović + team
- **disclosure citation:** Brooks, R.A. + MIT AI Lab. Cog humanoid project 1993-2003. Brooks, R.A. + Stein, L.A. 'Building Brains for Bodies'. MIT AI Lab Memo 1439, 1993. Brooks, R.A. et al. 'The Cog Project: Building a Humanoid Robot'. In 'Computation for Metaphors, Analogy, and Agents'. Springer 1998.
- **disclosed subsystems:** `humanoid-bipedal`, `control-behavior-based`

**Prior art notes:**

> Cog (Rodney Brooks MIT AI Lab 1993-2003) is the foundational behavior-based humanoid — Brooks's 'embodied AI' manifesto in robot form. 32-year-deep academic-publication prior art. Ancestor of the entire modern humanoid-research lineage.

**Sources:**

1. Brooks, R.A. + Stein, L.A. 'Building Brains for Bodies'. MIT AI Lab Memo 1439, 1993.

---

### 2000-01 — Kismet (Cynthia Breazeal MIT 2000; sociable robot + facial expressions)

- **id:** `kismet-breazeal-mit-2000`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** MIT Artificial Intelligence Laboratory; Cynthia Breazeal (PhD thesis 2000)
- **disclosure citation:** Breazeal, C. PhD thesis 'Sociable Machines: Expressive Social Exchange Between Humans and Robots'. MIT 2000. Breazeal, C. 'Designing Sociable Robots'. MIT Press 2002. Kismet developed at MIT AI Lab (Brooks's group, corpus cog-brooks-mit-1993).
- **disclosed subsystems:** `companion-robot`, `control-behavior-based`

**Prior art notes:**

> Kismet (Cynthia Breazeal MIT 1997-2000) is the foundational 'sociable robot' — facial-expression + emotion-regulation as the architecture. 25-year-deep academic-publication prior art. Foundational to every subsequent social robot + HRI field. Breazeal → MIT Media Lab → Jibo (corpus).

**Sources:**

1. Breazeal, C. PhD thesis, MIT 2000.
2. Breazeal, C. 'Designing Sociable Robots'. MIT Press 2002.

---

### 2007-07 — MIT Domo + Meka Robotics (Aaron Edsinger)

- **id:** `edsinger-meka-mit-domo-2008`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT CSAIL Brooks group + Meka Robotics; Aaron Edsinger + Jeff Weber
- **disclosure citation:** Edsinger, A. PhD thesis 'Robot Manipulation in Human Environments' MIT 2007. Domo humanoid demonstrator in Brooks group MIT CSAIL. Meka Robotics commercial spinout founded 2006 by Edsinger + Jeff Weber. Acquired by Google December 2013 (one of 8 robotics startups acquired by Google that month). Lineage continues through Hello Robot (Edsinger co-founded with Charles Kemp 2017).
- **disclosed subsystems:** `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `actuator-electric-series-elastic`, `control-behavior-based`

**Prior art notes:**

> Edsinger's MIT Domo + Meka Robotics (MIT 2007 + Meka 2006-2013) is the foundational compliant-humanoid academic + commercial lineage. 18-year-deep public-domain prior art. **Direct architectural ancestor of Hello Robot Stretch (round-17)** — Edsinger founded Hello Robot 2017 with Charles Kemp. Series-elastic actuator commercial deployment via Meka predates Pratt-Williamson commercial-deployment narrative. Direct shielding for any commercial humanoid claim deriving from compliant-actuator humanoids or Edsinger lineage.

**Sources:**

1. Edsinger, A. PhD thesis 'Robot Manipulation in Human Environments' MIT 2007.
2. Meka Robotics history (now defunct corporate site; acquired by Google December 2013).
3. Hello Robot history (Edsinger + Kemp co-founders 2017).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `cd2f551`.*
