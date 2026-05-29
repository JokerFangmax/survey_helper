# Survey-Oriented Paper Notes for Predictive World Models from Videos

## Usage Note

The notes below follow your requested repository-oriented structure, but I compress subsection titles into bold labels to keep the whole batch manageable. For **BibTeX key** and **Current category**, I use your local inventory. For **venue**, I keep your local entry when the primary source I checked was an arXiv/ar5iv page rather than an official proceedings page; when I saw possible ambiguity, I mark it explicitly. Primary claims are grounded in paper sources, mainly arXiv abstract pages and ar5iv HTML renderings of the papers. citeturn25view1turn25view0turn22view0turn5view0turn5view1

## Foundations of Action-Conditional Video Prediction

### Paper Note: P004 Action-Conditional Video Prediction using Deep Networks in Atari Games

**Metadata**

- Paper ID: P004
- Title: *Action-Conditional Video Prediction using Deep Networks in Atari Games*. citeturn2academia1turn9view0
- Authors: Junhyuk Oh, Xiaoxiao Guo, Honglak Lee, Richard L. Lewis, Satinder Singh. citeturn2academia1turn9view0
- Year: 2015
- Venue: NeurIPS
- URL: arXiv abstract page. citeturn2academia1turn9view0
- arXiv ID / DOI: arXiv:1507.08750. citeturn9view0
- BibTeX key: `oh2015_action_conditional_video_prediction_prov`
- Current category: `video_prediction`

**One-sentence survey summary**

An early landmark in predictive world modeling, this paper shows that high-dimensional future video can be predicted **conditioned on control actions**, making video prediction explicitly relevant to model-based decision making rather than only passive forecasting. citeturn2academia1turn9view0turn16view0

**Problem setting**

The paper studies action-conditioned future frame prediction in Atari games, where future observations depend on both prior frames and action inputs. This matters for world models because it turns video prediction into a learned transition model for agent–environment interaction, not just a passive next-frame estimator. citeturn9view0

**Representation of the world**

Representation: **pixel space + learned feature space**. The model encodes recent frames into high-level features with CNNs or CNN+LSTM, applies an action-conditional transformation in feature space, and decodes back to pixels. It is not object-centric and not latent-state planning in the later PlaNet/Dreamer sense. citeturn9view0turn16view0

**Dynamics modeling**

Temporal evolution is modeled with two architectures: a feedforward encoder using stacked recent frames, and a recurrent encoder using an LSTM over per-frame features. Actions enter through a multiplicative transformation layer that modulates latent features before deconvolution to the next frame; multi-step rollouts are obtained by recursively feeding predictions back in. citeturn9view0turn16view0

**Conditioning and interaction**

The model is explicitly conditioned on **discrete Atari actions** as one-hot vectors, plus previous frames. It does not model rewards directly, though the authors evaluate whether predicted frames are useful for DQN control and informed exploration. citeturn9view0turn16view1turn16view2

**Training objective**

Main training uses average multi-step **squared pixel error**, with curriculum learning over increasing rollout length, optimized by BPTT. The curriculum is important because single-step training causes compounding errors at rollout time. citeturn16view0

**Evaluation**

Datasets/tasks: Atari ALE games including Seaquest, Space Invaders, Freeway, Q*Bert, and Ms. Pac-Man. Metrics: long-horizon mean squared prediction error, qualitative rollouts, DQN score when emulator frames are replaced by predicted frames, and DQN performance under informed exploration. citeturn9view0turn16view1turn16view2

**Key contribution**

Its key contribution is making **long-horizon, action-conditioned video prediction** concrete and evaluating it not only by pixel error but also by downstream control usefulness, which strongly influenced later “world model” framing in RL. citeturn2academia1turn16view1turn16view2

**Main limitations**

The model is deterministic, pixel-level, and MSE-trained, so it handles stochasticity poorly and struggles with small but task-critical objects like bullets. It also does not learn a compact latent state for planning, nor explicit physical or object structure, which limits long-horizon robustness and generalization beyond the training domain. citeturn16view1

**Relation to the survey taxonomy**

Roles: **historical video prediction foundation; interactive world model**.

**Reliable claims I can cite**

- Claim: The paper is an early action-conditioned, long-horizon video prediction study for high-dimensional RL observations.  
  - Evidence from the paper: The abstract and introduction state that it is the first to make and evaluate long-term predictions on high-dimensional video conditioned by control inputs. citeturn2academia1turn9view0
  - Source location if available: Abstract; Sec. 1.
  - Suggested citation usage: Use when introducing action-conditioned video prediction as a precursor to world models.
  - Confidence: high

- Claim: The model uses multiplicative action-conditioned transformations in feature space.  
  - Evidence from the paper: Sec. 3.2 describes multiplicative interactions between encoded features and action variables, including a factored approximation of the action-conditioned tensor. citeturn9view0
  - Source location if available: Sec. 3.2.
  - Suggested citation usage: Use when describing early conditioning mechanisms before modern latent-transition models.
  - Confidence: high

- Claim: Frame prediction quality alone underestimates usefulness for control.  
  - Evidence from the paper: The authors show much larger gains in DQN-with-predicted-frames performance than MSE differences alone would suggest, and they also improve exploration in some games. citeturn16view1turn16view2
  - Source location if available: Sec. 4.2.
  - Suggested citation usage: Use when arguing that evaluation of world models should go beyond pixel reconstruction metrics.
  - Confidence: high

**Comparison with nearby papers**

Compared with **P005**, this paper stays in Atari and uses direct pixel reconstruction rather than motion transformation. Compared with **P006**, it is deterministic and therefore weaker for multi-modal futures. Compared with **P003/P001/P002**, it lacks a compact latent state for imagination or planning. citeturn15view0turn11view0turn8view0turn26view1turn26view0

**Open questions raised by this paper**

- How should action-conditioned video models represent **uncertainty** instead of averaging futures into blur?
- What evaluation protocol best reflects **control relevance** rather than only pixel accuracy?
- Can one move from pixel-space rollouts to a **compact latent dynamics model** without losing control-critical visual information?

### Paper Note: P005 Unsupervised Learning for Physical Interaction through Video Prediction

**Metadata**

- Paper ID: P005
- Title: *Unsupervised Learning for Physical Interaction through Video Prediction*. citeturn2academia2turn14view0
- Authors: Chelsea Finn, Ian Goodfellow, Sergey Levine. citeturn2academia2turn14view0
- Year: 2016
- Venue: NeurIPS
- URL: arXiv abstract page. citeturn2academia2turn14view0
- arXiv ID / DOI: arXiv:1605.07157. citeturn14view0
- BibTeX key: `finn2016_physical_interaction_video_prediction_prov`
- Current category: `video_prediction`

**One-sentence survey summary**

This paper is a foundational bridge from generic video prediction to **physical interaction modeling**, showing that action-conditioned prediction can exploit pixel motion and weak object structure to imagine robot-object futures from raw video. citeturn2academia2turn15view0

**Problem setting**

The paper asks how an interactive agent can learn how actions affect real objects **without labeled object states**. This matters for predictive world models because physical dynamics in embodied settings often must be learned from raw images and actions rather than symbolic states. citeturn14view0turn15view0

**Representation of the world**

Representation: **pixel space with motion-centric, weakly object-centric structure**. The model keeps appearance in previous frames and predicts how pixels move, using DNA/CDNA/STP transformations and compositing masks; CDNA/STP introduce an unsupervised object-like decomposition. citeturn15view0turn14view1

**Dynamics modeling**

The model predicts the next frame by transforming previous pixels instead of reconstructing appearance from scratch. It uses stacked convolutional LSTMs to predict motion transformations and masks, enabling multi-step rollout by recursively applying predicted transformations. citeturn15view0turn14view1

**Conditioning and interaction**

The main robotic setting is conditioned on **future robot actions** and initial robot state; there is also human motion prediction without actions. The action-conditioned setting is explicitly framed as useful for decision making in robotic control. citeturn14view2turn14view3

**Training objective**

The training loss is an **image reconstruction / mean-squared error objective**. The paper explicitly notes that this objective causes blur under uncertainty and suggests stochastic modeling as future work. citeturn15view0turn14view3

**Evaluation**

Datasets/tasks: a new large robot pushing dataset with seen-object and novel-object test sets, plus Human3.6M for action-free human motion prediction. Metrics: PSNR, SSIM, qualitative video comparisons, and action-intervention analyses. The abstract also reports a dataset of 59,000 robot interactions. citeturn2academia2turn14view2turn14view3

**Key contribution**

The most important contribution is the shift from reconstructing pixels to **predicting motion transformations**, which improved robustness to appearance variation and made generalization to unseen objects much more plausible for physical interaction learning. citeturn15view0turn14view3

**Main limitations**

It remains deterministic and blur-prone, so multi-modal futures are not represented explicitly. The learned structure is only weakly object-centric, long-horizon performance degrades over time, and the model still operates in image space rather than an abstract latent world state that supports large-scale planning. citeturn14view3

**Relation to the survey taxonomy**

Roles: **historical video prediction foundation; physical dynamics learning; interactive world model**.

**Reliable claims I can cite**

- Claim: The paper explicitly models pixel motion rather than reconstructing future appearance from scratch.  
  - Evidence from the paper: The introduction and Sec. 3 describe DNA/CDNA/STP motion transforms that advect pixels from previous frames and compose them with masks. citeturn15view0turn14view1
  - Source location if available: Sec. 1; Sec. 3.
  - Suggested citation usage: Use when motivating motion-based video prediction as an intermediate step toward physical world modeling.
  - Confidence: high

- Claim: CDNA and STP induce an unsupervised, object-like decomposition.  
  - Evidence from the paper: The authors state that CDNA/STP transformations are intended to handle separate objects and that masks naturally learn moving segments, yielding a more object-centric representation. citeturn15view0turn14view1
  - Source location if available: Sec. 3.1–3.2.
  - Suggested citation usage: Use when discussing pre-object-centric structure before explicit object slots and relational models.
  - Confidence: high

- Claim: The proposed models outperform prior methods on robot pushing and Human3.6M and generalize better to novel objects.  
  - Evidence from the paper: The experiments report higher PSNR/SSIM and better qualitative predictions, with especially visible gains for motion-predictive models on novel objects. citeturn14view2turn14view3
  - Source location if available: Sec. 5.1–5.2.
  - Suggested citation usage: Use when arguing that physically informed inductive bias improves video prediction for manipulation.
  - Confidence: high

**Comparison with nearby papers**

Compared with **P004**, this paper moves from Atari to real robot interaction and introduces motion transforms instead of direct frame decoding. Compared with **P006**, it remains deterministic. Compared with **P007–P009**, it does not require explicit object states or graphs, but its object structure is weaker and less directly actionable. citeturn9view0turn11view0turn17view0turn23view0

**Open questions raised by this paper**

- How can motion-based predictors represent **stochastic contact outcomes** without blur?
- What is the best path from soft masks to **fully object-factorized dynamics**?
- How should robotic world models be evaluated beyond PSNR/SSIM, especially for **planning utility**?

### Paper Note: P006 Stochastic Variational Video Prediction

**Metadata**

- Paper ID: P006
- Title: *Stochastic Variational Video Prediction*. citeturn3academia3turn10view0
- Authors: Mohammad Babaeizadeh, Chelsea Finn, Dumitru Erhan, Roy H. Campbell, Sergey Levine. citeturn3academia3turn10view0
- Year: 2018
- Venue: ICLR
- URL: arXiv abstract page. citeturn3academia3turn10view0
- arXiv ID / DOI: arXiv:1710.11252. citeturn10view0
- BibTeX key: `babaeizadeh2018_sv2p_prov`
- Current category: `video_prediction`

**One-sentence survey summary**

SV2P is a key stochastic future-modeling paper because it inserts latent variables into multi-frame video prediction and shows that world models should represent **distributions over futures**, not only deterministic rollouts. citeturn3academia3turn11view0

**Problem setting**

The paper addresses the mismatch between deterministic video prediction and real-world stochasticity, including in action-conditioned settings. This is central for predictive world models because ambiguity, hidden variables, and partial observability all make single-future rollouts physically and behaviorally misleading. citeturn11view0

**Representation of the world**

Representation: **pixel space + latent stochastic variables**. The generative backbone is based on CDNA-style image prediction, but the future is conditioned on sampled latent variables, either time-invariant per video or time-varying per frame. citeturn11view0turn12view0

**Dynamics modeling**

The model predicts future frames autoregressively using a stochastic latent variable model. A variational inference network conditions on future frames during training to infer posterior latents; at test time, latents are sampled from the prior to generate multiple plausible futures. citeturn11view0

**Conditioning and interaction**

SV2P supports both **action-free** and **action-conditioned** prediction. In action-conditioned settings, it still models residual stochasticity when actions do not fully determine outcomes. citeturn10view0turn11view0

**Training objective**

Training uses a **variational lower bound** with reconstruction and KL terms, plus a three-phase procedure: deterministic generative pretraining, inference-network training without KL, then gradual KL activation. This schedule is introduced because naïve training tends to ignore the latent variables. citeturn11view0turn12view0

**Evaluation**

Datasets/tasks: a toy stochastic movement dataset, BAIR robot pushing (action-conditioned and action-free), Human3.6M, and the earlier robotic pushing prediction dataset used for comparing against VPN. Metrics: PSNR and SSIM, including “best of N samples” style evaluation for stochastic models, plus qualitative diversity/consistency checks. citeturn12view2turn12view3turn13view0

**Key contribution**

Its main contribution is demonstrating that **latent-variable stochastic multi-frame video prediction** can work on real-world datasets, not only synthetic sprites, and that deterministic baselines systematically blur away physically relevant uncertainty. citeturn11view0turn12view2

**Main limitations**

The model still predicts in pixel space and relies on “best sample” metrics that only partially solve the evaluation problem for stochastic futures. It does not disentangle object-level or physical state, and the posterior uses future frames during training, which highlights a train-test gap that later latent world models address differently. citeturn11view0turn13view0

**Relation to the survey taxonomy**

Roles: **stochastic future modeling; interactive world model**.

**Reliable claims I can cite**

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

**Comparison with nearby papers**

Compared with **P004** and **P005**, SV2P explicitly models multi-modal futures. Compared with **P001/P002**, however, it still remains primarily a pixel-space video predictor rather than a compact latent world model for control. citeturn16view0turn15view0turn26view1turn26view0

**Open questions raised by this paper**

- How should stochastic video models be evaluated without relying on “best of many samples” heuristics?
- Can latent stochasticity be tied to **objects, forces, or hidden physical variables** rather than global noise?
- How should long-horizon stochastic rollouts be constrained for **physical consistency**?

## Object-Centric Physics and Interaction Modeling

### Paper Note: P007 Interaction Networks for Learning about Objects, Relations and Physics

**Metadata**

- Paper ID: P007
- Title: *Interaction Networks for Learning about Objects, Relations and Physics*. citeturn2academia0turn17view0
- Authors: Peter W. Battaglia, Razvan Pascanu, Matthew Lai, Danilo Jimenez Rezende, Koray Kavukcuoglu. citeturn2academia0turn17view0
- Year: 2016
- Venue: NeurIPS
- URL: arXiv abstract page. citeturn2academia0turn17view0
- arXiv ID / DOI: arXiv:1612.00222. citeturn17view0
- BibTeX key: `battaglia2016_interaction_networks_prov`
- Current category: `generative_simulation`

**One-sentence survey summary**

Interaction Networks are a canonical object-relational dynamics model that established the idea that learned world models can act like a **general-purpose, learnable physics engine** over objects and relations. citeturn17view0turn18view0

**Problem setting**

The paper addresses physical prediction and abstract property estimation in systems where dynamics are driven by pairwise or structured object interactions. For survey purposes, it matters because many later visual world models inherit its premise that good dynamics models should be **object- and relation-centric**, not monolithic pixel predictors. citeturn17view0turn17view1

**Representation of the world**

Representation: **graph / relational state** over explicit objects. Inputs are attributed objects, attributed directed relations, and external effects; the model reasons over a multigraph rather than pixels or generic latent vectors. citeturn17view1turn18view0

**Dynamics modeling**

Dynamics are modeled by a relation network that computes per-edge interaction effects and an object network that aggregates these effects with per-object state and external input to predict next-step object velocities or other outputs. Multi-step simulation is obtained by iterating one-step predictions. citeturn17view1turn18view0

**Conditioning and interaction**

The model can condition on **external effects** such as gravitational acceleration or control-like inputs applied to each object. Interactions among objects are explicit and central to the model design. citeturn17view1turn17view2

**Training objective**

Training and testing use **mean squared error** on target physical quantities such as next-step velocities or potential energy. Regularization and some training noise were explored to improve generalization and rollout realism. citeturn18view0

**Evaluation**

Domains: n-body gravity, bouncing balls, and spring-string systems with collisions. Tasks: next-step prediction, long rollout simulation, and potential-energy estimation. Metrics: test MSE on targets and qualitative/quantitative rollout fidelity, including generalization to new numbers of objects and configurations. citeturn17view2turn18view0

**Key contribution**

The key contribution is the explicit decomposition of dynamics into **relation-centric interaction functions and object-centric update functions**, which became one of the most influential templates for physical world modeling. citeturn17view1turn18view0

**Main limitations**

The model assumes an explicit object graph and ground-truth state-like inputs rather than learning directly from video, so it is not itself a video world model. Its impressive long rollouts still accumulate error in nonlinear regimes, and its evaluation stays within synthetic physics settings rather than embodied, partially observed visual environments. citeturn17view3turn18view0

**Relation to the survey taxonomy**

Roles: **object-centric dynamics; physical dynamics learning**.

**Reliable claims I can cite**

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

**Comparison with nearby papers**

Compared with **P004–P006**, P007 is not pixel-based and does not learn from video; compared with **P008**, it provides the relational dynamics core that VIN adds visual perception to; compared with **P009**, it does not solve planning from images but strongly informs the physics module design. citeturn16view0turn15view0turn11view0turn19view0turn23view0

**Open questions raised by this paper**

- How can object graphs be learned directly from raw video rather than assumed?
- Which relational biases remain helpful once observations become **partial, cluttered, or noisy**?
- How should graph-based physical simulators be connected to **action selection and planning** in visual environments?

### Paper Note: P008 Visual Interaction Networks

**Metadata**

- Paper ID: P008
- Title: *Visual Interaction Networks*. citeturn19view0
- Authors: Nicholas Watters, Andrea Tacchetti, Théophane Weber, Razvan Pascanu, Peter Battaglia, Daniel Zoran. citeturn19view0
- Year: 2017
- Venue: NeurIPS
- URL: arXiv abstract page / ar5iv HTML. citeturn19view0
- arXiv ID / DOI: arXiv:1706.01433. citeturn19view0
- BibTeX key: `watters2017_visual_interaction_networks_prov`
- Current category: `physical_dynamics`

**One-sentence survey summary**

VIN is a crucial step toward visual world models because it couples a learned visual encoder with interaction-network dynamics, showing how **object-centric physical prediction can be learned from video-like inputs**. citeturn19view0turn20view0

**Problem setting**

The paper addresses prediction of future physical states from raw visual observations, aiming to build a model that can infer object states and then roll them forward under interactions. This matters because predictive world models need a bridge from pixels to structured physical dynamics. citeturn19view0

**Representation of the world**

Representation: **object-centric latent state**. A visual encoder maps short frame triplets into a state code containing one slot per object; a linear decoder maps each slot to position/velocity. This is latent, but explicitly factored by object. citeturn19view0

**Dynamics modeling**

Dynamics are predicted by an interaction-network-based recurrent predictor with multiple temporal offsets, whose candidate next-state codes are aggregated by an MLP. Future trajectories are produced by recurrent rollout in state-code space. citeturn19view0turn20view1

**Conditioning and interaction**

There are no explicit actions in the main benchmarks. Interaction is entirely among objects through learned relational dynamics; some datasets include hidden objects or variable masses that must be inferred from visual evidence and interactions. citeturn19view0turn20view1

**Training objective**

The model is trained to predict **eight unseen future states**, with a normalized weighted sum of rollout losses plus an auxiliary encoder loss. The rollout weighting schedule gradually increases emphasis on farther future predictions. citeturn20view0turn20view1

**Evaluation**

Datasets/tasks: simulated 2D spring, gravity, billiards, magnetic billiards, drift, invisible-object springs, and variable-mass settings with natural-image backgrounds. Metrics: Inverse Normalized Loss, Euclidean prediction error on long rollouts, and qualitative rendered rollout trajectories. citeturn19view0turn20view0turn20view2

**Key contribution**

Its main contribution is demonstrating that a model can jointly learn **visual perception plus relational physical rollout**, and in some rollout metrics even outperform state-to-state baselines despite only observing images. citeturn20view0turn20view1

**Main limitations**

VIN still uses supervised object-state targets during training, so it is not fully unsupervised from video. Its environments are visually simple synthetic physics scenes, and the object count is fixed within each dataset, leaving open the harder problems of open-world segmentation, appearance variation, and embodied control. citeturn19view0turn20view0

**Relation to the survey taxonomy**

Roles: **object-centric dynamics; physical dynamics learning**.

**Reliable claims I can cite**

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

**Comparison with nearby papers**

Compared with **P007**, VIN adds the visual front-end needed to start from images. Compared with **P009**, VIN still uses supervised state targets whereas O2P2 relaxes object-property supervision. Compared with **P005/P006**, VIN is much more explicitly object-relational but also less realistic in visual complexity. citeturn17view0turn23view0turn15view0turn11view0

**Open questions raised by this paper**

- Can object slots and state targets be learned **without state supervision**?
- How well do object-centric latent dynamics survive realistic clutter, occlusion, and camera motion?
- What is the right evaluation for long rollouts when trajectory identity diverges but **physical plausibility** remains high?

### Paper Note: P009 Reasoning About Physical Interactions with Object-Oriented Prediction and Planning

**Metadata**

- Paper ID: P009
- Title: *Reasoning About Physical Interactions with Object-Oriented Prediction and Planning*. citeturn22view0turn23view0
- Authors: Michael Janner, Sergey Levine, William T. Freeman, Joshua B. Tenenbaum, Chelsea Finn, Jiajun Wu. **Note:** this author list differs from your local BibTeX entry; I am following the paper source here. citeturn22view0turn23view0
- Year: 2019
- Venue: ICLR
- URL: arXiv abstract page / project page linked from arXiv. citeturn22view0
- arXiv ID / DOI: arXiv:1812.10972. citeturn22view0
- BibTeX key: `janner2019_o2p2_prov`
- Current category: `object_centric_world_models`

**One-sentence survey summary**

O2P2 is an important object-centric world-model paper because it jointly learns perception, pairwise physics, and rendering using only **pixel supervision plus segments**, then demonstrates that the resulting representation is actually useful for planning. citeturn22view0turn23view0

**Problem setting**

The paper asks whether physically useful object representations can be learned **without direct supervision of object properties**. For survey purposes, this directly targets a central problem in world modeling: how to obtain actionable, object-factorized latent structure from visual data with minimal annotation. citeturn22view0turn23view0

**Representation of the world**

Representation: **object-centric latent state**. Each segmented object is encoded into a vector by a perception module; the model is trained only through reconstruction/prediction losses rather than labels for position, identity, or orientation. citeturn23view0

**Dynamics modeling**

The physics module predicts the outcome of pairwise interactions plus unary transitions over object vectors. Importantly, the model predicts a **single steady-state post-physics configuration** rather than a full time-indexed rollout, because the planning task mainly needs the final stable arrangement. citeturn23view0

**Conditioning and interaction**

Training uses before/after images of blocks, with access to **segments or region proposals** in the initial frame. For planning, the model evaluates sampled block-placement actions in representation space, optionally via CEM, and can also transfer to a real Sawyer arm with an action embedder. citeturn23view0turn24view2

**Training objective**

Perception, physics, and rendering are trained jointly with **image reconstruction and prediction losses**, combining pixel-space distance and a VGG-based perceptual loss. Different modules are indirectly supervised by reconstruction of the current image and prediction of the post-physics image. citeturn23view0

**Evaluation**

Tasks: reconstruction/prediction on block-drop scenes; tower-building via planning from goal images; transfer to a Sawyer robot. Data: 60,000 MuJoCo-generated training images for synthetic block scenes. Metrics: tower-build accuracy, qualitative planning analysis, and real-robot success counts. O2P2 reports 76% synthetic tower-building accuracy and 17/25 correct on real-robot goals. citeturn24view0turn24view1turn24view2

**Key contribution**

The paper’s most important contribution is the demonstration that an object-centric visual representation learned without object-property labels can be **good enough for planning**, not just for reconstruction. citeturn22view0turn24view0turn24view1

**Main limitations**

O2P2 uses segmentation masks / object proposals, so it is not fully unsupervised. It predicts steady-state outcomes rather than long temporal rollouts, focuses on synthetic stacking rather than diverse natural videos, and its planner relies on fairly structured action spaces and object geometry. citeturn23view0turn24view1

**Relation to the survey taxonomy**

Roles: **object-centric dynamics; physical dynamics learning; latent world model for planning; interactive world model**.

**Reliable claims I can cite**

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

**Comparison with nearby papers**

Compared with **P008**, O2P2 needs less direct state supervision but more segmentation structure. Compared with **P007**, it is much closer to a visual world model and supports planning. Compared with **P005/P006**, it is more explicitly object-centric and planning-oriented, but less focused on realistic long-horizon video rollouts. citeturn19view0turn17view0turn15view0turn11view0

**Open questions raised by this paper**

- Can object-centric planning work without segmentation masks or proposal boxes?
- How should one extend steady-state prediction to **long-horizon interactive simulation**?
- What is the best interface between learned object representations and **continuous robotic control**?

## Latent World Models for Control

### Paper Note: P003 Recurrent World Models Facilitate Policy Evolution

**Metadata**

- Paper ID: P003
- Title: *World Models* on the arXiv page; your local database lists the survey title form *Recurrent World Models Facilitate Policy Evolution*. I am preserving your paper ID and BibTeX key while grounding details in the arXiv paper. citeturn7view0turn8view0
- Authors: David Ha, Jürgen Schmidhuber. citeturn7view0turn8view0
- Year: 2018
- Venue: NeurIPS
- URL: interactive project / arXiv abstract page. citeturn7view0turn8view0
- arXiv ID / DOI: arXiv:1803.10122. citeturn7view0
- BibTeX key: `ha2018_world_models_prov`
- Current category: `latent_world_models`

**One-sentence survey summary**

This paper crystallized the “world model” paradigm in RL by decomposing perception, memory, and control into VAE, MDN-RNN, and controller modules, and by showing that policies can even be trained inside a **hallucinated environment**. citeturn7view0turn8view0turn30view1

**Problem setting**

The paper addresses how to learn a compact world model from high-dimensional observations and use it to train a very small controller efficiently. It matters because it made latent predictive modeling a central lens for model-based RL and simulation-based policy learning. citeturn8view0

**Representation of the world**

Representation: **latent state**. A VAE compresses pixels into a latent vector *z*, an MDN-RNN predicts future latent dynamics and maintains memory *h*, and the controller acts from `[z, h]`. citeturn8view0

**Dynamics modeling**

Temporal evolution is modeled by an **MDN-RNN** that predicts a mixture-of-Gaussians distribution over next latent vectors, conditioned on previous latent, action, and recurrent hidden state. In the Doom experiment, the world model also predicts terminal/death-related information so it can serve as a stand-in environment. citeturn8view0turn30view0

**Conditioning and interaction**

The world model is conditioned on **actions**. Rewards are not part of the unsupervised world-model training in CarRacing, but the controller is later optimized for task reward using CMA-ES; in Doom, the world model is used as a full simulated environment for policy evolution. citeturn29view0turn30view0

**Training objective**

The VAE is trained for frame reconstruction; the MDN-RNN is trained as a probabilistic next-latent predictor; the controller is optimized separately with **CMA-ES** on task return. Training is modular rather than end-to-end. citeturn8view0turn29view3

**Evaluation**

Tasks: CarRacing-v0 and VizDoom Take Cover. Metrics: environment return / survival time. Reported results include CarRacing average score 906 for the full world model and Doom transfer performance around 1100 average survival steps on the real environment after training inside the dream. citeturn29view0turn30view1turn30view2

**Key contribution**

The key contribution is conceptual: it popularized the idea that compact latent predictive models can be used not only for representation learning but as **simulators for downstream policy learning**. citeturn8view0turn30view1

**Main limitations**

The training is decoupled, the controller is tiny and evolved rather than gradient-trained through the model, and the VAE+MDN design is relatively weak compared with later RSSM-based approaches. The paper also emphasizes proof-of-concept more than standardized large-benchmark evaluation. citeturn8view0turn29view3

**Relation to the survey taxonomy**

Roles: **latent world model for planning; historical video prediction foundation; interactive world model**.

**Reliable claims I can cite**

- Claim: The world model is factorized into VAE, MDN-RNN, and controller modules.  
  - Evidence from the paper: Sec. 2 defines the V, M, and C components and their interactions. citeturn8view0
  - Source location if available: Sec. 2.
  - Suggested citation usage: Use when presenting the historical emergence of latent world models in RL.
  - Confidence: high

- Claim: Policies can be trained entirely inside a hallucinated environment and transferred back to the real one.  
  - Evidence from the paper: The abstract states this, and the VizDoom sections describe training inside the dream and evaluating in the actual environment. citeturn7view0turn30view0turn30view1
  - Source location if available: Abstract; Sec. 4.
  - Suggested citation usage: Use when motivating generative simulation as a training substrate.
  - Confidence: high

- Claim: The full world model solves CarRacing-v0 by exceeding the benchmark score of 900.  
  - Evidence from the paper: Table 1 reports a full-world-model average score of 906 and explains that solving CarRacing requires an average reward above 900. citeturn29view0
  - Source location if available: Sec. 3.3; Table 1.
  - Suggested citation usage: Use when citing early empirical success of latent world models from pixels.
  - Confidence: high

**Comparison with nearby papers**

Compared with **P001** and **P002**, this is the looser, earlier VAE+RNN formulation before RSSM and latent overshooting / imagination actor-critic. Compared with **P004–P006**, it shifts decisively from pixel-space future-frame modeling to compact latent dynamics for control. citeturn26view1turn26view0turn16view0turn15view0turn11view0

**Open questions raised by this paper**

- When does modular training of perception, dynamics, and controller underperform end-to-end latent world-model learning?
- How accurate must a dream environment be for **policy transfer** to remain reliable?
- How should uncertainty in latent dynamics be regularized so the controller cannot exploit simulator flaws?

### Paper Note: P001 Learning Latent Dynamics for Planning from Pixels

**Metadata**

- Paper ID: P001
- Title: *Learning Latent Dynamics for Planning from Pixels*. citeturn25view1turn1view0
- Authors: Danijar Hafner, Timothy Lillicrap, Ian Fischer, Ruben Villegas, David Ha, Honglak Lee, James Davidson. citeturn25view1turn1view0
- Year: 2019
- Venue: ICML
- URL: arXiv abstract page. citeturn25view1
- arXiv ID / DOI: arXiv:1811.04551. citeturn25view1
- BibTeX key: `hafner2019_planet_prov`
- Current category: `latent_world_models`

**One-sentence survey summary**

PlaNet is a landmark latent world model because it shows that planning can be done directly in a compact learned latent state, avoiding image-space rollouts while still solving challenging visual control tasks. citeturn25view1turn1view0turn27view2

**Problem setting**

PlaNet targets model-based control from pixels in partially observed, continuous-action environments where image-level planning is too expensive and brittle. This is important because it reframes world modeling around **latent transition learning plus online planning**, which becomes a major branch of later work. citeturn25view1turn1view0

**Representation of the world**

Representation: **latent state** via RSSM. The state has deterministic and stochastic components, with an encoder / representation model, transition model, observation model, and reward model. The planner uses only latent states and predicted rewards, not decoded images. citeturn1view0

**Dynamics modeling**

Temporal evolution is modeled by a **recurrent state-space model (RSSM)** that combines deterministic memory and stochastic latent variables. Rollouts in latent space are used inside a CEM planner with online replanning (MPC). citeturn1view0turn27view2

**Conditioning and interaction**

The world model is conditioned on **actions** and trained also to predict **rewards** from latent states. Planning is action-sequence search rather than a learned policy. citeturn1view0

**Training objective**

Training uses a variational objective with observation and reward reconstruction/prediction terms plus KL regularization, and introduces **latent overshooting** as a multi-step latent-space consistency objective. The appendix/result discussion notes that RSSM itself did not require latent overshooting in the final agent. citeturn1view0turn27view0

**Evaluation**

Tasks: six visual DeepMind Control Suite tasks including Cartpole Swing Up, Reacher Easy, Cheetah Run, Finger Spin, Cup Catch, and Walker Walk. Metrics: episodic return versus number of collected episodes; comparisons to A3C, D4PG, and planning with the true simulator. citeturn27view1turn27view3

**Key contribution**

The key contribution is the combination of **RSSM latent dynamics + latent-space MPC**, which made world-model planning from pixels substantially more sample efficient and computationally practical. citeturn25view1turn1view0turn27view3

**Main limitations**

PlaNet depends on online planning, which is slower at action time than policy amortization. Long-horizon behavior still depends on finite-horizon CEM search, and the method is specialized to continuous-control settings with hand-designed reward signals rather than open-ended video simulation. citeturn27view2turn27view3

**Relation to the survey taxonomy**

Roles: **latent world model for planning; embodied world model**.

**Reliable claims I can cite**

- Claim: PlaNet plans in latent space rather than image space.  
  - Evidence from the paper: The abstract and Sec. 2 state that PlaNet chooses actions via fast online planning in latent space, with rewards predicted from latent states. citeturn25view1turn1view0
  - Source location if available: Abstract; Sec. 2.
  - Suggested citation usage: Use when motivating world models that separate planning from pixel generation.
  - Confidence: high

- Claim: The RSSM’s combination of deterministic and stochastic transitions is important for performance.  
  - Evidence from the paper: Sec. 3 and experimental analysis report that both components are crucial; the stochastic component is especially important. citeturn1view0turn27view3
  - Source location if available: Sec. 3; Sec. 5.
  - Suggested citation usage: Use when discussing latent-state design for world models.
  - Confidence: high

- Claim: PlaNet is markedly more data-efficient than pixel-based D4PG on the tested control tasks.  
  - Evidence from the paper: Table 1 reports PlaNet on 1,000 episodes versus D4PG on 100,000, along with large estimated data-efficiency gains. citeturn27view3
  - Source location if available: Sec. 5; Table 1.
  - Suggested citation usage: Use when surveying data efficiency gains from latent model-based control.
  - Confidence: high

**Comparison with nearby papers**

Compared with **P003**, PlaNet replaces VAE+MDN modularity with a more principled RSSM and explicit latent-space MPC. Compared with **P002**, PlaNet still plans online instead of learning a latent-space actor-critic policy. Compared with **P004–P006**, it moves decisively away from pixel-space rollout evaluation. citeturn8view0turn26view0turn16view0turn15view0turn11view0

**Open questions raised by this paper**

- When should world models prefer **online planning** versus **amortized policy learning**?
- How can latent models preserve control-critical visual detail without decoding every step?
- What is the right evaluation for latent simulators beyond reward curves?

### Paper Note: P002 Dream to Control: Learning Behaviors by Latent Imagination

**Metadata**

- Paper ID: P002
- Title: *Dream to Control: Learning Behaviors by Latent Imagination*. citeturn25view0turn26view0
- Authors: Danijar Hafner, Timothy Lillicrap, Jimmy Ba, Mohammad Norouzi. citeturn25view0turn26view0
- Year: 2020
- Venue: ICLR
- URL: arXiv abstract page. citeturn25view0
- arXiv ID / DOI: arXiv:1912.01603. citeturn25view0
- BibTeX key: `hafner2020_dreamer_prov`
- Current category: `latent_world_models`

**One-sentence survey summary**

Dreamer shifts latent world modeling from online planning to **latent imagination with actor-critic learning**, making world models a scalable substrate for long-horizon behavior learning from images. citeturn25view0turn26view0turn28view0

**Problem setting**

The paper asks how to derive strong long-horizon behaviors from a learned world model without relying on expensive online planning or short imagination horizons. This matters because predictive world models become substantially more usable once policy learning is amortized through imagination. citeturn25view0turn26view0

**Representation of the world**

Representation: **latent state** using an RSSM world model inherited from PlaNet-style reconstruction learning, though the paper also discusses contrastive alternatives. The agent imagines trajectories in compact latent state space rather than in pixels. citeturn28view1turn26view0

**Dynamics modeling**

The world model predicts next latent states and rewards; the actor and critic then learn from imagined latent trajectories. Values account for rewards beyond the finite imagination horizon, and gradients are backpropagated analytically through the imagined dynamics and action samples. citeturn26view0

**Conditioning and interaction**

The model is conditioned on **actions** and predicts **rewards**; in some settings it also predicts discounts for early termination. Dreamer executes a learned action model in the environment, rather than performing CEM-style online search at test time. citeturn26view0

**Training objective**

The world model can be trained with reconstruction ELBO-style losses or alternative representation-learning objectives; the actor maximizes imagined value estimates, and the critic regresses λ-return-like value targets. The world model is held fixed while behavior is updated. citeturn26view0turn28view1

**Evaluation**

Tasks: 20 visual DeepMind Control Suite tasks, with additional discrete-action / early-termination experiments on subsets of Atari and DeepMind Lab in the appendix. Metrics: task return, data efficiency, and training time; the paper reports superior average performance relative to PlaNet and strong model-free baselines under matched image-input settings. citeturn25view0turn28view0

**Key contribution**

Its key contribution is making latent world models practical for **policy learning by imagination**, which strongly influenced later Dreamer variants and many contemporary world-model pipelines. citeturn26view0turn28view0

**Main limitations**

Dreamer still depends on the quality of the learned latent model and is centered on RL reward optimization rather than general-purpose generative simulation. The paper also evaluates mostly through return, so it says less about physical faithfulness, causal consistency, or open-world video realism. citeturn28view0turn28view1

**Relation to the survey taxonomy**

Roles: **latent world model for planning; embodied world model**.

**Reliable claims I can cite**

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

**Comparison with nearby papers**

Compared with **P001**, Dreamer replaces online CEM planning with a learned actor-critic. Compared with **P003**, it uses a more principled RSSM-style world model and gradient-based behavior learning. Compared with **P012**, Dreamer remains a latent-state world model rather than an image-space diffusion simulator. citeturn26view1turn8view0turn31view1

**Open questions raised by this paper**

- How can imagination-based agents be evaluated for **simulation fidelity**, not only return?
- When do latent models omit visual details that later prove behaviorally necessary?
- How should latent imagination handle **multi-modal physical futures** and heavy partial observability?

## Diffusion and Interactive Generative Environments

### Paper Note: P012 Diffusion for World Modeling: Visual Details Matter in Atari

**Metadata**

- Paper ID: P012
- Title: *Diffusion for World Modeling: Visual Details Matter in Atari*. citeturn5view2turn32view0
- Authors: Eloi Alonso, Adam Jelley, Vincent Micheli, Anssi Kanervisto, Amos Storkey, Tim Pearce, François Fleuret. citeturn32view0
- Year: 2024
- Venue: NeurIPS
- URL: arXiv abstract page / ar5iv HTML. citeturn5view2turn32view0
- arXiv ID / DOI: arXiv:2405.12399. citeturn5view2
- BibTeX key: `alonso2024_diamond_prov`
- Current category: `diffusion_world_models`

**One-sentence survey summary**

DIAMOND is a major diffusion-based world model that argues image-space generative fidelity is not cosmetic but can materially improve downstream control when small visual details matter. citeturn32view0turn31view2turn31view3

**Problem setting**

The paper asks whether compressing observations into discrete latent representations may discard visual details that matter for reinforcement learning, and whether diffusion can serve as a better world-modeling primitive. This matters because many world models face a trade-off between compactness and detail fidelity. citeturn32view0turn31view2

**Representation of the world**

Representation: **diffusion / noise space operating directly in image space**. The model predicts the next observation conditioned on a history of observations and actions, using a score-based diffusion process rather than a discrete latent tokenizer. citeturn31view1turn32view1

**Dynamics modeling**

The world model is a conditional diffusion model of environment dynamics, trained to generate the next observation from past observations/actions. Temporal rollout is autoregressive: generated observations are fed back as context, and the paper explicitly studies stability under few denoising steps. citeturn31view1turn32view3

**Conditioning and interaction**

The model conditions on **past observations and past actions**. A replay buffer of trajectory segments is used for training; the learned world model then serves as the environment in which the RL agent is trained. citeturn31view1turn32view1

**Training objective**

Training follows diffusion denoising / score-matching style objectives, with EDM-style preconditioning rather than a standard DDPM choice. One practical contribution is selecting a diffusion formulation that remains stable over long rollouts even with very low numbers of denoising steps. citeturn31view1turn32view3

**Evaluation**

Main benchmark: Atari 100k over 26 games. Metrics: game returns, mean and IQM human-normalized score, bootstrap confidence intervals, and qualitative analysis of world-model trajectories; the paper reports mean HNS 1.459/1.46 and 11 superhuman games. citeturn31view0turn31view3turn32view2

**Key contribution**

The key contribution is showing that **diffusion-based image-space world models** can outperform prior world-model baselines on Atari 100k, while also making qualitative simulator analysis easier because the model can directly substitute for the environment. citeturn31view0turn31view3

**Main limitations**

The evaluation is concentrated on Atari rather than realistic physical video. The method is computationally heavier than many latent-state models, and its gains are tied to preserving image details rather than explicit physical abstraction, so questions about long-horizon causal/physical correctness remain open. citeturn31view3turn32view3

**Relation to the survey taxonomy**

Roles: **diffusion-based world model; interactive world model**.

**Reliable claims I can cite**

- Claim: DIAMOND models environment dynamics directly with a conditional diffusion model in image space.  
  - Evidence from the paper: Sec. 2.3 defines the conditional diffusion formulation for next-observation prediction from observation/action history. citeturn31view1
  - Source location if available: Sec. 2.3.
  - Suggested citation usage: Use when surveying diffusion-based world models.
  - Confidence: high

- Claim: The paper argues that preserving visual details can improve RL performance.  
  - Evidence from the paper: The abstract/introduction and analysis state that better modeling of critical visual details explains performance gains in some games. citeturn32view0turn31view3
  - Source location if available: Abstract; Sec. 4–5.
  - Suggested citation usage: Use when discussing the cost of aggressive perceptual compression in latent world models.
  - Confidence: high

- Claim: DIAMOND achieves a new best mean human-normalized score among agents trained entirely within a world model on Atari 100k.  
  - Evidence from the paper: Table 1 / Figure 2 report mean HNS 1.459 and IQM 0.641, above the listed world-model baselines. citeturn31view3turn32view2
  - Source location if available: Sec. 4.2; Table 1; Figure 2.
  - Suggested citation usage: Use when citing empirical progress in world-model-based RL.
  - Confidence: high

**Comparison with nearby papers**

Compared with **P001/P002**, DIAMOND rejects compact latent-state imagination in favor of image-space diffusion. Compared with **P013**, it still uses real actions and RL benchmarks rather than action-free latent actions from internet videos. Compared with **P004–P006**, it revisits image-space generation but with much stronger generative machinery and RL integration. citeturn26view1turn26view0turn33view1turn16view0turn11view0

**Open questions raised by this paper**

- When do image-space diffusion models beat latent-state models enough to justify the compute cost?
- How should diffusion world models be evaluated for **physical correctness** rather than Atari return alone?
- Can diffusion simulators support **controllability and planning** in embodied, real-world video domains?

### Paper Note: P013 Genie: Generative Interactive Environments

**Metadata**

- Paper ID: P013
- Title: *Genie: Generative Interactive Environments*. citeturn5view0turn6view0
- Authors: Jake Bruce, Michael Dennis, Ashley Edwards, Jack Parker-Holder, Yuge Shi, Edward Hughes, Matthew Lai, Aditi Mavalankar, Richie Steigerwald, Chris Apps, Yusuf Aytar, Sarah Bechtle, Feryal Behbahani, Stephanie Chan, Nicolas Heess, Lucy Gonzalez, Simon Osindero, Sherjil Ozair, Scott Reed, Jingwei Zhang, Konrad Zolna, Jeff Clune, Nando de Freitas, Satinder Singh, Tim Rocktäschel. citeturn5view0turn6view0
- Year: 2024
- Venue: ICML
- URL: arXiv abstract page. citeturn5view0
- arXiv ID / DOI: arXiv:2402.15391. citeturn5view0
- BibTeX key: `bruce2024_genie_prov`
- Current category: `interactive_world_models`

**One-sentence survey summary**

Genie pushes world modeling toward foundation-style interactive generation by learning **frame-level controllability from unlabeled internet video** through discrete latent actions rather than ground-truth action labels. citeturn5view0turn6view0

**Problem setting**

The paper asks whether one can train an interactive, controllable environment model from **video-only data**, without action annotations. This matters greatly for predictive world models because internet-scale video is abundant while action-labeled embodied data is scarce. citeturn5view0turn6view0

**Representation of the world**

Representation: **token space + latent action space**. Genie tokenizes video into discrete spatiotemporal tokens with a VQ-VAE-like tokenizer, and separately learns a small discrete latent action codebook inferred from videos. citeturn6view0turn33view1

**Dynamics modeling**

The dynamics model is a decoder-only **MaskGIT-style autoregressive next-frame token predictor** over tokenized frames, conditioned on latent action embeddings. At inference, the user supplies discrete latent actions and the model iteratively generates the next frame tokens and decodes them to pixels. citeturn6view0turn33view2

**Conditioning and interaction**

The model is conditioned on **prompt images / frames** and **learned latent actions** rather than real actions. It can be prompted by text, images, photos, or sketches at the interface level, but the core training is video-only and action-free. citeturn5view0turn6view0

**Training objective**

Training proceeds in two phases: first the video tokenizer with a VQ-VAE objective, then co-training of the latent action model and the dynamics model. The latent action model uses a VQ-VAE objective; the dynamics model uses cross-entropy on next-frame tokens. Metrics include FVD for fidelity and a controllability metric based on PSNR differences between ground-truth-inferred vs random latent actions. citeturn6view0turn33view1turn34view3

**Evaluation**

Training/eval settings include hundreds of 2D platformer games from internet gameplay videos, a curated 30,000-hour platformer subset drawn from a larger 200,000-hour pool, and robotics videos including RT-1-style data. Metrics include FVD and controllability; imitation-from-observation analysis on CoinRun shows the latent-action policy can match an oracle BC model with as few as 200 expert samples for adaptation. citeturn33view0turn34view3turn34view1

**Key contribution**

The key contribution is showing that **interactive controllability can be learned without action supervision**, which is a major conceptual expansion of what counts as a world model. citeturn5view0turn6view0

**Main limitations**

Genie’s actions are latent and need post hoc interpretation, so controllability is not yet semantically grounded like real control inputs. It operates in relatively structured domains such as platformers and robotics clips, and physical faithfulness is not the main evaluation target. citeturn33view1turn34view3

**Relation to the survey taxonomy**

Roles: **interactive world model; embodied world model**.

**Reliable claims I can cite**

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

**Comparison with nearby papers**

Compared with **P012**, Genie is not an RL world model benchmarked on Atari but a video-only interactive generator. Compared with **P001/P002**, it abandons explicit reward-conditioned control in favor of unsupervised latent controllability. Compared with **P009**, it needs less object-level structure but also offers weaker explicit physical semantics. citeturn31view0turn26view1turn26view0turn23view0

**Open questions raised by this paper**

- How can latent actions be mapped to **semantically meaningful control variables**?
- How stable are Genie-style interactive environments over **long horizons and persistent causal interaction**?
- What benchmarks should measure **physical consistency** in action-free interactive generators?

## Evaluation and Physical-Law Benchmarks

### Paper Note: P037 VideoPhy: Evaluating Physical Commonsense for Video Generation

**Metadata**

- Paper ID: P037
- Title: *VideoPhy: Evaluating Physical Commonsense for Video Generation*. citeturn5view1turn6view1
- Authors: Hritik Bansal, Zongyu Lin, Tianyi Xie, Zeshun Zong, Michal Yarom, Yonatan Bitton, Chenfanfu Jiang, Yizhou Sun, Kai-Wei Chang, Aditya Grover. citeturn5view1
- Year: 2025
- Venue: ICLR 2025 **[from your local database; official venue page not separately checked in this pass]**
- URL: arXiv abstract page. citeturn5view1
- arXiv ID / DOI: arXiv:2406.03520. citeturn5view1
- BibTeX key: `bansal2025_videophy_prov`
- Current category: `evaluation_benchmarks`

**One-sentence survey summary**

VideoPhy is a benchmark paper that redirects the field away from visual impressiveness alone and toward **physical commonsense evaluation** for generative video and simulation models. citeturn5view1turn35view0

**Problem setting**

The paper asks whether current text-to-video models actually obey semantic prompts and physical commonsense, rather than merely producing visually plausible videos. This is directly relevant to world-model surveys because high-fidelity video generation is often mistaken for accurate world simulation. citeturn5view1

**Representation of the world**

Representation: **evaluation benchmark / prompt space**, not a learned world representation. The benchmark is organized around physical interaction captions spanning categories of material interactions and complexity. citeturn35view2

**Dynamics modeling**

This paper does not propose a predictive dynamics model. Instead, it evaluates whether externally generated videos reflect physically sensible dynamics implied by prompts. It also introduces an automatic evaluator, VideoCon-Physics, to approximate human judgments. citeturn5view1turn35view0

**Conditioning and interaction**

The evaluated generative systems are conditioned on **text prompts**. VideoPhy’s caption set spans solid-solid, solid-fluid, and fluid-fluid interactions and includes easy/hard difficulty subsets. citeturn5view1turn35view2

**Training objective**

For the benchmark itself: none. For the automatic evaluator, the objective is to predict human judgments of **semantic adherence** and **physical commonsense**; the paper reports ROC-AUC comparisons against other evaluators, including GPT-4-Vision and Gemini-Pro-Vision-1.5. citeturn35view0

**Evaluation**

The benchmark contains curated physical-interaction captions across 3 material-interaction categories, evaluates a range of open and closed text-to-video models, collects human annotations, and reports semantic-adherence and physical-commonsense judgments. The abstract states that the best model in their evaluation, CogVideoX-5B, satisfies caption + physical-law criteria on only 39.6% of instances. citeturn5view1turn35view2

**Key contribution**

The paper’s main contribution is to make **physical-law evaluation explicit and measurable** for video generation, exposing a major gap between visual quality and genuine world simulation. citeturn5view1turn35view0

**Main limitations**

Benchmark quality depends on prompt design and human annotation protocols. The benchmark is about generated video, not embodied interaction or action-conditioned control, and physical commonsense judgments remain partly qualitative even with the proposed automatic evaluator. citeturn35view0turn35view2

**Relation to the survey taxonomy**

Roles: **evaluation benchmark; physical-law evaluation**.

**Reliable claims I can cite**

- Claim: Existing text-to-video models remain far from accurate physical simulation.  
  - Evidence from the paper: The abstract states that the best-performing model satisfies the caption and physical laws for only 39.6% of instances. citeturn5view1
  - Source location if available: Abstract.
  - Suggested citation usage: Use when arguing that visual realism should not be equated with world-model correctness.
  - Confidence: high

- Claim: VideoPhy organizes prompts around solid-solid, solid-fluid, and fluid-fluid interactions.  
  - Evidence from the paper: Dataset construction and statistics explicitly list these three categories. citeturn5view1turn35view2
  - Source location if available: Sec. 3 / Table 1.
  - Suggested citation usage: Use when describing physical-law benchmark design.
  - Confidence: high

- Claim: VideoCon-Physics is a stronger automatic evaluator than the compared multimodal baselines for this benchmark.  
  - Evidence from the paper: Table 4 reports ROC-AUC 82/73 for VideoCon-Physics versus lower values for GPT-4-Vision, Gemini-Pro-Vision-1.5, and VideoCon. citeturn35view0
  - Source location if available: Sec. 5.2; Table 4.
  - Suggested citation usage: Use when discussing scalable evaluation of physical consistency in video generation.
  - Confidence: high

**Comparison with nearby papers**

Unlike **P004–P013**, VideoPhy is not a world model but an evaluation instrument. It is especially valuable when read beside **P012** and **P013**, because both show impressive generative ability but do not by themselves establish strong physical commonsense or physical-law compliance. citeturn31view3turn33view1turn5view1

**Open questions raised by this paper**

- How should physical evaluation benchmarks include **interaction, control, and counterfactual rollout** rather than text-only generation?
- Can automatic evaluators reliably judge **causality and conservation-style physics**, not just surface plausibility?
- What benchmark suite best unifies **video quality, controllability, and physical correctness** for world models?

## Open Questions and Unresolved Checks

A few metadata items still merit later verification against official proceedings rather than arXiv alone. The most notable one is **P009’s author list**, where your local BibTeX entry appears inconsistent with the paper source I checked; in the notes above I followed the paper source. For **P013** and **P037**, I preserved the venue information from your local inventory while grounding the methodological content in primary arXiv/ar5iv sources. If you want, the next pass can focus only on **metadata normalization and note-file cleanup** rather than literature understanding.