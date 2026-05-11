---
title: "actuator-pneumatic-muscle"
parent: "Invalidity Contentions"
nav_order: 19
layout: default
---

# Invalidity Contention Packet — `actuator-pneumatic-muscle`

**Generated:** 2026-05-11  
**Cross-cut tag:** `actuator-pneumatic-muscle`  
**Entries:** 7 (7 commons-grade, 0 draft)  
**Earliest disclosure:** 1957-01  
**Most recent disclosure:** 2018-07-30

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-pneumatic-muscle`.

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

### 1957-01 — McKibben pneumatic artificial muscle

- **id:** `mckibben-pneumatic-muscle-1957`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Joseph L. McKibben (NIH, Bethesda)
- **disclosure citation:** McKibben, J. L. (1957). Pneumatic artificial muscle developed at the National Institutes of Health for an orthotic device for polio patients. The original technical reports describe the braided-shell pneumatic actuator that contracts when pressurized. Subsequently extensively studied — Daerden + Lefeber 'Pneumatic Artificial Muscles: actuators for robotics and automation' European Journal of Mechanical and Environmental Engineering 47(1) 2002 is a canonical academic survey.
- **disclosed subsystems:** `actuator-pneumatic-muscle`, `actuator-compliant`

**Prior art notes:**

> The McKibben pneumatic artificial muscle is the canonical compliant-actuator foundation of soft robotics. 68-year-deep public-domain prior art (1957). The architectural parent of: Festo Fluidic Muscle (round-16 entry below), Shadow Robot Air Muscle, Pisa-IIT McKibben-actuated humanoid platforms (e.g., Walk-Man's compliant-joint design), Pneubotics. Direct shielding for any commercial humanoid claim on pneumatic-actuated compliant motion or biologically-mimetic actuator design. Particularly relevant if free-humanoid-platform pivots toward a soft-humanoid v0.2 variant — the pneumatic-actuator branch is well-anticipated.

**Sources:**

1. McKibben, J. L. NIH technical reports 1957.
2. Daerden, F., Lefeber, D. 'Pneumatic Artificial Muscles' EJMEE 47(1) 2002 — canonical academic survey.
3. Tondu, B. 'Modelling of the McKibben artificial muscle' J. Intelligent Material Systems 23(3) 2012.

---

### 1983 — Raibert One-Legged Hopper

- **id:** `raibert-hopping-1leg`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Marc H. Raibert; CMU Leg Laboratory, then MIT Leg Laboratory
- **disclosure citation:** Raibert, Marc H. 'Hopping in legged systems — modeling and simulation for the two-dimensional one-legged case'. IEEE Transactions on Systems, Man, and Cybernetics SMC-14(3): 451-463, May/June 1984. Earlier: Raibert, M.H. and Brown, H.B. 'Experiments in balance with a 2D one-legged machine'. Trans. ASME, J. Dyn. Sys., Meas., Cont., 106:75-81, 1984.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-pneumatic-muscle`, `control-reduced-order-model`

**Prior art notes:**

> Raibert's hoppers are the foundational academic disclosure of dynamic legged balance and reduced-order-model control. The three-part decoupling (leg height / foot placement / body attitude) is the *exact* control architecture used by every subsequent dynamic-legged academic and commercial system, from Cassie to Atlas to MIT Mini Cheetah. Modern claims on reduced-order-model legged control all face Raibert's 1984 disclosure as 102 prior art. The 1985 book (Legged Robots that Balance, MIT Press) extends the disclosure to 2-legged and 4-legged versions and is one of the most-cited works in legged robotics. Publicly funded research; open publication.

**Sources:**

1. Raibert, M.H. 'Hopping in legged systems'. IEEE Trans. SMC, 1984.
2. Raibert, M.H. and Brown, H.B. 'Experiments in balance with a 2D one-legged machine'. ASME J. DSMC, 1984.
3. Raibert, M.H. Legged Robots that Balance. MIT Press, 1986.

---

### 2002 — Shadow Dexterous Hand

- **id:** `shadow-dexterous-hand`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Shadow Robot Company (Richard Greenhill, Rich Walker, et al.)
- **disclosure citation:** Greenhill, Richard et al. (Shadow Robot Company). 'Shadow Dexterous Hand'. ICRA workshops 2002 onwards; mechanical disclosures in Greenhill, R., Walker, R. et al. 'The Shadow C5 Hand Prototype'. ICRA Workshop on Humanoid Manipulation, 2007.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-pneumatic-muscle`, `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `sensing-tactile-fingertip`

**Prior art notes:**

> Shadow's hand is the longest-running academic-grade dexterous hand platform and is the standard reference for tendon-routed anthropomorphic manipulators. Anticipates and provides extensive prior art for: (1) 24-DOF anthropomorphic hand mechanism with separate-finger control — relevant to modern humanoid hand IP; (2) McKibben-style pneumatic muscle actuation in a hand — relevant to artificial-muscle hand claims; (3) tendon-tension control as a viable closed-loop mode for dexterity — relevant to tendon-controlled hand IP. Shadow has published extensively in IEEE proceedings since 2002, and the platform is licensed to academic labs worldwide. Modern Tesla, Figure, and 1X hand patents face Shadow's 22+ years of accumulated public disclosure.

**Sources:**

1. Shadow Robot Company. 'Shadow C5 Hand'. ICRA Workshop on Humanoid Manipulation, 2007.
2. Shadow Robot Company. Shadow Dexterous Hand technical specification (publicly distributed).

---

### 2003 — Shadow Dexterous Hand

- **id:** `shadow-hand`
- **corpus:** private
- **ip status:** patented
- **creator:** Shadow Robot Company
- **disclosure citation:** Shadow Robot Company. Shadow Dexterous Hand, commercial release approximately 2003.
- **disclosed subsystems:** `actuator-pneumatic-muscle`, `actuator-electric-tendon-driven`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `sensing-tactile-fingertip`

**Prior art notes:**

> Shadow Hand is among the deepest prior art references for anthropomorphic robotic hands. Most modern humanoid hand claims are anticipated by Shadow's 20+ years of disclosure.

**Sources:**

1. shadowrobot.com
2. Shadow Robot academic publications.

---

### 2010-10-25 — Cornell Universal Jamming Gripper

- **id:** `cornell-jamming-gripper`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Eric Brown, Nicholas Rodenberg, John Amend, Annan Mozeika, Erik Steltz, Mitchell R. Zakin, Hod Lipson, Heinrich M. Jaeger; Cornell University and University of Chicago
- **disclosure citation:** Brown, E., Rodenberg, N., Amend, J., Mozeika, A., Steltz, E., Zakin, M.R., Lipson, H., Jaeger, H.M. 'Universal robotic gripper based on the jamming of granular material'. PNAS 107(44): 18809-18814, October 25, 2010.
- **disclosed subsystems:** `actuator-pneumatic-muscle`, `mechanism-underactuated-grasping`

**Prior art notes:**

> The Cornell jamming gripper introduces granular-jamming as a fundamental new class of robotic gripper. Anticipates: (1) jamming-based universal grippers with single-DOF actuation — relevant to modern claims on universal/adaptive grippers; (2) the principle that compliance during approach and rigidity during grasp can be combined in a single deformable structure — relevant to compliant-grasp IP across the soft robotics field. The 2010 PNAS paper is one of the most-cited soft-robotics papers and has been licensed/extended by Empire Robotics (commercial spinoff) and many academic labs. Modern universal-gripper claims face this 2010 anchor.

**Sources:**

1. Brown, E. et al. 'Universal robotic gripper based on the jamming of granular material'. PNAS 107(44), 2010.
2. Steltz, E., Mozeika, A. et al. 'JSEL: jamming skin enabled locomotion'. IROS 2009 (precursor disclosure).

---

### 2014-11-07 — Baymax

- **id:** `baymax-big-hero-6`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Disney; design influenced by CMU/Disney soft-robot research (Stanton, Hines, Atkeson, et al.)
- **disclosure citation:** Hall, Don and Williams, Chris (dir.). Big Hero 6. Walt Disney Animation Studios, November 7, 2014. Inspired by Disney/Carnegie Mellon collaboration on inflatable robotics, Stanton et al. CMU.
- **disclosed subsystems:** `actuator-pneumatic-muscle`, `mechanism-anthropomorphic-hand`, `sensing-tactile-whole-body`, `safety-hard-constraint`

**Prior art notes:**

> Anticipates inflatable / pneumatic soft-body humanoid architecture for human-safe medical interaction. Notably, the Baymax design is *grounded* in real CMU Robotics Institute research: Atkeson and colleagues at CMU developed inflatable pneumatic robotic arms specifically to demonstrate the safety properties shown in the film. The 2014 release date follows actual academic work on inflatable robots published in 2011-2014. Modern patents on soft-pneumatic medical/care humanoids face this combined fictional+academic disclosure as 102/103 prior art. The film is continuously in distribution; CMU's research is in IEEE proceedings.

**Sources:**

1. Hall, D. and Williams, C. Big Hero 6. Walt Disney Animation Studios, 2014.
2. Stanton, K., Hines, L. et al. 'Tools for inflatable robots'. (CMU Robotics Institute working papers, 2010-2014)
3. Atkeson, C.G. (CMU lab personal correspondence with Disney production team).

---

### 2018-07-30 — OpenAI Dactyl

- **id:** `openai-dactyl`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Andrychowicz, Akkaya, Mordatch, Plappert, Petron, Powell, Wong, Schneider, Tezak, Tobin, et al.; OpenAI
- **disclosure citation:** Andrychowicz, M. et al. 'Learning Dexterous In-Hand Manipulation'. arXiv:1808.00177, July 30, 2018; OpenAI. Akkaya, I. et al. 'Solving Rubik's Cube with a Robot Hand'. arXiv:1910.07113, October 16, 2019.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `mechanism-anthropomorphic-hand`, `actuator-pneumatic-muscle`

**Prior art notes:**

> Dactyl is the foundational academic disclosure of large-scale sim-to-real RL for in-hand dexterous manipulation. Anticipates: (1) zero-shot policy transfer from massively-randomized simulation to real hardware — directly relevant to claims on sim-to-real humanoid manipulation IP (every modern humanoid hand uses this paradigm); (2) automatic domain randomization (ADR) as a self-tuning training procedure — relevant to claims on adaptive-randomization training; (3) LSTM-based policies for partial-observability manipulation — relevant to recurrent-policy IP. OpenAI's open-source code release plus the arXiv preprints provide deep prior art coverage. Modern in-hand-manipulation claims face this 2018-2019 anchor.

**Sources:**

1. Andrychowicz, M. et al. 'Learning Dexterous In-Hand Manipulation'. arXiv:1808.00177, 2018.
2. Akkaya, I. et al. 'Solving Rubik's Cube with a Robot Hand'. arXiv:1910.07113, 2019.
3. OpenAI Dactyl GitHub releases.

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
