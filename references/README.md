# References

`library.bib` is the **single master bibliography** for this workspace. Every
manuscript pulls from it (the REVTeX template is wired up that way).

## Cite-key convention

`LastnameYear` for single-author, `LastnameLastnameYear` for two authors,
`AcronymYear` (e.g. `AMPS2013`) for >2 authors when it's the well-known label.
Append `a`/`b`/... to disambiguate same-year papers by the same author
(see `Page1993a`, `Page1993b`).

## Adding a paper

1. Add an entry to `library.bib`, sorted alphabetically by cite key.
2. Save the PDF to `../papers/<topic>/<CiteKey>.pdf` (filename matches cite key).
3. Create `../notes/per_paper/<CiteKey>.md` from `_template.md`.

## Fetching BibTeX from arXiv / INSPIRE

INSPIRE-HEP gives you well-formatted BibTeX directly — search the paper, click
the "cite" link, copy the BibTeX. Prefer INSPIRE over arXiv's auto-generated
BibTeX because it has DOIs and journal info.
