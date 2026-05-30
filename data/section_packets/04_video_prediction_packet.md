# Source Packet: `manuscript/sections/04_video_prediction.tex`

## Packet Scope

This packet supports the section on video prediction and visual dynamics. It is not manuscript prose. It summarizes evidence that can be used later to draft a concept-driven section on how future-frame prediction becomes relevant to predictive world models.

Evidence policy:

- Use only completed analytical notes as claim evidence.
- Current evidence-ready papers for this section: P004, P005, P006.
- Metadata-only coverage targets: P020, P023, P024, P025, P026, P027, P028. Their note files exist but contain `UNKNOWN` evidence fields, so they should not support technical manuscript claims yet.
- Claims about P020 or P023-P028 must be marked `[NEEDS SOURCE]` until their notes are completed.

## Relevant Papers

| Paper ID | Citation key | Evidence status | One-sentence role for this section |
|---|---|---|---|
| P004 | `oh2015_action_conditional_video_prediction_prov` | Completed note | Core evidence for early deterministic, action-conditioned video prediction from high-dimensional Atari observations. |
| P005 | `finn2016_physical_interaction_video_prediction_prov` | Completed note | Core evidence for robot video prediction with action conditioning and pixel-motion transformations such as DNA/CDNA/STP. |
| P006 | `babaeizadeh2018_sv2p_prov` | Completed note | Core evidence for stochastic video prediction using latent variables to represent multiple plausible futures. |
| P020 | `voleti2022_mcvd_prov` | Metadata only; note incomplete | Candidate diffusion-video prediction bridge; use only as future coverage until notes are completed. |
| P023 | `leguen2020_phydnet_prov` | Metadata only; note incomplete | Candidate physics-informed video prediction paper about disentangling physical dynamics from unknown factors. |
| P024 | `gupta2023_maskvit_prov` | Metadata only; note incomplete | Candidate masked-token video prediction and planning-oriented video prediction paper. |
| P025 | `wang2019_e3dlstm_prov` | Metadata only; note incomplete | Candidate recurrent video prediction baseline representing mature LSTM-style spatiotemporal prediction. |
| P026 | `gao2022_simvp_prov` | Metadata only; note incomplete | Candidate simplified video prediction baseline for comparing strong non-interactive spatiotemporal predictors. |
| P027 | `villegas2017_motion_content_prov` | Metadata only; note incomplete | Candidate motion/content factorization paper for historical factorized prediction coverage. |
| P028 | `denton2018_svg_lp_prov` | Metadata only; note incomplete | Candidate stochastic-video extension with a learned prior; use only after note completion. |

## Evidence-Ready Claims

### C001: Action Conditioning Bridges Passive Prediction and World Modeling

- Claim: Action-conditioned video prediction is an early bridge from passive future-frame prediction to world modeling because it predicts future observations conditioned on candidate actions.
- Evidence-ready paper: P004.
- Citation: `\cite{oh2015_action_conditional_video_prediction_prov}`.
- Evidence summary: The P004 note states that the paper is an early action-conditioned, long-horizon video prediction study for high-dimensional RL observations and that the model uses action-conditioned feature transformations.
- Use in section: Opening motivation for why video prediction belongs in a world-model survey.
- Status: supported, narrow.

### C002: Pixel-Motion Prediction Reframes Robotic Future Prediction

- Claim: Pixel-motion prediction methods reframed video prediction from reconstructing future frames from scratch to transforming observed pixels, which is useful for physical interaction settings.
- Evidence-ready paper: P005.
- Citation: `\cite{finn2016_physical_interaction_video_prediction_prov}`.
- Evidence summary: The P005 note reports that the paper models pixel motion rather than reconstructing all appearance, using DNA, CDNA, and STP transformation mechanisms.
- Use in section: Transition from action-conditioned game video prediction to robot video prediction and visual physical interaction.
- Status: supported, narrow.

### C003: Pixel Metrics Are Insufficient for World-Model Evaluation

- Claim: Pixel prediction quality alone is not enough to evaluate world models; downstream control or planning utility can reveal usefulness that frame metrics miss.
- Evidence-ready papers: P004, P009, P012.
- Citation: `\cite{oh2015_action_conditional_video_prediction_prov,janner2019_o2p2_prov,alonso2024_diamond_prov}`.
- Evidence summary: P004 supports the section-relevant part: frame prediction quality alone can underestimate control usefulness. P009 and P012 broaden the evaluation point outside this section.
- Use in section: Limitation/evaluation paragraph explaining why future-frame metrics should not be treated as world-model correctness.
- Status: supported, but use P009/P012 only for cross-section framing if needed.

### C004: Stochastic Latents Address Multi-Modal Futures

- Claim: Stochastic latent variables are a central response to the multi-modal nature of future video prediction, where a single deterministic rollout can average over plausible futures.
- Evidence-ready paper: P006.
- Citation: `\cite{babaeizadeh2018_sv2p_prov}`.
- Evidence summary: The P006 note says SV2P is designed to generate different plausible futures from different latent samples and motivates stochastic prediction as a remedy for deterministic blurring under uncertainty.
- Use in section: Subsection on stochastic video prediction.
- Status: supported, narrow.

### C005: Stochastic Video Models May Need Special Training

- Claim: Stochastic video models can require special training procedures because naive end-to-end optimization may ignore latent variables.
- Evidence-ready paper: P006.
- Citation: `\cite{babaeizadeh2018_sv2p_prov}`.
- Evidence summary: The P006 note reports a variational lower bound and a three-phase training scheme introduced because naive training tends to ignore the latents.
- Use in section: Technical limitation of stochastic video prediction.
- Status: supported, narrow.

### C006: Temporal Structure of Stochastic Latents Matters

- Claim: The temporal structure of stochastic latents matters: time-varying latents can improve long-horizon stability, while time-invariant latents may better capture persistent factors.
- Evidence-ready paper: P006.
- Citation: `\cite{babaeizadeh2018_sv2p_prov}`.
- Evidence summary: The P006 note states that time-varying latents help long-horizon stability on some datasets, whereas time-invariant latents can work better when the key latent factor persists over the whole video.
- Use in section: Design trade-off inside stochastic prediction.
- Status: supported by one paper; phrase as a paper-specific design observation, not a general law.

### C019: Prediction Becomes Embodied When Futures Depend on Interventions

- Claim: Action-conditioned and interactive video models connect prediction to embodied use by making future video depend on interventions, policies, or latent controls.
- Evidence-ready papers: P004, P005, P013.
- Citation: `\cite{oh2015_action_conditional_video_prediction_prov,finn2016_physical_interaction_video_prediction_prov,bruce2024_genie_prov}`.
- Evidence summary: For this section, P004 and P005 support the action-conditioned video-prediction part. P013 belongs more naturally to the interactive-environments section.
- Use in section: Concluding bridge from video prediction to later interactive world models.
- Status: supported, but avoid making P013 central in `04_video_prediction.tex`.

## Paper-Level Notes for Drafting

### P004: Action-Conditional Video Prediction using Deep Networks in Atari Games

- Citation key: `oh2015_action_conditional_video_prediction_prov`.
- Role: Establishes action-conditioned future-frame prediction as an early bridge from passive video forecasting to learned transition models for agent-environment interaction.
- Inputs/outputs: past Atari frames plus discrete actions -> future video frames.
- Dynamics: CNN or CNN+LSTM encoder with multiplicative action-conditioned feature transformations; multi-step rollouts feed predictions back into the model.
- Evaluation: long-horizon MSE, qualitative rollouts, DQN score when predicted frames replace emulator frames, and informed exploration.
- Supported claims:
  - early action-conditioned long-horizon prediction from high-dimensional RL observations;
  - multiplicative action-conditioned transformations in feature space;
  - frame prediction quality alone can underestimate usefulness for control.
- Limitations from notes: deterministic, pixel-level, MSE-trained; handles stochasticity poorly; struggles with small task-critical objects; does not learn compact latent planning state or explicit physical/object structure.

### P005: Unsupervised Learning for Physical Interaction through Video Prediction

- Citation key: `finn2016_physical_interaction_video_prediction_prov`.
- Role: Moves video prediction toward physical interaction by predicting robot-object futures from raw video and robot actions.
- Inputs/outputs: previous frames plus future robot actions / initial robot state -> future video frames.
- Dynamics: predicts pixel motion rather than reconstructing full appearance; uses DNA, CDNA, and STP motion transformations with masks.
- Evaluation: BAIR robot pushing, seen/novel objects, Human3.6M; PSNR, SSIM, qualitative comparisons, action-intervention analysis.
- Supported claims:
  - models pixel motion instead of reconstructing future appearance from scratch;
  - CDNA/STP can induce unsupervised object-like decompositions;
  - proposed models outperform prior methods on robot pushing and Human3.6M and generalize better to novel objects.
- Limitations from notes: deterministic and blur-prone; multi-modal futures are not explicit; object structure is weakly object-centric; long-horizon performance degrades; still image-space rather than abstract latent world state.

### P006: Stochastic Variational Video Prediction

- Citation key: `babaeizadeh2018_sv2p_prov`.
- Role: Adds stochastic latent variables to future-frame prediction to represent multiple plausible futures.
- Inputs/outputs: past frames, optional actions, and sampled latent variables -> future video frames.
- Dynamics: autoregressive stochastic latent-variable predictor; inference network uses future frames during training, while test-time generation samples from the prior.
- Evaluation: toy stochastic movement, BAIR robot pushing, Human3.6M, earlier robotic pushing dataset; PSNR/SSIM, best-of-samples, qualitative diversity/consistency checks.
- Supported claims:
  - different latent samples can produce different plausible futures;
  - variational objective and staged training address latent ignoring;
  - time-varying and time-invariant latents have different empirical strengths.
- Limitations from notes: still pixel-space; relies partly on best-of-many metrics; does not disentangle object-level or physical state; posterior uses future frames during training.

## Metadata-Only Coverage Targets

These papers are relevant to the requested focus areas but cannot yet support technical claims because their notes contain `UNKNOWN` evidence fields.

### P023: PhyDNet

- Citation key: `leguen2020_phydnet_prov`.
- Metadata role: physics-informed future-frame prediction / physical-dynamics disentanglement.
- Metadata fields: category `video_prediction`; model family `physics_informed_rnn`; physical prior `pde_inspired`; datasets listed as traffic, human motion, physical sequences; metrics PSNR/SSIM.
- Usable claim now: The paper exists in metadata as a candidate for physics-informed video prediction coverage.
- Unsupported claim to mark: "PhyDNet disentangles physical dynamics from unknown residual factors" `[NEEDS SOURCE]`.

### P024: MaskViT

- Citation key: `gupta2023_maskvit_prov`.
- Metadata role: masked-token video prediction with planning-oriented use.
- Metadata fields: category `video_prediction`; sub-category `masked_token_prediction`; input `video_plus_action`; model family `masked_transformer`; datasets RoboNet / robotic manipulation; metrics prediction metrics / task success.
- Usable claim now: The paper exists in metadata as a candidate for masked video prediction and planning-oriented video prediction.
- Unsupported claim to mark: "Masked token prediction improves planning-oriented video prediction" `[NEEDS SOURCE]`.

### P025: Eidetic 3D LSTM

- Citation key: `wang2019_e3dlstm_prov`.
- Metadata role: recurrent video prediction baseline.
- Metadata fields: category `video_prediction`; model family `rnn_lstm`; datasets MovingMNIST, KTH, Human3.6M; metrics prediction metrics.
- Usable claim now: The paper exists in metadata as a candidate recurrent baseline.
- Unsupported claim to mark: "E3D-LSTM is a strong recurrent baseline for mature spatiotemporal prediction" `[NEEDS SOURCE]`.

### P026: SimVP

- Citation key: `gao2022_simvp_prov`.
- Metadata role: simplified video prediction baseline.
- Metadata fields: category `video_prediction`; model family `cnn_based_predictor`; datasets MovingMNIST, weather, traffic; metrics prediction metrics.
- Usable claim now: The paper exists in metadata as a candidate simplified baseline.
- Unsupported claim to mark: "SimVP provides a strong simple baseline for spatiotemporal prediction" `[NEEDS SOURCE]`.

### P027: Decomposing Motion and Content

- Citation key: `villegas2017_motion_content_prov`.
- Metadata role: motion/content factorization for natural video prediction.
- Metadata fields: category `video_prediction`; sub-category `content_motion_factorization`; model family `cnn_convlstm`; datasets KTH and UCF101.
- Usable claim now: The paper exists in metadata as a candidate factorized prediction paper.
- Unsupported claim to mark: "Motion/content factorization improves natural video sequence prediction" `[NEEDS SOURCE]`.

### P028: Stochastic Video Generation with a Learned Prior

- Citation key: `denton2018_svg_lp_prov`.
- Metadata role: stochastic video generation with learned prior.
- Metadata fields: category `video_prediction`; sub-category `stochastic_prediction`; model family `vae_rnn`; datasets MovingMNIST, BAIR, KTH.
- Usable claim now: The paper exists in metadata as a candidate stochastic-video extension beyond SV2P.
- Unsupported claim to mark: "A learned prior improves stochastic future prediction relative to fixed-prior variants" `[NEEDS SOURCE]`.

### P020: MCVD

- Citation key: `voleti2022_mcvd_prov`.
- Metadata role: diffusion-based video prediction, generation, and interpolation.
- Metadata fields: category `diffusion_world_models`; sub-category `diffusion_video_prediction`; task future-frame prediction; datasets BAIR, KTH, Cityscapes sequence; metrics FVD and prediction metrics.
- Use recommendation: Mention only as a boundary paper or defer to the diffusion section until notes are completed.
- Unsupported claim to mark: "MCVD provides a direct diffusion formulation for video prediction and interpolation" `[NEEDS SOURCE]`.

## Comparison Dimensions

Use these dimensions to synthesize rather than list papers:

1. Deterministic versus stochastic futures.
   - P004 and P005 are deterministic in the completed notes.
   - P006 explicitly models multiple plausible futures with latent variables.

2. Passive prediction versus action-conditioned prediction.
   - P004 and P005 condition on actions.
   - P006 supports action-free and action-conditioned settings.
   - P025-P027 appear metadata-relevant to mostly action-free prediction but need notes.

3. Pixel reconstruction versus pixel transformation.
   - P004 decodes future frames from learned features.
   - P005 transforms previous pixels through DNA/CDNA/STP-style mechanisms.
   - P027 is a candidate for motion/content factorization but needs evidence.

4. Image-space prediction versus abstract world state.
   - P004-P006 remain primarily image/pixel-space predictors.
   - The section should bridge to later latent/object-centric sections by explaining why image-space prediction can be useful but limited.

5. Evaluation by visual fidelity versus downstream utility.
   - P004 supports the claim that frame quality alone may miss control usefulness.
   - P005 uses PSNR/SSIM and qualitative/action-intervention analyses.
   - Broader evaluation claims should be deferred to the evaluation section.

6. Short-horizon reconstruction versus long-horizon rollout.
   - P004 uses curriculum learning over rollout length.
   - P005 notes long-horizon degradation.
   - P006 raises long-horizon stochastic stability issues through time-varying versus time-invariant latents.

7. Model assumptions and inductive biases.
   - P005 introduces motion-transform bias and weak object-like masks.
   - P023 is a candidate physics-informed baseline but needs notes.
   - P024 is a candidate masked-token / planning-oriented predictor but needs notes.

## Unresolved or Weakly Supported Claims

- Later recurrent video prediction baselines such as E3D-LSTM and SimVP should be included for context, but claims about their empirical strength are `[NEEDS SOURCE]`.
- Motion/content factorization beyond P005's pixel-motion transformations is `[NEEDS SOURCE]` until P027 is completed.
- Masked-token prediction and planning-oriented video prediction are `[NEEDS SOURCE]` until P024 is completed.
- Physics-informed future-frame prediction is `[NEEDS SOURCE]` until P023 is completed.
- SVG-LP-style learned-prior stochastic prediction is `[NEEDS SOURCE]` until P028 is completed.
- Diffusion-based video prediction as part of the video-prediction lineage is `[NEEDS SOURCE]` until P020 is completed; it may be better handled in the diffusion section.
- Any broad claim that video prediction "solves" physical dynamics or learns physical laws is unsupported by current completed notes and should be avoided.
- Any claim that pixel-level prediction is sufficient for world modeling is contradicted by the evaluation limitations in P004/P005/P006 and should be weakened.

## Suggested Subsection Structure for `04_video_prediction.tex`

1. `\subsection{From Future Frames to Action-Conditioned Prediction}`
   - Purpose: explain why video prediction enters the survey.
   - Evidence: P004, with P005 as transition to robot interaction.
   - Claims: C001, C019.

2. `\subsection{Robot Video Prediction and Pixel-Motion Dynamics}`
   - Purpose: describe motion-transform prediction and physical interaction from pixels.
   - Evidence: P005.
   - Claims: C002; P005 reliable claims about DNA/CDNA/STP and weak object-like masks.

3. `\subsection{Stochastic Futures and Latent Uncertainty}`
   - Purpose: show why deterministic prediction is insufficient under ambiguity.
   - Evidence: P006.
   - Claims: C004, C005, C006.

4. `\subsection{Broader Video-Prediction Baselines and Factorizations}`
   - Purpose: reserve space for recurrent baselines, simplified baselines, motion/content factorization, physics-informed prediction, and masked prediction.
   - Evidence: currently metadata only for P023-P028; do not state technical claims without `[NEEDS SOURCE]`.
   - Drafting note: this subsection should remain short or explicitly provisional until notes are completed.

5. `\subsection{Limits of Pixel-Level Prediction for World Modeling}`
   - Purpose: synthesize limitations and bridge to object-centric, latent, diffusion, and interactive sections.
   - Evidence: P004, P005, P006; optionally cross-reference P009/P012 for evaluation beyond frame metrics if the section needs a forward pointer.
   - Claims: C003, C019; limitations from notes.

## Drafting Guidance

- Lead with concepts: action conditioning, motion transformation, stochasticity, and evaluation limitations.
- Do not organize the section as "P004 did X, P005 did Y, P006 did Z"; instead, use the papers as evidence for conceptual transitions.
- Use cautious terms such as "illustrates", "provides evidence that", "in this setting", and "in the completed notes" where the support is narrow.
- Keep P023-P028 in a coverage paragraph or table until their notes are complete.
- Do not cite P023-P028 for claims in manuscript prose yet, even though their BibTeX entries exist.
- Avoid broad field claims about deterministic baselines, masked prediction, or learned-prior stochastic models until evidence is extracted from notes.

## Immediate Note-Completion Priorities

1. P024, because it directly connects video prediction with planning-oriented use.
2. P027, because motion/content factorization is explicitly requested and helps compare with P005's motion-transform approach.
3. P025 and P026, because they anchor recurrent and simplified prediction baselines.
4. P028, because it broadens stochastic prediction beyond SV2P.
5. P023, because it may connect video prediction to physical dynamics priors.
6. P020, if the section needs a bridge to diffusion-based prediction rather than leaving that for the diffusion section.
