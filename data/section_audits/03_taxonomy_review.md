# Reviewer-Style Self-Review: `manuscript/sections/03_taxonomy.tex`

## Evidence Read

- Manuscript section reviewed: `manuscript/sections/03_taxonomy.tex`.
- Context files read: `taxonomy.md`, `outline.md`, `data/claim_bank.md`, `data/claim_evidence_map.md`, `data/papers.csv`, and `bib/references.bib`.
- Existing requested audit file `data/section_audits/03_taxonomy_audit.md` was not found. Only the background audits currently exist in `data/section_audits/`.
- Notes read/checked: P001-P009, P012, P013, and P037 contain usable evidence. P010-P011 and P014-P040 mostly exist as placeholder notes with `UNKNOWN` claims, except for metadata-level information in `data/papers.csv`; these should not yet support technical claims.

## Overall Assessment

The section is currently a planning scaffold rather than a review-ready taxonomy section. Its intended axes are concept-driven, and they match the survey goal better than a chronological paper list. However, the actual manuscript text does not yet explain the axes, justify why they are useful, compare branches, or prepare the reader for later sections. A skeptical reviewer would likely see it as a table-of-contents draft with citation anchors, not as a taxonomy that interprets the field.

## 1. Paragraph-Level Review

### Section Title

Current text: `A Concept-Driven Taxonomy`.

Review: The title is appropriate and signals the desired contribution. The problem is that the section body does not yet deliver a concept-driven taxonomy. It names axes and branches but does not define the concepts, explain the boundaries among branches, or show how a reader should use the taxonomy to understand predictive world models from video.

Revision need: Keep the title only if the rewritten section actually frames the taxonomy as an analytic tool. Otherwise, reviewers may read the title as overpromising.

### Section Thesis

Current text: "A useful taxonomy should classify methods by modeling goal, representation type, dynamics model, conditioning signal, and evaluation protocol."

Review: This is the strongest sentence in the section because it foregrounds axes rather than papers. However, it remains too abstract. It does not define each axis, explain why these axes are the right ones for this survey, or distinguish them from alternative organization schemes such as chronology, architecture family, or benchmark family. The sentence also uses the evaluative word "useful" without explaining useful for what: comparing simulation fidelity, control utility, physical consistency, or generative realism.

Evidence status: The axis choice is supported indirectly by `taxonomy.md`, `outline.md`, and the claim bank, but it has no explicit citation because it is a survey design claim. This is acceptable if the next paragraph motivates the design from recurring differences in the cited literature.

Revision need: Expand this into an opening paragraph that says these axes expose three survey-specific distinctions: passive prediction versus intervention-conditioned simulation, image fidelity versus compact latent controllability, and visual realism versus physical correctness.

### Planned Subsections

Current text: a list of Branches A-G.

Review: The branch list is concept-oriented in intention, but it still reads as an outline rather than prose. Several branches overlap: Branch A and Branch F both involve action-conditioned or interactive prediction; Branch D and Branch F both involve control; Branch E and Branch F overlap for interactive diffusion models; Branch G is an evaluation axis rather than a model family branch. The current list does not tell the reader whether branches are mutually exclusive categories, recurrent design patterns, or later section headings.

Evidence status: Branches C, D, E, F, and G have some support in the current claim bank. Branch A and Branch B are underrepresented in the manuscript's key-claim list despite support from P004-P006. Branches involving P010-P011 and P014-P040 should remain provisional until notes contain actual claims, not just metadata.

Revision need: Recast the branches as non-exclusive "views" over methods rather than disjoint bins. Add one sentence per branch explaining its conceptual role and the later section it prepares.

### Key Claims

Current text: five claim bullets: C007, C011, C015, C018, and C021.

Review: The cited claims are mostly supported by the claim bank, but the list is paper-list-like because each bullet names a claim and supporting papers without synthesizing the taxonomy. It also omits key taxonomy claims needed for Branch A and Branch B: C001-C003 for action-conditioned prediction and C004-C006 for stochastic future modeling. The list also does not include C019, which is central for distinguishing world models from generic video generation because it links predictions to actions, policies, or latent controls.

Evidence status:

- C007 is supported by P007, P008, and P009.
- C011 is supported by P001, P002, and P003.
- C015 is supported by P012 but is narrow and DIAMOND-centered.
- C018 is supported by P013 but is narrow and Genie-centered.
- C021 is supported by P037 and P012, but the P037 evidence concerns text-to-video physical commonsense evaluation rather than an action-conditioned world model.

Revision need: Replace the claim list with synthesized paragraphs. Use claim IDs internally while drafting, but final prose should not read like a claim-bank export.

### Expected Figures and Tables

Current text: Table 3 and Figure 2 are named.

Review: The figure/table plan is useful but underspecified. The section should say what each visual will clarify. The table should compare branches across axes; the figure should show how axes intersect rather than repeat the branch list. There is also a numbering mismatch risk: `outline.md` expects taxonomy material as Section 2 with Table 1/Table 2, while this file is `03_taxonomy.tex` and currently lists Table 3/Figure 2.

Revision need: Specify that the table maps branch, modeling goal, representation, dynamics, conditioning, evaluation, and evidence-ready papers. Specify that the figure should show predictive world models as a subset of video models, separated by intervention, state abstraction, and evaluation purpose.

### Missing Evidence

Current text: two bullets say branches involving indexed papers without completed notes should remain provisional, and the evaluation branch needs completed notes for P033-P040.

Review: The caution is right, but the wording is now imprecise. P033-P040 note files exist, but most are placeholder notes with `UNKNOWN` fields. The manuscript should distinguish "note file exists" from "completed analytical note supports a claim." This paragraph is also internal project bookkeeping, not final survey prose. In a manuscript draft, it should either be a LaTeX comment/TODO or be converted into a transparent limitation statement about evidence coverage.

Revision need: Replace "completed notes" with "completed analytical notes with extracted reliable claims." Do not cite P033-P040 for technical claims until their notes contain evidence. Keep this as an audit/TODO item rather than reader-facing prose unless the final survey explicitly discusses evidence gaps.

## 2. Taxonomy-Level Weaknesses

1. The taxonomy is concept-driven in intent but not yet concept-driven in execution. It names conceptual axes, but the section does not yet explain how the axes reorganize the literature or what interpretive payoff they provide.

2. The axes are plausible but not yet clearly differentiated. "Modeling goal" and "evaluation protocol" can collapse into each other for control papers; "representation type" and "dynamics model" overlap for diffusion/noise-space methods; "conditioning signal" and "interaction ability" overlap for action-conditioned and latent-action methods.

3. The branch structure mixes model families, tasks, and evaluation. Branch G is an evaluation layer, not a model branch. Branch F is partly a conditioning regime, partly a task regime, and partly a model family. Branch E is architecture-centered, while Branch C is representation-centered.

4. The section does not yet explain why these axes are useful for this survey. The most important motivation should be that predictive world models from video differ along whether they support intervention, compact state abstraction, long-horizon rollout, physical reasoning, and downstream control.

5. The section does not clearly distinguish predictive world models from generic video generation. The distinction should be stated early: generic video generation may optimize visual plausibility or prompt adherence, while predictive world models must represent environment dynamics under actions, latent controls, or counterfactual conditions and should be evaluated by control utility or physical consistency when relevant.

6. The current manuscript underuses the richer taxonomy in `taxonomy.md`. The source taxonomy already contains axis definitions, branch roles, limitations, open questions, and a cross-cutting comparison table. The manuscript currently imports only a small outline from it.

7. The taxonomy does not yet prepare the reader for later body sections. The branch list matches the outline, but the text does not preview what each later section will argue or what question each branch answers.

## 3. Claim-Evidence Problems

| Location | Claim / Issue | Evidence Problem | Recommendation |
|---|---|---|---|
| Lines 3-4 | A useful taxonomy should classify methods by five axes. | This is a survey-design claim and does not need paper citation, but it needs explanation. | Add a motivation paragraph tying axes to recurring contrasts in P004-P013 and P037. |
| Lines 9-15 | Branches A-G are proposed. | Branches are not defined and overlap. | Add concise branch definitions and mark branches as non-exclusive analytical lenses. |
| Line 20 | Object-centric and relational representations encode entities and interactions. | Supported by P007-P009, but P007 is not video-based and P008 uses supervised state targets. | Keep citation, but qualify the branch as structured physical dynamics spanning state-based and visual models. |
| Line 21 | Latent world models use compact state dynamics for planning or policy learning. | Supported by P001-P003. | Keep citation; add contrast between online planning, latent imagination, and hallucinated policy training. |
| Line 22 | Conditional diffusion can model image-space environment dynamics. | Supported only by P012 as a narrow Atari-centered world-model example. | State as a narrow example, not as a mature general category. Do not cite P011/P020 until notes are completed. |
| Line 23 | Interactive generative environments can learn latent actions from unlabeled video. | Supported by P013 only. | Keep narrow wording and connect to C019: interaction depends on known actions, policies, or latent controls. |
| Line 24 | Visual realism should not be equated with physical correctness. | Supported by P037 and P012, but these support different parts of the claim. | Use P037 for physical commonsense failure in text-to-video generation and P012 for open questions about world-model correctness beyond Atari return. |
| Lines 35-36 | Evaluation branch needs completed notes for P033-P040. | P033-P040 notes exist but mostly lack extracted evidence. | Say "completed analytical notes" and do not use them as support until reliable claims are extracted. |

## 4. Missing Citation Suggestions

Use these only after the corresponding notes contain usable evidence. For now, many of these are candidate citations based on `data/papers.csv` metadata, not claim-ready support.

- Branch A, action-conditioned pixel and motion prediction: add C001-C003 with P004 `\cite{oh2015_action_conditional_video_prediction_prov}` and P005 `\cite{finn2016_physical_interaction_video_prediction_prov}`. Candidate expansion after notes: P023 `\cite{leguen2020_phydnet_prov}`, P024 `\cite{gupta2023_maskvit_prov}`, P025 `\cite{wang2019_e3dlstm_prov}`, P026 `\cite{gao2022_simvp_prov}`, P027 `\cite{villegas2017_motion_content_prov}`.

- Branch B, stochastic future modeling: add C004-C006 with P006 `\cite{babaeizadeh2018_sv2p_prov}`. Candidate expansion after notes: P028 `\cite{denton2018_svg_lp_prov}`.

- Branch C, object-centric and relational dynamics: keep P007-P009. Candidate expansion after notes: P017 `\cite{kipf2020_cswm_prov}`, P018 `\cite{wu2023_slotformer_prov}`, P019 `\cite{veerapaneni2019_op3_prov}`, P029 `\cite{fragkiadaki2016_billiards_prov}`, P030 `\cite{chang2016_compositional_object_physics_prov}`, P031 `\cite{minderer2019_object_structure_dynamics_prov}`.

- Branch D, latent world models for planning and control: keep P001-P003. Candidate expansion after notes: P010 `\cite{zhou2025_dino_wm_prov}`, P014 `\cite{micheli2023_iris_prov}`, P015 `\cite{hafner2021_dreamerv2_prov}`, P016 `\cite{wu2022_daydreamer_prov}`, P032 `\cite{wu2023_contextwm_prov}`.

- Branch E, image-space and diffusion-based world models: keep P012 for current support. Candidate expansion after notes: P011 `\cite{ho2022_video_diffusion_models_prov}` and P020 `\cite{voleti2022_mcvd_prov}` for video diffusion background; P022 `\cite{huang2026_vid2world_prov}` only if its note verifies the interactive-world-model claim.

- Branch F, interactive and embodied generative environments: keep P004, P005, and P013 for the action/latent-action distinction. Candidate expansion after notes: P016 `\cite{wu2022_daydreamer_prov}`, P021 `\cite{ren2025_videoworld_prov}`, P022 `\cite{huang2026_vid2world_prov}`, P024 `\cite{gupta2023_maskvit_prov}`.

- Branch G, evaluation and physical consistency: keep P037 and evaluation-relevant evidence from P004, P009, P012, and P013. Candidate expansion after notes: P033 `\cite{bakhtin2019_phyre_prov}`, P034 `\cite{yi2020_clevrer_prov}`, P035 `\cite{bear2021_physion_prov}`, P036 `\cite{unterthiner2018_fvd_prov}`, P038 `\cite{meng2025_phygenbench_prov}`, P039 `\cite{kang2025_physical_law_perspective_prov}`, P040 `\cite{motamed2025_physics_iq_prov}`.

## 5. Specific Revision Instructions

1. Replace the current scaffold with prose. Start with a paragraph that defines the purpose of the taxonomy: to separate predictive world models from generic video generators by intervention, representation, dynamics, and evaluation.

2. Define all five axes before listing branches. For each axis, give one sentence explaining what it captures and one example from evidence-ready papers.

3. State that branches are non-exclusive analytical lenses. This will avoid false boundaries when a paper belongs to multiple branches, such as P012 being both diffusion-based and interactive/control-oriented, or P009 being object-centric and planning-oriented.

4. Add a short "why these axes matter" paragraph. Emphasize that the axes expose trade-offs among pixel fidelity, compact latent abstraction, physical structure, controllability, and evaluation validity.

5. Add missing support for Branch A and Branch B using C001-C006. The current key claims skip the early video-prediction and stochastic-future foundations even though those branches are listed.

6. Add C019 near the definition of predictive world models. This claim is central because it explains that world-model relevance emerges when future predictions depend on actions, policies, or latent controls.

7. Tighten Branch E. Present diffusion world models as an emerging, currently narrow branch supported by P012. Do not make broad claims about video diffusion as world modeling until P011/P020/P022 notes are completed.

8. Tighten Branch G. Treat evaluation as a cross-cutting layer rather than a peer model family. It should explain what each branch fails to measure if judged only by frame metrics, FVD, return, or human preference.

9. Add a clear distinction from generic video generation. Suggested content: visual plausibility and prompt adherence are insufficient for world models unless the model also supports prediction under interventions, latent controllability, counterfactual reasoning, planning/control use, or physical-consistency evaluation.

10. Move internal evidence-gap bookkeeping out of final prose. Keep it as comments or audit notes unless the manuscript explicitly includes a limitation paragraph about coverage.

11. Update `data/claim_bank.md` and `data/claim_evidence_map.md` after completing notes for P010-P011 and P014-P040. The manuscript should not cite placeholder notes as technical support.

12. Before rewriting, decide whether the final structure should be "axis-first then branch table" or "branch-first with axes repeated in each branch." The first option is cleaner for a concept-driven taxonomy and better prepares the later body sections.

## Reviewer Risk Summary

- Major risk: The section currently reads like an outline, not a manuscript section.
- Major risk: The taxonomy axes are named but not justified, so the concept-driven contribution is not yet visible.
- Medium risk: Branch overlap could make the taxonomy seem redundant unless branches are explicitly non-exclusive.
- Medium risk: Several important categories are listed in project files but cannot yet be cited because notes contain `UNKNOWN` evidence fields.
- Medium risk: The section does not yet make the central boundary between predictive world models and generic video generation explicit enough.
