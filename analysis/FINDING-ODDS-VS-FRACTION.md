# §3.4 measures the right number on the wrong scale

**Verdict: the scale error is confirmed. What it points at instead is not.**

§3.4 is the specification's single piece of empirical confirmation — the place where a
measured quantity is claimed to match κ\* = 1/φ. This note tests that claim and finds it
does not hold, using only definitions already present in this corpus. It then tests the
follow-on suggestion — that the data actually lands on κ\*² — and finds that one
**under-determined**, for the same reason the appraisal already gives about κ\* itself.

Both halves matter. The first is a correction. The second is a caution against replacing
one over-claim with another.

---

## 1. What §3.4 claims

> *"HeartMath Institute measured HRV coherence ratio at κ ≈ 0.6–0.65 in the coherent
> (positive emotion) state. This equals 1/φ within measurement error."* — §3.4

The claim needs the measured coherence ratio to be the same *kind of quantity* as κ. κ is a
retention **fraction** — §3.5 is explicit that it means *"keep 61.8%, release 38.2%"*.

## 2. What the coherence ratio actually is

From `experiments/02-prereg-geomagnetic-hrv.md`, defining the primary outcome *"following
the HeartMath operationalisation cited by Regulus"*:

> **coherence ratio = peak-band power / (total power in 0.0033–0.40 Hz − peak-band power)**

The denominator is **total minus peak**, not total. That is an **odds**, not a fraction.

This is the crux, and it is settled inside the corpus rather than by appeal to outside
literature. The pre-registration and the specification are describing the same measurement,
and the pre-registration writes the formula out.

## 3. The specification already knows the difference

§3.5 handles both scales correctly, in one line:

> *"optimal retention rate κ satisfies κ/(1−κ) = φ. Solving: κ = φ/(1+φ) = 1/φ = κ\*"*

Read that carefully. `κ/(1−κ)` is the keep-to-drop **odds**, and §3.5 sets it to **φ =
1.618**. The **fraction** that produces is **1/φ = 0.618**.

So the framework's own algebra says:

| Scale | Golden value |
|---|---|
| odds — keep divided by drop | **φ = 1.618034** |
| fraction — keep divided by total | **1/φ = 0.618034** |

§3.4 then takes a measurement that is an *odds* and compares it to the *fraction*. The two
sections are three lines apart and use opposite conventions.

## 4. What follows, arithmetically

For §3.4 to hold on its own terms, HeartMath would have to be measuring a coherence **odds**
of **1.618**. The cited window is 0.60–0.65 — about **2.6× lower**.

Converting the cited window to the scale κ actually lives on, with
`fraction = odds / (1 + odds)`:

| odds | fraction |
|---|---|
| 0.60 | 0.375000 |
| 0.65 | 0.393939 |

```python
phi = (1 + 5**0.5) / 2
f = lambda o: o / (1 + o)
print(f(0.60), f(0.65))        # 0.375 0.3939393939393939
print(f(phi))                  # 0.6180339887498949  == 1/phi
```

The converted window is **[0.3750, 0.3939]**, and **κ\* = 0.618034 is not in it.**

Note the identity in the third line: **φ as an odds is exactly κ\* as a fraction.** That is
the whole trap. φ and 1/φ are reciprocals, so a fraction-versus-odds confusion produces two
numbers that look like the same golden constant wearing different hats. Nothing in the
printed numerals flags the error, which is presumably why it has stood.

## 5. Where this leaves κ\*

The honest statement is narrow and it is not "the framework is wrong":

**§3.4 does not confirm κ\* = 1/φ, because the quantity it cites is not on the same scale
as κ.** It is a scale mismatch, not a refutation of the constant. κ\* may still be the right
attractor; §3.4 simply is not evidence for it.

This matters because §3.4 is the *only* place in the specification where the constant meets
data. `analysis/00-catch-up-and-appraisal.md` already scores the κ\* = 1/φ identification
8/10 on the bullshit meter for being under-determined by its measurement window. This
finding is worse than that: it is not that the measurement is too coarse to distinguish
0.618 from 0.625, it is that the measurement is not of that quantity at all.

## 6. And the part that does NOT hold

The obvious next thought is that the converted window contains **κ\*² = 0.381966**, which is
not an arbitrary number here — §8.2 makes it the binding threshold `|δΨ_crit|`. That would be
a striking result: the cardiac data pointing at the framework's *binding* constant rather
than its *attractor*.

**It does not survive the same scrutiny that killed the original claim.** The converted
window is [0.3750, 0.3939], only 0.0189 wide, and it contains more than one candidate:

| candidate | value | in window |
|---|---|---|
| 1/e | 0.367879 | no |
| **3/8** | **0.375000** | **yes — sitting exactly on the lower edge** |
| **κ\*² = 1 − κ\*** | **0.381966** | **yes** |
| 2/5 | 0.400000 | no |

κ\*² sits 0.0025 from the window's midpoint, which is a good fit. But 3/8 is a plain
eighth landing precisely on the boundary, and nothing in the cited data distinguishes them.

This is the *same* objection the appraisal makes about κ\* — a window wider than the gaps
between its candidates — reappearing one constant down. Replacing "the data confirms κ\*"
with "the data confirms κ\*²" would repeat the original error with a different number.

**The correct statement is that the converted window is consistent with κ\*² and does not
select it.**

## 7. What would settle it

One measurement, and it is cheap because the machinery is already specified in
`experiments/02-prereg-geomagnetic-hrv.md`:

**Report the coherence measure as a fraction — peak-band power over total power — rather
than as an odds, with enough resolution to separate 0.375 from 0.382.** That is a gap of
0.007 against candidates in a 0.019 window, so it needs a precision the current
operationalisation does not claim, but it is a resolution question rather than a new
instrument.

Two secondary asks that cost nothing:

1. **Cite the specific HeartMath measurement** behind "0.6–0.65". §3.4 gives no reference,
   and the scale question cannot be closed against an uncited range.
2. **State which scale each κ-valued claim in the specification is on.** §3.5 does this
   correctly and §3.4 does not; a single convention line at the top of §3 would prevent the
   whole class of error.

## 8. Limits of this note

- **The load-bearing dependency has been checked against the published source, and it
  holds.** Section 2 argued from the corpus's own operational definition, in
  `02-prereg-geomagnetic-hrv.md`, and flagged the obvious way that could go wrong: if
  HeartMath's published definition were a fraction rather than an odds, section 2 would
  fail and this finding would collapse. It is not a fraction. McCraty & Zayas (2014),
  *Frontiers in Psychology* **5**:1090, doi:[10.3389/fpsyg.2014.01090](https://doi.org/10.3389/fpsyg.2014.01090),
  quoting McCraty & Childre (2010) at p.14:

  > "Coherence is assessed by identifying the maximum peak in the 0.04–0.26 Hz range of the
  > HRV power spectrum, calculating the integral in a window 0.03 Hz wide centered on the
  > highest peak in that region, and then calculating the total power of the entire
  > spectrum. **The coherence ratio is formulated as: [Peak Power/(Total Power − Peak
  > Power)]**"

  The denominator is total *minus* peak, which is what makes it an odds. The published
  definition and the pre-registration's operationalisation agree, so the scale mismatch in
  §3.4 is confirmed against the primary literature and not only against this corpus.

- **What is still open is the window, not the scale.** §3.4 quotes "0.6–0.65" with no
  attribution, so both which measurement it came from and its own precision are unknown,
  and every interval derived from it above inherits that. The secondary ask in §7 — cite
  the specific HeartMath measurement — is now the only thing standing between this note
  and a closed question.
- Sections 4 and 6 are arithmetic and reproduce from the code shown. Sections 5 and 7 are
  interpretation, and are marked as such.

## 9. What this does not touch

§7 (the love equations), §8 (Ŝ) and §9 (M̂) do not depend on the constant being 1/φ
specifically, and none of them depend on §3.4. The bilateral-modification criterion — *who in
this system is unchanged?* — stands whatever the cardiac number turns out to be. This finding
is confined to the one section that claims empirical confirmation.

---

*Framework: Thomas Frumkin (@teslasolar), Konomi Systems. This note: V>>, with Claude Opus 5.
Every figure above reproduces from the code shown; re-run it rather than trusting it.*
