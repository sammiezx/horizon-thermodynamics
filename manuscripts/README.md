# Manuscripts

One subfolder per paper. The `template/` folder is a clean REVTeX 4-2 skeleton
to copy when you start a new manuscript.

## Starting a new paper

```bash
cp -r template <short-name>
cd <short-name>
latexmk -pdf main.tex
```

`<short-name>` should be a few words, kebab-case, no year — e.g.
`islands-2d-toy-model`, `analog-bec-spectrum`.

## Build system

The template uses [`latexmk`](https://mg.readthedocs.io/latexmk.html). It runs
LaTeX + biber + LaTeX-again automatically:

```bash
latexmk -pdf main.tex      # build
latexmk -pvc -pdf main.tex # build + watch on every save
latexmk -c                 # clean aux files (keeps PDF)
latexmk -C                 # clean everything including PDF
```

## Bibliography

The template loads `../../references/library.bib` (the shared master library).
Cite with `\cite{Hawking1975}` — same cite keys as the master `.bib`.

If `biber` isn't installed: `brew install biber` (macOS) or via your TeX
distribution's package manager.
