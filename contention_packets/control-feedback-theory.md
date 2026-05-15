---
title: "control-feedback-theory"
parent: "Invalidity Contentions"
nav_order: 64
layout: default
---

# Invalidity Contention Packet — `control-feedback-theory`

**Generated:** 2026-05-15  
**Cross-cut tag:** `control-feedback-theory`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1922-01  
**Most recent disclosure:** 1948-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-feedback-theory`.

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

### 1922-01 — PID Control (Nicolas Minorsky 1922; ship autopilot)

- **id:** `minorsky-pid-control-1922`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** US Navy; Nicolas Minorsky
- **disclosure citation:** Minorsky, N. 'Directional stability of automatically steered bodies'. Journal of the American Society of Naval Engineers 34(2):280-309, 1922. US Navy. Derived from observing how a helmsman steers a ship — the first theoretical treatment of three-term (PID) control.
- **disclosed subsystems:** `control-feedback-theory`, `control-pid`

**Prior art notes:**

> PID Control (Nicolas Minorsky US Navy 1922) is the foundational three-term feedback controller. 103-year-deep public-domain prior art. The single most-deployed control algorithm in history.

**Sources:**

1. Minorsky, N. J. Am. Soc. Naval Engineers 34(2):280-309, 1922.

---

### 1948-01 — Cybernetics (Norbert Wiener 1948)

- **id:** `wiener-cybernetics-1948`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT; Norbert Wiener (with Arturo Rosenblueth, Julian Bigelow)
- **disclosure citation:** Wiener, N. 'Cybernetics: Or Control and Communication in the Animal and the Machine'. MIT Press / Hermann & Cie / John Wiley, 1948. MIT. Coined the term 'cybernetics' (from Greek kybernetes, 'steersman').
- **disclosed subsystems:** `control-feedback-theory`

**Prior art notes:**

> Cybernetics (Norbert Wiener MIT 1948) is the founding text of feedback-control theory + the unification of control across machines and organisms. 77-year-deep public-domain prior art.

**Sources:**

1. Wiener, N. 'Cybernetics'. MIT Press 1948.

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
