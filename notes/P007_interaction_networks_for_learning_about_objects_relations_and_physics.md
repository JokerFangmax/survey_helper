# Interaction Networks for Learning about Objects, Relations and Physics

## Metadata

- Paper ID: P007
- Title: Interaction Networks for Learning about Objects, Relations and Physics
- Authors: Peter W. Battaglia et al.
- Citation key: battaglia2016_interaction_networks_prov
- Year: 2016
- Venue: NeurIPS
- arXiv ID: 1612.00222
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/1612.00222
- Category: generative_simulation
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

None.

## One-sentence summary

Interaction Networks are a canonical object-relational dynamics model that established the idea that learned world models can act like a **general-purpose, learnable physics engine** over objects and relations. citeturn17view0turn18view0

## Problem setting

The paper addresses physical prediction and abstract property estimation in systems where dynamics are driven by pairwise or structured object interactions. For survey purposes, it matters because many later visual world models inherit its premise that good dynamics models should be **object- and relation-centric**, not monolithic pixel predictors. citeturn17view0turn17view1

## Core idea

The key contribution is the explicit decomposition of dynamics into **relation-centric interaction functions and object-centric update functions**, which became one of the most influential templates for physical world modeling. citeturn17view1turn18view0

## Method

### Representation of the world

Representation: **graph / relational state** over explicit objects. Inputs are attributed objects, attributed directed relations, and external effects; the model reasons over a multigraph rather than pixels or generic latent vectors. citeturn17view1turn18view0

### Training objective

Training and testing use **mean squared error** on target physical quantities such as next-step velocities or potential energy. Regularization and some training noise were explored to improve generalization and rollout realism. citeturn18view0

## Input and output

[TODO]

## Dynamics modeling

Dynamics are modeled by a relation network that computes per-edge interaction effects and an object network that aggregates these effects with per-object state and external input to predict next-step object velocities or other outputs. Multi-step simulation is obtained by iterating one-step predictions. citeturn17view1turn18view0

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

The model can condition on **external effects** such as gravitational acceleration or control-like inputs applied to each object. Interactions among objects are explicit and central to the model design. citeturn17view1turn17view2

## Dataset and benchmark

Domains: n-body gravity, bouncing balls, and spring-string systems with collisions. Tasks: next-step prediction, long rollout simulation, and potential-energy estimation. Metrics: test MSE on targets and qualitative/quantitative rollout fidelity, including generalization to new numbers of objects and configurations. citeturn17view2turn18view0

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

The model assumes an explicit object graph and ground-truth state-like inputs rather than learning directly from video, so it is not itself a video world model. Its impressive long rollouts still accumulate error in nonlinear regimes, and its evaluation stays within synthetic physics settings rather than embodied, partially observed visual environments. citeturn17view3turn18view0

## Relation to this survey

### Relation to the survey taxonomy

Roles: **object-centric dynamics; physical dynamics learning**.

### Comparison with nearby papers

Compared with **P004–P006**, P007 is not pixel-based and does not learn from video; compared with **P008**, it provides the relational dynamics core that VIN adds visual perception to; compared with **P009**, it does not solve planning from images but strongly informs the physics module design. citeturn16view0turn15view0turn11view0turn19view0turn23view0

### Open questions raised by this paper

- How can object graphs be learned directly from raw video rather than assumed?
- Which relational biases remain helpful once observations become **partial, cluttered, or noisy**?
- How should graph-based physical simulators be connected to **action selection and planning** in visual environments?

## Possible citation usage

This paper can be cited when discussing:

- Use when motivating graph-based world models and relational inductive bias.
- Use when arguing that object-relational factorization improves combinatorial generalization.
- Use when discussing long-horizon rollout potential of structured dynamics models.

## Reliable claims extracted from this paper

- Claim: Interaction Networks operate on objects and relations represented as a graph.  
  - Evidence from the paper: Sec. 2 defines the system as an attributed directed multigraph with object states, relations, and external effects. citeturn17view1
  - Source location if available: Sec. 2.
  - Suggested citation usage: Use when motivating graph-based world models and relational inductive bias.
  - Confidence: high

- Claim: The model generalizes to different numbers and configurations of objects.  
  - Evidence from the paper: The experiments explicitly test training on one system size and evaluating on smaller/larger systems; the paper reports effective generalization. citeturn17view2turn17view3
  - Source location if available: Sec. 3–4.
  - Suggested citation usage: Use when arguing that object-relational factorization improves combinatorial generalization.
  - Confidence: high

- Claim: One-step-trained INs can still produce long rollouts over thousands of steps that remain visually plausible.  
  - Evidence from the paper: The results section states that single-step-trained models can simulate trajectories over thousands of steps effectively, especially in n-body and string domains. citeturn17view3
  - Source location if available: Sec. 4.
  - Suggested citation usage: Use when discussing long-horizon rollout potential of structured dynamics models.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
