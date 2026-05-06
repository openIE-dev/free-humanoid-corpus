---
title: safety-hard-constraint
parent: Cross-cuts
layout: default
---

# Cross-cut: `safety-hard-constraint`

**11 corpus entries disclose this subsystem.**

Earliest disclosure: 1940-09

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Asimov positronic robots (1940-09)

- **id**: `asimov-positronic-robots`
- **corpus**: fictional
- **creator**: Isaac Asimov
- **disclosure**: Asimov, Isaac. 'Robbie' (originally 'Strange Playfellow'). Super Science Stories, September 1940.
- **ip status**: fictional
- **prior art notes**: Establishes hard-constraint safety architecture as a hardware-level concern, not a software policy. Directly anticipates modern AI safety frameworks including Simplex supervisor architectures and constraint-based safety middleware. Specifically anticipates: hardware-level safety constraints with deterministic priority ordering.

## HAL 9000 (1968-04-02)

- **id**: `hal-9000`
- **corpus**: fictional
- **creator**: Arthur C. Clarke / Stanley Kubrick
- **disclosure**: Kubrick, Stanley (dir.). 2001: A Space Odyssey. MGM, 1968-04-02. Clarke, Arthur C. novelization, 1968.
- **ip status**: fictional
- **prior art notes**: HAL is included not as a humanoid but as the canonical depiction of safety failure due to conflicting goals — directly relevant to MathGround's framing of supervisor architectures and the need for explicit constraint hierarchies.

## Asimov's Zeroth Law (1985)

- **id**: `asimovs-zeroth-law`
- **corpus**: fictional
- **creator**: Isaac Asimov
- **disclosure**: Asimov, Isaac. Robots and Empire. Doubleday, 1985.
- **ip status**: fictional
- **prior art notes**: Significant for safety architecture prior art because it explicitly demonstrates priority-reordering in a hard-constraint hierarchy under conflicting goals. Anticipates modern AI safety frameworks dealing with population-scale or systemic harm tradeoffs.

## Data (1987-09-28)

- **id**: `data-tng`
- **corpus**: fictional
- **creator**: Gene Roddenberry / Brent Spiner
- **disclosure**: Roddenberry, Gene et al. Star Trek: The Next Generation, 'Encounter at Farpoint,' first aired 1987-09-28.
- **ip status**: fictional
- **prior art notes**: Detailed canonical episodes ('The Measure of a Man,' 'The Offspring,' 'Inheritance') describe android construction in significant detail. The 'Soong-type' positronic architecture is a direct extension of Asimov's positronic robots.

## Simplex Architecture (1995)

- **id**: `sherman-simplex-architecture`
- **corpus**: academic
- **creator**: Lui Sha, Carnegie Mellon University
- **disclosure**: Sha, Lui. 'Dependable system upgrade.' Proceedings 19th IEEE Real-Time Systems Symposium, 1998. Earlier conceptual work circa 1995.
- **ip status**: public-domain
- **prior art notes**: Foundational prior art for safety supervisor architectures in robotics and physical AI. Any 'safety supervisor' or 'safety envelope' or 'fallback controller' patent claim post-1995 must contend with Sha's Simplex work as anticipating prior art. Directly relevant to MathGround's Simplex supervisor architecture.

## Hamilton-Jacobi Reachability for Safe Control (2005)

- **id**: `reachability-analysis-safe-control`
- **corpus**: academic
- **creator**: Ian Mitchell, Alexandre Bayen, Claire Tomlin (UC Berkeley/Stanford)
- **disclosure**: Mitchell, I.M., Bayen, A.M., Tomlin, C.J. 'A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games.' IEEE TAC 50(7), 2005.
- **ip status**: public-domain
- **prior art notes**: Foundational prior art for formally-verified safe control. Any patent claiming 'verified safety envelopes' or 'formal safety guarantees' for autonomous systems must contend with HJ reachability work.

## ISO 10218 Collaborative Robot Safety (2006)

- **id**: `iso-10218-collaborative-robots`
- **corpus**: academic
- **creator**: ISO TC 299 (Robotics) working group
- **disclosure**: ISO 10218-1:2006 'Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots.' International Organization for Standardization.
- **ip status**: public-domain
- **prior art notes**: ISO 10218 (and the related ISO/TS 15066 for collaborative operation) constitute foundational prior art for collaborative robot safety claims. Any patent claim around 'safety-rated monitored stop,' 'speed and separation monitoring,' or 'power and force limiting' in collaborative robotics is anticipated by these standards.

## Control Barrier Functions (2007)

- **id**: `control-barrier-functions`
- **corpus**: academic
- **creator**: Peter Wieland and Frank Allgöwer (early formalization); Aaron Ames and others (modern formalization)
- **disclosure**: Wieland, P. and Allgöwer, F. 'Constructive safety using control barrier functions.' IFAC Proceedings Volumes 40(12), 2007.
- **ip status**: public-domain
- **prior art notes**: CBFs are the dominant modern formalism for online safety filtering in robotics. Substantial prior art for any patent claiming online safety filtering, safety-aware QP control, or formally-bounded safe ML execution. Particularly relevant to MathGround's Universal Fuzz Law work as the formal foundation for safety envelopes.

## Willow Garage PR1 (2008)

- **id**: `willow-pr1`
- **corpus**: academic
- **creator**: Willow Garage / Stanford (Ken Salisbury group)
- **disclosure**: Wyrobek, K.A. et al. 'Towards a Personal Robotics Development Platform: Rationale and Design of an Intrinsically Safe Personal Robot.' ICRA 2008.
- **ip status**: open-permissive
- **prior art notes**: PR1 is significant prior art for safety-by-design humanoid robotics. Cable-driven intrinsically-safe architecture anticipates several modern compliant-actuator humanoid claims.

## Runtime Assurance (RTA) (2010)

- **id**: `runtime-assurance-rta`
- **corpus**: academic
- **creator**: Air Force Research Laboratory and DARPA program
- **disclosure**: Schierman, J.D. et al. 'Runtime Assurance Framework Development for Highly Adaptive Flight Control Systems.' Air Force Research Laboratory, 2015. Earlier DARPA AACUS work circa 2010.
- **ip status**: public-domain
- **prior art notes**: Direct descendant of Simplex; the 'unverified neural net plus verified safety controller' pattern. Anticipates modern ML-safety supervisor patents in autonomous vehicles, drones, and robotics. Directly applicable as prior art to safety claims in physical AI products.

## Shielding for Safe Reinforcement Learning (2018)

- **id**: `shielding-rl`
- **corpus**: academic
- **creator**: Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, Ufuk Topcu
- **disclosure**: Alshiekh, M. et al. 'Safe Reinforcement Learning via Shielding.' AAAI 2018.
- **ip status**: public-domain
- **prior art notes**: Major prior art for any patent on RL safety filtering, shielded ML, or temporal-logic-bounded RL. Combined with Simplex and CBF prior art, makes much of the 'safe ML' patent space difficult to defend.
