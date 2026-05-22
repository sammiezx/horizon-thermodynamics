# Black Hole Radiation — Research Workspace

A long-lived workspace for studying black hole radiation and producing research papers.
Scope is intentionally broad: Hawking radiation theory, the information paradox,
numerical work, and analog-gravity experiments.

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

## Standards & conventions

- **Bibliography:** one master `references/library.bib`; cite keys are
  `LastnameYear` (e.g., `Hawking1975`, `PenningtonShenkerStanford2019`).
- **Notes:** Markdown, one paper per file, cite key as filename.
- **Python:** Python ≥ 3.11, type hints, `ruff` + `pytest`, `uv` for env mgmt.
- **LaTeX:** REVTeX 4-2, biblatex/biber, `latexmk` for builds.

See per-folder `README.md` files for details.
