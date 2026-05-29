# Genie: Generative Interactive Environments

## Metadata

- Paper ID: P013
- Title: Genie: Generative Interactive Environments
- Authors: Jake Bruce et al.
- Citation key: bruce2024_genie_prov
- Year: 2024
- Venue: ICML
- arXiv ID: 2402.15391
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/2402.15391
- Category: interactive_world_models
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

None.

## One-sentence summary

Genie pushes world modeling toward foundation-style interactive generation by learning **frame-level controllability from unlabeled internet video** through discrete latent actions rather than ground-truth action labels. citeturn5view0turn6view0

## Problem setting

The paper asks whether one can train an interactive, controllable environment model from **video-only data**, without action annotations. This matters greatly for predictive world models because internet-scale video is abundant while action-labeled embodied data is scarce. citeturn5view0turn6view0

## Core idea

The key contribution is showing that **interactive controllability can be learned without action supervision**, which is a major conceptual expansion of what counts as a world model. citeturn5view0turn6view0

## Method

### Representation of the world

Representation: **token space + latent action space**. Genie tokenizes video into discrete spatiotemporal tokens with a VQ-VAE-like tokenizer, and separately learns a small discrete latent action codebook inferred from videos. citeturn6view0turn33view1

### Training objective

Training proceeds in two phases: first the video tokenizer with a VQ-VAE objective, then co-training of the latent action model and the dynamics model. The latent action model uses a VQ-VAE objective; the dynamics model uses cross-entropy on next-frame tokens. Metrics include FVD for fidelity and a controllability metric based on PSNR differences between ground-truth-inferred vs random latent actions. citeturn6view0turn33view1turn34view3

## Input and output

[TODO]

## Dynamics modeling

The dynamics model is a decoder-only **MaskGIT-style autoregressive next-frame token predictor** over tokenized frames, conditioned on latent action embeddings. At inference, the user supplies discrete latent actions and the model iteratively generates the next frame tokens and decodes them to pixels. citeturn6view0turn33view2

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

The model is conditioned on **prompt images / frames** and **learned latent actions** rather than real actions. It can be prompted by text, images, photos, or sketches at the interface level, but the core training is video-only and action-free. citeturn5view0turn6view0

## Dataset and benchmark

Training/eval settings include hundreds of 2D platformer games from internet gameplay videos, a curated 30,000-hour platformer subset drawn from a larger 200,000-hour pool, and robotics videos including RT-1-style data. Metrics include FVD and controllability; imitation-from-observation analysis on CoinRun shows the latent-action policy can match an oracle BC model with as few as 200 expert samples for adaptation. citeturn33view0turn34view3turn34view1

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

Genie’s actions are latent and need post hoc interpretation, so controllability is not yet semantically grounded like real control inputs. It operates in relatively structured domains such as platformers and robotics clips, and physical faithfulness is not the main evaluation target. citeturn33view1turn34view3

## Relation to this survey

### Relation to the survey taxonomy

Roles: **interactive world model; embodied world model**.

### Comparison with nearby papers

Compared with **P012**, Genie is not an RL world model benchmarked on Atari but a video-only interactive generator. Compared with **P001/P002**, it abandons explicit reward-conditioned control in favor of unsupervised latent controllability. Compared with **P009**, it needs less object-level structure but also offers weaker explicit physical semantics. citeturn31view0turn26view1turn26view0turn23view0

### Open questions raised by this paper

- How can latent actions be mapped to **semantically meaningful control variables**?
- How stable are Genie-style interactive environments over **long horizons and persistent causal interaction**?
- What benchmarks should measure **physical consistency** in action-free interactive generators?

## Possible citation usage

This paper can be cited when discussing:

- Use when discussing action-free learning of controllable environments.
- Use when describing architectural ingredients of interactive generative environments.
- Use when arguing that latent-action world models can support agent training beyond generation alone.

## Reliable claims extracted from this paper

- Claim: Genie is trained from unlabeled video without ground-truth action labels.  
  - Evidence from the paper: The abstract and methodology explicitly say Genie is trained unsupervised from video-only data and learns latent actions without action labels. citeturn5view0turn6view0turn33view1
  - Source location if available: Abstract; Sec. 2.1.
  - Suggested citation usage: Use when discussing action-free learning of controllable environments.
  - Confidence: high

- Claim: Genie combines a spatiotemporal tokenizer, latent action model, and MaskGIT dynamics model.  
  - Evidence from the paper: The abstract and method section list these three components and describe their training/inference roles. citeturn5view0turn6view0turn33view2
  - Source location if available: Abstract; Sec. 2.
  - Suggested citation usage: Use when describing architectural ingredients of interactive generative environments.
  - Confidence: high

- Claim: Latent actions learned from video can support downstream imitation, reaching oracle-level CoinRun performance with very few expert samples.  
  - Evidence from the paper: The CoinRun behavioral-cloning result says the LAM-based policy matches the oracle with as few as 200 expert samples for adaptation. citeturn34view1
  - Source location if available: Sec. 3 / Fig. 14.
  - Suggested citation usage: Use when arguing that latent-action world models can support agent training beyond generation alone.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
