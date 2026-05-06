---
title: Schema
layout: default
nav_order: 4
---

# Free Humanoid Corpus — Schema v0.2

## Status

v0.2 is the first version that treats the corpus as the prior art commons
itself rather than as substrate for a separate commons. Changes from v0.1:

- Quality bar for entries made explicit and load-bearing
- Timestamping infrastructure required (not optional)
- `disclosed_subsystems` field added with structured taxonomy
- `cpc_classifications` field added for examiner discoverability
- `draft` flag added so incremental progress is visible without polluting
  the commons-quality entry pool

Existing seed entries from v0.1 carry `schema_version: 1` and will be migrated
in a separate pass; v0.2 entries carry `schema_version: 2`.

## Purpose

A structured catalog of every robot, humanoid, and humanoid-adjacent entity from
private companies, open source repositories, science fiction (film/TV/comics/games/literature),
and academia.

**The corpus IS the prior art commons.** This is a load-bearing architectural
decision. Every entry is a defensive publication artifact, not a Wikipedia entry.
The commons does not sit on top of the corpus as a separate layer; the structured
data in this repository, timestamped at the moment of commit, is itself the
invalidity-contention material that future challenges will draw from.

The corpus serves three functions, in priority order:

1. **Defensive publication.** Every entry, at the moment of merge and timestamp,
   is a public disclosure of the engineering, design, and prior art it describes.
   `prior_art_notes` is not editorial commentary — it is the element-by-element
   analysis a competent examiner or invalidity-contention attorney could cite.
2. **Design space map.** What has been imagined, what has been built, what has
   been claimed, and where the gaps are.
3. **Citation graph.** Who built on whom, what lineage each design belongs to,
   what intellectual debts are owed.

## Quality bar for entries

An entry is not done when the schema fields are filled. An entry is done when:

- `disclosure_citation` resolves to a primary source verifiable by a third party.
- `first_disclosure_date` is defensible against challenge — earliest verifiable
  public disclosure, not earliest plausible date.
- `prior_art_notes` reads as a 102/103 anticipation analysis someone unrelated
  to us could cite without rewriting. It identifies specific subsystems disclosed
  and what claims those disclosures could anticipate.
- `sources` cite primary references (papers, books, patents, episodes), not
  Wikipedia or aggregators, except where the aggregator is itself the primary
  source.
- For patented entries, `ip_citations` lists actual patent numbers, and
  `prior_art_notes` points back at anticipating prior art entries by id.

Entries below this bar may be merged with a `draft: true` flag to make
incremental progress visible, but they do not yet count as commons material.

## License posture

CC0-1.0. The corpus itself is public domain dedication. Individual entries cite
their sources but the structured catalog is unencumbered.

## Timestamping

Because the corpus is the commons, the timestamp of disclosure for each entry
must be defensible. Git commit timestamps alone are insufficient for legal
purposes — they can be rewritten and are not third-party attested.

Required timestamping infrastructure:

- **RFC 3161 timestamping** of every release tag via a recognized Time Stamping
  Authority (e.g., FreeTSA, DigiCert TSA). Signature artifacts committed
  alongside the release.
- **OpenTimestamps** anchoring of release commits to Bitcoin (free, decentralized,
  cryptographically strong attestation of pre-existence).
- **Periodic releases** tagged at minimum quarterly so that newly-merged entries
  receive third-party-attested timestamps within a bounded window.
- **Submission to discoverable indices**: Google Patents non-patent literature
  corpus, IP.com Prior Art Database (or its open equivalent), and any other
  indices examiners actually use.

A commons that examiners cannot find when searching does not invalidate anything.
Discoverability is not optional.

## Entry schema

Each entry is one record. Required fields are marked [R], optional [O].

```
id                      [R]  slug, kebab-case, globally unique within corpus
canonical_name          [R]  the name most commonly used in literature
aliases                 [O]  list of alternate names, model numbers, codenames
corpus                  [R]  one of: private | open | fictional | academic
first_disclosure_date   [R]  ISO 8601 date or year; earliest verifiable public reference
disclosure_citation     [R]  source for the first_disclosure_date (DOI, ISBN, URL, patent #, episode ID)
creator                 [R]  company / lab / studio / author / collective
creator_country         [O]  ISO country code of creator
morphology_family       [R]  see morphology taxonomy below
dof_count               [O]  total degrees of freedom if disclosed
actuator_type           [O]  electric | hydraulic | pneumatic | tendon | exotic | unknown | mixed
actuator_details        [O]  specific actuator IP / topology if disclosed
height_m                [O]  meters, if disclosed
mass_kg                 [O]  kilograms, if disclosed
payload_kg              [O]  kilograms, if disclosed
power_source            [O]  battery chemistry, fuel cell, tethered, fictional, etc.
runtime_minutes         [O]  if disclosed
end_effector            [O]  hand DoF, gripper type, tendon routing, etc.
control_architecture    [O]  MPC, RL policy, behavior tree, scripted, fictional, etc.
sensing                 [O]  cameras, LiDAR, IMUs, tactile, fictional sensors
notable_capabilities    [O]  list of disclosed/claimed capabilities
ip_status               [R]  patented | open-permissive | open-copyleft | public-domain | fictional | trade-secret | unknown
ip_citations            [O]  patent numbers, license identifiers, repo URLs
prior_art_notes         [O]  what subsystems/claims this entry could anticipate as 102/103 prior art
lineage_ancestors       [O]  ids of entries this design descends from
lineage_descendants     [O]  ids of entries that descend from this (filled in later passes)
sources                 [R]  list of citations (papers, books, articles, repos, episodes)
notes                   [O]  free-text observations
disclosed_subsystems    [O]  structured tags identifying specific subsystems disclosed
                             (see subsystem taxonomy below); enables targeted prior art search
cpc_classifications     [O]  CPC classification codes for examiner discoverability
                             (e.g., "B25J 9/00" for manipulators, "G05D 1/00" for autonomous control)
draft                   [O]  boolean; true if the entry has not yet cleared the quality bar
schema_version          [R]  integer matching schema spec version
last_updated            [R]  ISO 8601 date
```

## Morphology taxonomy

- `humanoid_bipedal` — two legs, two arms, head; the canonical form
- `humanoid_wheeled` — humanoid torso on wheeled base
- `humanoid_aquatic` — humanoid form for underwater operation
- `humanoid_partial` — torso/arms only, no locomotion
- `quadruped` — four-legged
- `quadruped_armed` — four-legged with manipulator arm(s)
- `hexapod` — six-legged
- `wheel_leg_hybrid` — articulated wheel-leg
- `tracked` — caterpillar tracks
- `aerial` — flying, includes drones and humanoid-aerial hybrids
- `serpentine` — snake-like
- `mecha` — humanoid form, piloted, typically fictional and large-scale
- `android` — humanoid form indistinguishable from human (fictional or aspirational)
- `cyborg` — biological substrate with mechanical augmentation
- `manipulator` — fixed-base or mobile-base arm only
- `swarm` — entity is a collective
- `transformer` — morphology changes between modes
- `other` — escape hatch with explanation in notes

## IP status definitions

- `patented` — known patents asserted, with patent numbers
- `open-permissive` — MIT, BSD, Apache, CERN-OHL-P, etc.
- `open-copyleft` — GPL, CERN-OHL-S, etc.
- `public-domain` — CC0 or equivalent dedication, or expired protection
- `fictional` — exists only in narrative; copyright on the depiction may exist but the engineering description is unencumbered as prior art
- `trade-secret` — claimed but not disclosed
- `unknown` — needs investigation

## Subsystem taxonomy

Tags applied to `disclosed_subsystems` to enable targeted prior art search. An
entry tags every subsystem it discloses with enough specificity to cite. Tags
are append-only to preserve cross-entry searchability.

**Actuators**
- `actuator-electric-direct-drive`
- `actuator-electric-quasi-direct-drive`
- `actuator-electric-harmonic-drive`
- `actuator-electric-cycloidal`
- `actuator-electric-planetary`
- `actuator-electric-series-elastic`
- `actuator-electric-tendon-driven`
- `actuator-hydraulic`
- `actuator-pneumatic`
- `actuator-pneumatic-muscle`
- `actuator-spherical-multi-dof`
- `actuator-bldc-controller`
- `actuator-foc-controller`

**Mechanism**
- `mechanism-bipedal-locomotion`
- `mechanism-quadrupedal-locomotion`
- `mechanism-wheel-leg-hybrid`
- `mechanism-wheeled-balancing`
- `mechanism-tendon-routing`
- `mechanism-anthropomorphic-hand`
- `mechanism-underactuated-grasping`
- `mechanism-compliant-spine`
- `mechanism-passive-dynamic-walking`

**Control**
- `control-zmp-balancing`
- `control-mpc`
- `control-reduced-order-model`
- `control-rl-policy`
- `control-sim-to-real`
- `control-behavior-tree`
- `control-hard-constraint-supervisor`
- `control-teleoperation`
- `control-vla-vision-language-action`

**Sensing**
- `sensing-stereo-camera`
- `sensing-monocular-depth`
- `sensing-lidar`
- `sensing-imu`
- `sensing-force-torque`
- `sensing-tactile-fingertip`
- `sensing-tactile-whole-body`
- `sensing-proprioceptive-actuator`

**Power and thermal**
- `power-li-ion`
- `power-li-po`
- `power-tethered`
- `power-fuel-cell`
- `power-hot-swap`
- `thermal-passive`
- `thermal-active-liquid`

**Software and middleware**
- `software-ros1`
- `software-ros2`
- `software-yarp`
- `software-openhrp`
- `software-mjbots-stack`

**Safety**
- `safety-hard-constraint`
- `safety-simplex-supervisor`
- `safety-watchdog`
- `safety-emergency-stop`
- `safety-collision-avoidance`

This taxonomy is expected to grow. New tags are added with provenance — the
first entry to introduce a tag documents it in `notes`.

## Storage format

Master corpus: `corpus.jsonl` — one JSON object per line, append-only, git-tracked.
Per-corpus mirrors: `private.jsonl`, `open.jsonl`, `fictional.jsonl`, `academic.jsonl`.
Index: `CORPUS_INDEX.md` — generated, alphabetical by canonical_name with id and one-line summary.
Lineage graph: `lineage.json` — derived, ancestor/descendant DAG.

## Versioning

Schema version increments on breaking changes. Entries carry `schema_version` so
older entries can be migrated. v0.1 is the starting point and should be expected
to evolve once the seed slice exposes inadequacies.
```
