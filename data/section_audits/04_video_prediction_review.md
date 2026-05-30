# Reviewer-Style Self-Review: `04_video_prediction.tex`

## Overall Assessment

The section is mostly concept-driven and substantially stronger than a paper-list narrative. It organizes the material around visual dynamics, action conditioning, physical interaction, stochastic futures, architectural coverage gaps, and the transition to structured/latent world models. It also appropriately avoids treating video prediction as equivalent to world modeling: the opening paragraph, the architectural-limits subsection, and the final transition all state that pixel-space prediction is a foundation rather than a sufficient endpoint.

The main weakness is evidence granularity. Several claims are defensible as survey-level synthesis, but the completed evidence base for this section is narrow: P004, P005, and P006 are the only evidence-ready video-prediction papers. The section should therefore make its synthesis more explicitly conditional on the completed notes, reduce a few broad historical claims, and avoid implying that later architecture families have already been reviewed in detail. Citation keys used in the section are valid in `bib/references.bib`, and most are relevant, but several citations in the final transition are forward pointers rather than direct support for claims about video prediction.

## 1. Paragraph-Level Review

### Opening Paragraph

- Role: Defines why video prediction belongs in the survey and distinguishes it from a complete world model.
- Strengths: Clear thesis; aligns with Section~3 taxonomy; explicitly avoids overclaiming by saying this alone does not make a model a full world model.
- Issues: The phrase "the state is usually an image or feature map" is plausible but not directly supported by a citation in this paragraph beyond P004. It is taxonomy-consistent, but a skeptical reviewer may ask whether this is a general historical claim.
- Revision instruction: Keep the paragraph, but slightly narrow the generalization: "In the evidence-ready papers reviewed here..." or "In this branch..." before describing image or feature-map states.

### From Future-Frame Prediction to Visual Dynamics, Paragraph 1

- Role: Distinguishes predictive visual dynamics from generic video synthesis.
- Strengths: This is concept-driven and directly addresses the survey boundary. It also prepares the reader for object-centric, latent, and diffusion sections.
- Issues: "Generic video generation may be judged by plausibility or appearance" is a broad claim and is not directly supported by the video-prediction packet. It is consistent with the taxonomy and evaluation framing, but it would be stronger with a later evaluation citation such as P037 or with softer wording.
- Revision instruction: Either cite VideoPhy when contrasting visual plausibility with world-model correctness, or soften to "can often be judged..." and frame it as a survey distinction rather than a historical fact.

### From Future-Frame Prediction to Visual Dynamics, Paragraph 2

- Role: Explains deterministic prediction limits.
- Strengths: The paragraph clearly motivates stochastic prediction and avoids saying deterministic methods are useless.
- Issues: "When hidden variables, contact outcomes, or uncertain human or object motion matter" is conceptually right but broader than the cited P004/P005 evidence. The strongest citation for averaging over plausible futures is P006, not P004/P005.
- Revision instruction: Add P006 to the citation or split the claim: use P006 for multimodality/averaging, and P004/P005 for long-horizon and small-detail limitations.

### Action-Conditioned Prediction and Physical Interaction, Paragraph 1

- Role: Explains action conditioning as the bridge to control.
- Strengths: Very clear, concept-driven, and well supported by P004/C001/C003. The passive-versus-intervention contrast is useful.
- Issues: "specified intervention" is conceptually stronger than simple action conditioning; acceptable, but should not imply causal counterfactual validity beyond the model's action-conditioned rollout.
- Revision instruction: Consider "specified action sequence" or "candidate action" when describing P004, reserving "intervention" for broader taxonomy language.

### Action-Conditioned Prediction and Physical Interaction, Paragraph 2

- Role: Introduces robot video prediction and pixel-motion transformations.
- Strengths: Strongest paragraph in the section. It explains design motivation, technical mechanism, and limitation without becoming paper-list-driven.
- Issues: "This motion-transform bias is well aligned with manipulation settings because many local appearances persist while object positions change" is reasonable but not explicitly in the claim bank. It follows from P005's pixel-motion setup, but it is an inference.
- Revision instruction: Mark the sentence as an interpretive synthesis or soften: "This design is intended to exploit the persistence of local appearance..." if supported by P005 notes; otherwise keep it as cautious survey interpretation.

### Stochastic Futures and Long-Horizon Uncertainty, Paragraph 1

- Role: Motivates stochastic latent-variable video prediction.
- Strengths: Clear and evidence-supported by P006/C004. It explains why stochasticity matters for world modeling rather than only visual quality.
- Issues: "different action outcomes, contact events, or downstream decisions" extends beyond P006's direct evidence. P006 supports multiple plausible futures, but not necessarily downstream decision consequences.
- Revision instruction: Keep the conceptual point but weaken to "may correspond to" or "can matter for" action outcomes and decisions.

### Stochastic Futures and Long-Horizon Uncertainty, Paragraph 2

- Role: Discusses optimization and latent temporal structure.
- Strengths: Well aligned with C005 and C006. The paragraph correctly states that the evidence is one-paper evidence and should not be generalized as a law.
- Issues: No major support issue. The final sentence about "meaningful uncertainty" versus "sampling visually different frames" is a good evaluation point but not directly supported by a specific citation.
- Revision instruction: Keep the sentence, but consider moving it to the evaluation/limits paragraph or flag it as an open evaluation issue if evidence remains narrow.

### Architectural Progress and Remaining Limits, Paragraph 1

- Role: Acknowledges architecture-oriented video-prediction categories without unsupported claims.
- Strengths: It correctly marks recurrent baselines, simplified baselines, motion/content factorization, physics-informed prediction, masked-token prediction, and diffusion-video prediction as not evidence-ready.
- Issues: The sentence "The current paper index includes..." is supported by the packet and metadata, but there is no manuscript citation because metadata files are not cited. This is acceptable for an internal draft, but it may read awkwardly in a final manuscript because it refers to the project index rather than the literature.
- Revision instruction: In the next revision, either convert this paragraph into a short "coverage gap" note outside manuscript prose, or mention these categories with explicit `[NEEDS SOURCE]` markers tied to the relevant BibTeX keys only after notes are completed.

### Architectural Progress and Remaining Limits, Paragraph 2

- Role: Synthesizes limits of pixel-level prediction and frame metrics.
- Strengths: Strong conceptual paragraph; it connects limitations to evaluation beyond frame fidelity and uses P009/P012 only as forward pointers.
- Issues: "supports counterfactual actions" and "physically coherent over long rollouts" are broader than the current evidence. C003 supports frame metrics versus control/planning utility, while C021/C024 support broader physical-consistency evaluation but are not cited here.
- Revision instruction: Either cite P037/P012 if making physical-correctness claims, or narrow the sentence to "control-relevant details and long-horizon rollout behavior" for this section.

### Transition Toward Structured and Latent World Models

- Role: Bridges Section 04 to later object-centric, latent, diffusion, and interactive sections.
- Strengths: Natural transition; clearly states that video prediction is a foundation and warning, not the final world-model form.
- Issues: The list of later families is citation-heavy and risks becoming a compressed survey of future sections. "Responses to these limitations" is a synthesis, not directly established by each cited paper.
- Revision instruction: Keep the transition but reduce citation load or make it more explicit that this is the survey's organizing interpretation. For example, use fewer representative citations or say "The next sections examine responses along these axes..."

### Commented Claim-Evidence Audit

- Role: Documents major claims and evidence.
- Strengths: Useful and mostly accurate. It correctly flags medium-confidence claims and missing notes.
- Issues: The audit says deterministic pixel prediction struggles with multimodal futures and cites C004; C004 is P006-based and specifically about stochastic latents, not direct evidence from P004/P005. The audit is acceptable but should separate "deterministic blur under uncertainty" from "P004/P005 long-horizon/details limitations."
- Revision instruction: Split the deterministic-limit audit item into two entries: one for deterministic video-prediction limitations from P004/P005 and one for multimodal-future motivation from P006.

## 2. Section-Level Weaknesses

1. The section is concept-driven, but it currently has a weak "architecture-oriented" subsection because many requested categories are metadata-only. It handles this honestly, yet the manuscript prose may feel like an internal note rather than a polished survey paragraph.

2. The section explains why video prediction is relevant to world modeling, but it could be more explicit about the minimal boundary condition: video prediction becomes world-model-relevant when the rollout is conditioned, useful for interventions, connected to planning/control, or evaluated beyond visual reconstruction.

3. Deterministic, action-conditioned, robotic, and stochastic prediction are coherent. However, "architecture-oriented video prediction" remains underdeveloped because P020 and P023-P028 are not evidence-ready.

4. The transition to object-centric and latent world models is natural, but the final paragraph compresses too many future branches at once. This risks reducing the punch of the section's own conclusion.

5. The section repeats some background/taxonomy ideas from Sections 02 and 03. This is not fatal, but revision should make Section 04 more technical and less definitional.

## 3. Claim-Evidence Problems

1. Claim: "Generic video generation may be judged by plausibility or appearance."
   - Problem: Broad evaluation claim not directly supported by P004-P006.
   - Suggested support: P037 (`bansal2025_videophy_prov`) if contrasting visual plausibility with physical correctness, or rewrite as a survey framing without citation.

2. Claim: Deterministic predictors average over hidden variables, contact outcomes, or uncertain human/object motion.
   - Problem: P006 supports deterministic averaging under uncertainty; P004/P005 support deterministic/long-horizon limitations. Contact outcomes and human/object motion are broader than current citations.
   - Suggested support: Add P006 citation and soften the examples.

3. Claim: Motion-transform bias is well aligned with manipulation because local appearance persists while object positions change.
   - Problem: This is a reasonable interpretation of P005, but not explicitly listed in C002.
   - Suggested support: Keep as interpretation with cautious language, or verify in P005 note before leaving as a technical claim.

4. Claim: Different stochastic futures can imply different action outcomes, contact events, or downstream decisions.
   - Problem: P006 supports plausible futures but not direct decision consequences.
   - Suggested support: Soften to "may matter for"; later planning/control sections can support downstream consequences with P009/P001/P002.

5. Claim: Pixel losses do not test physical coherence over long rollouts.
   - Problem: This is plausible and aligned with survey goals, but Section 04 citations mainly support control utility and long-horizon degradation, not physical coherence broadly.
   - Suggested support: Cite P037 only if discussing physical correctness, or defer the physical-coherence claim to the evaluation section.

6. Claim: Later object-centric, latent, diffusion, and interactive models are responses to video-prediction limitations.
   - Problem: This is a high-level synthesis rather than directly evidenced by all cited papers.
   - Suggested support: Rephrase as "can be organized as responses" or "the survey next considers complementary responses."

## 4. Overclaiming Problems

1. "Video prediction provides an early formulation of predictive visual world modeling" is acceptable because it is immediately qualified, but it should remain "an early formulation" rather than "the origin" or "the foundation."

2. "The main limitation of deterministic frame prediction..." is slightly too singular. Deterministic prediction has multiple limitations, and the evidence base is narrow.

3. "Stochastic video prediction addresses the fact that future visual observations are often multi-modal" is supported by P006 but should be framed as "addresses one important limitation" rather than implying stochastic latents solve uncertainty.

4. "Later video-prediction architectures broaden the design space..." is true from metadata but not yet evidence-backed in notes. Keep as a coverage-gap statement or remove from polished manuscript until notes are complete.

5. "Physically faithful simulator" in the final transition is an appropriate survey goal, but the section itself does not establish physical faithfulness evidence. Keep it as a limitation/goal, not a property of any video predictor.

## 5. Missing Citation Suggestions

These should not be added as claim support until notes are complete, but they are the right missing-paper targets:

- P024 `gupta2023_maskvit_prov`: needed for masked-token and planning-oriented video prediction.
- P027 `villegas2017_motion_content_prov`: needed for motion/content factorization.
- P025 `wang2019_e3dlstm_prov`: needed for recurrent spatiotemporal video-prediction baselines.
- P026 `gao2022_simvp_prov`: needed for simplified video-prediction baselines.
- P028 `denton2018_svg_lp_prov`: needed for stochastic prediction beyond SV2P.
- P023 `leguen2020_phydnet_prov`: needed for physics-informed video prediction.
- P020 `voleti2022_mcvd_prov`: needed for diffusion-based video prediction if this section keeps a diffusion-video bridge.
- P037 `bansal2025_videophy_prov`: optional citation if the section contrasts visual plausibility with physical correctness, but this may be better saved for the evaluation section.

Citation validity check: all citation keys currently used in `04_video_prediction.tex` exist in `bib/references.bib`. The current keys are relevant, but P007/P008/P009/P001/P002/P012/P013 are mostly forward-transition citations rather than core evidence for video prediction.

## 6. Specific Revision Instructions

1. Keep the section structure, but rename or refocus "Architectural Progress and Remaining Limits" so it reads less like an internal evidence-gap note. Possible direction: "Coverage Gaps in Current Evidence" for draft mode, or remove the category list from final prose until notes are complete.

2. Add P006 support to the deterministic/multimodal limitation paragraph, or split the paragraph into deterministic rollout limitations from P004/P005 and multimodal-future motivation from P006.

3. Soften broad examples such as "contact outcomes," "downstream decisions," "counterfactual actions," and "physically coherent over long rollouts" unless additional citations are added.

4. Make the evidence boundary explicit once near the architecture paragraph: "Because the completed notes currently cover only P004-P006 for this section..." This will explain why several categories are deferred.

5. Reduce the final paragraph's citation load by citing representative families or by moving detailed citations into later sections. The transition should point forward, not summarize all future branches.

6. Split the commented audit item on deterministic pixel prediction into two claims: one for long-horizon/small-detail/pixel-space limitations from P004/P005, and one for multimodal-future motivation from P006.

7. Consider adding one concise comparison table after completing missing notes. The table should compare conditioning signal, representation, dynamics mechanism, uncertainty treatment, evaluation, and world-model relevance.

8. Do not add citations for P020 or P023-P028 as technical support until their notes are completed. If they remain mentioned before note completion, keep `[NEEDS SOURCE]` in place.
