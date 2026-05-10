---
title: "control-vision-language"
parent: "Invalidity Contentions"
nav_order: 137
layout: default
---

# Invalidity Contention Packet — `control-vision-language`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-vision-language`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2022-04  
**Most recent disclosure:** 2023-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-vision-language`.

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

### 2022-04 — Flamingo (DeepMind multimodal VLM)

- **id:** `flamingo-alayrac-deepmind-2022`
- **corpus:** academic
- **ip status:** trade-secret
- **creator:** DeepMind; Jean-Baptiste Alayrac, Karen Simonyan et al.
- **disclosure citation:** Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I., Hasson, Y., Lenc, K., Mensch, A., Millican, K., Reynolds, M., Ring, R., Rutherford, E., Cabi, S., Han, T., Gong, Z., Samangouei, S., Monteiro, M., Menick, J., Borgeaud, S., Brock, A., Nematzadeh, A., Sharifzadeh, S., Binkowski, M., Barreira, R., Vinyals, O., Zisserman, A., Simonyan, K. 'Flamingo: a Visual Language Model for Few-Shot Learning'. NeurIPS 2022. arXiv:2204.14198. DeepMind.
- **disclosed subsystems:** `control-foundation-model`, `control-vision-language`

**Prior art notes:**

> Flamingo (Alayrac et al. DeepMind NeurIPS 2022) is the foundational multimodal VLM. 3-year-deep public-disclosure prior art. The architectural ancestor of OpenFlamingo + RoboFlamingo (round-29) and the multimodal-VLM lineage that underlies many modern VLAs.

**Sources:**

1. Alayrac et al. arXiv:2204.14198 NeurIPS 2022.

---

### 2023-03 — SigLIP

- **id:** `siglip-zhai-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google Research; Zhai, Mustafa, Kolesnikov, Beyer
- **disclosure citation:** Zhai, X., Mustafa, B., Kolesnikov, A., Beyer, L. 'Sigmoid Loss for Language Image Pre-Training'. arXiv:2303.15343, March 2023. ICCV 2023. Google Research.
- **disclosed subsystems:** `control-vision-language`, `control-foundation-model-perception`

**Prior art notes:**

> SigLIP is the canonical sigmoid-loss vision-language foundation model (Google ICCV 2023). 2-year-deep prior art for: sigmoid-loss contrastive vision-language training, large-batch-friendly training regime. The text-encoder backbone in OpenVLA, RADIO-ViPE, and many VLA systems. Direct shielding for any commercial humanoid claim on open-vocabulary text-image alignment for instruction following.

**Sources:**

1. Zhai et al. arXiv:2303.15343 March 2023; ICCV 2023.
2. HuggingFace: huggingface.co/google/siglip-base-patch16-224 et al.

---

### 2023-12 — AM-RADIO (NVIDIA)

- **id:** `nvidia-am-radio-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA Learning and Perception Research; Ranzinger, Heinrich, Kautz, Molchanov
- **disclosure citation:** Ranzinger, M., Heinrich, G., Kautz, J., Molchanov, P. 'AM-RADIO: Agglomerative Vision Foundation Model -- Reduce All Domains Into One'. arXiv:2312.06709, December 2023. CVPR 2024. NVIDIA Learning and Perception Research. RADIOv2.5 follow-up: arXiv:2412.07679 December 2024.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-vision-language`, `control-multi-teacher-distillation`

**Prior art notes:**

> AM-RADIO is the canonical agglomerative-distillation vision foundation model (NVIDIA, CVPR 2024). 1.5-year-deep open-permissive prior art for: multi-teacher vision-foundation distillation, single-backbone CLIP+DINOv2+SAM amalgamation. **The literal embedding substrate of RADIO-ViPE** — the round-10 RADIO-ViPE entry's name comes from this. Direct shielding for any commercial humanoid claim on multi-modal vision-foundation backbones for onboard perception.

**Sources:**

1. Ranzinger et al. arXiv:2312.06709 December 2023; CVPR 2024.
2. Heinrich et al. RADIOv2.5 arXiv:2412.07679 December 2024.
3. HuggingFace: huggingface.co/nvidia/RADIO.
4. Project page: research.nvidia.com/labs/lpr/publication/ranzinger2024radio/.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `7ee2634`.*
