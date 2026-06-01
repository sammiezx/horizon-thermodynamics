# Manuscript — Greybody factors for [SPACETIME-TBD]

**Status:** scaffold. Spacetime, field content, and numerical method are not
yet locked in.

**Target venue:** arXiv (gr-qc) preprint first; submit to *Phys. Rev. D* or
*Class. Quantum Grav.* after the preprint has lived in the open for ~2 weeks.

**Why this paper exists.** It is the centerpiece of the MSc-scholarship
portfolio (see memory: `project-centerpiece-paper`, `feedback-paper-strategy`).
It must be **finishable solo on a ~6–9 month timeline** and must leave its
author with more theory machinery than they started with.

## The plan, end-to-end

1. **Read and absorb** (weeks 1–4)
   - [[Hawking1975]] — three-pass study with the reading guide at
     `notes/topics/hawking_1975_reading_guide.md`.
   - [[Jacobson2003]] — modern pedagogical companion, alongside Hawking.
   - [[Page1976]] — the *direct precursor* to this paper. Reproduces
     greybody-factor numerics for Schwarzschild.
   - One modern review of greybody factors in non-Schwarzschild spacetimes
     *(TBD — add to reading list once identified)*.

2. **Pick the spacetime** (week ~5). Criteria below.

3. **Reproduce Schwarzschild as a sanity benchmark** (weeks 6–8). The numerics
   pipeline must match Page 1976's Schwarzschild greybody factors to plotting
   accuracy before doing anything novel. This is non-negotiable.

4. **Run on the chosen spacetime** (weeks 9–16). Extract
   $\Gamma_{\omega\ell}(\omega)$ and the integrated emission spectrum.

5. **Write up** (weeks 16–24). `main.tex` is already scaffolded.

6. **Solicit feedback** before arXiv submission — at minimum one physicist
   who works in the area, even cold-email. Iterate.

7. **arXiv** preprint, then journal.

## Open research decisions

### 1. Which spacetime?

Literature-scan results live in
[`../../notes/topics/greybody_literature_scan.md`](../../notes/topics/greybody_literature_scan.md).
Two finalists emerged from that scan:

1. **A regular BH (Bardeen / Hayward)** with a perturbation type or stability
   angle not covered by Rincón–Santos 2020 ([[RinconSantos2020]]) or Wu–Cai–Xie 2024
   ([[WuCaiXie2024]]). Safer — generous scaffolding already exists.
2. **A dirty BH** (BH + a specific matter profile: dark matter halo,
   quintessence, accretion disk). Higher payoff — the niche is fresh after
   Konoplya–Pappas 2025 ([[KonoplyaPappas2025]]) and writes its own physics
   motivation.

**Other families considered and provisionally ruled out for a *first* paper:**
- Einstein–Gauss–Bonnet — the Konoplya group dominates ([[KonoplyaZinhailo2020]]).
  Competing directly is a bad bet from outside the field.
- RN–de Sitter in non-trivial regimes — two-horizon scattering raises the
  technical bar more than is wise for a first paper.

**Decision criteria** (apply *after* the reading phase):
- Tractable on a laptop with continued fractions or shooting.
- Real literature gap — confirmed against arXiv listings, not just the
  scan above. Don't reinvent.
- Pedagogical richness — the geometry should teach Sameer something
  about QFT in curved spacetime that pure Schwarzschild does not.
- One spacetime, not several. Scope discipline.

### 2. Field content

Default: massless minimally-coupled scalar. Add EM / Dirac / gravitational
perturbations only if scope clearly permits. (It probably won't — punt to a
sequel.)

### 3. Numerical method

Three candidates:

- **Direct shooting** — conceptually simplest, easy to debug, good first
  implementation.
- **Leaver-style continued fractions** — gold standard for high precision and
  for QNMs. Worth learning; reuse value is high.
- **WKB / higher-order WKB** — fast analytic-ish approximation, good for
  cross-checks.

**Recommendation:** ship the paper with continued fractions, cross-check with
shooting and WKB.

## Files

- `main.tex` — REVTeX 4-2 draft, scaffolded with the standard section
  structure and red `[TODO]` markers everywhere a decision is pending.
- `latexmkrc` — build configuration.
- `figures/` — figures go here; reference them from `main.tex` with relative
  paths.
- Numerics live in `../../code/`, *not* in this folder. Manuscripts and code
  are kept separate; figures are exported from `code/` into `figures/`.

## Scope discipline (read before adding scope)

Things that are **out of scope** for this paper and belong in a sequel:

- Additional spacetimes.
- Additional fields (EM, Dirac, gravitational perturbations).
- QNM spectrum of the same spacetime.
- Holographic / AdS/CFT interpretations.
- Back-reaction.
- Comparison to analog-gravity experiments.

Each of these is interesting. None of them belong in a first paper that needs
to ship in time for MSc application cycles.
