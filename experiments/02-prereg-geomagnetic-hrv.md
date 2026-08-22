# OSF Pre-Registration

> ### ⚠ Reviewer note — read before filing
>
> An independent methodological review of this protocol (`analysis/REGULUS-BRIEF.md`,
> finding **E1**) reports that the **H1b** null is too narrow and over-rejects.
>
> The day-shuffle used for H1b destroys the temporal autocorrelation the data actually
> has, so the resulting null distribution is narrower than the truth and the test
> **false-positives at a measured 13.0% against a nominal 5%** (300 simulations,
> twelve independent AR(1) participants, ninety days, φ = 0.6 — parameters assumed, not
> the protocol's) — it is more than twice as likely to
> declare inter-participant synchronisation as the registered α implies.
>
> The correct null is **already registered in this same document**, for the other test:
> a per-participant circular shift, which preserves autocorrelation while destroying the
> alignment being tested. Applying it to H1b as well measures 7.0% on the same
> simulation — a large improvement, though at 300 runs that is consistent with correct
> sizing rather than proof of it. Procedure and replacement text in
> `analysis/PREREG-CORRECTIONS.md`.
>
> The H1b test is otherwise the harder-to-confound of the two signatures here and worth
> keeping. Only its null needs changing.
>
> *Note added by review; the protocol below is unchanged.*

## Study Information

### Title

Does human heart-rate-variability coherence differ between geomagnetically quiet and storm days? A prospective intensive-longitudinal test of the Regulus "Bus D" claim, with a phase-shuffled negative control and an inter-participant synchronisation test.

### Description

The Regulus / ASS-OS framework (§5.4, "Bus D — Magnetic") proposes that the human autonomic nervous system couples to the Earth's geomagnetic and Schumann-resonance environment — that the Earth-ionosphere cavity (7.83 Hz fundamental, sustained by global lightning) is a genuine "communication bus" to which human physiology entrains. Its cited empirical anchor is McCraty et al. 2017 (*IJERPH* 14(7):770), which reported significant correlations of group heart-rate-variability (HRV) with the planetary Kp/Ap indices, solar-wind variables, and Schumann-resonance power, plus multi-day inter-participant HRV synchronisation. That study is **correlational, HeartMath-funded, and used a small convenience sample**; the geomagnetic-biology literature more broadly is notorious for positive findings that do not replicate once shared seasonality and temporal autocorrelation are controlled.

This study is the falsification test the "quiet day vs storm day" contrast sets up directly: it asks whether an individual's HRV-coherence measurably differs between geomagnetically **quiet** days (planetary Kp ≤ 2) and **storm** days (Kp ≥ 5), by a margin that a **phase-shuffled negative-control exposure cannot reproduce**. Because geomagnetic exposure cannot be manipulated, the design is observational/quasi-experimental and the entire evidential weight rests on the controls: objective third-party exposure data locked before analysis, analyst blinding to day classification, explicit modelling of seasonality/behaviour, a permutation-based negative control, and a second, harder-to-confound signature — synchronisation of HRV between participants who never meet.

**Honest prior.** We expect the null or a very small effect. A quiet-vs-storm HRV difference that survives the negative control would be a genuinely surprising, publishable positive result; a difference that does *not* exceed the phase-shuffled null is the expected outcome and would indicate that any raw correlation is driven by seasonality/autocorrelation/behaviour rather than a geomagnetic "bus". The study is designed to be able to return that null cleanly.

### Hypotheses

- **H1 (Regulus / Bus D, directional).** Within participants, mean HRV-coherence on storm days (Kp ≥ 5) differs from quiet days (Kp ≤ 2) in a pre-registered direction (Regulus predicts geomagnetic activity perturbs autonomic balance; we register the directional prediction that coherence is **lower** on storm days, consistent with the framing that storm activity moves κ away from its optimum), and the magnitude of the storm-minus-quiet contrast **exceeds the 95th percentile of the phase-shuffled negative-control null distribution**.
- **H1b (inter-participant synchronisation).** Day-to-day HRV of geographically co-exposed but socially unrelated participants correlates above the level expected under day-permutation — i.e. strangers' autonomic states co-vary with the shared geomagnetic day, a signature local weather and individual behaviour cannot easily manufacture.
- **H0 (null / standard chronobiology).** The storm-minus-quiet HRV contrast does not exceed the phase-shuffled negative-control null, and inter-participant HRV correlation does not exceed the day-permutation null. Any apparent raw association is attributable to shared seasonality, temporal autocorrelation, weather, and behaviour.
- **Falsifier (stated up front).** If the observed storm-minus-quiet effect is ≤ the negative-control null (primary) **and** inter-participant synchronisation is ≤ the permutation null (secondary), the Bus D claim is not supported by this test — the "bus" is a metaphor rather than a measured channel.

## Design Plan

### Study type

Observational, prospective, intensive-longitudinal (daily-sampled) cohort. The independent variable (geomagnetic activity) is a natural exposure, not manipulated; causal-inference safeguards (blinding, negative control, pre-registered covariates and lag structure) substitute for randomisation.

### Blinding

- **Exposure classification is external and locked.** Daily Kp comes from NOAA/SWPC (planetary Kp, 3-hourly → daily aggregate); Schumann-power from a public feed (e.g. Tomsk State University / GCI magnetometer network). The quiet/storm classification rule is fixed in this registration and applied by a data manager who does not touch the HRV data.
- **Analyst-blind.** HRV recordings are computed into daily coherence values under arm-neutral date codes; the analyst who fits the models does not know which coded days are quiet vs storm until the analysis pipeline is locked and the code is broken by a third party.
- **Participant-blind to hypothesis-of-record.** Participants are told the study concerns "daily heart-rhythm patterns and the environment" and are **not** told the geomagnetic hypothesis or which days are geomagnetically active, to prevent expectancy-driven self-regulation (note: the Regulus addendum's "vagal counter-sequences" are exactly the kind of deliberate self-regulation that would confound this — participants must not be cued to deploy them on storm days).

### Is there a control / comparison condition?

Yes — three layers. (1) The **within-subject** quiet-vs-storm contrast (each participant is their own control across the exposure range). (2) A **phase-shuffled negative-control exposure**: the Kp time series is circularly time-shifted / phase-randomised (≥ 1000 permutations) and the entire analysis re-run to build the null distribution of the storm-minus-quiet effect under "no real coupling"; the real effect must beat this null. (3) A **day-permutation null** for the inter-participant synchronisation test.

### Study design

Each participant records a standardised morning resting HRV session daily for a fixed window of 60 consecutive days, timed (opportunistically or during solar-maximum months) to capture both quiet and storm days. The primary analytic unit is the participant-day. The exposure contrast is quiet (Kp ≤ 2) vs storm (Kp ≥ 5); intermediate days (2 < Kp < 5) are retained for the continuous dose-response secondary analysis but excluded from the primary categorical contrast. A pre-registered **lag structure** is tested (same-day, +1 day, and −1 day relative to the geomagnetic day, reflecting that autonomic effects reported in the literature are not strictly same-day); the same-day lag is primary, others exploratory.

### Randomization

Not applicable to the exposure (natural). Randomisation is used only for the negative control (random circular shifts / phase-randomisation seeds, pre-specified count ≥ 1000) and for the day-permutation null.

## Sampling Plan

### Existing data

No. Registration precedes data collection. Public geomagnetic/Schumann archives exist but the paired HRV data do not; the exposure series will be downloaded only after HRV collection windows are fixed, and classification is locked here.

### Data collection procedures

N = 40 healthy adults recruited from ≥ 2 geographically separated sites (to dissociate a genuinely global geomagnetic exposure from any single-site weather/behaviour artefact). Each records a 5-minute seated, paced-breathing-free resting HRV session every morning within a fixed 90-minute clock window, using a **research-validated chest-strap single-lead ECG** (e.g. Polar H10 with beat-to-beat RR export, or an ambulatory ECG) — **not** wrist PPG, whose high-frequency HRV fidelity is inadequate. Participants log wake time, prior-night sleep (device or diary), caffeine/alcohol, illness, exercise, and menstrual-cycle day where applicable; a wrist accelerometer captures pre-session activity. Local temperature, barometric pressure, and daylight length are pulled per site-day from public weather archives.

### Sample size

40 participants × 60 days = up to 2,400 participant-days. Inclusion of a participant-window requires ≥ 6 valid quiet days and ≥ 6 valid storm days within the window; windows are scheduled during elevated-activity months so that Kp ≥ 5 days (which occur several times per month near solar maximum) are captured. Target ≥ 30 participants meeting the quiet/storm minimums after attrition and data-quality exclusions.

### Sample-size rationale (power calculation)

The effect is expected to be small (published geomagnetic-HRV associations are r ≈ 0.1–0.2). Power derives from the intensive within-subject sampling, not from N alone. A linear mixed-effects model with ~12+ exposure-classified days per participant across ~30 participants yields > 0.8 power to detect a standardised within-subject storm-minus-quiet difference of d ≈ 0.25 at α = 0.05 (two-tailed), under a conservative intraclass correlation of 0.4 for repeated within-person HRV (estimated via simulation, script deposited with the registration). Critically, the **operative bar is not the nominal p-value but exceeding the phase-shuffled negative-control null** — the real storm-minus-quiet contrast must sit above the 95th percentile of the ≥ 1000-permutation null, which automatically absorbs autocorrelation-inflated false positives that a naive mixed model would pass.

### Stopping rule

Collection stops at the fixed 60-day window per participant; no interim analyses of the exposure-outcome association are performed (data-quality monitoring only). Analysis begins after all windows close and the pipeline is locked.

## Variables

### Manipulated / independent variables

None manipulated. **Exposure (natural):** daily geomagnetic activity, classified quiet (Kp ≤ 2) vs storm (Kp ≥ 5) from NOAA/SWPC planetary Kp; continuous daily Kp and daily Schumann-resonance power (μV²/Hz at the 7.83 Hz mode) as secondary continuous exposures.

### Measured / dependent variables

**Primary:** daily HRV-coherence, defined operationally below. **Secondary HRV:** RMSSD, HF power (0.15–0.40 Hz), LF power (0.04–0.15 Hz), and the peak frequency of the LF band — reported FDR-corrected and labelled exploratory. **Covariates:** sleep duration, prior-day activity (accelerometer counts), caffeine/alcohol, illness flag, site, weekday/weekend, calendar season, local temperature, barometric pressure, daylight length, menstrual-cycle phase where applicable.

### Indices — operational definitions of every metric

- **HRV-coherence (primary).** Following the HeartMath operationalisation cited by Regulus: from the 5-minute RR series (artefact-corrected, cubic-spline resampled to 4 Hz), compute the power spectral density; identify the peak in the 0.04–0.26 Hz band; **coherence ratio = peak-band power / (total power in 0.0033–0.40 Hz − peak-band power)**, with the peak band defined as peak ± 0.015 Hz. Higher = more coherent (a sharp ~0.1 Hz oscillation).
- **Quiet / storm day.** Quiet = daily max Kp ≤ 2; storm = daily max Kp ≥ 5 (NOAA G1+). Locked; not analyst-adjustable.
- **Negative-control statistic.** The storm-minus-quiet coherence contrast recomputed on ≥ 1000 circularly-shifted/phase-randomised Kp series; the null is this distribution; the real effect's percentile within it is the inferential quantity.
- **Inter-participant synchronisation.** Mean pairwise Spearman correlation of participants' daily coherence series across socially unrelated participants, compared to a distribution generated by independently permuting each participant's day labels (≥ 1000 permutations).

## Analysis Plan

### Statistical models

**Primary (confirmatory):** linear mixed-effects model — `coherence ~ storm_vs_quiet + sleep + activity + caffeine + temperature + daylight + weekday + season + site + (1 + storm_vs_quiet | participant)` — same-day lag. The confirmatory test is **not** the model's Wald p on `storm_vs_quiet`; it is whether the fitted `storm_vs_quiet` coefficient exceeds the 95th percentile of the identical model refit on ≥ 1000 phase-shuffled Kp series. **Secondary (H1b):** the observed mean inter-participant coherence correlation vs the ≥ 1000-permutation day-label null. **Secondary (dose-response):** continuous daily Kp and Schumann power as predictors (mixed model, same covariates), FDR-corrected. **Lag:** +1/−1 day models are exploratory.

### Transformations

Spectral powers log-transformed; coherence ratio logit-adjusted if bounded; predictors standardised. All transformations fixed here, applied before unblinding.

### Inference criteria

Primary: real effect > 95th percentile of the phase-shuffled negative-control null (one-sided on the pre-registered direction; a two-sided |effect| > 97.5th percentile reported alongside). Secondary/exploratory endpoints: α = 0.05 with Benjamini–Hochberg FDR across the secondary family, explicitly labelled exploratory. A nominally "significant" mixed-model coefficient that does **not** exceed the negative-control null is reported as **null** for the confirmatory question.

### Data exclusion

Sessions with > 10% ectopic/artefact beats or < 4 minutes of usable RR are excluded (rule fixed here). Participant-windows with < 6 quiet or < 6 storm valid days are excluded from the primary contrast but retained for dose-response. Illness-flagged days excluded from primary, retained in a sensitivity analysis.

### Missing data

Missing days are left missing (mixed models use all available participant-days under MAR); no imputation of the primary outcome. Missing covariates handled by multiple imputation for the covariate set only, sensitivity-checked against complete-case.

### Exploratory vs confirmatory

Confirmatory: H1 (same-day storm-minus-quiet vs negative control) and H1b (inter-participant sync vs permutation). Everything else — dose-response, lag ±1, per-band HRV, Schumann-specific effects, sub-group and seasonal interactions — is exploratory and FDR-corrected.

## Other

### Ethics / IRB

Non-invasive wearable ECG in healthy adults; standard human-subjects review (IRB/REC), informed consent, right to withdraw. No deception beyond withholding the specific geomagnetic hypothesis (disclosed at debrief). De-identified, date-coded data; results — including a null — committed to publication in advance so a disconfirming outcome cannot be buried.

### Negative control (the load-bearing element)

The phase-shuffled Kp negative control is what separates this from the many geomagnetic-biology studies that report raw correlations inflated by shared seasonality and temporal autocorrelation. Because a real ~27-day solar-rotation and seasonal structure lives in both Kp and human physiology, *any* naive correlation is suspect. Circularly shifting/phase-randomising Kp preserves its autocorrelation structure while destroying its true temporal alignment to the HRV series; if the "real" alignment produces no larger an effect than a random alignment, there is no coupling to detect. This control is pre-specified as the primary inferential yardstick precisely so the result cannot be narrated around.

### Inter-participant synchronisation (the hard-to-confound signature)

Local weather, sleep, and behaviour are participant- and site-specific; they cannot easily produce correlated day-to-day HRV among strangers at *different* sites. A genuine global geomagnetic driver can. Multi-site recruitment plus the day-permutation null makes this the most diagnostic test in the design: a positive H1b that survives permutation would be difficult to explain by any local confound, and its absence alongside a raw H1 correlation would strongly implicate seasonality/autocorrelation.

### Confound-control summary

| Confound | Why it threatens the result | Control |
|---|---|---|
| Shared seasonality / 27-day solar rotation | Both Kp and HRV carry slow periodic structure → spurious correlation | Phase-shuffled negative control (preserves autocorrelation); season covariate |
| Temporal autocorrelation of daily HRV | Inflates naive significance | Negative-control null is the inferential yardstick; mixed model with per-subject slopes |
| Local weather (temperature, pressure, daylight) | Co-varies with mood/HRV and with slow geomagnetic trends | Per-site covariates; multi-site design; inter-site synchronisation test |
| Behaviour (sleep, caffeine, activity) | Direct large HRV drivers | Daily logs + accelerometer as covariates |
| Expectancy / deliberate self-regulation | Participant vagal "counters" on perceived-active days | Hypothesis withheld; participants uncued to geomagnetic state |
| Device/measurement drift, time-of-day | Systematic HRV variance | Fixed morning window; same device; artefact QC thresholds |
| Analyst degrees of freedom | Post-hoc fitting to a free target | Full pre-registration; date-coded blinded analysis; locked pipeline |

### Anchor citation

McCraty, Atkinson, Stolc, Alabdulgader, Vainoras & Ragulskis (2017), "Synchronization of Human Autonomic Nervous System Rhythms with Geomagnetic Activity in Human Subjects," *IJERPH* 14(7):770 — the correlational, HeartMath-funded source this study is designed to test under proper negative-control and multi-site conditions.

### Analytic-software note

All analysis code (mixed-effects models, spectral/coherence pipeline, permutation and phase-shuffle routines, power simulation) is deposited with this registration and version-pinned; the blind is broken only after the code is frozen.
