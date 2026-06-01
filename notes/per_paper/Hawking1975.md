---
citekey: Hawking1975
title: Particle creation by black holes
authors: Hawking, S. W.
year: 1975
arxiv:
doi: 10.1007/BF02345020
topics: [hawking_radiation, foundations]
read_on:
status: skimmed
---

# Particle creation by black holes

> **Reading goal.** This is the foundational paper of the field. Aim to *understand the
> Bogoliubov-coefficient argument well enough to reproduce its spine on a whiteboard*,
> not just to recognize the conclusion. The TL;DR / key idea / derivation sections
> below are intentionally left for you to write in your own words — see the template's
> rule: "if you can't write this without re-opening the paper, you don't understand
> it yet." The scaffolding below points you at *what to extract*, not *what to think*.

## TL;DR

<!-- fill in after first full pass -->

## Setup / context

What you should be able to state from memory after section 1–2:

- The four laws of black hole mechanics ([[BardeenCarterHawking1973]]) had just been
  established and looked formally identical to the laws of thermodynamics, *but* with
  surface gravity κ playing the role of temperature only by analogy — classically a
  black hole has T = 0 (nothing escapes the horizon).
- The puzzle: if Bekenstein's A/4 is a real entropy, the analogy demands a real
  temperature too. Where does it come from?
- Hawking's setting: quantum field theory of a **free scalar field on a fixed
  classical background** describing gravitational collapse to a Schwarzschild black
  hole. No back-reaction. The geometry is dynamical only in the sense that it
  *forms* — the late-time exterior is stationary.

## Key idea

<!-- in your own words -- the spine of the Bogoliubov argument: in-vacuum is not
out-vacuum, because positive-frequency modes get mixed with negative-frequency
modes by the time-dependent collapse geometry. Try to write this in 3-4 sentences
without re-opening the paper. -->

## Main result

The late-time particle flux at infinity in mode $\omega$ is

$$
\langle N_\omega \rangle \;=\; \frac{\Gamma_\omega}{\exp(2\pi\omega/\kappa) - 1},
$$

i.e. a **thermal spectrum** at the Hawking temperature

$$
T_H \;=\; \frac{\hbar \kappa}{2\pi k_B c} \;\;\xrightarrow{\text{Schwarzschild}}\;\;
\frac{\hbar c^3}{8\pi G M k_B},
$$

modulated by a frequency-dependent **greybody factor** $\Gamma_\omega$ (the
absorption cross-section of the same mode). The thermality is *exact* in the
semiclassical limit, independent of the details of collapse.

## Derivation sketch

What to extract from §§2–4 (write this as a numbered list — your spine):

1. Set up two natural mode bases: **in-modes** (positive frequency on past null
   infinity $\mathcal{I}^-$) and **out-modes** (positive frequency on future null
   infinity $\mathcal{I}^+$ plus modes that fall through the horizon).
2. Relate them by a Bogoliubov transformation,
   $\hat b_\omega = \sum_{\omega'} (\alpha^*_{\omega\omega'} \hat a_{\omega'} -
   \beta^*_{\omega\omega'} \hat a^\dagger_{\omega'})$. Particle creation iff
   $\beta \neq 0$.
3. Compute $\beta$ by tracing an outgoing mode at $\mathcal{I}^+$ *backwards*
   through the collapsing geometry to $\mathcal{I}^-$. The geometric-optics
   approximation gives a **logarithmic phase pile-up** near the horizon-forming
   ray:
   $u \sim -\kappa^{-1} \ln(v_0 - v)$ as $v \to v_0$.
4. That log singularity is the whole game: Fourier-transforming a log-phase wave
   gives $|\beta_{\omega\omega'}|^2 / |\alpha_{\omega\omega'}|^2 =
   e^{-2\pi\omega/\kappa}$ — the **Planck factor**.
5. Sum over modes / include backscattering by the exterior potential to recover
   the greybody factor $\Gamma_\omega$.

Cross-check this against Jacobson's pedagogical re-derivation (see reading guide)
once you've tried writing it yourself.

## What I don't understand yet

<!-- be specific. Examples of the kind of question that lives here:
  - the trans-Planckian problem (does the log pile-up actually trust mode
    frequencies that, propagated back to ℐ⁻, are arbitrarily blue-shifted?)
  - what exactly fails if we try to do this in a non-stationary late-time geometry
  - where does the "free field, no back-reaction" assumption break down
-->

## Connections

- **Builds on:** [[BardeenCarterHawking1973]] (four laws), Bekenstein 1973 (entropy
  proposal — not yet in library.bib)
- **Used by:** essentially everything downstream. Direct numerical follow-up:
  [[Page1976]] (computes $\Gamma_\omega$ explicitly for Schwarzschild). Modern
  re-framings: [[AlmheiriHartmanMaldacenaShaghoulianTajdini2020]] review and the
  islands literature ([[Penington2019]], [[AEMM2019]]).
- **Refined / sharpened by:** [[Unruh1976]] (clarified the role of the horizon and
  the vacuum choice); [[GibbonsHawking1977]] (Euclidean / partition-function
  derivation — same answer, very different machinery).

## Critique

What to think about as you read:

- The fixed-background, no-back-reaction assumption is *the* limit of this
  calculation. The whole information paradox is what happens when you try to push
  past it.
- The trans-Planckian frequencies in step 3 of the sketch are physically suspect.
  Modern derivations using **horizon-localized correlators** or **Euclidean
  methods** sidestep this — worth understanding why.
- "Thermal" here means thermal *expectation values for occupation numbers* — it
  does *not* by itself imply the state is a thermal density matrix in any stronger
  sense. This subtlety is what the Page-curve / islands story re-litigates.

## Follow-ups

- [ ] Reproduce the Bogoliubov derivation on a single sheet of paper, no notes.
- [ ] Read the pedagogical companion (see reading guide) and compare derivations.
- [ ] Read [[Page1976]] for the explicit $\Gamma_\omega$ computation — this is
      directly relevant to a potential **Path-1 numerical paper** on greybody
      factors for a less-studied spacetime.
- [ ] Read [[AlmheiriHartmanMaldacenaShaghoulianTajdini2020]] (the islands review)
      to see what modern theory does with this result — relevant to **Path-2/3**.
