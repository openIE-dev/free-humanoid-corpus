---
title: "sensing-neural"
parent: "Invalidity Contentions"
nav_order: 205
layout: default
---

# Invalidity Contention Packet — `sensing-neural`

**Generated:** 2026-05-09  
**Cross-cut tag:** `sensing-neural`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1991-01  
**Most recent disclosure:** 2019-08

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-neural`.

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

### 1991-01 — Blackrock Neurotech Utah Array (Normann 1990s)

- **id:** `blackrock-utah-array-normann-1990s`
- **corpus:** private
- **ip status:** public-domain (foundational design); trade-secret (commercial implementation)
- **creator:** University of Utah Bioengineering; Richard Normann; commercialized via Bionic Technologies → Cyberkinetics → Blackrock Neurotech
- **disclosure citation:** Normann, R.A. et al. 'A neural interface for a cortical vision prosthesis'. Vision Research 39(15), 1999. Utah Array developed at University of Utah Bioengineering ~1990s by Richard Normann's group. Bionic Technologies LLC commercial spinout 1997 → acquired by Cyberkinetics 2002 → Blackrock Microsystems / Blackrock Neurotech 2008. First FDA-cleared for human implantation.
- **disclosed subsystems:** `bci-cortical`, `sensing-neural`, `bci-microelectrode-array`

**Prior art notes:**

> Blackrock Neurotech Utah Array (Normann Utah 1990s; commercial via Bionic Tech → Cyberkinetics → Blackrock) is the foundational implanted BCI microelectrode array. 30+-year-deep public-domain prior art. Direct shielding for any commercial humanoid or Iron Man-class claim deriving from cortical microelectrode arrays. Underlies BrainGate (corpus braingate-donoghue-2002), APL MPL (corpus apl-mpl-revolutionizing-prosthetics-2009), Synchron Stentrode (round-43 sister-chain), Neuralink (corpus neuralink-2017) competitive position. Belongs in every BCI prior-art landscape.

**Sources:**

1. Normann, R.A. et al. Vision Research 39(15), 1999.
2. Blackrock Neurotech corporate site.

---

### 2019-08 — Synchron Stentrode endovascular brain-computer interface

- **id:** `synchron-stentrode-endovascular-bci-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Synchron Inc. (Brooklyn NY + Melbourne); Tom Oxley + Nick Opie + Rahul Sharma; University of Melbourne origin
- **disclosure citation:** Synchron Inc. (Brooklyn, NY, USA + Melbourne, Australia; founded 2012 by Tom Oxley + Nick Opie + Rahul Sharma at University of Melbourne). First human implant August 2019 at Royal Melbourne Hospital. First in-human FDA Investigational Device Exemption (IDE) BCI of its endovascular class July 2021; first US implant July 2022.
- **disclosed subsystems:** `bci-endovascular`, `bci-cortical-motor-decoding`, `sensing-neural`

**Prior art notes:**

> Synchron Stentrode (Brooklyn + Melbourne 2019+; FDA IDE 2021) is the first endovascular brain-computer interface — the no-craniotomy alternative to Neuralink. 6-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or Iron Man-class claim deriving from BCI-driven powered armor / prostheses without surgical craniotomy. Sister to Neuralink (corpus neuralink-2017) and BrainGate (corpus braingate-donoghue-2002) in the implanted-BCI prior-art chain.

**Sources:**

1. en.wikipedia.org/wiki/Stent-electrode_recording_array
2. en.wikipedia.org/wiki/Thomas_Oxley_(neurologist)

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `d6a964d`.*
