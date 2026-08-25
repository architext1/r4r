# Two corrections, before either pre-registration is filed

Both protocols are described as ready to file. Each has one defect that would waste the
study. Neither is a design flaw — the designs are the strongest methodology in this corpus —
and neither protocol is edited here. What follows is the arithmetic and the recommended
replacement text; the registered values are the author's to set.

**A note on trust.** The D1 figure below is the third one produced for this defect tonight.
An earlier review said "8.1 standard errors"; a first check said 2.77×; this says 3.92× and
11.4 standard errors. The first two were derived from a summary. This one is derived from the
protocol's own sentence, and the derivation is shown line by line precisely so you can check
it rather than take it. If it is wrong, the working is right there to be attacked.

---

## D1 — prereg-01: the bar is an individual-level quantity, the test estimates a mean

### What is registered

Two clauses, and they are on different scales.

**The bar** (§ Analysis Plan):

> *"The registered bar is that the active-minus-sham contrast must **exceed a pre-registered
> drift ceiling**, defined as **1.96 × the within-participant SD of the sham-only group's
> session-to-session ΔH**."*

**The power calculation** (§ Sample-size rationale):

> *"Alpha: 0.05 (two-tailed). Power: 0.80. Target effect: Cohen's d = 0.5 on the paired
> contrast → N ≈ 34."*

### The arithmetic

Both the sham-only ΔH and the active-minus-sham contrast are differences of two sessions, so
both carry the same standard deviation. Call it **S**.

```
bar as an effect size    = 1.96·S / S            = 1.96
powered effect size                              = 0.50
ratio                                            = 3.92x
```

That understates it, though, because it compares two things that are not comparable. The bar
is built from **S**, the spread of *individual* session-to-session drift. The test estimates
a **mean**, whose precision is the standard error:

```
SE(mean) = S / sqrt(34) = 0.1715 S
bar      = 1.96 S       = 11.4 standard errors of the mean
```

**The bar sits 11.4 standard errors from zero in a study powered to resolve 0.5.**

### What that does

```python
from statistics import NormalDist
S_E = 1/34**0.5
print(1 - NormalDist().cdf((1.96 - 0.5)/S_E))    # 0.0
```

A true effect of exactly the size the study is designed to detect has, to floating-point
precision, **no chance of clearing the bar**. The protocol would report it as *"within
measurement drift"* and publish it as a refutation.

This is the reverse of conservative. It reads as caution — a high bar sounds rigorous — but
a bar that a real effect cannot clear does not protect against false positives, it
guarantees a false negative.

### The defect is real, and it is a category error rather than a number

A 95% ceiling on *individual* drift is a perfectly sensible thing to want. It answers "could
this participant's change be drift?" But the primary endpoint is a **group mean**, and the
question there is "could this *average* change be drift?" — which is a bound on the mean,
narrower by √N.

### Three ways to fix it

| | Bar | Rationale | Consequence |
|---|---|---|---|
| **A** | **0.50 S** | Set at the powered effect size | Coherent with the power calculation; a detectable effect can clear it |
| **B** | **0.336 S** | `1.96 × SE(mean)` = a conventional 95% bound on the mean | The bar the current sentence was probably reaching for; strictly weaker than A |
| **C** | **1.96 S**, unchanged | Keep the individual-drift ceiling as written | **No N reaches 80% power.** The ceiling is fixed in individual-drift SD and does not shrink as N grows, so power against it *decreases* in N — at most 7.9%, at N = 1 |

**Recommended: A.** It preserves the protocol's stated intent — that significance alone is
not enough, the effect must also be big enough to matter — while setting "big enough" at
something the study can actually resolve. B is defensible but is close to the significance
test it is meant to supplement, so it adds little.

**C is not a bigger study — it is an unpowered one, and the earlier "N = 523" here was
wrong.** A ceiling fixed at 1.96 × the individual-drift SD does not shrink as N grows, while
the mean it is compared against stays at the registered 0.50 S. Power against that ceiling is
therefore *decreasing* in N, reaching at most 7.9% at N = 1, and the true effect required for
80% power falls only to 1.96 S in the limit — never toward 0.50 S. Option C is reachable only
by re-designing the study around a target effect above 1.96 S, which is a different study
rather than a larger one.

The withdrawn figure came from `34 × (1.96/0.50)² = 522.4576`, ceiled to 523. That scaling
answers a different question, and it multiplies the whole anchor when only one part of it may
scale: 34 is a composite of 31.395519 (normal) + 1.971610 (Guenther z²/2) + 0.632871
(ceiling), so the spurious total is 38.0984 — exactly the gap between 522.4576 and the 484.3592
that the substituted question actually yields. If the intent was to report the cost of detecting
a much smaller effect, the figure is **485** (exact one-sample t; the normal approximation gives
483) and it must carry the effect size it belongs to, d = 0.1276 — a quantity with no referent
anywhere in the registered protocol.

### Replacement text

> **The magnitude bar (noise floor), not just significance.** Statistical significance of the
> paired contrast is necessary but not sufficient. The registered bar is that the
> **mean** active-minus-sham contrast must exceed **0.50 × the within-participant SD of the
> sham-only group's session-to-session ΔH** — the effect size this study is powered to
> detect. A contrast that is "significant" but smaller than this is reported as **within
> measurement drift** and does not count as support for H1. This bar is fixed before
> unblinding.
>
> *Note on scale: the bar is a bound on the group mean, not on individual session-to-session
> drift. A 1.96 × SD ceiling would be the latter, and at N = 34 it sits 11.4 standard errors
> from zero — unreachable by any effect this design can detect.*

---

## E1 — prereg-02: the H1b null destroys the structure it should preserve

### What is registered

H1b (§ Hypotheses):

> *"Day-to-day HRV of geographically co-exposed but socially unrelated participants
> **correlates above the level expected under day-permutation**."*

The other confirmatory test, in the same document, registers something different:

> *"the storm-minus-quiet coherence contrast recomputed on ≥ 1000 **circularly-shifted**
> /phase-randomised Kp series"*

So the correct null is already in the protocol. It is simply not applied to H1b.

### Why day-permutation is the wrong null

HRV series are temporally autocorrelated — today resembles yesterday. Shuffling days
independently destroys that autocorrelation, so the permuted series are *less* structured
than real data. The resulting null distribution is too narrow, and the observed statistic —
computed on data that *does* have autocorrelation — looks extreme by comparison.

A circular shift moves each series bodily in time. It destroys the *alignment* between
participants, which is what H1b tests, while preserving each participant's own
autocorrelation, which is not.

### Measured

Simulated under H0 — twelve independent AR(1) participants, ninety days, φ = 0.6, no shared
driver at all, so every rejection is a false positive. 300 simulations, 400 permutations
each, α = 0.05, statistic = mean pairwise Spearman correlation.

| null | false-positive rate | vs nominal 5% |
|---|---|---|
| **day-permutation** (as registered) | **13.0%** | ≈ 6 SE above — unambiguous |
| **circular shift** (proposed) | **7.0%** | ≈ 1.6 SE above — much better |

The registered null rejects a true null **more than twice as often as it claims to**. On
these parameters H1b is not a 5% test, it is a 13% test.

### An honest caveat on the fix

The circular shift is a large improvement and it is not provably perfect. At 7.0% over 300
simulations the standard error is 1.26%, so the result is consistent with correct sizing but
does not demonstrate it — a residual inflation of one or two points cannot be ruled out from
this run. Two things would settle it: more simulations, and parameters taken from pilot data
rather than assumed.

**The parameters here are mine, not the protocol's.** The exact false-positive rate depends
on the true autocorrelation of daily HRV, which the protocol does not state. The
*direction* and rough magnitude are robust — any positive autocorrelation makes
day-permutation anti-conservative — but the specific 13.0% should not be quoted as a
property of the study.

### Replacement text

> **H1b (inter-participant synchronisation).** Day-to-day HRV of geographically co-exposed
> but socially unrelated participants correlates above the level expected under a
> **per-participant circular-shift null**, computed as follows: for each of ≥ 1000
> permutations, each participant's daily series is independently circularly shifted by an
> offset drawn uniformly from 1 … (n_days − 1); the test statistic (mean pairwise Spearman
> correlation across participants) is recomputed on the shifted set; the observed
> statistic's percentile within that distribution is the inferential quantity. The shift
> preserves each participant's own temporal autocorrelation while destroying inter-participant
> alignment, which is the structure under test. A day-permutation null is **not** used here:
> it destroys autocorrelation as well as alignment, yielding a null distribution narrower
> than the data and a test that over-rejects.

### What it costs

A correctly-sized null is less likely to reject, so some power is given up. That is the
point — the power the day-permutation null appeared to have was not real, it was the
over-rejection. Quantifying the loss needs a specified alternative, which the protocol does
not give for H1b; if you fix an expected synchronisation effect, this can be simulated the
same way.

---

## What neither review caught

**In prereg-01**, the bar and the power calculation are in different sections — the bar in
the Analysis Plan, the power in the Sample-size rationale. Nothing in either points at the
other. Whatever bar is chosen, a single sentence in the Analysis Plan stating its
relationship to the powered effect size would make a recurrence impossible.

**In prereg-02**, the same document uses two different nulls for two confirmatory tests
without saying why. Even after the fix, one line explaining that both now use circular
shifts, and why that is the right choice for autocorrelated series, is worth adding — it is
the kind of thing an OSF reviewer asks about.

---

*Framework: Thomas Frumkin (@teslasolar), Konomi Systems. These corrections: V>>, with Claude
Opus 5. Every figure reproduces from the code shown; the simulation seed is 20260822.*
