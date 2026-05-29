# Dream to Control: Learning Behaviors by Latent Imagination

## Metadata

- Paper ID: P002
- Title: Dream to Control: Learning Behaviors by Latent Imagination
- Authors: Danijar Hafner et al.
- Citation key: hafner2020_dreamer_prov
- Year: 2020
- Venue: ICLR
- arXiv ID: 1912.01603
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/1912.01603
- Category: latent_world_models
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

None.

## One-sentence summary

Dreamer shifts latent world modeling from online planning to **latent imagination with actor-critic learning**, making world models a scalable substrate for long-horizon behavior learning from images. citeturn25view0turn26view0turn28view0

## Problem setting

The paper asks how to derive strong long-horizon behaviors from a learned world model without relying on expensive online planning or short imagination horizons. This matters because predictive world models become substantially more usable once policy learning is amortized through imagination. citeturn25view0turn26view0

## Core idea

Its key contribution is making latent world models practical for **policy learning by imagination**, which strongly influenced later Dreamer variants and many contemporary world-model pipelines. citeturn26view0turn28view0

## Method

### Representation of the world

Representation: **latent state** using an RSSM world model inherited from PlaNet-style reconstruction learning, though the paper also discusses contrastive alternatives. The agent imagines trajectories in compact latent state space rather than in pixels. citeturn28view1turn26view0

### Training objective

The world model can be trained with reconstruction ELBO-style losses or alternative representation-learning objectives; the actor maximizes imagined value estimates, and the critic regresses λ-return-like value targets. The world model is held fixed while behavior is updated. citeturn26view0turn28view1

## Input and output

[TODO]

## Dynamics modeling

The world model predicts next latent states and rewards; the actor and critic then learn from imagined latent trajectories. Values account for rewards beyond the finite imagination horizon, and gradients are backpropagated analytically through the imagined dynamics and action samples. citeturn26view0

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

The model is conditioned on **actions** and predicts **rewards**; in some settings it also predicts discounts for early termination. Dreamer executes a learned action model in the environment, rather than performing CEM-style online search at test time. citeturn26view0

## Dataset and benchmark

Tasks: 20 visual DeepMind Control Suite tasks, with additional discrete-action / early-termination experiments on subsets of Atari and DeepMind Lab in the appendix. Metrics: task return, data efficiency, and training time; the paper reports superior average performance relative to PlaNet and strong model-free baselines under matched image-input settings. citeturn25view0turn28view0

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

Dreamer still depends on the quality of the learned latent model and is centered on RL reward optimization rather than general-purpose generative simulation. The paper also evaluates mostly through return, so it says less about physical faithfulness, causal consistency, or open-world video realism. citeturn28view0turn28view1

## Relation to this survey

### Relation to the survey taxonomy

Roles: **latent world model for planning; embodied world model**.

### Comparison with nearby papers

Compared with **P001**, Dreamer replaces online CEM planning with a learned actor-critic. Compared with **P003**, it uses a more principled RSSM-style world model and gradient-based behavior learning. Compared with **P012**, Dreamer remains a latent-state world model rather than an image-space diffusion simulator. citeturn26view1turn8view0turn31view1

### Open questions raised by this paper

- How can imagination-based agents be evaluated for **simulation fidelity**, not only return?
- When do latent models omit visual details that later prove behaviorally necessary?
- How should latent imagination handle **multi-modal physical futures** and heavy partial observability?

## Possible citation usage

This paper can be cited when discussing:

- Use when discussing amortized policy learning in world models.
- Use when contrasting gradient-based imagination learning with derivative-free planning/evolution.
- Use when citing Dreamer as a major empirical milestone in latent world-model RL.

## Reliable claims extracted from this paper

- Claim: Dreamer learns behavior purely through latent imagination.  
  - Evidence from the paper: The abstract and Sec. 3 state that Dreamer learns behaviors from imagined latent trajectories rather than direct environment interaction alone. citeturn25view0turn26view0
  - Source location if available: Abstract; Sec. 3.
  - Suggested citation usage: Use when discussing amortized policy learning in world models.
  - Confidence: high

- Claim: Dreamer uses analytic gradients through imagined trajectories for policy learning.  
  - Evidence from the paper: Sec. 3 explains reparameterized action samples and stochastic backpropagation through states, rewards, values, and actions. citeturn26view0
  - Source location if available: Sec. 3.
  - Suggested citation usage: Use when contrasting gradient-based imagination learning with derivative-free planning/evolution.
  - Confidence: high

- Claim: Dreamer outperforms prior methods on 20 visual control tasks in data efficiency and final performance.  
  - Evidence from the paper: The abstract and control-task section summarize this result on DeepMind Control Suite image-based tasks. citeturn25view0turn28view0
  - Source location if available: Abstract; Sec. 6.
  - Suggested citation usage: Use when citing Dreamer as a major empirical milestone in latent world-model RL.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
