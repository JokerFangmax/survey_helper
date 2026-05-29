# Stochastic Variational Video Prediction

## Metadata

- Paper ID: P006
- Title: Stochastic Variational Video Prediction
- Authors: Mohammad Babaeizadeh et al.
- Citation key: babaeizadeh2018_sv2p_prov
- Year: 2018
- Venue: ICLR
- arXiv ID: 1710.11252
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/1710.11252
- Category: video_prediction
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

None.

## One-sentence summary

SV2P is a key stochastic future-modeling paper because it inserts latent variables into multi-frame video prediction and shows that world models should represent **distributions over futures**, not only deterministic rollouts. citeturn3academia3turn11view0

## Problem setting

The paper addresses the mismatch between deterministic video prediction and real-world stochasticity, including in action-conditioned settings. This is central for predictive world models because ambiguity, hidden variables, and partial observability all make single-future rollouts physically and behaviorally misleading. citeturn11view0

## Core idea

Its main contribution is demonstrating that **latent-variable stochastic multi-frame video prediction** can work on real-world datasets, not only synthetic sprites, and that deterministic baselines systematically blur away physically relevant uncertainty. citeturn11view0turn12view2

## Method

### Representation of the world

Representation: **pixel space + latent stochastic variables**. The generative backbone is based on CDNA-style image prediction, but the future is conditioned on sampled latent variables, either time-invariant per video or time-varying per frame. citeturn11view0turn12view0

### Training objective

Training uses a **variational lower bound** with reconstruction and KL terms, plus a three-phase procedure: deterministic generative pretraining, inference-network training without KL, then gradual KL activation. This schedule is introduced because naïve training tends to ignore the latent variables. citeturn11view0turn12view0

## Input and output

[TODO]

## Dynamics modeling

The model predicts future frames autoregressively using a stochastic latent variable model. A variational inference network conditions on future frames during training to infer posterior latents; at test time, latents are sampled from the prior to generate multiple plausible futures. citeturn11view0

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

SV2P supports both **action-free** and **action-conditioned** prediction. In action-conditioned settings, it still models residual stochasticity when actions do not fully determine outcomes. citeturn10view0turn11view0

## Dataset and benchmark

Datasets/tasks: a toy stochastic movement dataset, BAIR robot pushing (action-conditioned and action-free), Human3.6M, and the earlier robotic pushing prediction dataset used for comparing against VPN. Metrics: PSNR and SSIM, including “best of N samples” style evaluation for stochastic models, plus qualitative diversity/consistency checks. citeturn12view2turn12view3turn13view0

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

The model still predicts in pixel space and relies on “best sample” metrics that only partially solve the evaluation problem for stochastic futures. It does not disentangle object-level or physical state, and the posterior uses future frames during training, which highlights a train-test gap that later latent world models address differently. citeturn11view0turn13view0

## Relation to this survey

### Relation to the survey taxonomy

Roles: **stochastic future modeling; interactive world model**.

### Comparison with nearby papers

Compared with **P004** and **P005**, SV2P explicitly models multi-modal futures. Compared with **P001/P002**, however, it still remains primarily a pixel-space video predictor rather than a compact latent world model for control. citeturn16view0turn15view0turn26view1turn26view0

### Open questions raised by this paper

- How should stochastic video models be evaluated without relying on “best of many samples” heuristics?
- Can latent stochasticity be tied to **objects, forces, or hidden physical variables** rather than global noise?
- How should long-horizon stochastic rollouts be constrained for **physical consistency**?

## Possible citation usage

This paper can be cited when discussing:

- Use when motivating stochastic rather than deterministic future prediction.
- Use when discussing optimization difficulties in stochastic video prediction.
- Use when discussing design trade-offs in stochastic latent dynamics.

## Reliable claims extracted from this paper

- Claim: SV2P is designed to produce different plausible futures from different latent samples.  
  - Evidence from the paper: The abstract and Sec. 1 explicitly frame SV2P as a stochastic variational video predictor that generates different plausible futures from latent samples. citeturn10view0turn11view0
  - Source location if available: Abstract; Sec. 1.
  - Suggested citation usage: Use when motivating stochastic rather than deterministic future prediction.
  - Confidence: high

- Claim: The model uses a variational objective and a staged training scheme because naïve end-to-end training tends to ignore the latents.  
  - Evidence from the paper: Sec. 3 derives the variational objective; Sec. 3.2 gives the three-phase training schedule and explains why it is needed. citeturn11view0turn12view0
  - Source location if available: Sec. 3; Sec. 3.2.
  - Suggested citation usage: Use when discussing optimization difficulties in stochastic video prediction.
  - Confidence: high

- Claim: Time-varying latents help long-horizon stability on some datasets, while time-invariant latents can work better when the key latent factor is persistent.  
  - Evidence from the paper: The quantitative section reports that time-varying latent sampling is more stable beyond the training horizon, but time-invariant latent performs better on Human3.6M where action identity persists over the whole video. citeturn13view0
  - Source location if available: Sec. 5.2.
  - Suggested citation usage: Use when discussing design trade-offs in stochastic latent dynamics.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
