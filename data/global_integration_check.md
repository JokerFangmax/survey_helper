# Global Integration Check

Generated after reading `AGENTS.md`, `SURVEY_RULES.md`, `manuscript/main.tex`, all `manuscript/sections/*.tex`, `bib/references.bib`, `taxonomy.md`, `outline.md`, `data/claim_bank.md`, `data/claim_evidence_map.md`, and `data/papers.csv`.

## Overall Readiness

Sections 02--08 form a coherent body sequence: background/scope -> taxonomy -> video prediction -> object-centric dynamics -> latent control -> diffusion/interactive world models -> evaluation/open challenges. The conceptual arc is clear and mostly matches the taxonomy axes: representation, dynamics, conditioning/interaction, and evaluation.

The manuscript is not ready for introduction/conclusion drafting as a polished paper yet, but it is ready for a cautious evidence-aware introduction outline. The main blockers are unresolved evidence markers, scaffolded Introduction/Conclusion files, incomplete benchmark/diffusion/modern model notes, and missing planned figures/tables.

## Sequence and Transitions

- Section 02 to 03 is strong: Section 02 introduces the organizing axes, and Section 03 formalizes them.
- Section 03 to 04 is strong: the taxonomy explicitly prepares the video-prediction section.
- Section 04 to 05 is strong: the transition from pixel-level prediction limits to object/entity structure is explicit.
- Section 05 to 06 is strong: the transition from explicit physical decomposition to compact latent state is explicit.
- Section 06 to 07 is strong: the abstraction-fidelity trade-off motivates image-space diffusion and interaction.
- Section 07 to 08 is strong: diffusion/interactive limitations motivate multi-axis evaluation.
- The main sequence issue is structural rather than prose-level: `outline.md` still treats diffusion and interactive environments as separate outline sections, while the current manuscript combines them in Section 07 and uses Section 08 for evaluation/open challenges. This is workable, but the outline should be synchronized before introduction drafting.

## Terminology Consistency

Mostly consistent:

- `predictive world model`, `world model`, `visual dynamics`, `latent world model`, `object-centric`, `image-space diffusion`, `interactive generative environment`, `physical consistency`, and `controllability` are used coherently.
- The manuscript consistently distinguishes video generation quality from world-model validity.
- `latent action` is consistently treated as controllable but not necessarily semantically grounded.

Needs tightening before Introduction:

- `visual plausibility`, `visual realism`, `visual quality`, and `generative video quality` are used as near-synonyms. The introduction should define which one is used as the umbrella term.
- `physical correctness`, `physical consistency`, `physical commonsense`, and `physical-law validity` are related but not identical. The introduction or background should define the distinctions or explicitly say they are evaluation facets.
- `generative simulation` appears in the title/scope but is less explicitly defined in the body than `world model` and `video generation`.

## Unresolved Markers

Marker inventory in manuscript files:

- `[NEEDS SOURCE]`: 20 occurrences.
- `[VERIFY]`: 0 occurrences.
- `[TODO]`: 0 occurrences.
- `[NEEDS MORE EVIDENCE]`: 0 occurrences.
- Raw `TODO`: 7 occurrences.

Important marker locations:

- `manuscript/main.tex`: author/date/abstract TODOs.
- `manuscript/sections/01_introduction.tex`: still a scaffold with evidence gaps.
- `manuscript/sections/09_conclusion.tex`: still a scaffold.
- Section 04: missing notes for P020 and P023--P028.
- Section 05: missing notes for P017--P019 and P029--P031.
- Section 06: missing notes for P010, P014--P016, and P032.
- Section 07: missing evidence for P011, P020, P021, P022, P040, and physical-law claims about diffusion rollouts.
- Section 08: missing detailed benchmark evidence for P033--P036 and P038--P040.

The raw `TODO` count includes comment headings such as `% - Revision TODOs:` in completed section audits. These are not LaTeX blockers, but they will show up in marker searches.

## Citation-Key Check

All citation keys used in `manuscript/main.tex` and `manuscript/sections/*.tex` exist in `bib/references.bib`.

Unique manuscript citation keys used: 23.

No obvious citation-key typos or LaTeX citation syntax problems were found. No manuscript citation fixes were made.

## Claim-Evidence Alignment

Generally aligned with the claim bank:

- Sections 02--06 mostly stay within C001--C014, C019, C025, and C026.
- Section 07 mainly stays within C015--C021 and C026, with unsupported diffusion-lineage claims explicitly marked.
- Section 08 mainly stays within C003, C021--C026, with unsupported benchmark details explicitly marked.

Potential overclaim risks:

- Section 07 says video diffusion models improved generative video modeling, but detailed evidence for P011/P020 is not completed. The sentence is followed by `[NEEDS SOURCE]`, so it is acceptable as a marked weak claim but should not be used in the introduction without completing those notes.
- Section 07 states that denoising objectives may not guarantee causal structure, conservation-like behavior, object permanence, or counterfactual validity. This is plausible but currently marked `[NEEDS SOURCE]` and should remain out of high-level claims until benchmark notes are completed.
- Section 08 names FVD, PHYRE, CLEVRER, Physion, PhyGenBench, Physical Law Perspective, and Physics-IQ as indexed targets. The manuscript correctly avoids detailed claims about their mechanisms/results, but any introduction/conclusion claim about these benchmarks must wait for notes.
- Section 08's sim-to-real challenge is appropriately cautious, but broad claims about deployment reliability remain unsupported.

## Missing Pieces Before Introduction and Conclusion

Blocking:

- Introduction and conclusion are scaffolds, not prose.
- Abstract has a TODO in `manuscript/main.tex`.
- Evidence gaps remain for diffusion-video lineage, modern latent/interactive world models, and most evaluation benchmarks.
- Planned figures/tables from `outline.md` are not yet drafted in manuscript prose.

Non-blocking but important:

- The outline numbering and manuscript section organization differ after Section 07.
- Several sections contain in-file claim-evidence audits. Useful for drafting, but decide later whether they stay as comments or are removed before submission.
- Some claims cite indexed papers with metadata-only notes as coverage targets. This is acceptable because the prose marks them weak, but they should not become central claims in the Introduction.

## Validation Results

Ran:

```powershell
python scripts\validate_papers.py
python scripts\check_bibtex_keys.py
```

Results:

- `validate_papers.py`: passed and wrote `data/validation_report.md`.
- `check_bibtex_keys.py`: passed.
- CSV rows with BibTeX keys: 40.
- Unique CSV BibTeX keys: 40.
- BibTeX entries: 40.
- Missing BibTeX entries for CSV keys: none.
- Unused BibTeX entries: none.

## Recommended Next Steps Before Writing Introduction

1. Synchronize `outline.md` with the current manuscript structure, especially the combined diffusion/interactive Section 07 and evaluation/open-challenges Section 08.
2. Complete or explicitly defer notes for P011, P020--P022, P033--P036, and P038--P040.
3. Decide whether Introduction should be a cautious roadmap based only on completed evidence or wait for high-priority notes.
4. Define the core terms once: `world model`, `generative simulation`, `visual quality`, `physical consistency`, `physical commonsense`, and `controllability`.
5. Draft at least a minimal Figure 1/table plan or remove figure/table promises from the Introduction until assets exist.
6. Keep all broad claims in the Introduction traceable to C001, C003, C011, C015, C019, C021, C024, C025, and C026.
