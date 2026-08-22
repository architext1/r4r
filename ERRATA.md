# Errata — ASS-OS / Regulus specification

Two transcription errors in the ASS-OS / Regulus specification, both found by implementing the
equations rather than by reading them. Neither is a flaw in the reasoning. Both are the
kind of slip that only surfaces when somebody tries to run the maths, and both will stop
the next person who does — which is the person the specification most wants.

Each is verified below by arithmetic you can re-run in a line of Python.

**This file is the long version, on purpose.** The second correction needs a stability
proof to be worth anything, and a proof belongs where somebody has come looking for one —
not in a code comment and not in the middle of an explainer. So the proof lives here in
full, and everything else points at it: `docs/assets/app.js` carries a short note at
`drift()`, and the R4R explainer shows the two lines in a table and links back. If you
want the working, you are in the right place. If you want the summary, the site has it.

---

## E1 — §3.1, the Fibonacci-in-exponents identity has its terms transposed

**Printed**

```
κ*ⁿ = κ*ⁿ⁻¹ − κ*ⁿ⁻²
```

**Should be**

```
κ*ⁿ = κ*ⁿ⁻² − κ*ⁿ⁻¹
```

**Why**

The printed order returns the correct magnitude with the wrong sign at every n:

| n | κ\*ⁿ | printed: κ\*ⁿ⁻¹ − κ\*ⁿ⁻² | corrected: κ\*ⁿ⁻² − κ\*ⁿ⁻¹ |
|---|---|---|---|
| 2 | 0.381966011 | −0.381966011 | +0.381966011 |
| 3 | 0.236067977 | −0.236067977 | +0.236067977 |
| 4 | 0.145898034 | −0.145898034 | +0.145898034 |
| 5 | 0.090169944 | −0.090169944 | +0.090169944 |

```python
k = (5**0.5 - 1) / 2
for n in (2, 3, 4, 5):
    print(n, k**n, k**(n-1) - k**(n-2), k**(n-2) - k**(n-1))
```

**Why it is certainly a typo and not a misunderstanding**

§3.2 already lists the same quantities as positive — β = κ\*³ = 0.2360 and
γ = κ\*⁵ = 0.0902. The document is internally consistent everywhere except this one line,
so two terms need swapping and nothing downstream is affected.

---

## E2 — §3.3, the dynamical equation's sign contradicts its own stability analysis

**Printed**

```
∂κ/∂t = α(κ − 1/φ)(1 − κ)κ + β∇²κ + γξ(t)
```

**Should be**

```
∂κ/∂t = α(1/φ − κ)(1 − κ)κ + β∇²κ + γξ(t)
```

§3.3 states three fixed points: κ = 0 unstable, κ = 1/φ **stable**, κ = 1 unstable. With
the bracket as printed, all three are false. Four independent arguments follow, and they
agree. Throughout, κ\* = 1/φ = 0.6180339887498949, and α > 0 is a rate constant —
`docs/assets/app.js` sets it to φ + 2 — so it scales the speed of everything below and
never flips a sign.

### 1. The direct argument

Take a κ just above the attractor, say 0.7. Then `(κ − 1/φ) > 0`, `(1 − κ) > 0` and
`κ > 0`, so the whole product is positive, `∂κ/∂t > 0`, and the trajectory moves *further
away*. The attractor repels. By the same argument κ = 0 and κ = 1 become attracting: every
starting point runs to whichever end it began nearest. This is the opposite of what the
section says three lines earlier.

### 2. The Lyapunov argument, and why it does not turn on V̇

This is the part worth being careful about, because the obvious move proves nothing.

For any drift of the form `∂κ/∂t = α·g(κ)`, take the standard candidate

```
L(κ) = −α ∫ g(x) dx        so that        L′(κ) = −α·g(κ)
```

Then along a trajectory

```
L̇ = L′(κ)·κ̇ = (−α·g)(α·g) = −α²·g² ≤ 0
```

**`L̇ ≤ 0` holds for either sign of the bracket.** It is a property of the construction,
not evidence about the fixed point. So §3.3's statement that V decreases is true as
printed and true as corrected, and on its own it settles nothing. The sign lives one
derivative further up.

### 3. The curvature at κ\*, which is where the two forms part company

Write the printed bracket as `f(κ) = (κ − κ*)(1 − κ)κ`. Its derivative at the fixed point
needs no expansion: with `f = (κ − κ*)·h(κ)` and `h(κ) = (1 − κ)κ`, the product rule gives
`f′ = h + (κ − κ*)h′`, and the second term vanishes at κ = κ\*. So

```
f′(κ*) = h(κ*) = (1 − κ*)κ* = 0.2360679774997898
```

Now compare the two forms. The printed drift is `g = f`; the corrected drift is `g = −f`.
Both give the same L̇ ≤ 0. They differ entirely in curvature:

| | drift g(κ) | Lyapunov L = −α∫g | L″(κ\*) | κ\* is a… | behaviour of a decreasing L |
|---|---|---|---|---|---|
| **Printed** | (κ − κ\*)(1 − κ)κ | −α∫f | **−0.2360679774997898** | local **maximum** | rolls off it — κ\* repels |
| **Corrected** | (1/φ − κ)(1 − κ)κ | +α∫f | **+0.2360679774997898** | local **minimum** | settles into it — κ\* attracts |

A system sitting at a maximum of a quantity that only ever decreases cannot stay there.
A system in a basin of one can do nothing else. That is the whole proof, and the printed
form lands on the wrong row of it.

### 4. One number, four ways

`f′(κ*)` is the hinge, so it is worth watching it arrive by four routes that share no
working. Everything below follows from the single exact identity `κ*² = 1 − κ*`.

| Route | Expression | Value |
|---|---|---|
| Product rule at the fixed point | (1 − κ\*)κ\* | 0.2360679774997898 |
| Expanded derivative, evaluated at κ\* | 2κ\* − 3κ\*² − κ\* + 2κ\*² | 0.23606797749978958 |
| Substituting 1 − κ\* = κ\*² | κ\*³ | 0.23606797749978975 |
| Substituting κ\*² = 1 − κ\* the other way | 2κ\* − 1 | 0.2360679774997898 |

The four differ only in the last two digits, which is floating-point noise and not
disagreement. Note that this number is β itself — §3.2's `β = κ*³ = 0.2360` — so the
curvature at the attractor is one of the constants the specification already carries.

```python
k = (5**0.5 - 1) / 2
print((1 - k)*k, 2*k - 3*k*k - k + 2*k*k, k**3, 2*k - 1)
```

### 5. Integrate it and watch

The arguments above are analytic. This one just runs the thing, from four starting values —
including both endpoints of the basin §3.3 states, (κ\*⁵, 1 − κ\*⁵) ≈ (0.0902, 0.9098).

```python
k = (5**0.5 - 1) / 2
a = (1 + 5**0.5) / 2 + 2               # α = φ + 2 = 3.618033988749895

def run(x, sign):                      # sign=+1 printed, sign=-1 corrected
    for _ in range(4000):
        x += a * (sign * (x - k)) * (1 - x) * x * 0.008
        x = min(max(x, 1e-9), 1 - 1e-9)
    return x

for x0 in (0.0902, 0.30, 0.70, 0.9098):
    print(x0, run(x0, +1), run(x0, -1))
```

| starting κ | printed form settles at | corrected form settles at |
|---|---|---|
| 0.0902 | 0.000000 | 0.618034 |
| 0.3000 | 0.000000 | 0.618034 |
| 0.7000 | 1.000000 | 0.618034 |
| 0.9098 | 1.000000 | 0.618034 |

The printed form runs to the two endpoints §3.3 calls unstable. The corrected form arrives
at 1/φ from every start, including both edges of the stated basin.

### What the correction restores

Negate the bracket and every claim in §3.3 holds exactly as written: κ\* attracting, 0 and
1 repelling, and the basin of attraction (κ\*⁵, 1 − κ\*⁵) ≈ (0.09, 0.91). Nothing else in
the section needs touching, which is the signature of a transcription slip rather than a
mistake in the thinking — one operator swapped, and a page that contradicted itself becomes
a page that does not.

One honest note on the basin. For the deterministic part alone, every κ strictly between 0
and 1 runs to κ\*, so the stated basin is narrower than the drift term by itself requires.
The likeliest reading is that (κ\*⁵, 1 − κ\*⁵) is the basin that survives the noise term
γξ(t), which can push a trajectory started near an edge over it. That is an inference about
intent, not something §3.3 says, and it is flagged as an inference here rather than
smoothed over.

### Where this is already implemented

`docs/assets/app.js` integrates the corrected form and points here. The live instrument on
the R4R explainer is therefore showing the intended dynamics, not the printed ones.

---

## Not an erratum, but the open question

κ\* = 1/φ = 0.6180 is presented in §3.4 as confirmed by HeartMath's coherence measurements,
which sit in a 0.60–0.65 window. That window also contains 5/8 = 0.625 and plain 0.6.

```
|1/φ − 5/8| = 0.0069660112501050975      window width = 0.05
```

The gap being claimed is roughly a seventh of the measurement window — 0.139 of it — so
nothing in the cited data can distinguish the three candidates. That makes φ **chosen**
rather than **confirmed** at present. It is not an error: the identity κ\*² = 1 − κ\* is
exact and the algebra around it is clean. But the empirical claim in §3.4 is stronger than
the measurement supports, and `analysis/00-catch-up-and-appraisal.md` scores that specific
claim 8/10 on its bullshit meter for exactly this reason.

Worth being clear about what this does *not* touch: §7 (the love equations), §8 (Ŝ) and §9
(M̂) do not depend on the constant being 1/φ specifically. You could drop the golden ratio
altogether and the bilateral-modification criterion — *who in this system is unchanged?* —
would stand exactly as it does now.
