# Reasoning About Physical Interactions with Object-Oriented Prediction and Planning

## Metadata

- Paper ID: P009
- Title: Reasoning About Physical Interactions with Object-Oriented Prediction and Planning
- Authors: Michael Janner et al.
- Citation key: janner2019_o2p2_prov
- Year: 2019
- Venue: ICLR
- arXiv ID: 1812.10972
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/1812.10972
- Category: object_centric_world_models
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

[CONFLICT: report notes an author-list inconsistency with the local BibTeX entry; CSV authors retained. Human verification needed.]

## One-sentence summary

O2P2 is an important object-centric world-model paper because it jointly learns perception, pairwise physics, and rendering using only **pixel supervision plus segments**, then demonstrates that the resulting representation is actually useful for planning. citeturn22view0turn23view0

## Problem setting

The paper asks whether physically useful object representations can be learned **without direct supervision of object properties**. For survey purposes, this directly targets a central problem in world modeling: how to obtain actionable, object-factorized latent structure from visual data with minimal annotation. citeturn22view0turn23view0

## Core idea

The paper’s most important contribution is the demonstration that an object-centric visual representation learned without object-property labels can be **good enough for planning**, not just for reconstruction. citeturn22view0turn24view0turn24view1

## Method

### Representation of the world

Representation: **object-centric latent state**. Each segmented object is encoded into a vector by a perception module; the model is trained only through reconstruction/prediction losses rather than labels for position, identity, or orientation. citeturn23view0

### Training objective

Perception, physics, and rendering are trained jointly with **image reconstruction and prediction losses**, combining pixel-space distance and a VGG-based perceptual loss. Different modules are indirectly supervised by reconstruction of the current image and prediction of the post-physics image. citeturn23view0

## Input and output

[TODO]

## Dynamics modeling

The physics module predicts the outcome of pairwise interactions plus unary transitions over object vectors. Importantly, the model predicts a **single steady-state post-physics configuration** rather than a full time-indexed rollout, because the planning task mainly needs the final stable arrangement. citeturn23view0

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

Training uses before/after images of blocks, with access to **segments or region proposals** in the initial frame. For planning, the model evaluates sampled block-placement actions in representation space, optionally via CEM, and can also transfer to a real Sawyer arm with an action embedder. citeturn23view0turn24view2

## Dataset and benchmark

Tasks: reconstruction/prediction on block-drop scenes; tower-building via planning from goal images; transfer to a Sawyer robot. Data: 60,000 MuJoCo-generated training images for synthetic block scenes. Metrics: tower-build accuracy, qualitative planning analysis, and real-robot success counts. O2P2 reports 76% synthetic tower-building accuracy and 17/25 correct on real-robot goals. citeturn24view0turn24view1turn24view2

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

O2P2 uses segmentation masks / object proposals, so it is not fully unsupervised. It predicts steady-state outcomes rather than long temporal rollouts, focuses on synthetic stacking rather than diverse natural videos, and its planner relies on fairly structured action spaces and object geometry. citeturn23view0turn24view1

## Relation to this survey

### Relation to the survey taxonomy

Roles: **object-centric dynamics; physical dynamics learning; latent world model for planning; interactive world model**.

### Comparison with nearby papers

Compared with **P008**, O2P2 needs less direct state supervision but more segmentation structure. Compared with **P007**, it is much closer to a visual world model and supports planning. Compared with **P005/P006**, it is more explicitly object-centric and planning-oriented, but less focused on realistic long-horizon video rollouts. citeturn19view0turn17view0turn15view0turn11view0

### Open questions raised by this paper

- Can object-centric planning work without segmentation masks or proposal boxes?
- How should one extend steady-state prediction to **long-horizon interactive simulation**?
- What is the best interface between learned object representations and **continuous robotic control**?

## Possible citation usage

This paper can be cited when discussing:

- Use when discussing minimally supervised object-centric world model learning.
- Use when contrasting full generative simulation with task-specific physical prediction.
- Use when arguing that representation structure matters for planning performance.

## Reliable claims extracted from this paper

- Claim: O2P2 learns perception, physics, and rendering jointly without direct supervision of object properties.  
  - Evidence from the paper: The abstract and Sec. 1–2 explicitly state this design goal and training setup. citeturn22view0turn23view0
  - Source location if available: Abstract; Sec. 1–2.
  - Suggested citation usage: Use when discussing minimally supervised object-centric world model learning.
  - Confidence: high

- Claim: The physics module predicts a final, steady-state configuration instead of a full temporal rollout.  
  - Evidence from the paper: Sec. 2.2 states that the model only needs a single prediction to estimate the steady-state result of simulating physics indefinitely. citeturn23view0
  - Source location if available: Sec. 2.2.
  - Suggested citation usage: Use when contrasting full generative simulation with task-specific physical prediction.
  - Confidence: high

- Claim: O2P2’s learned representation supports downstream planning better than an object-agnostic video predictor baseline in the tower task.  
  - Evidence from the paper: Table 1 reports 76% build accuracy for O2P2 versus 24% for SAVP and 0% for the no-physics ablation. citeturn24view1
  - Source location if available: Sec. 3.2; Table 1.
  - Suggested citation usage: Use when arguing that representation structure matters for planning performance.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
