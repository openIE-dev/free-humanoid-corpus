---
title: "control-pid"
parent: "Invalidity Contentions"
nav_order: 118
layout: default
---

# Invalidity Contention Packet — `control-pid`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-pid`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1922-01  
**Most recent disclosure:** 1942-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-pid`.

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

### 1942-11 — Ziegler-Nichols PID Tuning Rules (1942)

- **id:** `ziegler-nichols-pid-tuning-1942`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Taylor Instrument Companies (Rochester, NY, USA); John G. Ziegler + Nathaniel B. Nichols
- **disclosure citation:** Ziegler, J.G., Nichols, N.B. 'Optimum Settings for Automatic Controllers'. Transactions of the ASME 64:759-768, November 1942. Taylor Instrument Companies (Rochester, NY, USA).
- **disclosed subsystems:** `control-pid`

**Prior art notes:**

> Ziegler-Nichols PID Tuning Rules (Ziegler & Nichols Taylor Instrument Companies ASME 1942) are the foundational practical method for tuning PID controllers. 83-year-deep public-domain prior art. Made PID (corpus minorsky-pid-control-1922) universally deployable.

**Sources:**

1. Ziegler, J.G., Nichols, N.B. Transactions of the ASME 64:759-768, 1942.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `c61fc91`.*
