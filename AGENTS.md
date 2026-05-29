# AGENTS.md

## Project goal

This repository is for writing an English survey titled:

Learning Predictive World Models from Videos: A Survey on Generative Simulation and Physical Dynamics

The goal is to build a reproducible literature-review workspace, including paper metadata, reading notes, taxonomy, figures, BibTeX, and manuscript drafts.

## Core rules

- Do not fabricate papers, citations, venues, years, arXiv IDs, DOIs, or BibTeX entries.
- Do not infer unsupported claims from paper titles or abstracts alone.
- Every technical claim in manuscript drafts must be traceable to one or more entries in `data/papers.csv`, `bib/references.bib`, or `notes/`.
- If evidence is missing, mark the claim as `[NEEDS SOURCE]` instead of inventing a citation.
- Keep survey writing analytical, not just paper-by-paper listing.
- Prefer taxonomy-level synthesis: compare assumptions, inputs, outputs, supervision, dynamics modeling, physical consistency, interaction ability, benchmarks, and limitations.

## Writing style

- Use academic English.
- Avoid overclaiming.
- Prefer precise terms such as "suggests", "indicates", "is designed to", "aims to", and "empirically shows" when evidence is limited.
- Do not use marketing-style language.
- Preserve citation placeholders in LaTeX form, e.g. `\cite{}`.

## File discipline

- `data/papers.csv` is the single source of truth for paper metadata.
- `bib/references.bib` stores BibTeX entries.
- `notes/` stores per-paper reading notes.
- `taxonomy.md` stores the current classification system.
- `outline.md` stores the survey structure.
- `manuscript/` stores draft sections.

## Codex workflow

Before editing manuscript text:
1. Read `outline.md`.
2. Read `taxonomy.md`.
3. Read relevant rows from `data/papers.csv`.
4. Read relevant paper notes from `notes/`.
5. Use `$research-paper-writing` only for improving writing quality, paragraph logic, claim-evidence alignment, and reviewer-style self-check.

When asked to revise a section, output:
1. Revised text.
2. Claim-evidence map.
3. Unsupported claims.
4. Missing papers or missing notes.
5. Suggested next actions.