# Horizon Thermodynamics — Research Workspace

A long-lived workspace for studying black-hole thermodynamics and the physics of
horizons — from Hawking radiation and the information paradox to the
thermodynamic origin of gravity — and for producing research papers from that
study.

The unifying thread is **horizons as thermodynamic objects**: Hawking
temperature, horizon entropy, the generalized second law, and the line of work
(Jacobson 1995 onward) that treats the Einstein equation itself as an equation
of state.

## Two halves of the repo

- **`learning/` — self-built graduate courses (HTML).** No-steps-skipped
  lectures pitched at qualifying-exam level, with derivations, worked examples,
  and difficulty-tagged exercises. Open [learning/index.html](learning/index.html)
  as the hub. Current contents:
  - [hawking-1975-deep.html](learning/hawking-1975-deep.html) — equation-by-equation
    walkthrough of Hawking 1975, *Particle Creation by Black Holes*
  - [jacobson-1995-course.html](learning/jacobson-1995-course.html) /
    [jacobson-1995.html](learning/jacobson-1995.html) — thermodynamics of spacetime
  - [string-theory-course.html](learning/string-theory-course.html)
  - [research-craft-course.html](learning/research-craft-course.html) &
    [paper-worthiness-and-AI.html](learning/paper-worthiness-and-AI.html) — how to
    write a paper, judge what's paper-worthy, and use AI honestly in physics research
- **`papers/` + `notes/` + `manuscripts/` — the research pipeline.** Read PDFs,
  take per-paper notes, synthesize topic notes, draft manuscripts. Mechanics below.

## Start here

First time in the repo? Do the **first-time setup** below, then:

1. Open [reading_list.md](reading_list.md) and pick the top item.
2. Drop its PDF in the relevant `papers/<topic>/` folder as `<CiteKey>.pdf`.
3. Copy [notes/per_paper/_template.md](notes/per_paper/_template.md) to
   `notes/per_paper/<CiteKey>.md` and fill it in as you read.
4. Log the day in `notes/journal/YYYY-MM-DD.md`.

That's the loop. Everything below explains the mechanics.

## First-time setup

Three prerequisites before any build command works:

```bash
# uv — Python package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# TeX distribution with REVTeX 4-2 + biber (macOS; ~5 GB, includes biber)
brew install --cask mactex

# Sanity-check both toolchains
cd code && uv sync && uv run pytest
cd ../manuscripts/template && latexmk -pdf main.tex
```

A green test suite and a built `main.pdf` mean you're set.

## Layout

```
horizon-thermodynamics/
├── learning/          # Self-built graduate courses (HTML), open index.html
├── papers/            # PDFs of papers, organized by topic
├── notes/             # Markdown notes
│   ├── per_paper/     #   one file per paper, keyed by BibTeX cite key
│   ├── topics/        #   synthesis notes across many papers
│   └── journal/       #   dated research-journal entries (lab notebook)
├── references/        # Master BibTeX library
├── manuscripts/       # Paper drafts (one folder per paper) + REVTeX template
├── code/              # Python numerics (uv-managed) + Jupyter notebooks
├── talks/             # Beamer presentations
└── reading_list.md    # Prioritized backlog of what to read next
```

`papers/` topics: `foundations/` (GR / QFT-in-curved-spacetime),
`hawking_radiation/`, `information_paradox/`, `bh_successors/` (Page curve,
firewalls, ER=EPR, replica wormholes, …), `analog_gravity/`, `numerical/`,
`string_theory/`, plus `exemplars/` and `research_craft/` for model papers and
craft references.

## Why this shape

- **One master `references/library.bib`.** Every manuscript and every per-paper
  note cites from it. Cite keys are filenames everywhere else (PDFs, notes), so
  cross-references stay stable as the bib grows.
- **Durable vs. exploratory, separated on purpose.** `notes/topics/` and
  `code/src/bh_radiation/` are where understanding accumulates. `notes/journal/`
  and `code/notebooks/` are where you sketch — promote things out when they
  earn their keep.
- **Per-paper notes feed topic notes.** Once you have 3+ per-paper notes on the
  same idea (e.g., the Page curve), write a `notes/topics/page_curve.md` that
  synthesizes them. That topic note is where long-term value lives.

## Daily workflow

1. **Read** a paper. Drop the PDF into the relevant `papers/<topic>/` folder.
2. **Cite** it: add an entry to [references/library.bib](references/library.bib).
3. **Note** it: copy [notes/per_paper/_template.md](notes/per_paper/_template.md) to
   `notes/per_paper/<citekey>.md` and fill it in.
4. **Synthesize** when you see a pattern: add or extend a file in `notes/topics/`.
5. **Log** the day in `notes/journal/YYYY-MM-DD.md` — what you read, what you tried,
   what stuck.

## Writing a paper

```bash
cp -r manuscripts/template manuscripts/<short-name>
cd manuscripts/<short-name>
latexmk -pdf main.tex
```

The template uses REVTeX 4-2 with `biblatex` + `biber` and pulls citations from the
shared `references/library.bib`.

## Running numerics

```bash
cd code
uv sync                       # creates .venv from pyproject.toml
uv run jupyter lab            # for interactive work
uv run pytest                 # for the test suite
```

Library code lives under `src/bh_radiation/`. Exploratory notebooks live in `notebooks/`.

## Version control

This workspace is a git repo on `main`, pushed to
`github.com/sammiezx/horizon-thermodynamics`. Commit early — especially the
bibliography, notes, and manuscripts. Build artifacts and editor caches are
gitignored; see `.gitignore` for specifics.

## Standards & conventions

- **Bibliography:** one master `references/library.bib`; cite keys are
  `LastnameYear` (e.g., `Hawking1975`, `PenningtonShenkerStanford2019`).
- **Notes:** Markdown, one paper per file, cite key as filename.
- **Python:** Python ≥ 3.11, type hints, `ruff` + `pytest`, `uv` for env mgmt.
- **LaTeX:** REVTeX 4-2, biblatex/biber, `latexmk` for builds.

See per-folder `README.md` files for details.
