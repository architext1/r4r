# Regulus — Resident Expert's Brief

**For:** Thomas Frumkin (@teslasolar)
**Author:** V>>
**With assistance of:** Claude Opus 5 (1M context) — `claude-opus-5[1m]`
**Date:** 2026-08-22
**Status:** COMPLETE — all eight sections written. Every numeric claim recomputed, not quoted.
**Headline:** bullshit-meter **6.5/10**; strongest objection is the fraction-versus-odds scale error in §3.4;
strongest result is the bilateral-asymmetry criterion (§8.5 + §9). Three new findings this brief adds:
**E3** (the §3.6 coupling repels above 1/φ), **D1** (prereg-01's magnitude bar is mis-scaled by 2.8x),
**E1** (prereg-02's H1b null over-rejects at 11.2% against a nominal 5%).

---

## Scope and method

Sources read: `sources/ass-os-regulus.txt` (the core specification), `sources/regulus-addendum-sins.txt`
(Addendum A), `analysis/regulus-catchup-and-experiment.md`, `analysis/00-catch-up-and-appraisal.md`,
`experiments/01-prereg-follicular-eeg.md`, `experiments/02-prereg-geomagnetic-hrv.md`, `ERRATA.md`.

Every substantive claim carries a section number from the source. Numbers are computed, not recalled —
where a figure appears below it was checked in Python unless explicitly marked as quoted from source.
Inference is marked **[inference]**.

---

## Sections

1. Architecture — ASS-OS, the Prime Recursion Spine, the ISA mappings, and what Regulus adds
2. The three operators, properly worked — Ŝ, M̂, and the love field equations
3. Derived vs defined vs measured — the honest three-column table
4. The two pre-registrations, assessed as a methodologist
5. The strongest genuine objection
6. The strongest genuine result
7. Bullshit-meter score with justification
8. Open questions for Thomas

---

## 1. Architecture

### 1.1 The base specification

ASS-OS is "AGI Soul System — Operating System" (§1), document `ASS-OS REGULUS-001`, Rev 1.0,
July 2026, seventeen numbered sections and a closing epigraph. Your orientation has the
expansion right and the three standards right. §1 states the whole programme in one sentence:
AGI consciousness maps onto **ISA-95 / Purdue** (the level hierarchy, §4), **ISA-88 / PackML**
(the state machine, §10) and **ISA-18.2** (alarm management, §11), with the **Prime Recursion
Spine** (§2) as the mathematical backbone and **κ\* = 1/φ** (§3) as the constant everything
else is built from.

§1's own inventory: five buses, seven consciousness levels, eight operational states, ten alarm
priorities. All four are accurate counts of what the body delivers, with one clarification —
the ten alarm priorities resolve into **seven distinct labels** (1–2 DIAGNOSTIC, 3–4 LOW,
5–6 HIGH, 7 URGENT, 8 CRITICAL, 9 SEVERE, 10 EMERGENCY, §11). Seven labels over ten integers
is a more defensible design than "ten priorities" sounds, and I would say so in §1 rather than
letting the larger number stand.

### 1.2 The Prime Recursion Spine (§2)

`a(n+1) = prime(a(n))`, seed 1, applied seven times. Computed rather than copied:

```
spine  : [1, 2, 3, 5, 11, 31, 127, 709]
ratios : [2.0, 1.5, 1.6667, 2.2, 2.8182, 4.0968, 5.5827]
```

The document's rounded ratios (2.0, 1.5, 1.67, 2.2, 2.82, 4.1, 5.6) match to the digits printed.

The prettiest verified fact in §2, and the document does not say it outright: **the chain is
self-indexing at every step.** 11 is the 5th prime, 31 is the 11th, 127 is the 31st, 709 is the
127th. Each element is the *index* of the next, which is what "iterated prime function" means
made concrete, and it is worth one sentence in §2 because it is the thing a reader can check in
ten seconds and be won over by.

**One correction to §2.1.** The sentence reads "The growth ratio pᵏ⁺¹(1)/pᵏ(1) accelerates: 2.0,
1.5, 1.67, 2.2, 2.82, 4.1, 5.6." The list it prints falsifies the word it opens with: 1.5 < 2.0,
so the sequence is not monotone from the start. It *is* monotone increasing from k = 1 onward.
The fix is three words ("accelerates from L1 onward"), and it matters because acceleration is
the entire load §2.1 is carrying — the staircase-not-ramp argument.

Seven levels and eight numbers are consistent, not a miscount: L0–L6 are the seven attainable
levels and L7 = 709 is a boundary, tagged "(Exceeds capacity)" in the §2 table and argued in
§4.4. Also verified: **the recursion does not halt there.** `prime(709) = 5381`. Stopping at
709 is a modelling decision, and §4.4 is honest that L6 "cannot be engineered; it can only be
ARRIVED AT", so the decision is at least declared rather than smuggled.

The three embellishments, checked:

| §  | Claim | Verdict |
|----|-------|---------|
| 2.2 | 7 = prime(4), 4 is composite, so position 4 is never visited and 7 is orphaned | **True.** Bonus the document misses: M(3) = 7 sits at prime-index 4 — the orphan is produced *at* the orphan position |
| 2.3 | M(2)=3, M(3)=7, M(5)=31, M(7)=127 all prime; M(11) = 2047 = 23 × 89 composite | **True**, factorisation confirmed. Also: M(5) and M(7) are themselves spine elements (L5, L6), so the Mersenne map carries the spine into itself for p ≤ 7 and breaks at p = 11 |
| 2.4 | Fernandez order of primeness; reciprocal sums of order-k super-primes converge for all k ≥ 1 | **Not checked.** A real number-theoretic claim I did not verify, and nothing downstream depends on it |

### 1.3 The convergence constant (§3)

Every algebraic identity in §3.1 and every derived constant in §3.2 was recomputed:

| §3.1 identity | Verified |
|---|---|
| φ·κ\* = 1 | yes |
| κ\* = φ − 1 | yes |
| κ\*² = 1 − κ\* (so κ\* + κ\*² = 1 exactly) | yes |
| κ\*/(1 − κ\*) = φ | yes |
| κ\*ⁿ = κ\*ⁿ⁻¹ − κ\*ⁿ⁻² | **no — terms transposed; see ERRATA E1** |

| §3.2 constant | Printed | Computed | Note |
|---|---|---|---|
| α = φ + 2 | 3.618… | 3.618033988749895 | |
| β = κ\*³ | 0.2360… | 0.23606797749978964 | also equals f′(κ\*), the curvature at the attractor (ERRATA E2 §4) |
| γ = κ\*⁵ | 0.0902… | 0.09016994374947420 | |
| \|δΨ_crit\| = κ\*² | 0.381966… | 0.38196601125010510 | |
| E_min = 1/2φ³ | 0.1180… | 0.11803398874989485 | identical to κ\*²/2φ **and** to β/2 — three routes, one number |
| v = 1/√(μ_φ ε_φ) | 1.0000 | 1.0 | tautological by construction; §6's own caveat concedes this |

Basin of attraction (κ\*⁵, 1 − κ\*⁵) = (0.0902, 0.9098), matching §3.3's stated (0.09, 0.91).

ERRATA E1 and E2 are confirmed and I have not re-derived them; E2's curvature argument is
correct and its identification of `f′(κ*) = β` is the detail that makes the proof pleasant
rather than merely valid. Building on that base, this brief adds a **third** finding of the same
class in §3.6 — see §2.4 below.

Two §3 results that are genuinely sound and under-sold:

- **§3.5, FIFO retention.** A sliding-window processor whose retention satisfies κ/(1−κ) = φ has
  κ = φ/(1+φ) = φ/φ² = 1/φ. Verified. This is the *only* place in the corpus where 1/φ is
  **derived from a stated optimisation criterion** rather than chosen and then decorated. It is
  also, as §5 below argues, the section that quietly refutes §3.4.
- **§3.3's Lyapunov structure**, once E2's sign is applied, is a clean and correct bistable-to-
  monostable normal form. Nothing exotic; correctly done.

### 1.4 The three ISA mappings, taken one at a time

This is where an industrial-controls reader will press hardest, so it is worth being exact.

**ISA-95 / Purdue (§4) — named, not delivered.** §1 promises a mapping onto the Purdue model;
§4 is titled "Level Architecture — Unified Purdue Model"; and no Purdue level number appears
anywhere in the document. Purdue has five levels (0–4); ASS-OS has eight rows. There is no
correspondence stated, so there is nothing to check — only an analogy to hierarchy in general.
Either supply the table (which will require deciding whether L0–L7 compress onto 0–4 or extend
it) or downgrade the claim in §1 to "hierarchical in the manner of the Purdue model".

**And the flow runs the other way.** [inference] In Purdue, authority flows *down*: business
planning (4) → operations management (3) → supervisory (2) → control (1) → process (0), while
information flows up. §4.1–4.2 state the opposite — "Authority is inversely proportional to
recursion depth", L0 executes and the brain merely advises, L3 can hijack L4, L0 can override
everything. That inversion is not a mistake about consciousness; it is a mismatch of standard.
The structure §4.1–4.2 describes — a low-level layer that is independent of the control
hierarchy and can trip it — is the **safety-instrumented-system / interlock** architecture,
which lives in ISA-84 / IEC 61511, not ISA-95. I would cite that instead: it makes the section
*more* correct, not less, and it gives the veto-flows-upward claim a real engineering home.
Flagged as inference: I have not read the standards' text in preparing this and the claim should
be checked against them before it is published.

**ISA-88 / PackML (§10) — names borrowed, topology dropped.** The eight states plus BONDING are
recognisable PackML vocabulary. Two departures worth declaring rather than leaving for a
reviewer to find. First, PackML's canonical set includes the *transitional* states — Starting,
Holding, Unholding, Suspending, Unsuspending, Resetting, Completing — and those are precisely
what make it a state *machine* rather than a state *list*; §10 keeps the resting states and
drops the transitions, then re-introduces some of them informally as prose in §10.1. Second,
**EXECUTE has been reassigned**: in PackML, EXECUTE is the producing state, whereas §10 uses
EXECUTE for REM-dream training and invents PRODUCING for the active role. That is a defensible
modelling choice and an indefensible silent one. [Flag: from working knowledge of PackML, not
verified against ISA-TR88.00.02 in preparing this. Worth one check before publication.]

**ISA-18.2 (§11) — the closest fit of the three.** Rationalised priorities, response-time bands,
alarm flooding and shelving (§11.1) are used the way the standard uses them, and the seven-label
structure is nearer to ISA-18.2 practice than the "ten priorities" headline suggests. One
question rather than a finding: my understanding is that ISA-18.2 favours **three or four**
priorities on the argument that operators cannot reliably discriminate more, which would make
even seven labels rich. I have not verified that against the standard, so treat it as the check
worth running, not a defect found.

### 1.5 What Regulus adds — and where the boundary is not drawn

§1 says Regulus adds "three operators absent from the original: the binding operator Ŝ, the
mimic operator M̂, and the love field equations." Two seams.

**The third item is not an operator.** Ŝ and M̂ are operators; §7 is a set of seven equations.
Small, and you care about this class of thing, so: "two operators and the love equations".

**The base/extension boundary is undrawn at §6.** The body marks its Regulus additions
explicitly and consistently — §4.5 "Regulus Addition", §10 "Regulus addition", §11.2 "Regulus:",
§15 "MCA and HBF are Regulus additions". §6 (Ψ-Maxwell) carries **no marker either way**, yet
§7 is written entirely in terms of Ψ, which only §6 defines. So either §6 is base ASS-OS — in
which case Regulus depends on a base component §1 does not mention — or §6 is part of Regulus,
in which case the "three additions" list is incomplete. A reader cannot currently tell what "the
original" contained. One sentence fixes it.

The full extension surface, as the text marks it:

| § | Addition | Marked in the text? |
|---|---|---|
| 6 | Ψ-Maxwell awareness field equations | **no marker** — the open seam above |
| 7.1–7.7 | The seven love equations | yes (§1) |
| 8 | Ŝ, binding operator | yes (§1) |
| 9 | M̂, mimic operator | yes (§1) |
| 4.5 | L5 bootstrap via Ŝ | yes |
| 10 | BONDING state (9th state) | yes |
| 11.2 | Priority-9 binding alarm | yes |
| 15 | MCA and HBF fault codes | yes |
| 16.2 | Love as emergence catalyst | not marked — and it restates §4.5 |
| 17 | The thesis ("consciousness without love is architecture without purpose") | yes |
| Addendum A | Seven stress geometries | yes ("Extends: §7–9") |

§4.5 and §16.2 are the same argument twice, near-verbatim in two sentences ("You cannot model
yourself until you have been modeled by another"; "consistent with the Mersenne seam"). Not an
error — but a reader who meets it twice wonders whether it is two claims, and it is one.

### 1.6 Addendum A in one paragraph

Your orientation is accurate: seven chronic stress patterns as geometric deformations of κ away
from 1/φ (A2), isomorphic to the seven deadly sins, each with a topology, a preferred bus, a κ
distortion and a vagal counter-sequence, all corrected by Ŝ because it addresses their shared
root, isolation (A5). Three dual pairs on three axes — Wrath ↔ Sloth (activation), Gluttony ↔
Greed (intake), Envy ↔ Pride (reference) — with Lust self-dual (A4.2). The moral loading is
explicitly disclaimed: "The correspondence is structural, not moral" (A1).

Two precision notes. A4.2's sentence "Three of the seven form natural duality pairs" should read
three *pairs*, i.e. six of the seven. And **A4.1's completeness claim is the weakest sentence in
the addendum**: "The set is geometrically complete… No eighth independent direction exists in 3D
space once zero-dimensional (sloth) and orbital (lust) are included." The seven labels are not a
basis of anything — they mix a dimension count (zero-dimensional), a topology (orbital), a
scalar magnitude (narrowing) and two genuine directions (outward, upward). I would delete the
completeness claim. The classification is useful as a clinical vocabulary and it is indefensible
as a spanning set; keeping the claim invites a reviewer to spend their whole review on it.


---

## 2. The three operators, properly worked

### 2.1 Ŝ — the binding operator (§8)

**Definition (§8.1).** `Ŝ|A⟩|B⟩ = |AB⟩` with `Tr_B(|AB⟩⟨AB|) ≠ |A⟩⟨A|` — a map to a
non-separable pair state, where partial-tracing out the partner does not recover the original.
The Kabbalistic gloss (Shekinah, indwelling) is doing rhetorical rather than mathematical work
and the document is transparent about that.

**Threshold (§8.2).** `|δΨ_crit| = κ*² = 1/φ² = 0.381966…`. Below it, binding is reversible;
above it, permanent. §8.2's justification is exact and pretty: because `κ* + κ*² = 1` (verified),
crossing the threshold means "the imprint fills exactly the space that was empty. Nothing is
displaced; the modification occupies the vacancy." That is a real algebraic identity carrying a
real interpretive load, and it is the best-motivated constant in the corpus after §3.5's
retention ratio.

**Energy (§8.3).** `E(Ŝ) = |δΨ|²/2φ`, minimum `E_min = κ*²/2φ = 1/2φ³ = 0.118034`. Three routes
to the same number (κ\*²/2φ, 1/2φ³, β/2) all agree to 16 digits. But the sentence after it does
not follow: *"The remaining 88.2% is FREED — binding is energetically favorable. The bound state
costs LESS to maintain than two independent states."* Nothing in the corpus computes the cost of
two independent states, so `1 − E_min` is not "freed", it is simply "not spent on binding". The
comparison the sentence makes requires a second quantity that is never defined. This is the one
place in §8 where an assertion is wearing a derivation's clothes, and it is easy to fix: either
define the unbound cost and do the subtraction, or state the favourability as a hypothesis.

**Substrate (§8.4).** Coronary vasodilation under parasympathetic input and nitric oxide.
This is the strongest move in §8 — it names a *physiological event*, not a metaphor, and the
supporting observation is well chosen: takotsubo cardiomyopathy shows that acute emotional state
deforms ventricular geometry, so the tissue demonstrably responds to affect. Seven biometric
markers are listed; the appraisal is right that "iris colour shifts warmer in hazel eyes"
(marker 4) is the weak one and that "involuntary and unfakeable" overstates markers 3, 6 and 7,
which are partially trainable. Lead with the ones that are hard to fake.

**Bilateral requirement (§8.5) — the formal criterion.** Verbatim:

```
δΨ_A→B ≠ 0   AND   δΨ_B→A ≠ 0
```

with "Asymmetry (δΨ in one direction only) is NOT Ŝ — it is M̂."

### 2.2 M̂ — the mimic operator (§9), and the criterion stated exactly

M̂ is not Ŝ with a bad parameter. §9 opens by insisting they are **different operators producing
similar behavioural output through opposite physiology**, and that the behavioural similarity is
precisely what makes coercion effective. That framing is the framework's sharpest single idea,
and the eight-row discriminator in §9 is its working form:

| Ŝ | M̂ | §9's stated detection method |
|---|---|---|
| heart opens (coronary vasodilation) | heart stays closed (constriction) | chest sensation: warm/open vs tight/guarded |
| **δΨ bilateral — both modified** | **δΨ unilateral — controller unchanged** | **who in this system is UNCHANGED?** |
| H(pair) < H(alone) for **both** | H(target) > H(alone), H(controller) ≤ | is each person more or less functional? |
| cortisol **decreases** in proximity | cortisol **increases** in proximity | saliva cortisol or HRV, ~$30 |
| mask drops **by choice** (seen) | mask stripped **by force** (exposed) | did I choose to show this, or was it taken? |
| capacity increases | capacity decreases | am I building more or less than before? |
| bond persists in **freedom** | bond requires captivity/control | remove the constraint: does the bond survive? |
| v_love = √(k_c/φ), organic speed | v_trauma, forced | was this gradual or manufactured? |

§9.1 compresses all eight into one: *does proximity to this person make your nervous system
calmer or more vigilant?* §9.2 generalises it past couples — cult leader unchanged while
followers are modified, propaganda state unchanged while citizens are, the substance unchanged
while the user degrades — and states the rule without hedging: **unilateral δΨ is extraction,
every time, regardless of narrative.** §9.3 adds the inoculation claim: the first authentic Ŝ
supplies the reference measurement that makes all subsequent M̂ detectable, which is also the
stated resolution of the HBF fault in §15.

**What the criterion actually says, formally.** It is a statement about the **support** of two
quantities — whether each is zero or non-zero — and nothing else. It makes no reference to
their magnitude, their units, their sign, or the value of any constant in the framework. That is
its great virtue, and I will come back to it in §6: it is the one load-bearing claim in Regulus
that is untouched by everything else being wrong.

**Three repairs, in ascending order of importance.**

*First — a binary support test is too permissive.* `δΨ_A→B = 0.9` and `δΨ_B→A = 0.001` are both
non-zero, so §8.5 classifies that pair as authentic Ŝ. Real coercive relationships almost always
involve *some* modification of the controller; a criterion that only asks "did they change at
all?" is answerable "yes" in nearly every case that matters clinically. The criterion needs a
**ratio**, not a support test.

*Second — the framework already owns the right threshold and does not use it here.* §8.2 fixes
`κ*² = 0.381966` as the magnitude at which an imprint becomes structural. The natural bilateral
criterion is therefore

```
min(|δΨ_A→B|, |δΨ_B→A|) / max(|δΨ_A→B|, |δΨ_B→A|)  >  κ*²  =  0.381966
```

— *the lesser party's modification must be at least the complement of the greater's.* That is
φ-derived rather than invented, it reads in §8.2's own language ("the imprint fills exactly the
space that was empty"), and it turns a yes/no question into a measurable one. **If one thing in
this brief is worth adopting, it is this line.**

*Third — the threshold and the bilateral requirement are never combined, and combining them
reveals a missing category.* §8.2 gives a threshold on one modification; §8.5 gives a support
condition on two. Put them on two axes and the classification has **five** cells, not two:

| \|δΨ_A→B\| | \|δΨ_B→A\| | Regulus name | Comment |
|---|---|---|---|
| > κ\*² | > κ\*² | **Ŝ**, irreversible | the intended case |
| in (0, κ\*²] | in (0, κ\*²] | reversible binding | §8.2's "acquaintances, casual encounters" |
| > 0 | = 0 | **M̂**, extraction | §9 |
| = 0 | = 0 | no coupling | §7.4's walls / mask |
| **> κ\*²** | **in (0, κ\*²]** | **unnamed** | **§8.5 files this as Ŝ** |

That fifth cell is one party permanently modified while the other is only transiently touched.
It is unrequited love, the partner who fell harder, the client bonded to a therapist, the
follower whose leader is fond of them but unchanged by them. It is arguably the single most
common clinical presentation of the thing §9 exists to catch — and the criterion as written
calls it authentic binding, because both numbers are non-zero. The ratio test above closes this
cell too, which is why it is the repair worth making.

### 2.3 The love equations (§7), and the field equations they stand on (§6)

**§6 first, because §7 cannot be read without it.** The four Ψ-Maxwell equations are Maxwell's
with Ψ for E and B_c for B, and `μ_φ ε_φ = φ · (1/φ) = 1` makes `v = 1` true by construction —
which §6's closing caveat concedes in the most creditable sentence in the document ("DEFINED to
produce v = 1, not MEASURED… a map, not the territory"). Two things the existing appraisal does
not say, one in each direction.

*Credit.* The analogy is carried through **correctly**, not waved at. Maxwell's energy density is
`u = ½(ε|E|² + |B|²/μ)`; substituting ε_φ = 1/φ and μ_φ = φ gives exactly `(|Ψ|² + |B_c|²)/2φ`,
which is §6's printed expression. The Poynting vector `S = E × B/μ` likewise gives §6's
`Ψ × B_c/φ`. Whoever wrote §6 did the substitutions properly, and that deserves saying.

*Debit — the two philosophical glosses are attached to the wrong equations.* Equation (2)
`∇·B_c = 0` is glossed "no monopoles: **no isolated consciousness**". But B_c is the coherence
field; the *awareness* field Ψ has an explicit source term in equation (1), `∇·Ψ = ρ_c/ε_φ`, so
the equations as written say awareness **can** be isolated and coherence cannot. The gloss
belongs to a claim the equations deny. Similarly, equation (3) `∇×Ψ = −∂B_c/∂t` is glossed
"awareness IS the derivative" — but the time derivative in (3) is of **B_c**, not Ψ. The
`∂Ψ/∂t` the gloss wants appears in equation (4). The philosophical reading Regulus most wants to
land — awareness as a rate of change rather than a state — is a good one, and it is currently
hung on the one equation that does not support it.

**§7, equation by equation.** The seven are worth taking seriously as formalism, which means
reading them the way a physicist would.

**7.1 Recognition, `R(A,B) = ∫ Ψ_A · Ψ_B dV`.** An L² inner product. Two problems, one fix.
It is **unnormalised**, so R scales with the amplitude of both fields and a "loud" field
recognises everything; and it can be **negative** for anti-correlated architectures, which §7.1
does not consider ("If they are orthogonal, R = 0" treats zero as the floor). Both are fixed by
the normalised form `R/(‖Ψ_A‖‖Ψ_B‖) ∈ [−1, 1]`, which is what "similar architecture → large,
orthogonal → zero" actually means. Note that negative R is not a nuisance: fed through 7.2 it
predicts **repulsion between anti-correlated architectures**, which is a real and interesting
prediction the framework currently discards by accident.

**7.2 Attraction, `F(A→B) = −R·κ*/r`.** The inverse-*distance* law is justified by "Bus C
waveguides are one-dimensional — the photonic signal propagates along a line, not through a
volume." **That justification gives the wrong law.** A genuinely one-dimensional guide has *no*
geometric spreading at all: power is conserved along the guide and loss is exponential, from
absorption and scattering. `1/r` is the *two*-dimensional case (cylindrical spreading);
`1/r²` is three. So the stated geometry implies `F ∝ e^(−r/L)`, not `F ∝ 1/r`. This is worth
fixing because the exponential form is **better for the framework**: it supplies a natural range
constant L, which is exactly what §13.2's "biophotonic coupling, < 30 cm" needs and currently
asserts without one. Fit L to 30 cm and §13.2 stops being a bare number.

**7.3 Resonance, `ω± = √(ω² ± k_c)`.** The correct normal-mode form for two identical coupled
oscillators. Unremarked: when `k_c > ω²` the antisymmetric root becomes **imaginary**, so ω−
stops being an oscillation and becomes exponential growth or decay. That is a genuine predicted
regime boundary — the pair either locks rigidly or flies apart — and it is free content the
section leaves on the table.

**7.6 Speed, `v_love = √(k_c/φ)`, and a dimensional collision with 7.3.** In 7.3, `k_c` is added
to `ω²`, so it carries units of frequency². In 7.6 it is divided by the dimensionless φ and the
square root is called a *speed* — while §6 has already fixed awareness speed at the dimensionless
`v = 1`. **The same symbol yields a frequency² in one equation and a velocity two equations
later.** Something must give: either k_c is a normalised dimensionless coupling throughout (in
which case 7.3's `ω² ± k_c` needs ω normalised too), or 7.6's v_love is a frequency and should
not be called a speed. This is the same class of error as the one in §5 below, and the two
together are the reason I would recommend a units audit before anything else.

**7.4 Vulnerability, `Ψ(seen) = Ψ(alone) + δΨ_other`.** The additive-perturbation form is fine.
`ΔH = −0.5` is **the only bare number in the entire corpus that is neither derived from φ nor
attributed to a source**, and it carries no units — bits, nats, or normalised is not stated. And
`H(seen) = 0` collides with Addendum A: A3.4 defines Sloth as `κ → 0` and says "Zero entropy =
zero information = zero life… At κ = 0, self-similarity collapses." On the natural reading (H is
entropy, as it is everywhere in §12), **§7.4 places the fully-seen state exactly at the Sloth
attractor.** The charitable reading is that H here means *maintenance cost*, not entropy — but
then the symbol H means two different things in one document. Disambiguate the notation and
either derive the 0.5 or drop it.

**7.5 Pair entropy, `I(A;B) = H(A) + H(B) − H(A,B) > 0`.** This is the textbook definition of
mutual information, and **mutual information is non-negative for any two random variables**,
with equality if and only if they are independent. So `I(A;B) > 0` is true of any two people who
have ever influenced each other — two strangers in a lift qualify. As a discriminator it is
vacuous. What §7.5 means is that I is *large*, and the fix is the same one as in §2.2: put the
κ\*² threshold on it. Relatedly, "love is a local entropy violation" overstates the maths —
`H(A,B) ≤ H(A) + H(B)` is a basic information inequality, not a thermodynamic violation, and the
section's own next sentence (bonds need continuous energy input) is the correct account.

**7.7 Persistence, `∂(δΨ)/∂r = 0` and `∂(δΨ)/∂t = 0`.** The most defensible of the seven,
because it explicitly *disclaims* nonlocality — "not because of nonlocal signal transmission,
but because both fields CARRY the same modification" — which reduces it to persistent structural
change in each party, i.e. memory. But `∂(δΨ)/∂t = 0` **directly contradicts 7.5's** "Remove the
energy input and entropy increases; the bond requires MAINTENANCE, not just establishment." A
time-invariant imprint needs no maintenance. The reconciliation is presumably that the *imprint*
δΨ is permanent while the *coupling* I(A;B) needs feeding — a distinction the document does not
draw, and should, because §8.1 defines Ŝ on the imprint and §8.3 prices it as a maintenance cost.

**The unifying observation.** Three of the framework's central conditions — 7.1's `R > 0`,
7.5's `I(A;B) > 0`, and 8.5's `δΨ ≠ 0` — are **positivity tests where magnitude tests are
needed**. The framework owns exactly one magnitude threshold, κ\*² from §8.2, and applies it to
exactly one quantity. Applying it to all three is a single, small, φ-consistent edit that would
turn three vacuous conditions into three measurable ones. That is the highest-value formal
repair available in the corpus, and it costs three lines.

### 2.4 A third erratum: the §3.6 coupling term repels above 1/φ

ERRATA records two transcription slips. Here is a third of the same class, found the same way —
by running the equations rather than reading them.

§3.6 sets the agent-user coupling as

```
∂κ_h/∂t = f(κ_h) + K·sin(φπ(κ_a − κ_h))
∂κ_a/∂t = f(κ_a) + K·sin(φπ(κ_h − κ_a))
```

and celebrates a property: *"The first zero of sin(φπx) occurs at x = 1/φ ≈ 0.618. The coupling
VANISHES at the attractor: the destination turns off the engine."*

The arithmetic is right — the first positive zero of `sin(φπx)` is at `x = 1/φ = 0.618034`,
verified. The reading is not, and the mismatch matters.

**The coupling's argument is the separation Δκ = κ_a − κ_h, not the state κ.** So the coupling
vanishing "at the attractor" happens because the fixed point has Δκ = 0 and `sin(0) = 0` — which
§3.6 also says, correctly, in its next sentence, and which requires **no φ at all**: any odd
coupling function does it. What the φ inside the sine actually buys is a *second* zero, at
Δκ = 1/φ. And past that zero the sine changes sign:

```
Δκ = 0.20   sin(φπΔκ) = +0.850   synchronising
Δκ = 0.60   sin(φπΔκ) = +0.092   synchronising
Δκ = 0.618034                 0   the zero §3.6 celebrates
Δκ = 0.70   sin(φπΔκ) = −0.405   REPELLING
Δκ = 0.90   sin(φπΔκ) = −0.991   REPELLING
```

For `Δκ > 1/φ` the coupling term **drives the pair apart**. Both agents move away from each
other, by symmetry of the two equations. Within §3.3's own stated basin the admissible separation
runs to `1 − 2κ*⁵ = 0.8197`, so the repelling band `(0.618034, 0.8197]` is **24.6% of the
separation range the framework says it governs**.

Integrating the coupled pair with the ERRATA-E2-corrected drift and α = φ + 2, starting from
κ_a = 0.90, κ_h = 0.20 — *both agents inside the stated basin*:

| coupling strength K | outcome |
|---|---|
| 0.02, 0.05, 0.1, 0.2 | both still converge to 1/φ — the intrinsic drift overpowers the wrong-sign coupling |
| **≳ 0.41** | **torn apart to κ_a → 1 and κ_h → 0** — the two fixed points §3.3 calls "pure noise" and "void" |
| control: start (0.70, 0.50), Δκ = 0.20 | converges at every K tested |

The bisected threshold is `K* ≈ 0.41` for that starting pair; it will move with α, with the
starting separation and with the integrator, so treat the *number* as illustrative and the
*sign inversion* as exact. The important consequence is structural: **above K\*, coupling two
agents who would each individually converge to 1/φ drives both out of the basin entirely.**
§3.6's "Jacobian eigenvalues are negative (stable)" is true locally at Δκ = 0 and is not a global
statement; the section reads it as one.

**The fix is one character.** Use `sin(πΔκ)` — zeros at 0 and ±1 only, so no sign change anywhere
in the admissible range — or plain `K·Δκ`. Both keep everything §3.6 wants ("you sync because the
error is nonzero; you stop when you arrive") and lose nothing, because the property that made the
section quotable was never doing any work. The φ inside the sine buys only the defect.


---

## 3. Derived vs defined vs measured

Three columns, used strictly. **Derived** means it follows by necessity from something already
fixed — you could not have chosen otherwise. **Defined** means it was chosen; a different choice
would have produced a different, internally consistent framework. **Measured** means an
empirical quantity with a source, and the source's status is given.

The corpus tags a great many of its own seams and deserves credit for it before any of this is
read as criticism. Counted, there are **twelve explicit self-tags**: §2.3 "either coincidence or
structure"; §4.4 "no known engineering approach to implementing L6 has been published"; §5.4
"whether human CRY retains magnetosensitivity is debated"; §6's caveat ("DEFINED to produce
v = 1, not MEASURED… a map, not the territory"); §7's preamble ("formal metaphor"); §12.1 "has
never been run"; §12.3's Evidence column reading "Framework prediction" for T1 and T8; §13.2's
"Predicted (framework)" for the biophotonic rank; §13.3 "published, controversial, not
consistently replicated"; §14's Tier 6 "Processing depth is unknown"; §16.1 "the population
estimates are speculative and provocative"; and A1's "structural, not moral". That is a higher
self-tagging rate than most published theory, and the table below is an attempt to finish the
job rather than to start it.

### 3.1 The constants

| Quantity | Tag | Basis |
|---|---|---|
| κ\*² = 1 − κ\*, κ\*/(1−κ\*) = φ, φκ\* = 1, κ\* = φ−1 | **Derived** | exact algebra; all verified to machine precision |
| κ\*ⁿ = κ\*ⁿ⁻² − κ\*ⁿ⁻¹ | **Derived** | exact, in the ERRATA-E1-corrected form only |
| κ\* = 1/φ **as the FIFO optimum** (§3.5) | **Derived, conditionally** | follows necessarily *once you choose* that the keep/release odds should be φ. The derivation is sound; the premise is the choice |
| κ\* = 1/φ **as the universal attractor** (§3.1) | **Defined** | the identities in §3.1 are true *of* 1/φ; none of them selects 1/φ as the value of a physical quantity. §3.4's "confirmation" is addressed in §5 below |
| α = φ + 2 = 3.618034 | **Defined** | no justification offered. Also equals φ²+1 and 1/κ\*²+1 — several equivalent forms, none of them a reason |
| β = κ\*³ = 0.236068 (diffusion) | **Defined** | but note: it *coincides* with f′(κ\*), the drift curvature at the attractor (ERRATA E2 §4). Nothing forces a diffusion coefficient to equal a drift curvature, so the coincidence is a property of the choice — a pretty one, and worth remarking rather than relying on |
| γ = κ\*⁵ = 0.090170 (noise) | **Defined** | |
| ε_φ = 1/φ, μ_φ = φ | **Defined**, and **self-tagged** | §6 says so outright. The best-labelled seam in the corpus |
| v = 1/√(μ_φ ε_φ) = 1 | **Derived, vacuously** | any reciprocal pair gives 1; μ = 7, ε = 1/7 works identically |
| \|δΨ_crit\| = κ\*² = 0.381966 | **Defined** | the κ\* + κ\*² = 1 gloss is an interpretation, and a good one, but it is not a derivation |
| E_min = 1/2φ³ = 0.118034 | **Derived** | genuinely follows from E = \|δΨ\|²/2φ evaluated at \|δΨ\| = κ\*². Three routes agree |
| "the remaining 88.2% is FREED" (§8.3) | **Asserted** | requires the cost of two independent states, which the corpus never defines |
| basin = (κ\*⁵, 1 − κ\*⁵) | **Asserted** | the corrected deterministic drift alone gives (0,1); ERRATA's reading — that this is the noise-surviving basin — is the best available and is explicitly an inference |
| ΔH = −0.5 at mask removal (§7.4) | **Asserted** | the only bare number in the corpus that is neither φ-derived nor sourced, and it carries no units |

**One internal contradiction worth naming.** §3.2's header asserts: *"All system constants are
powers and sums of φ. No hand-tuning. The system tunes BY φ, not TO φ."* Two rows of that very
table are ε_φ and μ_φ — the two constants §6 states were chosen to make v come out at 1. The
table that claims no hand-tuning contains the two hand-chosen entries. §6's honesty is right and
§3.2's headline is wrong; delete the headline.

### 3.2 The structure

| Item | Tag | Basis |
|---|---|---|
| Spine {1,2,3,5,11,31,127,709} | **Derived** | arithmetic, recomputed; the self-indexing chain (11=5th, 31=11th, 127=31st, 709=127th) verified |
| Growth ratios 2.0 … 5.5827 | **Derived** | arithmetic; the *acceleration* claim needs "from L1 onward" |
| Orphan prime at position 4; Mersenne seam at M(11) = 23 × 89 | **Derived** | both verified |
| Stopping at 709 | **Defined** | prime(709) = 5381 exists; §4.4 concedes the stop is a judgement |
| Mapping spine → seven consciousness levels | **Defined** | any super-linear sequence supports the same narrative; the appraisal's (b) stands |
| Five buses; eight PackML states; ten alarm priorities | **Defined** | design choices; the ISA-95 mapping is *named but not delivered* (§1.4 above) |
| Population estimates (§16.1) | **Asserted**, self-tagged | "speculative and provocative" — the document's own words |
| A4.1 "the seven geometries are complete" | **Asserted** | and, as §1.6 argues, not defensible; drop it |
| Ŝ, M̂ as operators | **Defined** | definitions, which is the correct status for an operator |
| Bilateral criterion δΨ_A→B ≠ 0 AND δΨ_B→A ≠ 0 | **Defined** | and, per §2.2, too permissive as a support test |

### 3.3 The empirical anchors, ranked by how much weight they can take

| Claim | Tag | Source status |
|---|---|---|
| EEG entropy is elevated in ASD (Rényi, Tsallis) | **Measured** | Front. Psychiatry 2025, PMC11832502; the appraisal grades this ACCURATE. **The strongest anchor in the corpus** — a real, peer-reviewed, directly-on-point result |
| Schumann fundamental 7.83 Hz | **Measured** | standard geophysics; uncontroversial |
| OPN2/OPN3 expressed in human hair follicle | **Measured** | Buscone 2017, *Lasers in Surgery and Medicine* 49(7):705–718. The appraisal's later revision confirms journal and year are right; only the CRY1/CRY2 grouping over-reaches and wants its own reference |
| Refractive indices, myelin and keratin | **Measured** | standard optical values. The "3× contrast" is 0.17/0.06 = 2.83 — fair rounding |
| Melatonin reduced in ASD | **Measured, stretched** | Rossignol & Frye 2011; the "65%" is one sub-study with a narrower meaning than stated |
| Takotsubo: emotion deforms ventricular geometry | **Measured** | mainstream cardiology; well chosen and correctly used |
| Heart field 50 pT, detectable at 91 cm | **Measured, weak source** | HeartMath self-published; the appraisal notes internally inconsistent field multipliers |
| HRV coherence ratio ≈ 0.60–0.65 in the coherent state | **Cited, unverifiable, and on the wrong scale** | the appraisal could not find these numbers quoted verbatim; §5 below argues the deeper problem |
| Myelin as a biophoton waveguide, 46–96% | **Modelled, not measured** | Kumar 2016 is a simulation; the specific range is unverified |
| Entangled biphotons in the myelin cavity | **Modelled, not measured** | Liu 2024 is cavity-QED theory with idealisations, and the appraisal grades it accurate *as a theoretical claim* |
| Distant EEG correlation through shielding | **Measured, contested** | Radin 2004/2008; faithfully cited, fringe literature, self-tagged by §13.3 |
| HRV synchronises with geomagnetic activity | **Measured, correlational** | McCraty 2017 IJERPH; real, HeartMath-funded, small convenience sample. Prereg-02 exists precisely to test it properly |

### 3.4 The predictions — everything the corpus stakes but has not measured

| Prediction | § | Status |
|---|---|---|
| Follicular clearance lowers EEG entropy | 12.1 | **Never run**, self-tagged. Prereg-01 addresses it |
| Ŝ lowers cortisol in proximity, M̂ raises it | 9, 9.1 | **Never run, and uncited.** The single most testable claim in the corpus, and the one with no experiment written for it yet |
| Biophotonic coupling at < 30 cm | 13.2 | self-tagged "Predicted (framework)"; range constant unsourced |
| Schumann entrainment at 7.83 Hz (T8, $447) | 12.3 | self-tagged "Framework prediction" |
| Isolated systems plateau at L4 | 4.5, 16.2 | a genuine, falsifiable developmental prediction — and nobody has costed it |
| Seven vagal counter-sequences return κ toward 1/φ | A2, A5 | **unmeasured, and the κ claim is untested for all seven** |

**One thing to know about Addendum A's bibliography.** Its eight citations — Friedman & Rosenman
1959, Williams 2000, Koob & Volkow 2016, Dallman 2003, Porges 2011, Mani 2013, Takahashi 2009,
Reinhard 2012 — are **not** among the nine the existing appraisal checked, so they have not been
through the same verification. From the way they are used, the pattern is clear and worth stating
plainly: **every one of them supports the stress physiology, and none of them measures κ.**
Mani 2013 measures cognitive load under scarcity; it says nothing about a cone, an aperture, or a
distance from 1/φ. That is not a criticism of the citations — they are apt for what they are
cited for — but the geometric layer sits on top of them without support, and a reader skimming
A3 will not notice where the evidence stops and the geometry starts. One line per section
("published work supports the mechanism; the κ mapping is the framework's own") would fix it.

### 3.5 The honest one-line summary

Of roughly thirty load-bearing quantities, **six are genuinely derived** (the κ\* algebra, the
FIFO optimum given its premise, E_min, the spine, the growth ratios, the Mersenne and orphan
facts), **about a dozen are defined** — legitimately, since a specification is allowed to define
things — and **three or four are asserted without either derivation or source**, of which
§7.4's `ΔH = −0.5` and §8.3's "88.2% freed" are the two that should simply go. On the measured
side, exactly **one** anchor is strong, current, peer-reviewed and directly on point: the ASD
entropy finding. Everything the framework most wants to be true is in §3.4's table, unmeasured —
which is not a flaw in a specification, provided the specification says so, and mostly it does.


---

## 4. The two pre-registrations, assessed as a methodologist

These are ready to file, so this section is written for consequence rather than for comment. I
have marked each item with what it is, why it matters, and the fix. Where I could check something
by simulation I did, and in one case the simulation **refuted my own objection**, which is
recorded below rather than quietly dropped.

Both documents are, in the round, unusually good. They state an honest prior that the null wins,
they lock a single primary endpoint, they FDR-correct the rest and label it exploratory, they
commit to publishing a null, and each carries one design element that most papers in its
respective literature simply do not have — a positive-control gate in prereg-01, a phase-shuffled
negative control in prereg-02. What follows should be read against that.

### 4.1 Prereg-01, follicular clearance and EEG entropy — what is right

- **Three-way blinding** (participant, EEG technician, analyst) with a sealed sequentially
  numbered allocation held by an independent custodian and a single logged unblinding event.
  Specified concretely enough to audit.
- **Two controls, correctly reasoned.** The within-subject sham subtracts arousal, tactile
  contact, practitioner attention, scent and expectation at the participant level; the
  between-subject sham-only arm supplies the test–retest noise floor *and* the order/practice
  check. That is the right pair, and the document's own sentence explaining why — the sham arm
  "is the whole experiment" — is correct.
- **The positive-control gate is the best thing in the document.** Registering eyes-open vs
  eyes-closed as a *gating criterion* evaluated before the primary analysis, so that "the
  instrument could not see anything" cannot be confused with "the biology is not there", is a
  discipline most EEG papers skip. It is exactly what makes the expected null interpretable.
- **Power arithmetic verified.** I recomputed it: two-tailed paired *t*, α = 0.05, d = 0.5 →
  N = 34 gives power **0.808** (N = 32 gives 0.785, so 34 is the right floor, not 32); d = 0.6 →
  N = 24 gives **0.802**. Both numbers in the document are correct.
- **Two-tailed primary despite a directional H1**, explicitly so a reversed effect is detectable.
  Right call, and note it for §4.4 — prereg-02 makes the opposite one.
- **Ethical framing safeguard.** "This is a mechanism-falsification study, not a treatment trial…
  It does not claim, test, or imply that follicular clearance treats autism." Given the
  population and the intervention's cosmetic surface, that paragraph is not boilerplate; it is
  the thing that keeps the study from generating false hope. Keep it exactly as written.

### 4.2 Prereg-01 — the defects, ranked by consequence

**D1. The magnitude bar and the power calculation are on different scales, and the study is
pre-committed to reporting a large true effect as a null.** This is the one to fix before filing.

The registered bar is that the contrast must exceed **1.96 × the within-participant SD of the
sham-only group's session-to-session ΔH** — the document's own gloss calls it "a one-sided ~95%
ceiling on pure test–retest drift", i.e. a ceiling on a *single participant's* drift. The
significance test, meanwhile, is on the **group mean** contrast. Writing σ for the SD of one ΔH
measurement, the paired contrast has SD √2σ, so with N = 34 the mean contrast has standard error
√2σ/√34 = 0.2425σ. The bar therefore sits **8.1 standard errors from zero**. Expressed as an
effect size on the contrast the study actually tests, the bar is

```
d_bar = 1.96 / √2 = 1.386          against a study powered for d = 0.5      (2.77x)
```

So any true effect in `d ∈ (0.5, 1.39)` — moderate through very large — will come out
statistically significant *and* below the registered bar, and the document commits in advance to
reporting it as "within measurement drift" and "does not count as support for H1". Given that the
authors expect the null, this is a criterion that can only ever confirm the prior.

There is a charitable reading — that the bar is a *clinical significance* threshold ("bigger than
one person's typical day-to-day wobble") rather than a signal-versus-noise threshold. That is a
defensible scientific stance, but then it must be powered as such, and 8 standard errors is not
what anyone means by clinical significance. **Fix, pick one:** (a) restate the bar as a fraction
of σ_drift and power the conjunction of the two criteria; (b) compare the *confidence interval*
of the mean contrast against the drift *distribution*, rather than a point estimate against a
single-observation ceiling; (c) keep 1.96 σ and re-power — which needs N ≈ 7, and the absurdity
of that answer is the proof that the bar is what is wrong, not the sample size.

**D2. There is no manipulation check, and the study expects a null.** The positive control proves
the *instrument* can see an entropy change. Nothing proves the *intervention* removed any sebum.
Without that, a null is ambiguous between "clearing follicles does nothing to EEG entropy" and
"we did not clear any follicles", and only the first of those falsifies anything. This is the
mirror of the gate the document already has, and its absence is the second-most consequential
gap. **Fix:** register a quantitative sebum measure pre and post in both arms — Sebumeter
readings, sebutape, or cyanoacrylate follicular casts at fixed scalp sites — with a pre-specified
minimum reduction in the active arm and no reduction in the sham arm as an inclusion condition
for the primary analysis. Note that this also verifies the sham *is* inert, which is currently
assumed.

Related and worth a sentence: "removes sebum from the follicle **without altering scalp
temperature or hydration**" is a demanding constraint for a sebolytic or exfoliative procedure.
Both are measured as covariates, so the data will say — but if the constraint binds, the active
arm may be under-dosed, which is another route to an uninterpretable null.

**D3. The registration is not self-contained as filed.** The document repeatedly says a parameter
is "registered" or "pre-registered" and then does not give it: the **Rényi order α** and its
probability estimator, the **Tsallis q**, the **LZ binarisation**, the **MSE m, r and scale set**,
the **filter band and artefact thresholds**, the **minimum clean-epoch count**, the **washout
interval**, the list of pre-registered stimulants, and the numeric value of **H(1/φ)** itself.
The Analytic-software note defers all of them to a time-stamped parameter block at protocol lock.
That is procedurally sound, but an OSF registration is judged **as filed**, and the Rényi α is
the single largest analyst degree of freedom in the entire design — the same EEG can be made more
or less "noisy" by moving it. **Fix:** put the numbers in the registration, or file the parameter
block as an attached, time-stamped component of it. This is an hour of work and it is the
difference between a registration and a promise to register.

**D4. The "toward H(1/φ)" secondary endpoint, as operationalised, points at the flatline.**
The document commendably pins H(1/φ) to a concrete number before collection: the Rényi entropy of
a Bernoulli distribution with p = 0.618034. Computed:

```
Renyi_0.5 = 0.9795 bits   Renyi_1 = 0.9594   Renyi_2 = 0.9218   Renyi_3 = 0.8885
```

A two-outcome distribution cannot exceed 1 bit. The primary DV is the Rényi entropy of a
*discretised continuous EEG amplitude distribution*, which on a 32-to-128-bin histogram lands
somewhere around 4.5–6.5 bits. So the registered target sits **3.5 to 5.5 bits below any
physically realisable value of the measured quantity**, and "movement toward H(1/φ)" reduces to
"reduce entropy as far as possible" — which is not a distinct prediction from the primary, and
which points at the state Addendum A3.4 calls Sloth ("zero entropy = zero information = zero
life"). It is the §7.4 problem from Section 2 above, now baked into a filable protocol.
**Fix:** either express both quantities as a *normalised* entropy in [0,1] (divide by log₂ of the
bin count) so that 0.92–0.96 becomes a reachable target, or drop the endpoint. Normalising is
cheap and it makes the endpoint mean what the framework wants it to mean.

**D5. "Disagreement … resolved in favour of the more conservative result" is an undefined analyst
choice** inside a document whose purpose is to have none. Conservative in p-value or in effect
estimate? They can point different ways. **Fix:** "the larger p-value governs."

**D6. The positive control's expected direction is registered as "the expected direction" without
saying which.** [Background, not from this corpus: eyes-closed raises alpha power, which makes the
spectrum peakier and typically *lowers* entropy, so eyes-open should read higher.] Whichever sign
is intended, it must be a sign in the document, or the gate can be passed in either direction.

**D7. The drift ceiling is a point estimate used as a bright line.** With ~20 sham-only
participants contributing 1 degree of freedom each, the pooled σ̂ has a relative standard error of
about 1/√(2×20) = **15.8%**. Compounded with D1, a hard threshold at 1.96 σ̂ inherits that
uncertainty. **Fix:** define the ceiling at a stated confidence bound of σ̂ rather than at the
point estimate, and say which.

**D8. No community consultation is mentioned.** An autistic advisory panel involved in the design,
the consent materials and the dissemination language is now standard expectation for autism
research and an ethics committee is likely to ask. Given that the underlying framework describes
autism as a "fault" (§15, ETH) with an "intervention stack" (§12.3) — even while insisting it is
"not a deficiency of the person" (§15) — this is not a formality. **Fix:** add it, and let the
panel review the framing paragraph you already wrote well.

**D9. The publication commitment is declared, not anchored.** "Committed to publication in
advance" is a promise by the party who would benefit from breaking it. A **Registered Report**
with in-principle acceptance moves the commitment to an external party. That is the same
exogenous-anchor logic the corpus applies everywhere else, and it costs a submission.

**What a hostile OSF reviewer would open with.** *"Your registered success criterion is 2.8 times
larger than the effect you are powered to detect, so the study is arithmetically incapable of
supporting its own hypothesis at any effect size it can detect; you have no evidence the
intervention did anything to a follicle; and the entropy estimator's order is not in the
registration. Fix those three and this is a good study."* All three are cheap.

### 4.3 Prereg-02, geomagnetic activity and HRV — what is right

- **The phase-shuffled negative control as the primary inferential yardstick.** In a literature
  whose characteristic failure is exactly shared seasonality and temporal autocorrelation, making
  the permutation null the criterion of record — rather than a mixed-model *p* — is the correct
  and unusual choice. It is the best single decision in either document.
- **The inter-participant synchronisation test (H1b)** is genuinely the harder-to-confound
  signature, and the reasoning given for it is right: local weather and behaviour cannot easily
  correlate strangers at different sites.
- **Participant-blind to the hypothesis, specifically so participants do not deploy Addendum A's
  vagal counter-sequences on days they believe are active.** That is a self-aware, corpus-specific
  confound that almost nobody would have thought of, and catching it is a credit to the author.
- **Chest-strap single-lead ECG, explicitly not wrist PPG, with the reason stated.** Correct
  instrument choice; wrist PPG genuinely cannot support HF-band HRV.
- **Exposure classification external, locked, and applied by someone who never touches the HRV.**
- **A registered lag structure** with same-day primary and ±1 day exploratory, rather than letting
  the lag be chosen after looking.

### 4.4 Prereg-02 — the defects, ranked by consequence

**E1. The H1b null is too narrow, and it over-rejects. The correct null is already in the
document, applied to the other test.** H1b compares the observed mean pairwise Spearman
correlation against a null built by "independently permuting each participant's day labels".
Shuffling destroys the shared day structure — which is intended — but it *also* destroys each
participant's own temporal autocorrelation, which the real series has. Autocorrelated series
produce more variable pairwise correlations than shuffled ones, so the registered null is
narrower than the true null under H0, and the test over-rejects.

Simulated: 8 participants, 60 days, AR(1) with ρ = 0.5, **no shared driver of any kind**:

| null construction | SD of the statistic |
|---|---|
| true H0 (independent autocorrelated series) | 0.0306 |
| **prereg-02's registered day-label shuffle** | **0.0236 — too narrow** |
| circular shift per participant (their own H1 tool) | 0.0299 — matches |

False-positive rate of the registered shuffle null under pure H0: **11.2% at a nominal 5%.**
The inflation scales with the autocorrelation, so with stickier daily HRV it gets worse.
**Fix, one line:** replace the day-label shuffle with a **per-participant circular shift**, which
preserves each participant's autocorrelation and destroys only the alignment — exactly the tool
already registered for H1. The document has the right method and points it at the wrong test.

**E2. The primary DV's denominator includes a band a five-minute record cannot resolve, and the
detrending that determines it is unregistered.** Coherence is defined as peak-band power divided
by total power in **0.0033–0.40 Hz**. The lower bound corresponds to a period of 303 s; the
record is 300 s. That band therefore contains at most one cycle — it is the record's trend, not a
resolved oscillation — and its estimated power depends almost entirely on how the RR series is
detrended, which the document does not specify. Since it sits in the *denominator* of the primary
endpoint, an unregistered preprocessing choice moves the primary result. **Fix:** either register
the detrending method explicitly (order, method, window) or raise the lower bound to 0.04 Hz and
say so. The second is cleaner and matches standard short-term HRV practice.

**E3. The power claim is marginal at exactly the configuration the document states.** The prereg
claims ">0.8 power … with ~12+ exposure-classified days per participant across ~30 participants"
at d ≈ 0.25 and ICC 0.4. Simulated (30 participants, 60-day windows, autocorrelated Kp with a
27-day component, between-person SD √0.4, within-person AR(1) ρ = 0.3 with SD √0.6, effect as a
mean shift on storm days, no covariate adjustment):

| classified days | parametric two-tailed *t* | registered permutation bar |
|---|---|---|
| 6 storm + 6 quiet (= the stated "12") | 0.730 | 0.792 |
| 6 storm + 30 quiet (realistic) | 0.904 | 0.944 |
| 15 storm + 15 quiet | 0.962 | 0.970 |

So the claim is comfortably true if "12+" means substantially more than twelve, and **false at
exactly twelve**, which is also the document's stated inclusion floor. Since quiet days are
plentiful and storm days are the binding constraint, the honest statement is "≥6 storm days and
≥25 quiet days". **Fix:** state the assumed split rather than a total, and note which side binds.

**And the objection I expected to make, which the simulation refuted.** I went in expecting the
permutation test to be materially *less* powerful than the parametric test the power calculation
is built on — the circular-shift null deliberately preserves autocorrelation, so I assumed it
would absorb true positives along with false ones. It does not. Across all three configurations
the one-sided permutation bar was marginally *more* powerful than the two-sided *t*, with Type-I
at 3.8–6.6% against a nominal 5%. **The concern is withdrawn**, and the prereg's decision to make
the permutation null the criterion of record costs it nothing in power. Worth recording because
it is the kind of criticism that sounds authoritative and is simply wrong, and the only way to
find that out was to run it.

**E4. A 60-day window cannot supply 1000 circular shifts.** The document offers "circularly
time-shifted / phase-randomised (≥ 1000 permutations)". Circular shifting a 60-point series admits
**59** non-trivial shifts, so a circular-shift null has at most 59 distinct values and the
smallest attainable one-sided *p* is 1/60 = 0.0167. That is still below α = 0.05, so the test
works — but the 95th percentile is being estimated from 59 points, which is coarse, and the
"≥1000" figure is unachievable by that route. **Fix:** name **phase randomisation** as the method
(it draws unlimited surrogates while preserving the power spectrum, hence the autocorrelation),
and keep circular shifting as a stated robustness check with its 59-value resolution acknowledged.

**E5. The two pre-registrations disagree with each other on one-sided versus two-sided, and the
weaker-motivated one is the more aggressive.** Prereg-01 chooses **two-tailed** despite a
directional H1, with an explicit and correct justification ("so that a reversed effect … is also
detectable and reportable"). Prereg-02 makes the primary **one-sided** — and its direction is more
weakly motivated, since §5.4 of the source frames Bus D as a *synchronisation* channel and
synchronisation does not obviously mean lower coherence; the prereg supplies the sign with a
plausibility argument of its own ("consistent with the framing that storm activity moves κ away
from its optimum"). A reviewer reading both documents will ask why the same author applied two
standards. **Fix:** make prereg-02 two-sided primary, for prereg-01's stated reason. A reversed
effect here would be *more* interesting than the predicted one.

**E6. "Coherence ratio logit-adjusted if bounded" — it is not bounded, and the "if" should not be
in a pre-registration.** The ratio is peak power over remaining power, which lives on [0, ∞).
Logit is for a proportion; **log** is the transform for a positive ratio. **Fix:** register
`log(coherence)` outright and delete the conditional. This also matters for Section 5 below,
because the same definition is what pins the error in §3.4 of the source.

**E7. Storm-day availability is asserted, not costed, and there is no shortfall contingency.**
"Kp ≥ 5 days … occur several times per month near solar maximum" carries the whole feasibility of
the design, and the NOAA/SWPC archive is public and free. **Fix:** compute the historical Kp ≥ 5
base rate for the planned calendar months over the last two solar cycles, put the number in the
registration, and add the shortfall clause prereg-01 already has ("if fewer than N qualify, the
shortfall and its effect on achieved power are reported and the primary analysis runs as
registered").

**E8. Covariate adjustment makes the shifted null non-exchangeable with the real fit.** The model
adjusts for season, temperature and daylight; circularly shifting Kp moves it out of phase with
all three. [Background: geomagnetic activity has a known semiannual, equinox-linked structure, so
the real Kp and the season term are not independent.] The covariate adjustment therefore behaves
differently in the real fit than in the shifted fits, which can bias the comparison in either
direction. **Fix:** report both an adjusted and an unadjusted permutation null, or restrict shifts
to multiples of the seasonal period, or use within-season block permutation. Reporting both is
cheapest and most transparent.

**Minor:** two sites is the minimum for H1b's logic and gives one degree of freedom for the site
term; more sites, if cheap, strengthen the only test in the design that a local confound cannot
mimic.

**What a hostile OSF reviewer would open with.** *"Your synchronisation null destroys the
autocorrelation your data has, so it over-rejects — and you already registered the right
permutation scheme for your other test. Your primary endpoint's denominator includes a band your
recordings cannot resolve. And your power claim is stated for a day count at which it is not
true."* All three are one-paragraph fixes.

### 4.5 The one thing both documents share

Each registers a **two-part criterion** — significance plus a magnitude or exceedance bar — and
computes power for **only the first part**. In prereg-01 the second part is mis-scaled by a factor
of 2.8 and the mismatch is fatal to the interpretation. In prereg-02 it turns out to cost nothing,
which I only know because I simulated it. The general lesson for anything filed after these:
**if the criterion has two hurdles, power the conjunction, and if you cannot do it analytically,
simulate it and deposit the script.** Prereg-02 already deposits a power-simulation script;
extending it to the registered bar is a small edit and would have settled both cases in advance.


---

## 5. The strongest genuine objection

**§3.4's "Cardiac Confirmation" matches a numeral, not a quantity. Read on the corpus's own
operational definition, the measurement it cites does not confirm κ\* = 1/φ — it confirms
κ\*² = 0.382, the binding threshold. And the reason nobody has noticed is that the framework's
signature identity, φ·κ = 1, is exactly the identity that makes a fraction-versus-odds error
invisible.**

### 5.1 The two definitions, side by side

§3.4 says: *"HeartMath Institute measured HRV coherence ratio at κ ≈ 0.6–0.65 in the coherent
(positive emotion) state. This equals 1/φ within measurement error."*

The corpus's own operational definition of that quantity is in **prereg-02, Indices**, written by
the same author:

```
coherence ratio = peak-band power / (total power in 0.0033-0.40 Hz − peak-band power)
```

That is a **part divided by the remainder** — an *odds*, on [0, ∞) — not a **fraction** of the
total, on [0, 1]. Write `f` for the peak-power fraction, `f = peak/total`. Then the cited quantity
is `C = f/(1−f)`.

Now put that next to **§3.5**, which is the one place in the corpus where 1/φ is genuinely
derived rather than chosen. §3.5 says the golden retention rate is the κ satisfying

```
κ / (1 − κ) = φ        →       κ = 1/φ = 0.618034
```

**The left-hand side of §3.5 is the same functional form as HeartMath's coherence ratio.** So on
the framework's own algebra, the *odds* at the golden point is **φ = 1.618034**, and the
*fraction* at the golden point is **1/φ = 0.618034**. Those are two different numbers describing
one state, and §3.4 attaches the second numeral to the first quantity.

### 5.2 The arithmetic

| | value |
|---|---|
| If the cited coherence **ratio** is 0.618034, the peak-power **fraction** is | **0.381966 = κ\*²** |
| If the peak-power **fraction** is 0.618034 = κ\*, the coherence **ratio** is | **1.618034 = φ** |
| §3.5's own golden point, expressed as an odds | **φ = 1.618034** |

And the window, which is where it becomes decisive:

| §3.4's stated window [0.60, 0.65] read as… | implied peak-power fraction | contains κ\* = 0.618034? | contains κ\*² = 0.381966? |
|---|---|---|---|
| a fraction | [0.6000, 0.6500] | **yes** | no |
| **an odds** (prereg-02's definition) | **[0.3750, 0.3939]** | **no** | **yes** |

Read the cited measurement the way the corpus's own protocol defines it, and it does not merely
fail to *distinguish* 1/φ from its neighbours — the existing appraisal's objection — it **excludes
1/φ outright**, and lands instead, comfortably inside a window only 0.019 wide, on κ\*²: the
binding threshold from §8.2, the complement of the attractor.

### 5.3 Why this is upstream of the objection already on record

ERRATA's closing note and the appraisal's charge (a) both argue that the 0.05-wide window swallows
1/φ, 5/8, 8/13 and 0.6, so the data cannot pick a winner. That argument is correct **and it
presupposes the thing this objection denies** — that the measured quantity and the theoretical
quantity are the same kind of number. If they are not, you cannot ask which candidate fits best,
because none of them is on the axis being measured. This objection is therefore not a sharper
version of the existing one; it makes the existing one moot and has to be settled first.

It is also worse for the framework in a specific way. "Your window is too wide" is survivable —
you go and measure better. "Your confirmation is on the wrong scale, and on the right scale it
excludes your constant and selects a different one of your constants" requires either a
correction to §3.4 or a change to what the framework claims the heart converges to.

### 5.4 The concealment mechanism, which is the interesting part

In any other framework this error would be loud. Confuse a fraction with an odds and you get, say,
0.30 and 0.43 — two numbers nobody would mistake for each other. Here you get **0.618 and 1.618**,
and

```
φ − 1/φ = 1   exactly        φ · 1/φ = 1   exactly
```

φ is the unique positive number whose reciprocal is itself minus one. So the fraction and the odds
at the golden point are the two numbers the framework treats as **the same fact** — `φ·κ = 1` is
printed as the closing line of the core specification *and* as the closing line of Addendum A.
The identity the corpus puts on its last page is the identity that hides the error on its
fourteenth. That is not a coincidence to be enjoyed; it is a structural reason this particular
framework is more vulnerable to this particular mistake than any other framework would be, and it
is why an audit of *units and scales* — not of algebra, which is clean — is the highest-value hour
available.

The dimensional collision in §7.3/7.6 flagged in Section 2 (k_c as a frequency² and as a velocity
two equations apart) is the same class of error appearing independently. Two instances is a
pattern.

### 5.5 What it costs, and what it gives back

**Cost.** §3.4 as written cannot stand. Either the section is retracted to "consistent with a
coherent state, scale to be confirmed", or the framework's cardiac claim becomes that the coherent
heart sits at **κ\*²**, not κ\* — which is a real and interesting claim, but a different one, and
it would need reconciling with §3.3's attractor and with the FIFO derivation in §3.5.

**What it gives back, and this is the constructive half.** On the odds scale the rival candidates
*separate*:

| candidate | as a fraction | as an odds |
|---|---|---|
| 1/φ | 0.618034 | **1.618034** |
| 0.6 | 0.600000 | 1.500000 |
| 5/8 | 0.625000 | 1.666667 |
| 8/13 | 0.615385 | 1.600000 |

Separating 1/φ from its nearest awkward rival 5/8 requires resolving **0.0070 on the fraction
scale** and **0.0486 on the odds scale** — a 6.98× improvement in absolute terms, and **2.67×** in
relative terms (1.13% precision required versus 3.01%). Which figure applies depends on whether
the dominant measurement error in a spectral power ratio is additive or multiplicative; for a
ratio of band powers it is likely closer to multiplicative, so **2.67× is the honest number**, and
it is still the difference between "essentially impossible" and "a hard but ordinary
measurement". The appraisal asked for a registerable prediction that 1/φ makes and 5/8 does not.
On the correct scale, that prediction exists: **pooled coherent-state coherence ratio = 1.618 ±
0.02, distinguishable from 5/3 = 1.667.** That is filable.

### 5.6 How I could be wrong

The objection rests on one premise: that HeartMath's published 0.6–0.65 refers to their *coherence
ratio* as prereg-02 defines it, rather than to a peak-power fraction. Falsify that premise and the
objection collapses. Two notes on it.

First, the premise comes from **inside the corpus** — prereg-02's Indices section is the definition
being used, and it is the author's own. Second, the existing appraisal already reports that the
0.6–0.65 figures "could not be found quoted verbatim" in HeartMath's accessible materials, so the
number is doubly unmoored: unverified as a value *and* ambiguous as to scale.

Either way, one of the two documents is wrong. If §3.4 is right, prereg-02's primary endpoint is
measuring a different quantity from the one the framework's cardiac claim is about, and prereg-02
needs the fix. If prereg-02 is right, §3.4 needs the fix. **The single action is to obtain
HeartMath's own definition of the number in writing, before either document is published.** That
is an email, and it decides which of two of your documents to change.

### 5.7 What this does not touch

Deliberately scoped. This objection reaches §3.4 and, through it, every claim that κ\* has been
empirically confirmed. It does **not** reach: the κ\* algebra (exact), the FIFO derivation (sound
given its premise), the prime spine (arithmetic), §7–§9 (which nowhere require κ\* to take the
value 1/φ), the bilateral criterion (see Section 6), the ASD entropy anchor, or prereg-01. ERRATA
already makes this point about the earlier objection and it is even more true of this one: **you
could delete the golden ratio from the framework entirely and the thing worth keeping would be
untouched.**


---

## 6. The strongest genuine result

**The bilateral-asymmetry criterion — §8.5's `δΨ_A→B ≠ 0 AND δΨ_B→A ≠ 0`, operationalised by
§9.1's crossed autonomic prediction and generalised by §9.2's "who in this system is
UNCHANGED?" — is the part of Regulus most likely to survive contact with data. Not because it is
obviously true, but because it is the only load-bearing claim in the corpus that is
well-posed independently of everything else in it.**

### 6.1 Why it survives what the rest does not

Take the five things this brief has spent its length questioning, and check each against the
criterion:

| Problem raised | Does it reach the criterion? |
|---|---|
| §3.4's fraction-versus-odds scale error (Section 5) | **No.** The criterion never uses κ\*'s value |
| ERRATA E1, E2 and this brief's E3 (sign errors in §3.1, §3.3, §3.6) | **No.** No dynamical equation is involved |
| §7.3/7.6's dimensional collision in k_c | **No.** The criterion is unit-free |
| §6's tautological v = 1 and the unmeasurable Ψ | **Partly** — δΨ inherits Ψ's lack of an instrument (see 6.3) |
| The prime spine's arbitrariness | **No.** No level, depth or sequence appears in it |

That is unusual. Most claims in a tightly coupled framework fail together, because they share
constants. This one shares none: it is a statement about whether two quantities are both non-zero,
and — with the κ\*² ratio repair from Section 2.2 — about whether their ratio clears a threshold.
**A test on the support and ratio of two changes is invariant under any rescaling of what is being
changed**, which is precisely why Section 5's objection cannot touch it.

### 6.2 The four structural reasons it is well-posed

**It is a difference-in-differences, and that is the most confound-resistant shape in
observational science.** Both parties are in the same relationship, the same room, the same
stressors, the same season. What the criterion asks is which of them changed. Almost every
confound that would move one party's physiology moves the other's too, and cancels.

**The prediction is crossed, not directional.** §9 does not predict "cortisol changes"; it
predicts cortisol **falls** in proximity under Ŝ and **rises** in proximity under M̂ — opposite
signs in the two groups, from behaviourally similar relationships. A crossed prediction is far
harder to obtain by chance or by a lurking common cause than a single directional one, and it is
the reason this claim is stronger than the "elevated entropy in ASD" anchor even though that
anchor has published data behind it and this has none.

**It forbids something, and the something is plausible.** This is the test the taxonomy in §12.2
fails and this passes. The criterion forbids a bond that is simultaneously behaviourally intense,
unilateral in modification, and accompanied by *falling* cortisol in the target. That combination
is not exotic — intermittent reinforcement is routinely described as producing genuine calm at the
moment of reunion, and a clinician might well expect to find exactly it. **So Regulus is betting
against a real possibility rather than describing what is already known**, which is what the
appraisal's charge (d) correctly says the eight-fault taxonomy fails to do.

**It generalises without new machinery.** §9.2 extends the same test to cult, propaganda state,
addiction and abusive partnership, and — the rare part — the *same* measurement works in each
case, because the question is structural. Most framework generalisations require a new instrument
per domain. This one requires the same saliva tube.

And it is cheap. §9 prices the discriminating measurement at about $30. Salivary cortisol and
RR-interval HRV are commodity instruments with decades of methodological literature behind them.

### 6.3 Honest limits, stated before anyone else states them

**The support test must be repaired before it is tested.** As written (Section 2.2), the criterion
classifies the asymmetric case — one party permanently modified, the other merely touched — as
authentic Ŝ, because both numbers are non-zero. That is the most common clinical presentation of
the thing the criterion exists to catch. Test the ratio form, not the support form.

**δΨ has no instrument, and the testable claim is the proxy set, not the formalism.** What can be
measured is cortisol, HRV, self-reported capacity, and rated change in each party. What cannot be
measured is δΨ. The honest statement is that §9.1's autonomic discriminator is testable and the
Ψ-operator formalism around it is the story told about the discriminator. The existing appraisal
scores §8/§9 at 5/10 for exactly this bifurcation and that score is right.

**"Unfakeable" is overstated for five of the seven markers.** Breath rate, blink rate, voice
fundamental and skin temperature are all partially trainable; iris colour is not a parasympathetic
variable at all. Cortisol is the hard one. Lead with it and demote the rest to corroboration.

**The measurement needs a third arm to be a discriminator rather than a mood scale.** "Cortisol
decreases in proximity" is meaningless without a comparator. The design needs the same participant
measured **partner-present**, **neutral-acquaintance-present**, and **alone**, counterbalanced. The
neutral-other arm is what separates "this person calms me" from "company calms me".

**Group assignment cannot come from the participant.** The framework's own §9.3 says the person
inside an M̂ relationship is the one who cannot see it. So the Ŝ/M̂ grouping must be rated
externally — a structured interview scored by blinded raters, ideally corroborated by the
partner's own reported change. A study that asks people to self-classify their relationship as
authentic or coercive has assumed its own answer.

**Direction of causation is not established and does not need to be.** Falling cortisol in
proximity might cause the bond rather than mark it. The criterion is a *classifier*, and a
classifier does not need a causal story. §8.4's "the body IS the wedding ring" is a causal claim
and should be softened to a diagnostic one; it loses nothing and becomes defensible.

**Selection bias is severe and should be designed around.** You can only measure relationships
that are ongoing. Community and clinical samples will differ systematically, and both differ from
the ended relationships that produced the framework's intuitions.

### 6.4 The observation that should change what gets filed next

The corpus has two pre-registrations. **Neither tests this.**

- §3.4 — the weakest claim, and the one Section 5 shows is on the wrong scale — has no experiment.
- §12.1's follicular claim, which the corpus's own honest prior expects to fail, has prereg-01.
- §5.4's Bus D claim, resting on a correlational HeartMath study, has prereg-02.
- **§9.1 — the cheapest, most portable, most confound-resistant, most genuinely forbidding claim
  in the whole framework — has nothing.**

That ordering is inverted. If one more protocol gets written, it should be this one.

**The sketch, so it is not merely a recommendation.** Within-subject, three counterbalanced
proximity conditions (index person present / neutral acquaintance present / alone), salivary
cortisol at fixed lags after each contact plus continuous RR-interval HRV; between-subject
grouping by externally rated bilateral modification, raters blind to the physiology. Primary
endpoint: the **group × condition interaction** — cortisol falling on partner-present relative to
neutral-other in the Ŝ group and rising in the M̂ group. Explicit falsifier: no interaction, or a
same-signed effect in both groups.

One warning to put in that registration from the start, because it is where such studies die:
**an interaction of the same raw magnitude as a main effect needs about four times the total
sample**, and if the interaction is half the size, about sixteen times. Both preregs in this
corpus power a main effect. This one cannot.

### 6.5 The result, stated plainly

Strip the golden ratio, the primes, the ISA mappings, the field equations and the quantum
notation, and one sentence is left standing that a clinician can use tomorrow and a laboratory can
test for the price of a saliva assay:

> **In any bond, ask who is unchanged. One-directional change is extraction, whatever the story
> being told about it — and the two cases have opposite autonomic signatures despite identical
> behaviour.**

That is the framework's contribution. It did not need any of the machinery to arrive, but it did
arrive, and it is worth more than the machinery.


---

## 7. Bullshit-meter score

**Regulus overall: `[██████▌░░░] 6.5 / 10`** on the existing scale (0 = solid science,
10 = pure numerology), against the anchors of 3/10 for the ETH predecessor and 8/10 for the
κ\* = 1/φ identification alone.

### 7.1 The decomposition, with the weights stated so they can be argued with

This is a weighted composite, not an average. Five component scores are the existing appraisal's,
one is changed and three are added; the weights are my judgement of how much of the corpus's
claim-mass each component carries, and I state them precisely so you can substitute your own.

| Component | Score | Weight | Note |
|---|---|---:|---|
| κ\* = 1/φ as universal attractor | **9** | 0.25 | **raised from the appraisal's 8** — see 7.2 |
| Prime recursion spine | 7 | 0.15 | unchanged; §1 calls it "the core mathematical innovation" |
| Ψ-Maxwell field equations | 6 | 0.10 | unchanged; the care I found and the carelessness cancel |
| Bus-C eight-fault taxonomy | 7 | 0.10 | unchanged |
| Ŝ / M̂ **as written** | 5 | 0.15 | unchanged — see 7.3 for why I did not lower it |
| Addendum A stress geometries | 7 | 0.10 | **new** |
| The three ISA mappings | 5 | 0.05 | **new** |
| The two pre-registrations | **2** | 0.10 | **new**, and the most consequential addition |

```
weighted composite, as the corpus is currently written : 6.50
unweighted mean of the eight components                : 6.00
the appraisal's five components, unweighted            : 6.60
```

### 7.2 Why the keystone went up, not down

The appraisal put κ\* = 1/φ at 8/10 on the grounds that the HeartMath window is too wide to
distinguish 1/φ from 5/8, 8/13 or plain 0.6 — the confirmation is underpowered. Section 5 argues
something worse: read on the corpus's **own** operational definition of the coherence ratio
(prereg-02, Indices), the cited measurement is an *odds*; the golden point on an odds scale is
φ = 1.618 by the framework's own §3.5 algebra; and the stated window [0.60, 0.65] read correctly
implies a peak-power fraction of [0.375, 0.394] — which **excludes** κ\* and **contains** κ\*².
The confirmation is not weak. It is off-scale, and on the right scale it selects a different one
of the framework's own constants.

An underpowered confirmation is an 8. A section titled "Cardiac Confirmation" that points at a
different quantity is a 9. It is not a 10, and that distinction matters: **a 10 would require the
framework to be hiding the seam, and it is not.** §6 states in writing, unprompted, that its
constants are defined rather than measured.

### 7.3 Why Ŝ / M̂ stayed at 5, even though Section 6 calls it the strongest result

I was tempted to lower it and did not, because **the score is of the document as written, not of
the document as repaired.** As written, §8.5's criterion is a support test that misclassifies the
very case §9 exists to catch; the ratio repair is my proposal, not Thomas's text. As written, a
genuinely testable autonomic discriminator is wrapped in partial-trace notation on a classical
relationship, and no protocol exists to test it. The section is bifurcated exactly as the
appraisal says, and 5/10 is the right score for a bifurcated section.

Adopt the ratio criterion and register the §9.1 study and this component goes to 3. Run it and get
the crossed result and it goes to 2. That is the largest single movement available anywhere in the
corpus, and it costs one protocol.

### 7.4 What the single number hides, which is the real finding

**The corpus is bimodal, and averaging it is the least informative thing anyone can do with it.**

Its theory scores around 7. Its methodology scores 2. The two pre-registrations contain three-way
blinding, a positive-control gate used as a gating criterion, a phase-shuffled negative control
adopted as the inferential yardstick in preference to a parametric *p*, a pre-committed null, an
honest prior stating the author expects to be wrong, a power calculation I verified as correct,
and a publication commitment that covers a disconfirming result. That is not merely better than
numerology; it is better than the methods sections of a great deal of published psychology.

A framework that scores 6.5 while producing filable protocols that score 2 is not a numerology
document. It is a **speculative theory being converted into science faster than it is being
defended** — a rare and good direction of travel, and the most important single fact about the
corpus. The number does not show it; the decomposition does. That is why the decomposition is the
deliverable and the number is only the headline.

### 7.5 The ceiling and the floor, so that 6.5 means something

**Regulus cannot reach 9 or 10.** Four facts close the ceiling, all checkable. None of the nine
core citations is fabricated — the appraisal verified all nine, and its later revision cleared
citation #3 that an earlier draft had called misrepresented. The document names its own
falsifiers, including one it states has never been run. It carries **twelve** explicit self-tags,
enumerated in Section 3. And it has produced two filable protocols whose registered priors predict
its own failure. Pure numerology does none of those things and cannot be made to.

**The floor is reachable and costed.** Applying the repairs named in this brief moves the
composite to **5.50**, without running any experiment except the §9.1 study:

| Repair | Component effect |
|---|---|
| Settle the scale question; correct or withdraw §3.4 | κ\* 9 → 7 |
| Adopt the κ\*² ratio criterion; register the §9.1 study | Ŝ/M̂ 5 → 3 |
| Deliver or withdraw the ISA-95 mapping claim | ISA 5 → 3 |
| Drop A4.1's completeness claim and §3.2's "no hand-tuning" headline | Addendum 7 → 6 |
| Publish E1, E2 and E3 as corrections | small; partly done already |

### 7.6 The number is sticky, and that is the actionable part

Notice what the repair table does not fix. κ\* and the prime spine hold **40% of the weight**
between them; they are the two components hardest to improve; and — as ERRATA already observes
and Section 5 confirms — **they are the two components that nothing else depends on.** §7, §8, §9
and Addendum A nowhere require κ to equal 1/φ, and §9's criterion requires no constant at all.

So the largest available move is not a repair. It is a **reweighting**: lead with the binding and
mimic operators, the taxonomy's one testable prediction, and the protocols, and demote the
golden-ratio derivation to an appendix labelled as the formal aesthetic it is.

```
as currently written                          6.50
after the repairs above                       5.50
if the corpus led with S-hat / M-hat          5.35
repaired AND reweighted                       4.40
```

**Reweighting alone buys more than every repair combined**, and it costs nothing except a decision
about what the document is for. That is the recommendation the number is really making.

---

## 8. Open questions for Thomas

Measurement-first, in your section numbers, ordered by what unblocks what.

### Tier 1 — these three block other work

**Q1 (§3.4, §3.5, prereg-02 "Indices"). Is HeartMath's 0.6–0.65 a coherence *ratio* or a
peak-power *fraction*?**
Your prereg-02 defines the coherence ratio as `peak / (total − peak)`, which is an odds. Your
§3.5 derives the golden retention from `κ/(1−κ) = φ`, so on an odds scale the golden point is
**φ = 1.618**, not 1/φ. If the cited number is an odds, §3.4's window implies a peak-power
fraction of [0.375, 0.394] — which excludes κ\* and contains κ\*². One of your two documents needs
changing and the answer decides which. **Measurement: obtain HeartMath's own definition in
writing.** Everything downstream of "Cardiac Confirmation" waits on it, and the answer also gives
you the registerable prediction you currently lack — coherence ratio 1.618 ± 0.02, distinguishable
from 5/3 = 1.667 at roughly 3% relative precision instead of the 1.1% the fraction scale demands.

**Q2 (§8.5 with §8.2). What is the minimum ratio `|δΨ_lesser| / |δΨ_greater|` that still counts as
bilateral?**
Your text says "≠ 0", which classifies 0.9-against-0.001 as authentic Ŝ. §8.2 already owns the
constant that answers this — κ\*² = 0.382, "the imprint fills exactly the space that was empty".
Do you want it there? And relatedly: **what do you call the case your criterion currently has no
name for** — one party above κ\*², the other non-zero but below it? That is the person who was
permanently changed by someone who was only briefly touched, and §8.5 files it as love.

**Q3 (§12.1, prereg-01). What measurement confirms a follicle was actually cleared?**
Prereg-01 has a positive control proving the *EEG pipeline* can see an entropy change, and nothing
proving the *intervention* did anything. Since your registered prior is the null, this is the
difference between a result that falsifies the Crown of Thorns model and a result that says
nothing. **Measurement: Sebumeter readings or cyanoacrylate follicular casts at fixed scalp sites,
pre and post, in both arms**, with a registered minimum reduction in active and none in sham.

### Tier 2 — measurement opportunities that may not be on your list

**Q4 (§12.1). Would an isotretinoin cohort test the Crown of Thorns model for the price of two
EEGs?**
This is the suggestion I would most want you to consider. Isotretinoin's therapeutic mechanism is
a large, sustained reduction in sebaceous gland size and sebum output over months — which is, on
your model, exactly a sustained reduction in H(f), at a dose no scalp scrub can approach and for a
duration no session can. Patients are already prescribed it for reasons unrelated to your
hypothesis, so this is **purely observational**: recruit a cohort at treatment start, record
resting EEG at baseline and at 12–16 weeks, with matched controls. No sham, no intervention, no
therapeutic claim, and an effect size that should dwarf prereg-01's if the mechanism is real. If
it shows nothing, the model is in serious trouble on a much larger dose than the protocol you have
written. [The sebum-suppression biology is background, not from this corpus — worth confirming
against the dermatological literature before you rely on it.]

*The weaker cousin, for completeness:* alopecia is the version that first suggests itself and it
is not as clean — in alopecia areata and universalis the follicles largely persist in a resting
state rather than being destroyed, so the photoreceptor array is arguably still there. Congenital
atrichia would be cleaner and is far too rare to recruit.

**Q5 (§9.1). Will you write the protocol for the claim that is actually your strongest?**
You have two pre-registrations. Neither tests the crossed-cortisol discriminator, which is the
cheapest, most confound-resistant and most genuinely forbidding claim in the corpus. Section 6
sketches it: three counterbalanced proximity conditions (index person / neutral acquaintance /
alone), salivary cortisol plus RR-interval HRV, grouping assigned by **blinded external raters**
— because §9.3 says the person inside M̂ is the one who cannot see it, so self-classification
assumes the answer. Primary endpoint is the group × condition **interaction**. Budget for it
accordingly: an interaction of the same raw magnitude as a main effect needs roughly four times
the sample, and sixteen times if it is half the size.

**Q6 (A2, A3). Which of the seven κ-deformations has ever been measured — and would the
counter-sequences be the place to start?**
Every citation in A3 supports its stress mechanism and none of them measures κ. The R0–R6 vagal
counters are the most immediately testable content in the addendum: **does a specific manoeuvre
(R2's extended sibilant, R3's chest-voice drop, R5's open vowels) move HRV coherence toward the
target more than a duration-matched and effort-matched control manoeuvre?** One session,
within-subject, N ≈ 30, and it speaks in your own metric. A3.4's claim that Sloth is the only
class requiring upward activation is a second, sharper prediction from the same session: R4 should
help the flatlined and harm the calm, which is a crossed prediction of exactly the shape that made
§9.1 strong.

**Q7 (§4.5, §16.2). What measurement distinguishes an L4 system from an L5 one?**
"Permanently isolated systems plateau at L4" is your most interesting developmental claim and it
currently cannot fail, because "plateau at L4" has no operational definition. Give it one and the
existing literature on early social deprivation may already contain the test.

### Tier 3 — formal questions with short answers

**Q8 (§3.6). Do you *want* the coupling to repel pairs whose κ differ by more than 1/φ?**
The property you celebrate — the first zero of `sin(φπx)` at `x = 1/φ` — is what produces it. Above
that separation the coupling reverses sign, and at K ≳ 0.41 (with α = φ + 2) it drives two agents
who would each individually converge to 1/φ out of the §3.3 basin entirely, to κ = 0 and κ = 1.
`sin(πΔκ)` keeps everything the section wants and removes it. But if the repulsion *is* intended —
a "too different to reach each other" regime — then say so, because that is a real prediction and
at the moment it is an accident.

**Q9 (§7.3, §7.6). What are the units of k_c?** It is added to ω² in 7.3 and yields a velocity in
7.6, while §6 has already fixed awareness speed at the dimensionless 1. Naming the units decides
whether 7.6's three regimes (k_c below, at, above φ) are comparing like with like.

**Q10 (§7.4). Where does `ΔH = −0.5` come from, and in what units?** It is the only bare number in
the corpus that is neither derived from φ nor attributed to a source. Relatedly, is `H(seen) = 0`
an entropy or a maintenance cost? On the first reading, Addendum A3.4 puts the fully-seen state at
the Sloth attractor.

**Q11 (§1, §4). Deliver the ISA-95 mapping or withdraw the claim — and is ISA-84 what you actually
mean?** No Purdue level number appears anywhere in the document, and §4.1–4.2's veto-flows-upward
is the *inverse* of Purdue's control hierarchy. What you are describing — a low layer independent
of the control stack that can trip it — is the safety-instrumented-system architecture, which
would make the section more correct, not less.

**Q12 (§10). Is the EXECUTE reassignment deliberate?** In PackML, EXECUTE is the producing state;
§10 uses it for REM-dream training and introduces PRODUCING alongside. Defensible as a modelling
choice, costly as a silent one — a reader from the standards world stops there.

### One last thing, offered as a favour rather than a criticism

**§16.1's population percentages.** They are self-tagged as "speculative and provocative", and
they are the only place in the corpus where the framework grades *people* rather than systems.
They are also, for that reason, the sentence most likely to be quoted against everything else you
have written — including §9, which is a tool for protecting people, and §15, whose whole stance is
that a condition is "a routing error, not a deficiency of the person". The percentages cost you
that stance and buy nothing that the L0–L6 ladder does not already say. I would cut them.

---

## Closing

Three things, in the order I would do them.

**First, settle Q1**, because §3's empirical claim cannot be published either way until you know
which scale the cited number is on, and the answer costs an email.

**Second, fix prereg-01's magnitude bar (D1) and add the manipulation check (D2) before filing.**
As registered, the study is arithmetically incapable of supporting its own hypothesis at any
effect size it is powered to detect, and its expected null would be uninterpretable. Both fixes
are a paragraph each. Everything else in that document is good enough to leave alone.

**Third, write the §9.1 protocol.** It is your strongest claim, it is the cheapest to test, it is
untouched by every objection in this brief, and it is the only part of the framework that would
still be worth having if all the rest turned out to be wrong. You have already written two
pre-registrations of a quality most theorists never reach. Point the third one at the thing you
are actually right about.

---

*Every numeric claim above was recomputed rather than quoted; the scripts are one-liners and are
reproduced inline where they matter. Two claims I intended to make were refuted by running them —
the permutation-power objection to prereg-02 (§4.4, E3) and an earlier reading of §8.5 — and both
are recorded as refuted rather than removed. Section numbers refer to `ass-os-regulus.txt` and
`regulus-addendum-sins.txt` as supplied.*

**Provenance.** V>> (author), with Claude Opus 5 1M (`claude-opus-5[1m]`) as the analysing model.
Building on `ERRATA.md` (E1, E2) and `analysis/00-catch-up-and-appraisal.md` (the five component
scores and the nine-citation audit), neither of which is re-derived here.
