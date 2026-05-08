---
title: "control-generative-model"
parent: "Invalidity Contentions"
nav_order: 44
layout: default
---

# Invalidity Contention Packet — `control-generative-model`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-generative-model`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2013-12  
**Most recent disclosure:** 2020-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-generative-model`.

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

### 2013-12 — Variational Autoencoder (VAE)

- **id:** `vae-kingma-iclr-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Amsterdam; Diederik P. Kingma, Max Welling
- **disclosure citation:** Kingma, D. P., Welling, M. 'Auto-Encoding Variational Bayes'. ICLR 2014. arXiv:1312.6114. University of Amsterdam.
- **disclosed subsystems:** `control-generative-model`, `control-variational-inference`, `control-latent-space`

**Prior art notes:**

> VAE (Kingma + Welling ICLR 2014) is the foundational variational autoencoder paper. 11-year-deep public-domain prior art. The architectural ancestor of ASE latent skill embeddings (round-27) and every VAE-based generative model. Direct shielding for any commercial humanoid claim using latent-space policy methods.

**Sources:**

1. Kingma, D. P., Welling, M. arXiv:1312.6114 ICLR 2014.

---

### 2014-06 — Generative Adversarial Networks (GAN)

- **id:** `gan-goodfellow-nips-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Université de Montréal; Ian Goodfellow, Yoshua Bengio et al.
- **disclosure citation:** Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., Bengio, Y. 'Generative Adversarial Networks'. NeurIPS 2014. arXiv:1406.2661. Université de Montréal.
- **disclosed subsystems:** `control-generative-model`, `control-adversarial-training`

**Prior art notes:**

> GAN (Goodfellow et al. NeurIPS 2014) is the foundational generative-adversarial-networks paper. 11-year-deep public-domain prior art. >70,000 citations. **The architectural ancestor of AMP (round-21) + ASE (round-27)** adversarial-loss motion-imitation lineage. Direct shielding for any commercial humanoid claim using GAN-style adversarial training.

**Sources:**

1. Goodfellow et al. arXiv:1406.2661 NeurIPS 2014.

---

### 2020-06 — Denoising Diffusion Probabilistic Models (DDPM)

- **id:** `ddpm-ho-neurips-2020`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** UC Berkeley; Jonathan Ho, Ajay Jain, Pieter Abbeel; antecedent: Stanford Sohl-Dickstein 2015
- **disclosure citation:** Ho, J., Jain, A., Abbeel, P. 'Denoising Diffusion Probabilistic Models'. NeurIPS 2020. arXiv:2006.11239. UC Berkeley. The antecedent: Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S. 'Deep Unsupervised Learning using Nonequilibrium Thermodynamics'. ICML 2015 (the original diffusion model paper).
- **disclosed subsystems:** `control-foundation-model`, `control-diffusion-policy`, `control-generative-model`

**Prior art notes:**

> DDPM (Ho et al. NeurIPS 2020) is the foundational modern diffusion-models paper. 5-year-deep public-domain prior art. **Direct architectural ancestor of Diffusion Policy (corpus), DP3 (round-17), RDT-1B (round-13), π₀ (round-12)** — every diffusion-based VLA + manipulation policy. Direct shielding for any commercial humanoid claim on diffusion-based action generation. Closes a major foundational citation chain.

**Sources:**

1. Ho, Jain, Abbeel. arXiv:2006.11239 NeurIPS 2020.
2. Sohl-Dickstein et al. ICML 2015 (diffusion antecedent).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf3c8f5`.*
