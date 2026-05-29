# Visual Interaction Networks

## Metadata

- Paper ID: P008
- Title: Visual Interaction Networks
- Authors: Nicholas Watters et al.
- Citation key: watters2017_visual_interaction_networks_prov
- Year: 2017
- Venue: NeurIPS
- arXiv ID: 1706.01433
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/1706.01433
- Category: physical_dynamics
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

None.

## One-sentence summary

VIN is a crucial step toward visual world models because it couples a learned visual encoder with interaction-network dynamics, showing how **object-centric physical prediction can be learned from video-like inputs**. citeturn19view0turn20view0

## Problem setting

The paper addresses prediction of future physical states from raw visual observations, aiming to build a model that can infer object states and then roll them forward under interactions. This matters because predictive world models need a bridge from pixels to structured physical dynamics. citeturn19view0

## Core idea

Its main contribution is demonstrating that a model can jointly learn **visual perception plus relational physical rollout**, and in some rollout metrics even outperform state-to-state baselines despite only observing images. citeturn20view0turn20view1

## Method

### Representation of the world

Representation: **object-centric latent state**. A visual encoder maps short frame triplets into a state code containing one slot per object; a linear decoder maps each slot to position/velocity. This is latent, but explicitly factored by object. citeturn19view0

### Training objective

The model is trained to predict **eight unseen future states**, with a normalized weighted sum of rollout losses plus an auxiliary encoder loss. The rollout weighting schedule gradually increases emphasis on farther future predictions. citeturn20view0turn20view1

## Input and output

[TODO]

## Dynamics modeling

Dynamics are predicted by an interaction-network-based recurrent predictor with multiple temporal offsets, whose candidate next-state codes are aggregated by an MLP. Future trajectories are produced by recurrent rollout in state-code space. citeturn19view0turn20view1

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

There are no explicit actions in the main benchmarks. Interaction is entirely among objects through learned relational dynamics; some datasets include hidden objects or variable masses that must be inferred from visual evidence and interactions. citeturn19view0turn20view1

## Dataset and benchmark

Datasets/tasks: simulated 2D spring, gravity, billiards, magnetic billiards, drift, invisible-object springs, and variable-mass settings with natural-image backgrounds. Metrics: Inverse Normalized Loss, Euclidean prediction error on long rollouts, and qualitative rendered rollout trajectories. citeturn19view0turn20view0turn20view2

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

VIN still uses supervised object-state targets during training, so it is not fully unsupervised from video. Its environments are visually simple synthetic physics scenes, and the object count is fixed within each dataset, leaving open the harder problems of open-world segmentation, appearance variation, and embodied control. citeturn19view0turn20view0

## Relation to this survey

### Relation to the survey taxonomy

Roles: **object-centric dynamics; physical dynamics learning**.

### Comparison with nearby papers

Compared with **P007**, VIN adds the visual front-end needed to start from images. Compared with **P009**, VIN still uses supervised state targets whereas O2P2 relaxes object-property supervision. Compared with **P005/P006**, VIN is much more explicitly object-relational but also less realistic in visual complexity. citeturn17view0turn23view0turn15view0turn11view0

### Open questions raised by this paper

- Can object slots and state targets be learned **without state supervision**?
- How well do object-centric latent dynamics survive realistic clutter, occlusion, and camera motion?
- What is the right evaluation for long rollouts when trajectory identity diverges but **physical plausibility** remains high?

## Possible citation usage

This paper can be cited when discussing:

- Use when describing visually grounded object-centric world models.
- Use when arguing that structured dynamics can support latent physical inference, not only forward extrapolation.
- Use when motivating robustness advantages of jointly training perception and dynamics.

## Reliable claims extracted from this paper

- Claim: VIN combines a CNN-based visual encoder with an interaction-network dynamics predictor.  
  - Evidence from the paper: The abstract and model section explicitly describe a perceptual front-end and an IN-based dynamics module. citeturn19view0
  - Source location if available: Abstract; Sec. 2.
  - Suggested citation usage: Use when describing visually grounded object-centric world models.
  - Confidence: high

- Claim: VIN can infer hidden physical causes such as invisible objects and unknown mass from their visual effects.  
  - Evidence from the paper: The abstract and experiments emphasize invisible-object and variable-mass settings; the results report strong performance even in the invisible spring condition. citeturn19view0turn20view0
  - Source location if available: Abstract; Sec. 4.1.
  - Suggested citation usage: Use when arguing that structured dynamics can support latent physical inference, not only forward extrapolation.
  - Confidence: high

- Claim: VIN outperforms pixel-to-state and even state-to-state baselines on long rollout position error.  
  - Evidence from the paper: Sec. 4.2 reports lower Euclidean prediction error over 50-step rollouts than both visual and privileged-state baselines. citeturn20view0turn20view1
  - Source location if available: Sec. 4.2.
  - Suggested citation usage: Use when motivating robustness advantages of jointly training perception and dynamics.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
