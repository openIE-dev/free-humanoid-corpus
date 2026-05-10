---
title: "control-myoelectric"
parent: "Invalidity Contentions"
nav_order: 96
layout: default
---

# Invalidity Contention Packet — `control-myoelectric`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-myoelectric`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1963-01  
**Most recent disclosure:** 2007-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-myoelectric`.

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

### 1963-01 — Belgrade / Belgrade-USC Hand (Tomović + Bekey)

- **id:** `belgrade-usc-tomovic-bekey-hand-1963`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Mihailo Pupin Institute (Belgrade, Yugoslavia); Rajko Tomović + Miodrag Rakić; later Belgrade-USC version with George Bekey at USC
- **disclosure citation:** Tomović, R., Boni, G. 'An Adaptive Artificial Hand'. IRE Transactions on Automatic Control AC-7(3), 1962. Belgrade Hand developed at Mihailo Pupin Institute (Belgrade, Yugoslavia) 1961-1963. Subsequent Belgrade-USC Hand version with George Bekey at University of Southern California ~1988.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-underactuated-finger`, `control-myoelectric`, `actuator-electric`

**Prior art notes:**

> Belgrade / Belgrade-USC Hand (Tomović + Rakić 1963; Bekey USC 1988) is the foundational anthropomorphic prosthetic hand and the world's first externally-powered five-finger myoelectric prosthetic. 62-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from five-finger anthropomorphic hands, underactuated finger mechanisms, or myoelectric prosthetic control. Foundational to every modern anthropomorphic hand including Robotiq (round-42), Shadow Dexterous Hand (corpus), Salisbury Stanford-JPL Hand (corpus), Utah/MIT Hand (round-42), and the entire dexterous-hand research lineage.

**Sources:**

1. Tomović, R. + Boni, G. 'An Adaptive Artificial Hand'. IRE Transactions on Automatic Control AC-7(3), 1962.
2. en.techfokus.rs/belgrade-hand-first-bionic-prosthetic-robotics/
3. en.wikipedia.org/wiki/Rajko_Tomović

---

### 2002-09 — Targeted Muscle Reinnervation (TMR) — Kuiken RIC

- **id:** `kuiken-tmr-targeted-muscle-reinnervation-2002`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Rehabilitation Institute of Chicago (now Shirley Ryan AbilityLab) + Northwestern University; Todd Kuiken (PI)
- **disclosure citation:** Kuiken, T.A. et al. 'Targeted muscle reinnervation for real-time myoelectric control of multifunction artificial arms'. JAMA 301(6), 2009. First clinical case 2002 at Rehabilitation Institute of Chicago (RIC; now Shirley Ryan AbilityLab). The surgical procedure that re-routes amputated-limb motor nerves to chest/back muscles for intuitive myoelectric prosthesis control.
- **disclosed subsystems:** `control-myoelectric`, `control-pattern-recognition`, `surgical-nerve-redirection`

**Prior art notes:**

> TMR (Kuiken RIC 2002 first case; JAMA 2009) is the surgical procedure that enables intuitive multi-DOF prosthetic-arm control. 23-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from intuitive myoelectric multi-DOF prosthesis control. The surgical foundation of modern multi-articulated prosthetic hands (round-42 modern-multiarticulated-prosthetic-hands-2007-2012).

**Sources:**

1. Kuiken, T.A. et al. JAMA 301(6), 2009.

---

### 2007-07 — Modern multi-articulated prosthetic hands (i-LIMB / BeBionic / Michelangelo)

- **id:** `modern-multiarticulated-prosthetic-hands-2007-2012`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Touch Bionics (Edinburgh) → Össur (Iceland); RSL Steeper (UK) → Otto Bock (Germany); Otto Bock HealthCare (Duderstadt, Germany)
- **disclosure citation:** Touch Bionics Ltd. (Edinburgh, Scotland; founded 2003 by David Gow, NHS Lothian rehabilitation engineering spinout). i-LIMB myoelectric prosthetic hand product reveal July 2007. RSL Steeper Ltd. (UK) BeBionic hand 2010, acquired by Otto Bock HealthCare 2017. Otto Bock Michelangelo Hand reveal 2012. Touch Bionics acquired by Össur (Iceland) 2016; i-LIMB Quantum 2015.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-multi-articulated-finger`, `control-myoelectric`, `actuator-electric`

**Prior art notes:**

> Modern multi-articulated prosthetic hands (Touch Bionics i-LIMB 2007, RSL Steeper BeBionic 2010, Otto Bock Michelangelo 2012) are the defining commercial multi-articulated myoelectric prosthetic hand category. 13-19-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from individually-powered five-finger prosthetic hands or myoelectric multi-grip control. Lineage descends from Belgrade-USC Hand (round-42 belgrade-usc-tomovic-bekey-hand-1963) of foundational anthropomorphic prosthetics.

**Sources:**

1. ottobock.com/en-us/product/8E7----61161 (BeBionic).
2. Touch Bionics i-LIMB historical product page (Össur).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b980619`.*
