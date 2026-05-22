# Notes

Plain Markdown. Three sub-systems, each with a clear job.

## `per_paper/`

One file per paper, named `<CiteKey>.md` to match the BibTeX key. Use
[per_paper/_template.md](per_paper/_template.md) as your starting point.

A good per-paper note answers:

1. **What problem** does the paper claim to solve?
2. **What's the key idea / mechanism**, in your own words?
3. **What's the main result?** (one equation or one sentence)
4. **What do I not understand yet?** (the most valuable section)
5. **How does this connect** to other papers I've read? (link with `[[CiteKey]]`)

## `topics/`

Synthesis notes that cut *across* papers. Examples:

- `topics/page_curve.md` — the full story of the Page curve, citing many papers
- `topics/greybody_factors.md` — what they are, how they're computed
- `topics/replica_wormholes.md` — the construction and why it works

Build these *after* you have ≥ 3 per-paper notes that touch the same idea. A topic
note is where understanding lives long-term.

## `journal/`

Dated research-journal entries, one file per working day:
`journal/YYYY-MM-DD.md`. Treat it as a lab notebook:

- What did I read / try / compute today?
- What worked? What didn't?
- What's the next concrete step?

Future-you will thank present-you for being specific. Vague journals are useless.
