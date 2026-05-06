<!--
Thank you for contributing to the Free Humanoid Corpus.

The corpus is the prior art commons. Every entry is a defensive
publication artifact, not a Wikipedia entry. This template helps you
ship a contribution that holds up under that bar.
-->

## Summary

<!-- One or two sentences. What does this PR add, change, or remove? -->

## Type

- [ ] New entry
- [ ] Strengthen an existing entry (mark which one)
- [ ] Schema change (link discussion / RFC)
- [ ] Tooling fix
- [ ] Documentation
- [ ] Other (describe)

## Checklist for new entries

If this PR adds a new entry, please confirm before merge:

- [ ] **`disclosure_citation`** resolves to a primary source verifiable by a third party (paper, book, patent number, episode, code commit). Not Wikipedia, not aggregator URL.
- [ ] **`first_disclosure_date`** is the earliest verifiable public disclosure, defensible against challenge.
- [ ] **`prior_art_notes`** reads as element-by-element 102/103 anticipation analysis a competent examiner could cite without rewriting. It identifies specific subsystems disclosed and what claims those disclosures could anticipate.
- [ ] **`sources`** is a non-empty list of primary references.
- [ ] **`disclosed_subsystems`** uses tags from the existing taxonomy where possible (see `cross_cuts/` for the current set). New tags require justification.
- [ ] For patented entries: **`ip_citations`** lists actual patent numbers, and `prior_art_notes` points back at anticipating prior art entries by id.
- [ ] **`lineage_ancestors`** / **`lineage_descendants`** populated when applicable. Run `python3 tools/index.py .` and check for unresolved references.
- [ ] If the entry does not yet clear the quality bar, **`draft: true`** is set, and the work needed to clear the bar is documented in the entry's `notes` field.

## Validation

Please confirm both pass locally:

- [ ] `python3 tools/validate.py corpus.jsonl --strict` exits 0.
- [ ] `python3 tools/index.py .` reports 0 lineage warnings, 0 cycles. (If warnings, those are acceptable provided the referenced ids are intended for future entries — note them.)
- [ ] `python3 tools/cross_cuts.py` rebuilds without errors.
- [ ] `git diff` shows the regenerated `CORPUS_INDEX.md`, `lineage.json`, per-corpus mirrors, and `cross_cuts/` are committed alongside the entry change.

## Notes

<!--
Anything reviewers should know — provenance of citations, why a draft
flag is being kept, edge cases, etc.
-->

## License

By submitting this PR you agree to dedicate the contribution to the public domain under CC0 1.0. The corpus is structurally permissionless; there is no usage license to grant.
