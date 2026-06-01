# Reading guide — Hawking 1975 + modern companion

**Purpose.** [[Hawking1975]] (`papers/hawking_radiation/Hawking1975.pdf`) is the
foundational paper but it is genuinely hard to read cold: 1975 notation, dense
geometric-optics arguments, and a writing style that assumes you already know
what answer to expect. Pair it with one modern pedagogical source to make it
tractable. Don't try to brute-force the original alone.

## Recommended pairing

1. **Primary text:** Hawking 1975 — *Particle creation by black holes*,
   Commun. Math. Phys. 43, 199–220. `papers/hawking_radiation/Hawking1975.pdf`.
2. **Modern companion:** Jacobson 2003 — *Introduction to quantum fields in
   curved spacetime and the Hawking effect*, [[Jacobson2003]]
   (arXiv: gr-qc/0308048). Free, well-written, has the *same* Bogoliubov
   argument in modern language with explicit intermediate steps.

If you want a textbook treatment instead of/alongside lecture notes, the
canonical references are **[[BirrellDavies1982]] Ch. 8** and **[[Wald1984]]
Ch. 14** (the latter is terser but mathematically tighter). Both are in
`references/library.bib`.

## Suggested pass structure

Three passes, each with a different goal. Don't skip ahead — the first pass is
deliberately shallow.

### Pass 1 — orientation (≈ 2 hours)

Read Hawking 1975 §§1–2 and the *introduction + conclusions only* of the rest.
Goal: get the shape of the argument and the headline result. Don't try to
follow every equation.

After pass 1 you should be able to answer, without notes:
- What is the headline result, in one equation?
- What is the input geometry — is the black hole eternal or formed by collapse?
  Does it matter?
- What classical assumption is the whole calculation made on top of?

### Pass 2 — derivation, with Jacobson alongside (≈ 1 week of focused study)

This is the real work. Read Jacobson 2003 §§1–4 *in parallel with* Hawking 1975
§§3–4. The two cover the same Bogoliubov argument but Jacobson spells out the
intermediate steps Hawking compresses.

Targeted milestones — write each on paper before moving on:

- [ ] Write down the in-mode and out-mode decompositions, including which
      surface each is naturally defined on (𝓘⁻, 𝓘⁺, horizon).
- [ ] Derive the Bogoliubov relation between $\hat a$ and $\hat b$ operators
      and show that nonzero $\beta_{\omega\omega'}$ implies particle creation.
- [ ] Show the geometric-optics tracing of an outgoing late-time ray back
      through the collapsing geometry produces the logarithmic phase
      $u \sim -\kappa^{-1}\ln(v_0 - v)$. **This is the heart of the argument.**
- [ ] Fourier-transform that log phase and obtain the Planck factor
      $|\beta|^2/|\alpha|^2 = e^{-2\pi\omega/\kappa}$.
- [ ] State the final thermal spectrum, including the greybody factor
      $\Gamma_\omega$, and identify $T_H$ for Schwarzschild.

### Pass 3 — critique & connections (≈ 2 days)

Re-read Hawking 1975 §§5–6 and Jacobson 2003 §§5–6. Goal: understand the
*limits* of the calculation, not just the calculation itself.

After pass 3 you should be able to discuss, in your own words:
- The trans-Planckian problem (do the blue-shifted modes traced back to 𝓘⁻
  invalidate the argument?). See Jacobson's discussion.
- What "thermal" does and does not mean here — i.e. why this result by itself
  does *not* resolve the information paradox.
- Where back-reaction would enter, and why ignoring it is justified for an
  *initially* large black hole but not throughout its evaporation.

## After this paper

In order of priority for *your* trajectory (paper-toward-MSc-scholarship):

1. [[Page1976]] — explicit numerical computation of $\Gamma_\omega$ for
   Schwarzschild. Direct precursor to a potential **Path-1 paper** computing
   greybody factors for a less-studied spacetime.
2. [[Unruh1976]] — clarifies the role of the horizon and the vacuum choice;
   removes some of the conceptual fog in Hawking 1975.
3. [[GibbonsHawking1977]] — Euclidean/partition-function re-derivation. Same
   answer, different machinery. Worth studying because the Euclidean methods
   reappear *everywhere* downstream.
4. [[AlmheiriHartmanMaldacenaShaghoulianTajdini2020]] — modern review of the
   information-paradox story. This is the bridge into **Path-2/3** territory.

Update `notes/per_paper/Hawking1975.md` and your research journal as you go.
