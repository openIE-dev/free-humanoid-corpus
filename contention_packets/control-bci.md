---
title: "control-bci"
parent: "Invalidity Contentions"
nav_order: 18
layout: default
---

# Invalidity Contention Packet — `control-bci`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-bci`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2002-07  
**Most recent disclosure:** 2017-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-bci`.

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

### 2002-07 — BrainGate

- **id:** `braingate-donoghue-2002`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** BrainGate consortium; John Donoghue (Brown), Leigh Hochberg (Mass. General Hospital), Krishna Shenoy (Stanford), Andrew Schwartz (Pittsburgh)
- **disclosure citation:** Donoghue, J. P. et al. 'Connecting cortex to machines: recent advances in brain interfaces'. Nature Neuroscience 5(11) 2002. First human BrainGate implant: Matthew Nagle, July 2004 (Brown University + Cyberkinetics). Hochberg, L. R. et al. 'Reach and grasp by people with tetraplegia using a neurally controlled robotic arm'. Nature 485 (2012). BrainGate consortium: Brown + Stanford + Massachusetts General + Case Western + Providence VA.
- **disclosed subsystems:** `control-bci`, `control-neural-decoding`, `sensing-cortical-implant`, `control-prosthetic-control`

**Prior art notes:**

> BrainGate is the canonical academic long-term human cortical BCI for paralysis (Donoghue/Hochberg/Shenoy consortium, 2002+). 23-year-deep open-academic prior art for: cortical microelectrode BCI, neural decoding for prosthetic control, closed-loop cortical-somatosensory feedback. The architectural anchor for every subsequent commercial BCI (Neuralink, Synchron, Paradromics) and the substrate for Modular Prosthetic Limb integration. Direct shielding for any commercial humanoid claim on neural-controlled robotic-arm operation, BCI-mediated teleoperation, or cortical-feedback rehabilitation.

**Sources:**

1. Donoghue et al. Nature Neuroscience 5(11) 2002.
2. Hochberg et al. Nature 485 2012 ('Reach and grasp by people with tetraplegia').
3. Willett et al. Nature 593 2021 ('High-performance brain-to-text via handwriting').
4. BrainGate consortium site (braingate.org).

---

### 2009-12 — Modular Prosthetic Limb (MPL)

- **id:** `apl-mpl-revolutionizing-prosthetics-2009`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** JHU Applied Physics Laboratory; led under DARPA Revolutionizing Prosthetics program (Geoffrey Ling DARPA PM)
- **disclosure citation:** Johns Hopkins Applied Physics Laboratory. Modular Prosthetic Limb (MPL) v1.0 completed December 2009 under DARPA Revolutionizing Prosthetics program (2006-present). Johnson, M. J. et al. clinical evaluation: Scientific Reports 11 (2021). DARPA + APL + Johns Hopkins Medicine + multiple consortium partners.
- **disclosed subsystems:** `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `sensing-tactile`, `sensing-fingertip-tactile`, `control-bci`, `control-prosthetic-control`

**Prior art notes:**

> The Modular Prosthetic Limb is the canonical sophisticated anthropomorphic prosthetic arm + hand from the DARPA Revolutionizing Prosthetics program (APL/JHU 2009+). 16-year-deep public-domain prior art for: 25-DoF anthropomorphic arm-and-hand at human-limb mass, integrated 100+-sensor tactile/position/force network, BCI-controlled prosthetic operation. Direct shielding for any commercial humanoid claim on anthropomorphic arm + hand integration. Particularly relevant for Tesla Optimus Gen 3 (round-15 entry, 22-DoF hands × 50 actuators) — the MPL's 25-DoF arm-and-hand at 100+ sensors establishes 16-year-deep prior art at the architectural level.

**Sources:**

1. JHU APL Revolutionizing Prosthetics page (jhuapl.edu/work/projects-and-missions/revolutionizing-prosthetics).
2. DARPA Revolutionizing Prosthetics page (darpa.mil/research/programs/revolutionizing-prosthetics).
3. Johnson et al. Scientific Reports 11 2021 ('Clinical evaluation of the Revolutionizing Prosthetics modular prosthetic limb system').
4. Bridges, M. M. et al. 'The Modular Prosthetic Limb: A Year of Operational Experience' (APL Tech Digest 2011).

---

### 2017-04 — Neuralink

- **id:** `neuralink-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Neuralink Corporation; Elon Musk + founding team (subsequently most departed)
- **disclosure citation:** Neuralink Corporation. Founded 2016 by Elon Musk + multi-author founding team (some now departed). First public technical reveal: Musk, E. et al. 'An Integrated Brain-Machine Interface Platform with Thousands of Channels' bioRxiv 703801 / J. Medical Internet Research 2019. First human implant January 2024 (Noland Arbaugh, P-1 PRIME study). Subsequent implants Aug 2024, 2025+.
- **disclosed subsystems:** `control-bci`, `control-neural-decoding`, `sensing-cortical-implant`, `mechanism-implantable-medical-device`

**Prior art notes:**

> Neuralink is the canonical 2017+ commercial cortical BCI. 8-year-deep public-disclosure prior art for: high-channel-count flexible-electrode BCI, wireless implant, robotic surgical insertion. **The capability set is fully covered by deeper academic prior art chains**: BrainGate (2002+, round-18 entry above) for cortical-implant BCI architecture; Schwartz/Pittsburgh neuroprosthetic-control work back to 1980s; Utah-array and Michigan-array silicon-electrode literature 1990s+. Modern claims on commercial BCI face this 23-year-deep open-academic anticipation.

**Sources:**

1. Musk, E. et al. bioRxiv 703801 (2019); JMIR 2019.
2. Neuralink corporate site (neuralink.com).
3. P-1 PRIME study (clinicaltrials.gov NCT06017869).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `ca07ce2`.*
