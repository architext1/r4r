# Equation audit — the arithmetic is sound

**Headline: about twenty-five checkable quantities, and no new errors.**

Two transcription errors in this specification were found by running the arithmetic rather
than reading it, which raised a fair question — if two were hiding in plain sight, how many
more are there? This is the systematic sweep. The answer is none, and that is worth stating
as clearly as a list of faults would have been.

The known problems are the exceptions, not the rule. The prime spine is exact, every derived
constant recomputes to its printed value, and the golden-ratio algebra holds throughout.

---

## VERIFIED

### §2 — the Prime Recursion Spine

The claim is that each term is the *n*th prime where *n* is the previous term. Checked term
by term:

| step | computed | printed | |
|---|---|---|---|
| prime(1) | 2 | 2 | ✓ |
| prime(2) | 3 | 3 | ✓ |
| prime(3) | 5 | 5 | ✓ |
| prime(5) | 11 | 11 | ✓ |
| prime(11) | 31 | 31 | ✓ |
| prime(31) | 127 | 127 | ✓ |
| prime(127) | 709 | 709 | ✓ |

**Exact, all seven steps.** `{1, 2, 3, 5, 11, 31, 127, 709}` is correct as printed.

### §3.2 — the derived constants

Each recomputed from its own stated derivation, not copied:

| constant | derivation | computed | printed | |
|---|---|---|---|---|
| α | φ + 2 | 3.618034 | 3.618 | ✓ |
| β | κ\*³ | 0.236068 | 0.2360 | ✓ |
| γ | κ\*⁵ | 0.090170 | 0.0902 | ✓ |
| ε_φ | 1/φ | 0.618034 | 0.6180 | ✓ |
| μ_φ | φ | 1.618034 | 1.6180 | ✓ |
| v | 1/√(φ·1/φ) | 1.000000 | 1.0000 | ✓ |
| E_min | 1/2φ³ | 0.118034 | 0.1180 | ✓ |
| \|δΨ_crit\| | κ\*² | 0.381966 | 0.3820 | ✓ |

**All eight.** Every printed value is its derivation correctly evaluated and rounded. No
hand-tuning, exactly as §3.2 claims.

### §3.1 — the identities, excluding the one already in ERRATA

| identity | | |
|---|---|---|
| φ·κ\* = 1 | 1.000000000 | ✓ |
| κ\* = φ − 1 | 0.618033989 | ✓ |
| κ\*² = 1 − κ\* | 0.381966011 | ✓ |
| κ\*/(1−κ\*) = φ | 1.618033989 | ✓ |

All exact to floating-point precision.

### §3.3 — the basin

`(κ*⁵, 1 − κ*⁵)` = **(0.090170, 0.909830)**, matching the stated ≈ (0.09, 0.91). ✓

### §3.5 — the FIFO algebra

Three expressions the section claims are equal:

```
phi/(1+phi) = 0.618033989
phi/phi**2  = 0.618033989
1/phi       = 0.618033989
```

**Equal.** And "keep 61.8%, release 38.2%" is 61.8 / 38.2 exactly. ✓

### §8.3 — the binding energy

`E_min = κ*²/(2φ)` and `1/(2φ³)` are the same number, **0.118034**, to floating-point
precision. The claim that 88.2% is freed follows: `1 − 0.1180 = 0.8820`. ✓

### §2.3 — the Mersenne seam

`2¹¹ − 1 = 2047 = 23 × 89`, not prime. Correct, and correctly described as a seam — it is
the point where the pattern breaks, which is the section's own point. ✓

### Addendum A — directional completeness

A4.1 claims the seven geometries cover all deformation directions. Structurally they do:
three dual pairs on three axes — activation (Wrath / Sloth), intake (Gluttony / Greed),
reference (Envy / Pride) — plus Lust as self-dual, being a coupling failure rather than a
position. Seven, with no direction left unoccupied. ✓

---

## CONFIRMED INDEPENDENTLY (already reported elsewhere)

### §3.6 — the coupling repels above the attractor

The brief reports this; it reproduces. The claim is that the first zero of `sin(φπx)` at
x = 1/φ is where coupling vanishes, which is true —

```
sin(phi*pi*(1/phi)) = 5.67e-16      # zero
```

— but the sign either side is what matters:

```
x = 0.58  (below)  sin = +0.1921    attracts
x = 0.65  (above)  sin = -0.1618    repels
```

So the coupling term does not merely switch off at 1/φ, it **reverses**. Two agents
separated by more than 0.618 are pushed further apart by the very term meant to
synchronise them.

### §2.1 — the growth ratios are not monotone

The section describes the ratios as accelerating. Computed:

```
2.0000, 1.5000, 1.6667, 2.2000, 2.8182, 4.0968, 5.5827
```

The second is **lower** than the first. Acceleration holds from L1 onward, not from the
start. A wording fix, not a mathematical one.

---

## NOT AN ERROR — recorded so nobody re-reports it

β prints as `0.2360` against a computed `0.236068`, a difference of 6.8 × 10⁻⁵. That is the
specification printing to four significant figures, not a discrepancy. The same applies to
every other constant in §3.2. **Last-digit rounding is not an erratum** and none of these
should be raised as one.

---

## UNCHECKABLE from the documents alone

- **§6 Ψ-Maxwell** — internally consistent as written, but the field equations are an
  analogy to Maxwell rather than a derivation from anything measurable here. Nothing to
  compute against. Note also that §6 carries no Regulus marker while §7 depends on it
  entirely, so the base/extension boundary is genuinely undrawn there.
- **§7 the love equations** — dimensionally coherent and each does what its prose says, but
  the quantities (Ψ, δΨ, k_c) have no stated units or measurement procedure, so the
  equations cannot be checked numerically. The document is candid about this, calling them
  *"formal metaphor that encodes subjective experience in mathematical structure."*
- **§12 the eight fault mappings** — a taxonomy rather than a calculation. They partition
  the space consistently; whether they *predict* rather than *re-describe* is an empirical
  question, not an arithmetic one.
- **Every cited empirical value** — the HeartMath range, the Type A risk figures, the
  interoception dimensions. These need the original papers, which are outside this corpus.

---

## Judgement

**The specification's arithmetic is broadly sound.** Roughly twenty-five independently
checkable quantities, and every one of them holds. The prime spine — the most obviously
checkable claim and the easiest place to have slipped — is exact across all seven steps.

That has a bearing on how the known problems should be read. The two errata are
*transcription* slips in a document whose mathematics is otherwise clean: a transposed pair
of terms and a flipped sign, both in §3, both invisible to reading and both obvious to
computation. They are typing errors, not thinking errors, and the surrounding work
demonstrates that.

The genuine problems in this corpus are not arithmetic at all. They are the §3.4 scale
mismatch, where a measured odds is compared against a constant defined as a fraction, and
the two methodological defects in the pre-registrations. Those matter far more than
anything a calculator can find, and none of them would have been caught by this sweep.

---

*Framework: Thomas Frumkin (@teslasolar), Konomi Systems. This audit: V>>, with Claude Opus 5.
Every figure reproduces from the expressions shown; re-run them rather than trusting them.*
