# Reviewer-Style Self-Review: `02_background.tex`

Reviewed file: `manuscript/sections/02_background.tex`

Scope: reviewer-style self-review only. The manuscript section was not modified.

Evidence checked against:

- `data/claim_bank.md`
- `data/claim_evidence_map.md`
- `bib/references.bib`
- completed notes: P001, P002, P003, P004, P005, P006, P007, P008, P009, P012, P013, P037

## 1. Paragraph-Level Review

### Paragraph 1: Video Prediction as Predictive Modeling

- Message: clear. The paragraph defines video prediction and moves from passive prediction to action-conditioned and stochastic variants.
- Concept-driven: mostly yes. It uses P004, P005, and P006 as examples of concepts rather than as a chronological list.
- Evidence: citations are relevant and valid.
- Issue: the phrase "Video prediction studies how a model can infer future visual observations" is a definition-level statement and is acceptable, but not directly tied to one citation. This is fine if retained as a field definition.
- Revision instruction: keep the paragraph, but consider making the final sentence more cautious: "SV2P illustrates why..." rather than "Stochastic variational video prediction further shows why..." if you want to avoid making P006 stand in for the whole stochastic literature.

### Paragraph 2: World Models Beyond Future Frames

- Message: mostly clear, but the paragraph carries three messages: operational definition of world model, examples of latent world models, and evaluation beyond frame reconstruction.
- Concept-driven: yes, but it is dense.
- Evidence: P003, P001, and P002 support the latent-world-model examples. C011 supports the broader shift from pixel rollouts to latent state dynamics.
- Issue: "reasoning" and "evaluation" in the definition are broader than the currently cited evidence. Planning and policy learning are strongly supported; "reasoning" is supported only indirectly through object-centric/physical-dynamics work later, and "evaluation" is more about assessing models than what a world model itself supports.
- Revision instruction: split into two paragraphs or narrow the definition to "planning, policy learning, or controlled prediction" unless more citations are added.

### Paragraph 3: Useful Prediction and Physical Correctness

- Message: clear. The paragraph distinguishes utility, planning, visual realism, and physical correctness.
- Concept-driven: yes.
- Evidence: P004 supports control usefulness beyond pixel metrics; P009 supports planning utility of object-structured representation; P037 supports the gap between visual plausibility and physical commonsense. P012 is indirectly relevant but not cited in this paragraph except through the audit.
- Issue: "visually strong generative models are not automatically accurate simulators" is supported by P037, but it is broad. P037 evaluates text-to-video models, not all generative simulators.
- Revision instruction: revise to "text-to-video results indicate that visual plausibility should not be equated with accurate simulation" or add a qualifier such as "current evaluated generators."

### Paragraph 4: Representation Axis

- Message: clear. The paragraph explains representation as the first taxonomy axis.
- Concept-driven: yes.
- Evidence: citations are valid and relevant.
- Issue: "Diffusion-based world models" is supported only by P012 in the completed notes, making the branch narrow at this stage.
- Revision instruction: add a caution phrase such as "in the completed evidence so far" or "one recent example" when introducing diffusion-based world models, unless notes for P011/P020/P022 are completed.

### Paragraph 5: Dynamics Axis

- Message: clear. The paragraph explains dynamics as the second axis.
- Concept-driven: yes.
- Evidence: P005/P006 support pixel-space and stochastic dynamics; P001/P002 support recurrent latent dynamics; P007/P008 support relational dynamics.
- Issue: "Pixel-space predictors often use autoregressive convolutional, recurrent, or motion-transform mechanisms" is plausible and supported by P004/P005/P006, but "often" suggests broader survey coverage than the current completed notes provide.
- Revision instruction: change "often use" to "in the completed notes include" or add citations from future completed notes before retaining the broader phrasing.

### Paragraph 6: Conditioning and Interaction Axis

- Message: clear. The paragraph explains why conditioning distinguishes passive prediction from interactive world modeling.
- Concept-driven: yes.
- Evidence: P004/P005/P001/P002 support explicit actions; P013 supports latent actions.
- Issue: "interactive world model must account for interventions" is a useful taxonomy claim, but "must" may overstate if the section later includes passive generative simulators or benchmark-only models.
- Revision instruction: change "must account for interventions" to "is typically evaluated by how it accounts for interventions" or "requires some account of interventions when used for control."

### Paragraph 7: Evaluation Axis

- Message: clear but dense. It covers frame metrics, control utility, planning, learned-model RL, physical consistency, human evaluation, and automatic evaluation.
- Concept-driven: yes.
- Evidence: P004/P009/P012 support evaluation beyond frame metrics; P037 supports physical-consistency benchmarking.
- Issue: "A complete evaluation protocol for video world models should..." is normative and broader than current evidence. It is reasonable as survey guidance, but should be marked as the survey's proposed framework rather than a supported empirical claim.
- Revision instruction: revise to "For this survey, we therefore record which aspect..." or mark the broader evaluation prescription as `[NEEDS SOURCE]` until more benchmark notes are completed.

### Paragraph 8: Survey Scope and Conceptual Families

- Message: clear. It enumerates the six families required by the user.
- Concept-driven: mostly yes, but this is the closest paragraph to a compact citation list.
- Evidence: citations are valid and relevant.
- Issue: "historical bridge" for pixel-level video prediction is supported by P004/P005/P006 but would be stronger after P024-P028 notes are completed.
- Revision instruction: keep this paragraph because it prepares the taxonomy, but consider turning it into a short table later to avoid a long sequence of families and citations.

### Paragraph 9: Provisional Boundaries

- Message: clear. It explicitly marks evidence gaps.
- Concept-driven: yes.
- Evidence: consistent with the audit and claim bank.
- Issue: no major issue. This is helpful and reviewer-friendly.
- Revision instruction: keep it. Consider adding exact paper ranges in a footnote or comment only if desired.

## 2. Claim-Evidence Problems

1. Claim: "A world model is a learned predictive model that represents how an environment evolves and can support downstream reasoning, planning, policy learning, or evaluation."
   - Problem: planning and policy learning are well supported; "reasoning" and "evaluation" are broader than the cited latent-world-model examples.
   - Supporting evidence available: P001, P002, P003 support planning/policy learning; P007-P009 support structured physical reasoning more indirectly; P037 supports evaluation as a benchmark, not as a world-model capability.
   - Recommended fix: narrow to "planning, policy learning, controlled prediction, or simulator-style analysis" or add `[NEEDS SOURCE]` after "reasoning" until more notes are completed.

2. Claim: "Visually strong generative models are not automatically accurate simulators."
   - Problem: supported by P037 in spirit, but P037 is specifically about evaluated text-to-video models and physical commonsense prompts.
   - Supporting evidence available: C021, P037; P012 limitations also point to physical-correctness questions.
   - Recommended fix: weaken to "The VideoPhy evidence suggests that visual plausibility should not be equated with accurate physical simulation."

3. Claim: "Diffusion-based world models revisit image-space dynamics with conditional generative models."
   - Problem: currently rests mainly on P012. It is valid for DIAMOND but too broad for the family until P011/P020/P022 notes are complete.
   - Supporting evidence available: C015/C016/P012.
   - Recommended fix: change to "DIAMOND exemplifies a diffusion-based world model..." or add a qualifier.

4. Claim: "A complete evaluation protocol for video world models should report..."
   - Problem: this is a prescriptive survey framework, not a directly evidenced result.
   - Supporting evidence available: C003, C021-C024 support the need for broader evaluation, but not a final complete protocol.
   - Recommended fix: phrase as "This survey therefore tracks..." rather than "A complete protocol should..."

5. Claim: "Pixel-level video prediction provides the historical bridge from passive sequence modeling to action-conditioned prediction."
   - Problem: "historical bridge" is plausible from P004/P005/P006 but incomplete without notes for P024-P028 and possibly earlier/later baselines.
   - Supporting evidence available: C001/C002/C004.
   - Recommended fix: use "one historical bridge" or "a major bridge in the completed evidence."

## 3. Overclaiming Problems

- "World model" definition is slightly expansive. The section handles this partly with "In this survey," but "reasoning" and "evaluation" should be narrowed or marked.
- "Visually strong generative models" is too broad; use "evaluated text-to-video models" or "current video generators in VideoPhy."
- "Diffusion-based world models" should be framed as narrow evidence from P012 until notes for P011/P020/P022 are completed.
- "A complete evaluation protocol" sounds final. Since evaluation notes are incomplete, this should be revised to "the evaluation axes tracked by this survey."
- "Historical bridge" should be softened because the historical video-prediction branch is not fully covered by completed notes.

## 4. Missing Citation Suggestions

These are not citations to add immediately unless the corresponding notes are completed and checked:

- P011 (`ho2022_video_diffusion_models_prov`) and P020 (`voleti2022_mcvd_prov`) would strengthen the diffusion/video-generation background.
- P022 (`huang2026_vid2world_prov`) would strengthen the interactive diffusion boundary.
- P024-P028 would strengthen the video-prediction background, especially recurrent, masked-token, motion/content, and stochastic-video lines.
- P010, P014-P016, and P032 would broaden the latent-world-model paragraph beyond P001-P003.
- P017-P019 and P029-P031 would broaden object-centric physical dynamics beyond P007-P009.
- P033-P036 and P038-P040 would make the evaluation paragraph much stronger and reduce reliance on P037 alone.

## 5. Specific Revision Instructions

1. Split Paragraph 2 into two paragraphs:
   - one operational definition of "world model" with P001-P003;
   - one paragraph explaining why evaluation moves beyond future-frame prediction with P004/P009/P012.

2. Revise broad family-level claims to use cautious phrasing:
   - "DIAMOND exemplifies..." instead of "Diffusion-based world models..."
   - "VideoPhy suggests..." instead of "visually strong generative models are..."
   - "This survey tracks..." instead of "A complete evaluation protocol should..."

3. Add one sentence after the representation-axis paragraph explaining that some branches are currently narrow because the completed notes cover only representative papers.

4. Keep the section concept-driven by retaining the axes structure, but reduce list density in the final conceptual-family paragraph. A table may be better than a long sentence once the section is revised.

5. Keep the final provisional-boundaries paragraph. It is an important reviewer-facing safeguard.

6. Do not add currently missing paper citations until their notes are completed, even though the BibTeX keys exist.

## 6. Citation-Key Validity and Relevance

- All citation keys used in `02_background.tex` are present in `bib/references.bib`.
- Citation relevance is generally good.
- No fabricated citation keys were detected.
- No citation currently points to a paper outside `data/papers.csv`.

## 7. Does the Section Prepare Readers for the Taxonomy?

Yes. The section prepares the taxonomy by introducing the same axes used in `taxonomy.md`: representation, dynamics, conditioning/interaction, and evaluation. The main improvement would be to make the transition to the taxonomy section more explicit at the end, for example by saying that the next section formalizes these axes into branches and comparison tables.

## 8. Reviewer Verdict

Status: needs minor revision before being treated as a stable background section.

The section is concept-driven, mostly well supported, and appropriately cautious about incomplete evidence. The main risks are broad definitions and family-level claims that lean slightly beyond the completed-note set. These can be fixed by narrowing a few phrases, adding a clearer bridge to the taxonomy section, and postponing missing-paper citations until their notes are complete.
