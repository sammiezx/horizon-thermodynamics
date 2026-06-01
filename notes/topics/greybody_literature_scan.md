# Literature scan — greybody factors in non-Schwarzschild spacetimes

**Purpose.** Inform the spacetime choice for the centerpiece paper
([manuscripts/greybody-factors/](../../manuscripts/greybody-factors/)). All
papers below have been verified against their arXiv abstracts. BibTeX entries
are in [`references/library.bib`](../../references/library.bib).

This scan is a starting point, not a comprehensive bibliography. Treat the
"gap" notes as hypotheses to test, not as conclusions.

## Reviews — read for landscape + methods

### 1. Konoplya & Zhidenko 2011 (Rev. Mod. Phys.) — [[KonoplyaZhidenko2011]]

*"Quasinormal modes of black holes: from astrophysics to string theory"*,
arXiv: 1102.4014.

Strictly a QNM review, **but** the methods chapters (Frobenius / Leaver
continued fractions, WKB, time-domain integration, shooting) translate
one-to-one to greybody-factor numerics — same wave equation, different
boundary conditions. This is the methodological reference for the
centerpiece paper. **Priority: high.**

### 2. Kanti 2004 (IJMPA) — [[Kanti2004]]

*"Black holes in theories with large extra dimensions: a review"*,
arXiv: hep-ph/0402168.

Canonical review of greybody factors in higher-dimensional / brane-world
black holes. Sets the analytical framework (low/high-frequency expansions,
matching, transmission coefficient) that downstream numerical work uses.
Scope is brane-world-focused, so the *physics motivation* is dated — but the
*calculational machinery* is exactly what the centerpiece paper needs.
**Priority: medium — read selectively for the greybody-factor sections, skip
the brane-world phenomenology.**

## Recent technical papers — read for scope + method + literature gap

### 3. Rincón & Santos 2020 (EPJ C) — [[RinconSantos2020]] — *regular BHs*

*"Greybody factor and quasinormal modes of regular black holes"*,
arXiv: 2009.04386.

Greybody factors + QNMs for a family of regular BHs that generalizes
Bardeen and Hayward. Semi-analytic WKB + time-domain.
**Direct precursor** to a centerpiece paper in the regular-BH direction.
Read this carefully before picking Bardeen/Hayward — you need to know
exactly what they did and what they did not do.

### 4. Konoplya & Zinhailo 2020 (Phys. Lett. B) — [[KonoplyaZinhailo2020]] — *EGB*

*"Grey-body factors and Hawking radiation of black holes in 4D Einstein–Gauss–Bonnet gravity"*,
arXiv: 2004.02248.

Greybody factors for Dirac, EM, and gravitational fields in 4D EGB.
Note: the Konoplya group is *prolific* in this niche. Read this to
calibrate what the EGB-direction looks like, but **be honest about the
competition** before choosing EGB as the centerpiece spacetime.

### 5. Wu, Cai, Xie 2024 (PRD, in press) — [[WuCaiXie2024]] — *frontier: stability*

*"The stability of the greybody factor of Hayward black hole"*,
arXiv: 2411.07734.

Probes how $\Gamma_\omega$ for a Hayward BH responds to small bumps in the
effective potential — the greybody analog of the recently-discovered QNM-spectrum
instability. Uses a hyperboloidal framework. **This is a frontier direction**:
greybody-factor stability is opening up *right now*, and an MSc-track first
paper that engages with it (even just by computing the standard $\Gamma_\omega$
for a spacetime where stability has not been tested) is well-positioned.

### 6. Konoplya & Pappas 2025 (JCAP) — [[KonoplyaPappas2025]] — *dirty BHs*

*"Dirty black holes, clean signals: near-horizon vs. environmental effects on
grey-body factors and Hawking radiation"*, arXiv: 2507.01954.

Greybody factors for spherically symmetric BHs with localized deformations
(near-horizon vs. far-zone) that preserve the Hawking temperature.
**This paper was submitted ~10 months ago and is on the frontier.** The
"dirty BH" niche — BHs surrounded by matter halos, dark matter profiles,
quintessence, etc. — is the most open of the candidate families.

## Literature-gap hypotheses

These are starting hypotheses to **test against arXiv listings** before
committing. Spend half a day on `arxiv.org/list/gr-qc/new` archive searches
for each candidate before locking in.

| Family | Saturation | Best entry papers | First-paper hypothesis |
|---|---|---|---|
| **Regular BHs (Bardeen/Hayward)** | *Partially saturated for scalar / vacuum greybody* via [[RinconSantos2020]] and follow-ups. **Open**: massive scalars, fermions, gravitational perturbations, *and the stability angle just opened by* [[WuCaiXie2024]]. | RinconSantos2020, WuCaiXie2024 | Compute $\Gamma_\omega$ for a regular BH with a perturbation type or stability angle not covered by Rincón–Santos / Wu et al. |
| **Einstein–Gauss–Bonnet** | *Heavily occupied by the Konoplya group* ([[KonoplyaZinhailo2020]] and follow-ups). | KonoplyaZinhailo2020 | **Avoid for a first paper unless you find a clear gap.** Competing directly with a group that publishes 5+ papers/yr in this niche is a bad bet for someone outside the field. |
| **Dirty BHs** | *Wide open.* [[KonoplyaPappas2025]] is fresh; there are likely 12+ months of follow-up directions before saturation. | KonoplyaPappas2025 | Pick a specific astrophysically-motivated matter profile (DM halo, quintessence, accretion disk) and compute $\Gamma_\omega$ for it. Pedagogically rich and writes its own motivation. |
| **RN–de Sitter (non-trivial regimes)** | *Well-trodden* in standard parameter regimes. Open in extremal / near-extremal limits. | (search needed) | Lower priority for a first paper — the two-horizon scattering is technically harder. |

## Recommendation for the spacetime decision

Two finalists:

1. **A regular BH (Bardeen or Hayward) with a perturbation type / stability angle not yet covered.** Safest choice — the literature scaffolding ([[RinconSantos2020]], [[WuCaiXie2024]]) is generous. Decision after reading those two.
2. **A dirty BH with a specific matter profile.** Higher payoff — the niche is fresh, and the physics motivation writes itself. Decision after reading [[KonoplyaPappas2025]] and identifying one matter profile not covered there.

**The choice should be made after reading [[Hawking1975]] + [[Page1976]] +
the four papers tagged "Priority: high/frontier" in this scan.** Not before.
