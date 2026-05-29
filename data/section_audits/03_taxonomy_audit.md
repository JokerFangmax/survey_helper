# Revision Audit: `manuscript/sections/03_taxonomy.tex`

## Revision Summary

- Replaced the outline-style scaffold with manuscript prose.
- Kept the taxonomy concept-driven by organizing the section around modeling goal, representation, dynamics, conditioning/interaction, and evaluation.
- Added explicit transitions from taxonomy axes to non-exclusive conceptual families.
- Clarified the boundary between predictive world models and generic video generation.
- Preserved only citations supported by completed notes and the claim bank: P001-P009, P012, P013, and P037.
- Treated broader diffusion-video, benchmark, and modern latent-control coverage as provisional rather than citing placeholder notes.

## Review Requirements Addressed

1. Strengthen weak transitions: addressed by adding an opening motivation, axis-by-axis flow, and a final paragraph that maps the taxonomy to later body sections.
2. Remove or weaken unsupported claims: addressed by narrowing diffusion claims to DIAMOND, narrowing stochastic claims to P006, and qualifying object-centric evidence as mostly controlled/synthetic where appropriate.
3. Keep taxonomy concept-driven: addressed by using axes and conceptual families instead of paper-by-paper listing.
4. Preserve valid citations: all cited keys appear in `bib/references.bib` and are supported by `data/claim_bank.md` / `data/claim_evidence_map.md`.
5. Do not invent citations or paper claims: no new citation keys were introduced; placeholder-note papers are not cited in the revised manuscript.

## Claim-Evidence Map

| Revised claim | Evidence used | Status |
|---|---|---|
| Predictive world models should be distinguished from generic video generation by intervention, control, planning, or physical-evaluation use. | C001, C003, C011, C015, C019, C021; P004, P001-P003, P012, P013, P037 | Supported, but survey-design framing should remain cautious. |
| Action-conditioned video prediction bridges passive prediction and world modeling. | C001, C002, C019; P004, P005 | Supported. |
| Stochastic future modeling needs latent variables to represent multiple plausible futures. | C004-C006; P006 | Supported but narrow; broader stochastic-video coverage still needs completed notes. |
| Object-centric and relational representations model entities and interactions. | C007-C010; P007-P009 | Supported, with limitations from synthetic/controlled settings and supervision assumptions. |
| Latent world models use compact dynamics for planning, policy learning, or policy evolution. | C011-C014; P001-P003 | Supported. |
| Conditional diffusion can serve as an image-space environment model in the DIAMOND setting. | C015-C017; P012 | Supported but narrow; broader diffusion claims remain provisional. |
| Interactive environments can use known actions or learned latent actions. | C018-C020; P004, P005, P013 | Supported, with latent-action scope narrowed to Genie-style evidence. |
| Visual plausibility is not the same as physical correctness. | C021-C023; P037, with P012 for world-model evaluation concerns | Supported. |

## Remaining Evidence Gaps

- P010-P011 and P014-P040 note files mostly contain `UNKNOWN` evidence fields and should not yet support manuscript claims.
- Diffusion-video lineage beyond DIAMOND still needs completed analytical notes for P011, P020, and P022.
- Broader latent-control coverage still needs completed notes for P010, P014-P016, and P032.
- Object-centric expansion still needs completed notes for P017-P019 and P029-P031.
- Evaluation/benchmark coverage still needs completed notes for P033-P036 and P038-P040 before making stronger claims about physical-law benchmarks, FVD, PHYRE, CLEVRER, Physion, PhyGenBench, or Physics-IQ.

## Revision Risks

- The new section is more complete, but it may overlap with parts of `02_background.tex`, which already introduces several scope and axis ideas.
- The comparison table uses paper IDs rather than citations to avoid overloading the table; the supporting citations are provided in the surrounding prose.
- Some statements are survey-design claims rather than direct paper claims; they are phrased as organizing choices rather than empirical conclusions.
