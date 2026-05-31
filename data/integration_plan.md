# Section-Integration Plan
## "Learning Predictive World Models from Videos: A Survey on Generative Simulation and Physical Dynamics"

---

## Overview: Paper-to-Section Mapping

| New Paper | Primary Section | Secondary Section | Role |
|---|---|---|---|
| iVideoGPT (Wu et al., NeurIPS 2024) | Section 6 | Section 7 | Core |
| V-JEPA 2 (Assran et al., 2025) | Section 6 | — | Core |
| LAPA (Ye et al., ICLR 2025) | Section 7 | — | Core |
| Cosmos (NVIDIA, 2025) | Section 7 | — | Core |
| Diffusion Forcing (Chen et al., NeurIPS 2024) | Section 7 | Section 4 | Core |
| WorldModelBench (Li et al., NeurIPS 2025) | Section 8 | — | Core |
| VideoPhy-2 (Bansal et al., 2025) | Section 8 | — | Core |
| Morpheus (2025) | Section 8 | — | Core |
| WorldScore (Duan et al., ICCV 2025) | Section 8 | — | Supplementary |
| What-If World (2026) | Section 8 | — | Brief mention |

**Note:** Sections 4 and 5 receive the fewest new additions because the 10 selected papers concentrate in latent/token world models (Section 6), diffusion/interactive models (Section 7), and evaluation (Section 8). This reflects where the field has produced the most significant new work since 2024.

---

## SECTION 4: Video Prediction and Visual Dynamics

### 4.1 New Papers to Add
**Primary addition: Diffusion Forcing** (referenced, not fully discussed)

Diffusion Forcing does not belong in Section 4 as a core discussion, but it should be **referenced** in two places: (a) Section 4.4 as a hybrid prediction paradigm that bridges autoregressive next-token prediction with diffusion-based denoising, and (b) as a forward pointer to Section 7 where it is discussed in detail.

### 4.2 Existing Claims Strengthened
- The claim in Section 4.4 that "masked-token prediction" and "diffusion-based video prediction" are adjacent architectural directions worth noting. Diffusion Forcing is the most prominent example of their convergence.
- The transition claim in Section 4.5 that video prediction alone is insufficient and leads to structured/latent approaches.

### 4.3 New Comparison Dimension Introduced
**Next-token prediction vs. full-sequence diffusion as video dynamics mechanisms.** Currently, Section 4 separates autoregressive (next-token) and diffusion (full-sequence) as distinct dynamics families. Diffusion Forcing blurs this boundary by training a causal next-token diffusion model with per-token noise levels. This introduces a new taxonomy position: **causal diffusion** as a dynamics mechanism.

### 4.4 Sentence-Level Revisions

**Revision A** — In Section 4.4, after the sentence about "masked-token prediction, learned-prior stochastic prediction, and diffusion-based video prediction," add:

> "A convergent direction trains diffusion models causally for next-token prediction rather than full-sequence generation. Diffusion Forcing denoises each token with an independent noise level, enabling autoregressive video rollouts that combine next-token flexibility with diffusion guidance and sampling [cite Diffusion Forcing]. This hybrid mechanism is discussed further in the context of diffusion-based world models (Section 7)."

**Revision B** — In Section 4.5 (Transition Toward Structured and Latent World Models), after the sentence referencing Genie and DIAMOND, add a brief forward pointer:

> "Token-based autoregressive world models (Section 6) and causal diffusion predictors (Section 7) offer additional responses to the same limitations."

### 4.5 Paragraph-Level Revisions
**No new paragraph needed.** Diffusion Forcing should be integrated as a referenced example within existing paragraphs (4.4 and 4.5), not as a new subsection. Section 4's scope should remain focused on the foundational video-prediction papers (action-conditioned Atari, robot pushing, SV2P) that establish the predictive-problem framing.

### 4.6 Table/Figure Updates
**Table 1 (Concept-Driven Taxonomy):** Add "Diffusion Forcing" as a representative example in a new sub-row or parenthetical within the "Action-conditioned pixel/motion prediction" family, with a footnote clarifying it bridges to diffusion. Alternatively, add a note to the "Dynamics" column indicating that "causal diffusion" is a hybrid dynamics mechanism.

### 4.7 Overclaim to Avoid
Do not expand Section 4 to discuss Diffusion Forcing at the same depth as action-conditioned Atari prediction or SV2P. The paper's primary contribution is to diffusion-based dynamics (Section 7), not to foundational video prediction. Avoid implying that Diffusion Forcing is primarily a video-prediction paper—it is a dynamics-mechanism paper with implications for prediction.

---

## SECTION 5: Object-Centric and Structured Physical Dynamics

### 5.1 New Papers to Add
**No primary additions.** None of the 10 selected papers directly address object-centric or relational physical dynamics. This reflects where the recent research emphasis has shifted: toward latent/token representations and large-scale generative models rather than explicit object-relation graphs.

**Secondary reference: V-JEPA 2** (brief mention only in Section 5.4)

V-JEPA 2 can be briefly referenced in the "slot-based and compositional extensions" discussion as an example of **feature-space representations that implicitly capture object structure** without explicit object graphs.

### 5.2 Existing Claims Strengthened
- Section 5.4's discussion of slot-based and compositional extensions, which notes that "a structured model may assume ground-truth object states, infer object-centric codes from pixels, learn slots without direct object labels, or induce keypoints and latent entities from video." V-JEPA 2 exemplifies the "infer object-centric codes from pixels via self-supervised learning" path.

### 5.3 New Comparison Dimension Introduced
**Implicit vs. explicit object representations.** V-JEPA 2 learns dense features through self-supervised prediction without explicit object slots or graphs. This introduces a contrast between (a) models with explicit object structure (Interaction Networks, VIN, O2P2) and (b) models where object-like structure may emerge implicitly in feature space (V-JEPA 2). This dimension prepares the transition to Section 6.

### 5.4 Sentence-Level Revision
In Section 5.4, after the sentence listing different assumptions (object states, segmentation, slots, keypoints), add:

> "More recent self-supervised video representation models learn dense predictive features from internet-scale video without explicit object-level supervision, offering an alternative in which object-like structure may emerge implicitly rather than through explicit architectural bias [cite V-JEPA 2]. The trade-off is that such representations are less interpretable but may scale more effectively to complex real-world video."

### 5.5 Paragraph-Level Revision
**No new paragraph needed.** The V-JEPA 2 reference should be one sentence within the existing Section 5.4 discussion of slot-based and compositional extensions. Section 5's core focus (Interaction Networks, VIN, O2P2) should remain unchanged.

### 5.6 Table/Figure Updates
**No update to Table 1 required** for V-JEPA 2 in Section 5. V-JEPA 2 belongs in the latent world model family (Table 1, Row 4), not the object-centric family.

### 5.7 Overclaim to Avoid
Do not imply that V-JEPA 2 is an object-centric model. It does not use object graphs, slots, or relational dynamics. It is a feature-space model that may implicitly capture object structure. Avoid overstating the extent to which self-supervised feature learning replaces explicit physical structure.

---

## SECTION 6: Latent World Models for Planning and Control

### 6.1 New Papers to Add
**Primary additions:**
1. **iVideoGPT** (Wu et al., NeurIPS 2024) — Core discussion
2. **V-JEPA 2** (Assran et al., 2025) — Core discussion

### 6.2 Existing Claims Strengthened
**For iVideoGPT:**
- Section 6.1's claim that "policies can be trained inside a hallucinated environment" — iVideoGPT demonstrates this at scale with discrete token-based environments.
- Section 6.4's discussion of "discrete latent world models" and "token and transformer models" — iVideoGPT is the most prominent example, replacing the vague "should be compared carefully" placeholder with concrete evidence.

**For V-JEPA 2:**
- Section 6.1's central claim that "a learned latent model can act as a simulator for downstream control" — V-JEPA 2-AC provides the strongest recent evidence with zero-shot robot planning.
- Section 6.2's claim about RSSM-style latent dynamics — V-JEPA 2 offers a contrasting non-generative (latent-prediction) path.
- Section 6.4's discussion of "feature-space planning with pretrained visual representations" — V-JEPA 2 is the prime example.

### 6.3 New Comparison Dimensions Introduced
**Dimension 1: Discrete token vs. continuous latent states.** iVideoGPT introduces discrete token-based latent dynamics (via VQ-VAE tokenization + autoregressive transformer) as an alternative to RSSM's continuous latent states. This is a new representation axis within Section 6.

**Dimension 2: Generative vs. non-generative latent prediction.** V-JEPA 2 uses a joint-embedding predictive architecture (JEPA) that predicts in representation space without ever generating pixels or decoding observations. This contrasts with RSSM/Dreamer, which use generative observation models (VAE decoders) during training. This is a fundamental methodological distinction.

**Dimension 3: Scale of pretraining data.** iVideoGPT is pre-trained on "millions of human and robotic manipulation trajectories"; V-JEPA 2 on "over 1 million hours of internet video." This introduces the question of whether world models benefit from large-scale pretraining on diverse data—a dimension not discussed in the current manuscript's focus on single-environment models.

### 6.4 Sentence-Level Revisions

**Revision A (Section 6.1)** — After the sentence about the recurrent world-model formulation (VAE, MDN-RNN, controller), add:

> "More recent token-based approaches instead discretize visual observations into compressed tokens and apply autoregressive next-token prediction over observation-action-reward sequences. iVideoGPT pre-trains on millions of trajectories from multiple domains and transfers to downstream action-conditioned video prediction, visual planning, and model-based reinforcement learning, demonstrating that discrete token dynamics can achieve scalability and task generality not present in the earlier recurrent formulation [cite iVideoGPT]."

**Revision B (Section 6.2)** — After the discussion of PlaNet's RSSM, add a new methodological contrast:

> "An alternative latent-dynamics paradigm learns predictive representations without generative observation decoding. V-JEPA 2, trained on over one million hours of internet video through a joint-embedding predictive architecture, learns feature-space representations that support downstream planning when post-trained with a small amount of robot interaction data. Notably, V-JEPA 2 achieves zero-shot pick-and-place planning on physical robot arms without task-specific training or reward, suggesting that non-generative latent prediction can suffice for control [cite V-JEPA 2]."

**Revision C (Section 6.4)** — Replace the placeholder sentence "token and transformer models ask whether sequence modeling can replace recurrent latent dynamics" with:

> "Token and transformer models have moved from a theoretical question to an active research direction. iVideoGPT uses a compressive visual tokenizer and causal transformer to perform next-token prediction over multimodal sequences, while V-JEPA 2 scales self-supervised video representation learning to internet-scale data and demonstrates transfer to robot planning through a latent action-conditioned post-training stage [cite both]. These results suggest that both discrete token dynamics and non-generative feature prediction are viable alternatives to recurrent state-space models, though evidence remains partial: iVideoGPT's transfer is strongest within visually similar domains, and V-JEPA 2 requires the AC post-training step to function as a planner."

**Revision D (Section 6.5 / Transition)** — After the discussion of the abstraction-fidelity trade-off, add:

> "The latent-model family has also diversified internally. Discrete token-based models and non-generative feature predictors offer different points in the design space from RSSM-style continuous latents, raising new questions about which latent structure best supports planning, imagination, and physical reasoning."

### 6.5 Paragraph-Level Revisions

**New paragraph after Section 6.1's recurrent world-model discussion:**

> "Token-based latent simulators. A distinct branch of latent world models discretizes high-dimensional visual observations through learned compression (e.g., VQ-VAE) and treats world simulation as autoregressive next-token prediction over sequences of observation, action, and reward tokens. iVideoGPT exemplifies this approach: it introduces a novel compressive tokenization technique and trains a causal transformer on millions of human and robotic manipulation trajectories, achieving competitive performance on action-conditioned video prediction, visual planning, and model-based RL [cite iVideoGPT]. Unlike RSSM-style models, which use continuous latent states and generative observation decoders, token-based models naturally inherit the scalability properties of autoregressive transformers, including the ability to pre-train on diverse data and transfer to new tasks. However, they also inherit limitations: the discrete tokenization step may lose fine visual details relevant for control, and autoregressive generation can accumulate errors during long rollouts. iVideoGPT therefore represents a complementary point in the latent-model design space rather than a replacement for recurrent or continuous-state formulations."

**New paragraph after Section 6.2's PlaNet/RSSM discussion:**

> "Non-generative latent prediction. An alternative to the generative latent-state formulation (VAE encoder/decoder + recurrent dynamics) learns predictive representations without reconstructing observations. V-JEPA 2 uses a joint-embedding predictive architecture trained on over one million hours of internet video to learn dense visual representations [cite V-JEPA 2]. When combined with a small amount of robot interaction data through an action-conditioned post-training stage (V-JEPA 2-AC), the model achieves zero-shot planning for pick-and-place tasks on physical robot arms in novel environments. This result is notable because it demonstrates control-relevant latent dynamics without pixel generation during either training or inference. The trade-off is that V-JEPA 2's representations are not directly interpretable as physical state variables, and the model requires the AC post-training step to function as a planner—self-supervised video understanding alone does not yield action-conditioned prediction."

### 6.6 Table/Figure Updates

**Table 1 (Taxonomy):** Update Row 4 ("Latent planning and control"):
- **Representative examples column:** Add "iVideoGPT; V-JEPA 2" alongside "Recurrent World Models; PlaNet; Dreamer."
- **Representation column:** Expand to "Compact latent states, RSSM, VAE/RNN, **discrete tokens, joint-embedding features**"
- **Dynamics column:** Expand to include "Recurrent state-space transitions, **autoregressive token prediction, non-generative feature prediction**"

### 6.7 Overclaims to Avoid
1. **Do not claim iVideoGPT supersedes RSSM/Dreamer.** iVideoGPT and RSSM occupy different design points (discrete tokens vs. continuous states; transformer vs. recurrent). Present them as complementary.
2. **Do not claim V-JEPA 2 replaces generative world models.** V-JEPA 2 requires an action-conditioned post-training stage (AC) to function as a planner; the base model alone is not action-conditioned. Emphasize this limitation.
3. **Do not equate large-scale pretraining with physical understanding.** Both iVideoGPT and V-JEPA 2 leverage large-scale data, but neither is evaluated for physical-law generalization or long-horizon physical consistency.
4. **Do not overstate cross-domain transfer.** iVideoGPT's transfer is strongest within visually similar domains; the generalization gap between human videos and robot control remains significant.

---

## SECTION 7: Diffusion-Based and Interactive World Models

### 7.1 New Papers to Add
**Primary additions:**
1. **Cosmos** (NVIDIA, 2025) — Core discussion
2. **LAPA** (Ye et al., ICLR 2025) — Core discussion
3. **Diffusion Forcing** (Chen et al., NeurIPS 2024) — Core discussion

**Secondary addition:**
4. **iVideoGPT** (referenced as a bridge from Section 6)

### 7.2 Existing Claims Strengthened
**For Cosmos:**
- Section 7.1's discussion of the diffusion-video lineage — Cosmos is the largest-scale industrial effort in this lineage, explicitly designed for physical AI.
- Section 7.2's discussion of DIAMOND as the "main example" of diffusion world models — Cosmos extends this from Atari to robotics and autonomous driving.
- Section 7.5's discussion of the limitation that "visual realism, controllability, temporal consistency, and physical validity do not necessarily improve together" — Cosmos provides the strongest evidence for this limitation (poor performance on physical benchmarks despite high visual quality).

**For LAPA:**
- Section 7.3's discussion of Genie and learned latent actions — LAPA extends Genie's concept to vision-language-action models for real robots, and does so without action labels during pretraining.
- The claim that "controllability can emerge from video-only learning" — LAPA provides the strongest evidence by outperforming action-labeled VLA models.

**For Diffusion Forcing:**
- Section 7.2's discussion of conditional diffusion as image-space dynamics — Diffusion Forcing introduces a fundamentally different way to use diffusion (causal next-token rather than full-sequence).
- Section 7.4's discussion of newer interactive diffusion directions — Diffusion Forcing is the technical foundation for several follow-up papers.

### 7.3 New Comparison Dimensions Introduced
**Dimension 1: Full-sequence diffusion vs. causal diffusion for dynamics.** DIAMOND uses full-sequence conditional diffusion; Diffusion Forcing uses causal next-token diffusion with per-token noise levels. This is a new dynamics axis.

**Dimension 2: Labeled vs. unlabeled action pretraining for interactive models.** Genie and DIAMOND occupy different points (latent actions from unlabeled video vs. known actions). LAPA introduces a third point: unsupervised latent action learning via VQ-VAE between frames, followed by VLA fine-tuning with robot action labels.

**Dimension 3: Domain scope of diffusion world models.** DIAMOND = Atari games. Cosmos = robotics, autonomous driving, and general physical AI. This introduces the question of whether diffusion world models generalize across physical domains.

**Dimension 4: Open-weight world foundation models.** Cosmos is explicitly released as an open-weight platform for customization. This introduces the question of accessibility and reproducibility in world-model research.

### 7.4 Sentence-Level Revisions

**Revision A (Section 7.1)** — After the sentence about MCVD, add:

> "The diffusion-video lineage has since expanded to industrial scale. Cosmos, released by NVIDIA as an open-weight world foundation model platform, provides pre-trained diffusion and autoregressive video models at multiple scales, together with fine-tuning toolkits for physical AI applications including robotics and autonomous driving [cite Cosmos]. Cosmos represents an explicit industry effort to position video generation models as general-purpose world simulators rather than content-creation tools."

**Revision B (Section 7.2)** — After the DIAMOND discussion, add:

> "Causal diffusion offers an alternative dynamics mechanism. Diffusion Forcing trains a diffusion model to denoise tokens with independent per-token noise levels, applied causally for next-token prediction [cite Diffusion Forcing]. This combines the guidance and sampling strengths of diffusion with the variable-length rollout capability of autoregressive models. Experiments demonstrate rollout beyond the training horizon without divergence and improved performance in decision-making and planning tasks. Diffusion Forcing therefore blurs the boundary between diffusion-based and autoregressive world models: it is simultaneously a diffusion model and a causal next-token predictor."

**Revision C (Section 7.3)** — After the Genie discussion, add:

> "Latent action pretraining has been extended to vision-language-action models for robotics. LAPA (Latent Action Pretraining for general Action models) learns discrete latent actions via VQ-VAE between image frames from internet-scale videos without ground-truth action labels, pretrains a vision-language-action model to predict these latent actions conditioned on visual observations and task descriptions, and fine-tunes on small-scale robot data to map latent to physical actions [cite LAPA]. This extends Genie's video-only learning paradigm by showing that unsupervised latent actions can transfer to real robot manipulation and, remarkably, that pretraining on human manipulation videos without action labels can outperform state-of-the-art VLA models trained with explicit robot action labels. The limitation is that fine-tuning on robot data remains necessary: latent actions alone do not yield physically grounded control."

**Revision D (Section 7.4)** — Expand the placeholder paragraph about VideoWorld and Vid2World:

> "VideoWorld, Vid2World, and Nano World Models are newer efforts at the boundary between video generation, diffusion, and interactive world modeling [cite all]. These papers share a common technical lineage: they adopt causal or guided diffusion mechanisms (inspired by Diffusion Forcing) for next-frame prediction in game or robot domains. Their evaluation spans action-conditioned rollouts, long-horizon consistency, and transfer to control tasks. However, these results remain partial: action spaces are domain-specific, long-horizon physical consistency is not established, and generalization across diverse visual environments remains limited."

**Revision E (Section 7.5)** — After the discussion of VideoPhy and physical validity, add:

> "The physical-validity problem persists even at industrial scale. Cosmos models, despite high visual fidelity and domain-specific fine-tuning, exhibit systematic failures on physical-consistency benchmarks [cite Cosmos performance on Morpheus / physical benchmarks]. This confirms that scaling diffusion video models does not by itself resolve physical-law adherence, and that visual realism should not be treated as evidence of physically valid simulation even for models explicitly designed as world foundation models."

### 7.5 Paragraph-Level Revisions

**New subsection: 7.2.1 "Causal Diffusion as Next-Token Dynamics" (after Section 7.2)**

> "DIAMOND treats diffusion as a full-sequence conditional generation problem: the model generates an entire observation given a conditioning context. An alternative treats diffusion as a causal next-token prediction mechanism. Diffusion Forcing introduces a training paradigm where each token in a sequence is denoised with an independent noise level, enabling a causal model to generate one or several future tokens without fully diffusing past ones [cite Diffusion Forcing]. The key advantage is that the model can roll out sequences of continuous tokens (such as video latents) beyond the training horizon without the divergence typical of standard autoregressive predictors. Because each token has its own noise level, the model can also support novel sampling schemes that guide generation toward desirable trajectories—a capability particularly relevant for planning. Diffusion Forcing is proven to optimize a variational lower bound on the likelihoods of all subsequences, providing theoretical grounding. Empirically, it has been adopted as a foundational technique in subsequent world-model implementations, including interactive video generation systems. The limitation is that the computational cost of per-token diffusion remains higher than single-pass latent transitions in RSSM-style models, and the physical correctness of long rollouts in realistic environments has not been established."

**New subsection: 7.3.1 "Unsupervised Latent Actions for Robotic VLAs" (after Section 7.3)**

> "Genie demonstrated that controllability can emerge from video-only learning through inferred latent actions. LAPA extends this concept to vision-language-action models for robot manipulation. The key innovation is a three-stage pipeline: (1) a VQ-VAE action quantization model learns discrete latent actions between image frames from internet-scale videos without any robot action labels; (2) a latent vision-language-action model is pretrained to predict these discrete latent actions from visual observations and language task descriptions; (3) the model is fine-tuned on small-scale robot manipulation data to map latent actions to physical robot commands [cite LAPA]. This pipeline achieves strong performance on real-world manipulation tasks requiring language conditioning and generalization to unseen objects and instructions, and it outperforms state-of-the-art VLA models trained with explicit action labels during pretraining. The result is conceptually significant because it separates the scaling problem (pretraining on abundant unlabeled video) from the grounding problem (fine-tuning on scarce robot data). At the same time, the limitation is clear: robot action labels are still needed at the fine-tuning stage, and the latent actions learned during pretraining are not physically grounded until this mapping is learned. LAPA therefore shows that video-only pretraining improves downstream control, but it does not eliminate the need for robot-specific adaptation."

**Expanded subsection: 7.4 "Newer Interactive Diffusion Directions"**

Replace the current placeholder paragraph with:

> "Several newer papers advance the boundary between video generation, diffusion, and interactive world modeling. VideoWorld and Vid2World explore knowledge transfer from unlabeled video to interactive world models, applying causal diffusion mechanisms for controllable video generation [cite both]. Nano World Models provides a minimalist, reproducible implementation centered on Diffusion Forcing, enabling controlled studies of world-model design choices across environments and scales [cite Nano World Models]. These papers share a common technical lineage with Diffusion Forcing: they adopt causal or guided diffusion for next-frame prediction and evaluate through action-conditioned rollouts and downstream control performance. Collectively, they represent an emerging convergence between autoregressive token prediction (as in iVideoGPT, Section 6) and causal diffusion (as in Diffusion Forcing) for interactive world simulation. However, the evidence remains domain-specific: action spaces are tailored to particular games or robot settings, long-horizon physical consistency is not established, and the generalization gap between simulated and real-world interactive environments remains significant."

### 7.6 Table/Figure Updates

**Table 1 (Taxonomy):** Update Row 6 ("Interactive environments"):
- **Representative examples column:** Add "Cosmos; LAPA; Diffusion Forcing" alongside existing entries. Consider reorganizing the examples by sub-category: "Action-conditioned prediction; robot interaction prediction; Genie; **LAPA (unsupervised latent actions); Cosmos (world foundation model); Diffusion Forcing (causal diffusion dynamics)**"
- **Dynamics column:** Expand to include "**Causal diffusion rollouts, latent action VQ-VAE**"
- **Conditioning column:** Expand to include "**language instructions**" (for LAPA)

**Table 1 (Taxonomy):** Consider adding a new row or footnote for "Causal diffusion dynamics" as a cross-cutting dynamics mechanism that spans multiple representation families.

### 7.7 Overclaims to Avoid
1. **Do not claim causal diffusion replaces full-sequence diffusion.** Diffusion Forcing and DIAMOND serve different purposes; present them as complementary dynamics mechanisms.
2. **Do not claim LAPA eliminates the need for robot action labels.** The fine-tuning stage still requires robot data; LAPA reduces but does not remove this dependency.
3. **Do not present Cosmos as a solved physical simulator.** Despite the "world foundation model" branding, Cosmos exhibits systematic physical failures. Avoid endorsing marketing language.
4. **Do not conflate all "interactive" papers.** Action-conditioned prediction (Atari, robot pushing), latent actions (Genie, LAPA), and causal diffusion (Diffusion Forcing) represent distinct conditioning mechanisms. Maintain the survey's careful distinctions.
5. **Do not overstate the maturity of the causal-diffusion subfield.** VideoWorld, Vid2World, and Nano World Models are emerging; evidence is partial and domain-specific.

---

## SECTION 8: Evaluation and Open Challenges

### 8.1 New Papers to Add
**Primary additions:**
1. **WorldModelBench** (Li et al., NeurIPS 2025) — Core discussion
2. **VideoPhy-2** (Bansal et al., 2025) — Core discussion
3. **Morpheus** (2025) — Core discussion

**Secondary additions:**
4. **WorldScore** (Duan et al., ICCV 2025) — Supplementary
5. **What-If World** (2026) — Brief mention

### 8.2 Existing Claims Strengthened
**For WorldModelBench:**
- Section 8.1's claim that "reconstruction fidelity is best treated as a diagnostic for local observation prediction, not as evidence of physical dynamics" — WorldModelBench provides the most direct evidence by detecting physics violations that reconstruction metrics miss.
- Section 8.3's discussion of task utility — WorldModelBench introduces instruction-following as an evaluation axis.
- Section 8.4's discussion of uneven benchmark coverage — WorldModelBench fills a clear gap.

**For VideoPhy-2:**
- Section 8.3's discussion of VideoPhy — VideoPhy-2 provides a direct update with finer-grained analysis.
- The claim that "visually plausible generated videos can fail physical commonsense" — VideoPhy-2 quantifies this with a 22% joint performance rate on hard subsets.

**For Morpheus:**
- Section 8.3's discussion of physical consistency — Morpheus provides objective (PINN-based) evidence complementing human judgment benchmarks.
- Section 8.4's discussion of evaluation gaps — Morpheus addresses the "sim-to-real gap" in evaluation by using real physical experiments.

**For WorldScore:**
- Section 8.4's discussion of benchmark coverage — WorldScore unifies evaluation across 3D, 4D, and video generation.
- The claim that "no single axis is sufficient" — WorldScore's three-axis decomposition (controllability, quality, dynamics) provides empirical support.

**For What-If World:**
- Section 8.3's mention of causal and counterfactual evaluation as necessary — What-If World is the first modern benchmark explicitly targeting this.

### 8.3 New Comparison Dimensions Introduced
**Dimension 1: Human judgment vs. physics-based automatic evaluation.** VideoPhy/VideoPhy-2 rely on human evaluators and learned automatic evaluators. Morpheus uses PINN-fitted physical equations and conservation-law tests. WorldModelBench uses a fine-tuned specialized judger. This introduces a meta-evaluation question: what is the right way to automatically evaluate physical consistency?

**Dimension 2: Application-driven vs. general-world evaluation.** WorldModelBench evaluates in robotics and autonomous driving domains. WorldScore evaluates across static/dynamic, indoor/outdoor, photorealistic/stylized worlds. VideoPhy-2 focuses on action-centric real-world activities. This reveals that physical-evaluation benchmarks make different scope choices.

**Dimension 3: Causal/counterfactual evaluation.** What-If World introduces counterfactual action selection and causal structure discovery as evaluation tasks, distinct from forward physical prediction.

### 8.4 Sentence-Level Revisions

**Revision A (Section 8.1)** — After the discussion of why visual fidelity is not enough, add:

> "Recent benchmarks make this gap explicit through automated detection of subtle physics violations. WorldModelBench evaluates video generation models in robotics and autonomous driving domains using both instruction-following and physics-adherence criteria, and detects violations—such as objects irregularly changing size in ways that breach mass conservation—that are invisible to standard video quality metrics [cite WorldModelBench]. The benchmark includes 67K crowd-sourced human labels for 14 frontier models and a fine-tuned 2B-parameter judger that outperforms GPT-4o at detecting world-modeling violations. These results confirm that visual plausibility and physical correctness require separate measurement."

**Revision B (Section 8.3)** — After the VideoPhy discussion, add VideoPhy-2:

> "VideoPhy-2 extends physical-commonsense evaluation to action-centric real-world activities (e.g., playing tennis, backflips) and reports even stronger failure rates: the best model achieves only 22% joint performance (high semantic and physical adherence) on the hard subset, with particular weakness on conservation laws such as mass and momentum [cite VideoPhy-2]. The benchmark also introduces VideoPhy-AutoEval, a learned automatic evaluator for scalable assessment. These findings confirm that physical commonsense remains a critical unsolved problem even for state-of-the-art video generation models."

**Revision C (Section 8.3)** — After VideoPhy-2, add Morpheus:

> "Complementing human-judgment benchmarks, Morpheus evaluates video generative models through real-world physical experiments. Controlled laboratory recordings of falling balls, projectile motion, pendulums, and collisions are used to generate test prompts; generated videos are analyzed through zero-shot object segmentation, trajectory tracking, and physics-informed neural network (PINN) fitting to test conservation of energy, momentum, and acceleration [cite Morpheus]. Evaluation of six state-of-the-art models (including Cosmos, CogVideoX, and Veo3) reveals systematic physical failures across all models, with performance far below real-world physical invariance scores. Morpheus therefore provides objective, measurement-based evidence that complements the human-judgment approach of VideoPhy and VideoPhy-2."

**Revision D (Section 8.3)** — After the existing causal/counterfactual paragraph, add:

> "Causal reasoning evaluation has gained renewed attention. What-If World introduces the first benchmark explicitly focused on counterfactual reasoning for general world models in embodied scenarios, testing whether models can predict outcomes under alternative actions, select counterfactual interventions, and discover causal structure from video [cite What-If World]. This addresses a gap left by forward-prediction benchmarks: a model may predict physically plausible futures without understanding the causal effect of interventions."

**Revision E (Section 8.4)** — After the benchmark coverage discussion, add WorldScore:

> "WorldScore offers a unified evaluation framework across the full spectrum of world generation, from 3D and 4D scene generation to video generation models [cite WorldScore]. It decomposes world generation into next-scene generation tasks with camera-trajectory layout specifications and evaluates through three axes—controllability, quality, and dynamics—revealing that no single model family dominates across all axes. WorldScore thus provides a meta-evaluation perspective that complements domain-specific benchmarks such as WorldModelBench and physical-consistency benchmarks such as VideoPhy-2 and Morpheus."

### 8.5 Paragraph-Level Revisions

**New subsection: 8.1.1 "Automated Physics-Adherence Detection" (after Section 8.1)**

> "A promising direction in physical-evaluation research is the automated detection of world-modeling violations that are invisible to frame metrics. WorldModelBench exemplifies this approach: it collects 67K crowd-sourced human labels for instruction-following and physics-adherence violations in robotics and autonomous driving videos, then fine-tunes a 2B-parameter specialized judger that achieves 8.6% higher accuracy than GPT-4o at detecting violations [cite WorldModelBench]. VideoPhy-2 similarly trains VideoPhy-AutoEval, a learned automatic evaluator for physical-commonsense assessment [cite VideoPhy-2]. These efforts demonstrate that automated physical evaluation is feasible but requires domain-specific training: general-purpose multimodal models are not yet sufficient. The broader implication is that a robust evaluation suite should combine automatic metrics (for scalability), human judgment (for validity), and task-specific control evaluation (for utility)."

**Expanded subsection: 8.3 "Physical, Causal, and Counterfactual Evaluation"**

The current paragraph on VideoPhy should be expanded into a multi-paragraph discussion:

> "Physical consistency evaluation. VideoPhy established that generated videos can violate physical commonsense even when visually plausible, and organized prompts around solid-solid, solid-fluid, and fluid-fluid interactions [cite VideoPhy]. VideoPhy-2 extends this to action-centric real-world activities and reports that the best model achieves only 22% joint performance on hard subsets, with particular failure on conservation laws [cite VideoPhy-2]. Morpheus provides a complementary, object-measurement-based approach: it uses real-world physical experiments and PINN-fitted governing equations to test conservation of energy, momentum, and acceleration, revealing systematic failures across all tested models [cite Morpheus]. Together, these benchmarks establish physical-consistency evaluation as a multi-method enterprise: human judgment (VideoPhy, VideoPhy-2), automated judgers (WorldModelBench, VideoPhy-AutoEval), and physics-based measurement (Morpheus) each reveal different failure modes. No single method is sufficient.

> "Causal and counterfactual evaluation. While physical-consistency benchmarks test whether generated dynamics obey constraints, causal evaluation tests whether models understand the effect of interventions. Object-centric models provide partial evidence: Interaction Networks model object relations, Visual Interaction Networks infer hidden causes, and O2P2 uses object-oriented prediction for planning [cite all]. Modern benchmarks have extended this direction. What-If World evaluates counterfactual action selection, physical outcome prediction under intervention, and causal structure discovery from video [cite What-If World]. CLEVRER, PHYRE, and Physion remain relevant for causal video reasoning and physical prediction [cite all]. The key distinction is between forward prediction (what will happen?) and counterfactual reasoning (what would happen if a different action were taken?). A model may excel at the former while failing at the latter."

**Expanded subsection: 8.4 "Benchmark Coverage and Evidence Gaps"**

> "The current evaluation landscape is richer but still fragmented. VideoPhy, VideoPhy-2, Morpheus, and WorldModelBench each target physical consistency but through different methods and domains: VideoPhy-2 focuses on action-centric human activities with human evaluation; Morpheus uses real-world physical experiments with PINN-based measurement; WorldModelBench targets application-driven robotics and autonomous driving with automated judgers; and WorldScore unifies evaluation across 3D, 4D, and video generation through controllability, quality, and dynamics axes [cite all]. What-If World adds causal and counterfactual reasoning in embodied scenarios. This diversity is a strength—different benchmarks reveal different failure modes—but it also means that no single benchmark can establish world-model validity comprehensively. The survey's call for multi-axis evaluation (reconstruction fidelity, video quality, control return, physical consistency, causal reasoning, controllability, long-horizon robustness) is therefore more urgent than ever, and the exact composition of such a suite remains an open question."

### 8.6 Table/Figure Updates

**Table 1 (Taxonomy):** Update Row 8 ("Evaluation and benchmarks"):
- **Representative examples column:** Significantly expand. Current: "Control-utility evaluation; O2P2 planning; DIAMOND control; VideoPhy." New: "Control-utility evaluation; O2P2 planning; DIAMOND control; **WorldModelBench (physics-adherence detection); VideoPhy / VideoPhy-2 (physical commonsense); Morpheus (real-experiment measurement); WorldScore (unified world generation); What-If World (causal reasoning)**"
- **Metrics column:** Expand from "Metrics, prompts, generated videos, human judgments" to include "**PINN-fitted physical equations, automated physics judgers, counterfactual action evaluation**"

**Consider a new consolidated table:** A table summarizing the evaluation benchmarks discussed in Section 8, with columns for: benchmark name, evaluation method (human judgment / automatic / physical measurement), domain (general / robotics / autonomous driving / physical experiments), physical properties tested, and key finding about current model performance. This would replace the current scattered discussion with a centralized comparison.

### 8.7 Overclaims to Avoid
1. **Do not claim that automated physical evaluation is solved.** WorldModelBench's judger and VideoPhy-AutoEval are promising but imperfect; emphasize that human judgment remains necessary.
2. **Do not present Morpheus as replacing human-judgment benchmarks.** It complements them; different methods reveal different failure modes.
3. **Do not imply that newer benchmarks supersede older ones.** VideoPhy remains relevant; VideoPhy-2, Morpheus, and WorldModelBench extend rather than replace it.
4. **Do not overstate What-If World's maturity.** It is a 2026 arXiv preprint; present it as an emerging direction.
5. **Do not claim that benchmark diversity solves the evaluation problem.** The fragmentation across benchmarks (different methods, domains, properties) is itself a challenge; a unified evaluation suite remains unrealized.

---

## Paper Priority for Course-Assignment Version

### Absolutely Necessary (5 papers)
These papers are essential because they fill the largest gaps in the current manuscript, provide the clearest empirical results for student discussion, and cover the most active research directions.

| Paper | Why Essential |
|---|---|
| **WorldModelBench** (Li et al., NeurIPS 2025) | The most direct empirical support for the survey's central argument that video quality ≠ world-model validity. Clear results, accessible paper, strong pedagogical value. |
| **V-JEPA 2** (Assran et al., 2025) | Strongest recent evidence for Section 6's core claim about latent predictive states. Zero-shot robot planning is compelling for students. Accessible technical report. |
| **iVideoGPT** (Wu et al., NeurIPS 2024) | Best illustration of the token-based world model paradigm. Bridges Sections 6 and 7. Open-source code enables exploration. |
| **LAPA** (Ye et al., ICLR 2025) | Extends Genie (already cited) with rigorous experiments. The unsupervised-to-supervised transfer story is pedagogically valuable. |
| **VideoPhy-2** (Bansal et al., 2025) | Natural extension of VideoPhy (already cited). Quantified failure rates make physical commonsense gaps concrete for students. |

### Useful but Optional (4 papers)
These papers strengthen specific arguments but are not essential for a concise course-assignment version. Include them if space permits.

| Paper | When to Include |
|---|---|
| **Diffusion Forcing** (Chen et al., NeurIPS 2024) | If the course covers diffusion mechanisms in depth. Important for understanding the technical convergence between autoregressive and diffusion models. |
| **Morpheus** (2025) | If contrasting evaluation methodologies (human judgment vs. physics-based measurement) is a course theme. Provides the most objective physical-evaluation evidence. |
| **Cosmos** (NVIDIA, 2025) | If discussing industrial-scale world models or open-weight platforms. More suitable for background context than detailed analysis. |
| **WorldScore** (Duan et al., ICCV 2025) | If the course covers 3D/4D generation alongside video. Somewhat specialized; good as supplementary reading. |

### Brief Mention Only (1 paper)

| Paper | How to Mention |
|---|---|
| **What-If World** (2026) | Cite in Section 8.3's causal-evaluation paragraph as "an emerging direction in counterfactual world-model evaluation." Do not discuss in detail. Lower priority because it is a 2026 arXiv preprint with limited follow-up validation. |

---

## Cross-Cutting Integration Notes

### Reference Updates
- The **Introduction (Section 1)** should add forward references to iVideoGPT, V-JEPA 2, and WorldModelBench when listing the scope of the survey.
- **Section 2.2** should reference V-JEPA 2 as an example of a world model evaluated through behavior (robot planning) rather than frame reconstruction.
- **Section 3.2 (Conceptual Families)** should expand the "Image-space and diffusion-based world models" and "Evaluation" families with the new representative examples.
- **Section 9 (Conclusion)** should acknowledge that evaluation has become a more active research direction since the survey's initial drafting, citing WorldModelBench, VideoPhy-2, and Morpheus.

### Citation Consistency
- Use consistent citation keys for all 10 papers throughout.
- Where papers have both an arXiv version and a conference version (e.g., iVideoGPT at NeurIPS 2024, LAPA at ICLR 2025), cite the conference version as primary and note the arXiv ID.
- For technical reports without peer review (V-JEPA 2, Cosmos, VideoPhy-2, Morpheus, What-If World), use phrasing like "reported in" or "described in" rather than "shown" or "proved."

### Balance Check
- **Section 6** receives 2 core papers (iVideoGPT, V-JEPA 2). Ensure these do not dominate the existing PlaNet/Dreamer discussion. The recurrent world-model lineage remains the foundational content; iVideoGPT and V-JEPA 2 are extensions.
- **Section 7** receives 3 core papers (Cosmos, LAPA, Diffusion Forcing) + references. This section will grow substantially. Consider whether to split into subsections (7.1 diffusion, 7.2 interactive/latent actions, 7.3 causal diffusion) for clarity.
- **Section 8** receives 3 core + 2 supplementary papers. The evaluation discussion will become the longest part of the survey body. This is appropriate given the field's current emphasis on evaluation, but ensure the section remains organized (use subsections).

---

*End of Integration Plan*
