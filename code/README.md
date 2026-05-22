# Code

Python-based numerics for the workspace. Managed with [`uv`](https://docs.astral.sh/uv/),
the modern Python package manager (fast, replaces pip+virtualenv+pyenv).

## First-time setup

Install `uv` if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then from this `code/` directory:

```bash
uv sync           # creates .venv from pyproject.toml
```

That's it — `uv` reads `pyproject.toml`, resolves dependencies, and creates a
virtual environment at `.venv/`.

## Running things

```bash
uv run jupyter lab           # interactive notebooks
uv run pytest                # run the test suite
uv run python -c "import bh_radiation; print(bh_radiation.__version__)"
```

`uv run <cmd>` runs `<cmd>` inside the project's virtual env without needing to
activate it. If you prefer to activate:

```bash
source .venv/bin/activate
```

## Adding dependencies

```bash
uv add numpy scipy sympy matplotlib    # runtime deps
uv add --dev pytest ruff               # dev-only deps
```

`uv` will update `pyproject.toml` and `uv.lock` automatically.

## Layout

```
code/
├── pyproject.toml         # project metadata + dependencies
├── src/bh_radiation/      # library code (importable: `import bh_radiation`)
├── notebooks/             # exploratory Jupyter notebooks
└── tests/                 # pytest suite
```

**Notebooks are for exploration; the library is the durable form.** When code
in a notebook is worth keeping, move it into `src/bh_radiation/` and write a
test for it in `tests/`.
