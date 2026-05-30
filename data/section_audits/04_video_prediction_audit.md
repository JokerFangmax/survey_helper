# Section Audit: `04_video_prediction.tex`

## 1. Major Claims

1. Video prediction is relevant to predictive world modeling when it rolls observations forward under visual history, actions, or uncertainty, but it is not equivalent to a full world model.
   - Supporting papers: P004, P005, P006.
   - Citation keys: `oh2015_action_conditional_video_prediction_prov`, `finn2016_physical_interaction_video_prediction_prov`, `babaeizadeh2018_sv2p_prov`.
   - Evidence: C001, C002, C004; `data/section_packets/04_video_prediction_packet.md`; completed notes P004-P006.
   - Status: supported as a section framing; medium confidence because broader video-prediction notes remain incomplete.

2. Action-conditioned prediction connects video prediction to interaction because predicted observations depend on candidate action sequences rather than only passive extrapolation.
   - Supporting papers: P004.
   - Citation keys: `oh2015_action_conditional_video_prediction_prov`.
   - Evidence: C001, C019; section packet; completed note P004.
   - Status: supported, narrow.

3. Robot video prediction extends visual dynamics to physical interaction by conditioning on robot actions and predicting pixel motion through DNA/CDNA/STP-style transformations.
   - Supporting papers: P005.
   - Citation keys: `finn2016_physical_interaction_video_prediction_prov`.
   - Evidence: C002; section packet; completed note P005.
   - Status: supported.

4. Deterministic pixel-level predictors have long-horizon and detail-preservation limits in the completed action-conditioned and robot-prediction evidence.
   - Supporting papers: P004, P005.
   - Citation keys: `oh2015_action_conditional_video_prediction_prov`, `finn2016_physical_interaction_video_prediction_prov`.
   - Evidence: P004 and P005 limitations in the section packet.
   - Status: supported but narrow.

5. Stochastic latent-variable video prediction addresses multi-modal futures by sampling multiple plausible rollouts, but it also requires careful training and latent design.
   - Supporting papers: P006.
   - Citation keys: `babaeizadeh2018_sv2p_prov`.
   - Evidence: C004, C005, C006; section packet; completed note P006.
   - Status: supported for SV2P; broader stochastic-video claims need more notes.

6. Pixel-level prediction and frame metrics do not by themselves establish world-model usefulness.
   - Supporting papers: P004, P005, P006, P009, P012.
   - Citation keys: `oh2015_action_conditional_video_prediction_prov`, `finn2016_physical_interaction_video_prediction_prov`, `babaeizadeh2018_sv2p_prov`, `janner2019_o2p2_prov`, `alonso2024_diamond_prov`.
   - Evidence: C003; section packet; claim evidence map.
   - Status: supported, with broader benchmark evidence still pending.

7. Later object-centric, latent, diffusion-based, and interactive world-model families can be organized as complementary responses to limitations of pixel-level prediction.
   - Supporting papers: P009, P001, P002, P012, P013.
   - Citation keys: `janner2019_o2p2_prov`, `hafner2019_planet_prov`, `hafner2020_dreamer_prov`, `alonso2024_diamond_prov`, `bruce2024_genie_prov`.
   - Evidence: taxonomy.md; C007, C011, C015, C019.
   - Status: medium confidence synthesis; should be revisited after later sections mature.

## 2. Supporting Papers

- P004 `oh2015_action_conditional_video_prediction_prov`: early deterministic action-conditioned prediction from high-dimensional Atari observations; supports action-conditioning and frame-metric limitation claims.
- P005 `finn2016_physical_interaction_video_prediction_prov`: robot video prediction with action conditioning and pixel-motion transformations; supports physical-interaction and motion-transform claims.
- P006 `babaeizadeh2018_sv2p_prov`: stochastic latent-variable video prediction; supports multi-modal future, staged training, and latent temporal-structure claims.
- P009 `janner2019_o2p2_prov`: used as a forward pointer for planning-oriented evaluation beyond frame metrics.
- P012 `alonso2024_diamond_prov`: used as a forward pointer for image-space world-model evaluation through control.
- P001, P002, P013: used only in the transition paragraph to connect video prediction to later latent and interactive world-model families.

## 3. Unsupported or Weak Claims

- Claims about recurrent spatiotemporal predictors, simplified video-prediction baselines, motion/content factorization, physics-informed prediction, masked-token prediction, learned-prior stochastic prediction, and diffusion-based video prediction remain `[NEEDS SOURCE]` because P020 and P023-P028 do not yet have evidence-ready notes.
- The transition claim that later structured, latent, diffusion, and interactive models respond to video-prediction limits is a survey-level synthesis. It is now phrased as an organizing interpretation rather than a directly proven historical claim.
- The section avoids broad claims about physical correctness of video predictors. Physical reliability is framed as a later evaluation problem rather than an established property of the models in this section.

## 4. Possible Missing References

- P024 `gupta2023_maskvit_prov`: needed for masked-token and planning-oriented video prediction.
- P027 `villegas2017_motion_content_prov`: needed for motion/content factorization.
- P025 `wang2019_e3dlstm_prov` and P026 `gao2022_simvp_prov`: needed for recurrent and simplified video-prediction baselines.
- P028 `denton2018_svg_lp_prov`: needed for stochastic video prediction beyond SV2P.
- P023 `leguen2020_phydnet_prov`: needed for physics-informed video prediction.
- P020 `voleti2022_mcvd_prov`: needed if diffusion-based video prediction should be discussed directly in this section rather than deferred.

## 5. Suggestions for Improvement

- Complete notes for P024 and P027 first because they address planning-oriented masked prediction and motion/content factorization.
- Add a compact comparison table after the notes are complete, with columns for conditioning signal, representation, dynamics mechanism, uncertainty treatment, evaluation, and world-model relevance.
- Revisit the final transition after Sections 05-07 are fully drafted to avoid overlap and tune citation density.
- Strengthen evaluation claims after benchmark notes are complete, especially the relationship among frame metrics, control utility, physical consistency, and long-horizon reliability.
