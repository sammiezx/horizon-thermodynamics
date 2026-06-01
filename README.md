# Black Hole Radiation — Research Workspace

A long-lived workspace for studying black hole radiation and producing research papers.
Scope is intentionally broad, spanning four areas that map to the `papers/` subfolders:

- **Hawking radiation theory** → `papers/hawking_radiation/`
- **The information paradox** → `papers/information_paradox/`
- **Numerical work** → `papers/numerical/`
- **Analog-gravity experiments** → `papers/analog_gravity/`

(Plus `papers/foundations/` for GR / QFT-in-curved-spacetime references.)

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
black_hole_radiation/
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

This workspace is a git repo on `main`. Commit early — especially the bibliography,
notes, and manuscripts. Build artifacts and editor caches are gitignored; see
`.gitignore` for specifics.

## Standards & conventions

- **Bibliography:** one master `references/library.bib`; cite keys are
  `LastnameYear` (e.g., `Hawking1975`, `PenningtonShenkerStanford2019`).
- **Notes:** Markdown, one paper per file, cite key as filename.
- **Python:** Python ≥ 3.11, type hints, `ruff` + `pytest`, `uv` for env mgmt.
- **LaTeX:** REVTeX 4-2, biblatex/biber, `latexmk` for builds.

See per-folder `README.md` files for details.
