# Search Queries and Search Protocol

## Survey Title

Learning Predictive World Models from Videos: A Survey on Generative Simulation and Physical Dynamics

## Purpose

This file records the search process used to build and expand the literature pool. It is not the final paper list. The final structured paper database is stored in `data/papers.csv`, and citation entries are stored in `bib/references.bib`.

## Round 1: Initial Deep Research Search

- Date: 2026-05-29
- Tool: ChatGPT Deep Research
- Output file: `data/deep-research-report.md`
- Resulting files:
  - `data/papers.csv`
  - `bib/references.bib`

### Main search goal

Build an initial verified paper pool for a survey on predictive world models from videos, with emphasis on video prediction, latent world models, diffusion-based video generation, generative simulation, physical dynamics learning, embodied world models, and evaluation benchmarks.

### Keyword groups

#### Predictive world models from video

- predictive world model video
- learning world models from videos
- video world model
- visual world model
- latent world model video
- future prediction from video

#### Video prediction and dynamics

- video prediction physical dynamics
- future frame prediction dynamics
- long-horizon video prediction
- stochastic video prediction
- object-centric video prediction
- visual dynamics model

#### Generative simulation

- generative simulation world model
- neural simulator video
- learned simulator from video
- generative simulator physical dynamics
- simulation from video

#### Diffusion and generative video world models

- diffusion video prediction
- diffusion world model
- video diffusion physical consistency
- generative video model dynamics
- diffusion models for physical dynamics

#### Embodied and interactive world models

- embodied world model
- action-conditioned video prediction
- interactive world model
- robotics world model from video
- policy learning with video world models

#### Evaluation and benchmarks

- benchmark video world model
- physical reasoning benchmark video generation
- evaluation of video prediction models
- physical consistency video generation

### Inclusion criteria

Include a paper if it satisfies at least one of the following:

- It learns predictive dynamics from videos or visual observations.
- It models future states, future frames, or latent future trajectories.
- It proposes a world model with visual, physical, or interactive dynamics.
- It uses generative models to simulate dynamic environments.
- It evaluates physical consistency, temporal consistency, or controllability in generated videos.
- It is a foundational paper needed to explain the development of this area.

### Exclusion criteria

Exclude or mark as low priority if:

- The paper is only about static image generation.
- The paper is only about language models with no visual/video world modeling component.
- The paper is a classical physics simulator without a learned visual model.
- The paper is a pure robotics control paper without video prediction, visual dynamics, or world modeling.
- The paper is only about generic text-to-video generation and has no clear connection to prediction, dynamics, simulation, or physical consistency.

### Round 1 notes

- Initial pool size: 40 papers.
- Main categories discovered:
  - video prediction
  - latent world models
  - object-centric world models
  - physical dynamics
  - diffusion world models
  - interactive world models
  - evaluation benchmarks
- Next search should focus on:
  - recent embodied video world models
  - controllable video generation as simulation
  - physical consistency metrics
  - survey papers on video prediction and world models
  - missing SIGGRAPH / CoRL / RSS papers