---
title: control-vision-language
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-vision-language`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2022-04

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Flamingo (DeepMind multimodal VLM) (2022-04)

- **id**: `flamingo-alayrac-deepmind-2022`
- **corpus**: academic
- **creator**: DeepMind; Jean-Baptiste Alayrac, Karen Simonyan et al.
- **disclosure**: Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I., Hasson, Y., Lenc, K., Mensch, A., Millican, K., Reynolds, M., Ring, R., Rutherford, E., Cabi, S., Han, T., Gong, Z., Samangouei, S., Monteiro, M., Menick, J., Borgeaud, S., Brock, A., Nematzadeh, A., Sharifzadeh, S., Binkowski, M., Barreira, R., Vinyals, O., Zisserman, A., Simonyan, K. 'Flamingo: a Visual Language Model for Few-Shot Learning'. NeurIPS 2022. arXiv:2204.14198. DeepMind.
- **ip status**: trade-secret
- **prior art notes**: Flamingo (Alayrac et al. DeepMind NeurIPS 2022) is the foundational multimodal VLM. 3-year-deep public-disclosure prior art. The architectural ancestor of OpenFlamingo + RoboFlamingo (round-29) and the multimodal-VLM lineage that underlies many modern VLAs.

## SigLIP (2023-03)

- **id**: `siglip-zhai-2023`
- **corpus**: academic
- **creator**: Google Research; Zhai, Mustafa, Kolesnikov, Beyer
- **disclosure**: Zhai, X., Mustafa, B., Kolesnikov, A., Beyer, L. 'Sigmoid Loss for Language Image Pre-Training'. arXiv:2303.15343, March 2023. ICCV 2023. Google Research.
- **ip status**: open-permissive
- **prior art notes**: SigLIP is the canonical sigmoid-loss vision-language foundation model (Google ICCV 2023). 2-year-deep prior art for: sigmoid-loss contrastive vision-language training, large-batch-friendly training regime. The text-encoder backbone in OpenVLA, RADIO-ViPE, and many VLA systems. Direct shielding for any commercial humanoid claim on open-vocabulary text-image alignment for instruction following.

## AM-RADIO (NVIDIA) (2023-12)

- **id**: `nvidia-am-radio-2024`
- **corpus**: academic
- **creator**: NVIDIA Learning and Perception Research; Ranzinger, Heinrich, Kautz, Molchanov
- **disclosure**: Ranzinger, M., Heinrich, G., Kautz, J., Molchanov, P. 'AM-RADIO: Agglomerative Vision Foundation Model -- Reduce All Domains Into One'. arXiv:2312.06709, December 2023. CVPR 2024. NVIDIA Learning and Perception Research. RADIOv2.5 follow-up: arXiv:2412.07679 December 2024.
- **ip status**: open-permissive
- **prior art notes**: AM-RADIO is the canonical agglomerative-distillation vision foundation model (NVIDIA, CVPR 2024). 1.5-year-deep open-permissive prior art for: multi-teacher vision-foundation distillation, single-backbone CLIP+DINOv2+SAM amalgamation. **The literal embedding substrate of RADIO-ViPE** — the round-10 RADIO-ViPE entry's name comes from this. Direct shielding for any commercial humanoid claim on multi-modal vision-foundation backbones for onboard perception.
