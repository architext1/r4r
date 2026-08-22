# OSF Pre-Registration

> ### ⚠ Reviewer note — read before filing
>
> An independent methodological review of this protocol (`analysis/REGULUS-BRIEF.md`,
> finding **D1**) reports that the registered magnitude bar and the power calculation are
> expressed on different scales.
>
> The bar as registered sits **8.1 standard errors from zero** — `1.96 × √2 σ / √34 =
> 0.2425σ` — which is an effect size of `d = 1.386`, against a study powered for
> `d = 0.5`. That is a factor of 2.77.
>
> The consequence is the opposite of conservative: as written, this protocol is
> **pre-committed to reporting a large true effect as a null**. A real effect of the size
> the study was designed to detect would fail the registered bar and be published as a
> refutation.
>
> This is a scale error, not a design flaw — the design is otherwise sound and the
> sham-controlled, three-way-blinded structure is the strongest part of the corpus. But
> the bar needs reconciling with the power calculation before this is filed, and the
> choice of the corrected threshold is a scientific judgement for the author, not a
> mechanical fix.
>
> *Note added by review; the protocol below is unchanged.*

## Study Information

### Title

Does follicular sebum clearance reduce resting-state EEG entropy in autistic adults? A sham-controlled, three-way-blind within-subjects crossover with a between-subjects sham-only arm.

### Description

Autistic brains show elevated resting-state EEG entropy, an effect commonly described as increased "neural noise" (Frontiers in Psychiatry 2025, PMC11832502: higher Rényi and Tsallis entropy in ASD across all channels, explicitly attributed to increased neural noise; Lempel–Ziv complexity runs *lower* in ASD, reconciled as repetitive sharp oscillations). The mainstream mechanistic account of that elevated entropy is cortical excitation/inhibition (E/I) imbalance.

A speculative framework (the ASS-OS "Regulus"; "Crown of Thorns" model) proposes an alternative *source* for the same measured noise: that hair follicles act as body-wide photoreceptors (the follicle-expressed opsin OPN3 and cryptochromes CRY1/CRY2 are cited), that when follicles are obstructed by sebum they misread the body's own endogenous biophotons as incoming signal, and that this floods the cortex with noise. The framework's single cheapest falsifiable prediction is that mechanically/chemically **clearing follicular sebum reduces scalp-EEG entropy**, and it notes this experiment has never been run.

This study runs it. Each autistic adult participant is their own control across a *real* follicular-clearance session and a procedurally identical *sham* session (order-counterbalanced, washout between), while a parallel between-subjects sham-only group establishes the entropy measure's own session-to-session drift (the noise floor) and guards against order/practice/expectation effects. The primary endpoint is the active-minus-sham change in whole-scalp-averaged Rényi entropy. All procedures, entropy parameters, the EEG pipeline, the sample size, the blinding scheme, the positive-control gate, and the stopping rule are fixed here before any data are collected.

**We state the prior explicitly: we expect the null (H0) to win.** A causal chain running from scalp sebum to *intracranial-origin* EEG entropy is physiologically extravagant, and the elevated cortical entropy already has a parsimonious E/I explanation that requires no biophotons. The value of this study is not that we expect it to confirm the framework — it is that the framework's central medical claim is cheap, has never been tested, and is designed here so that it *can* fail. A pre-committed, sham-controlled, blinded null is a real scientific result; a "positive" that is really arousal, expectation, or measurement drift is not, and this design is built to tell those apart.

This is a mechanism-falsification study, not a treatment trial. It does not claim, test, or imply that follicular clearance treats autism or any autistic trait; the dependent variable is an EEG entropy measure, and the sole question is whether an active scalp-clearance procedure moves that measure more than an identical sham does.

### Hypotheses

**H1 (directional, framework prediction — the effect we are powered to detect).**
Relative to a procedurally identical sham, active follicular sebum clearance produces a **reduction** in resting-state, eyes-closed, whole-scalp-averaged Rényi entropy in autistic adults, measured from immediately pre-intervention to a fixed post-intervention window. Formally, the primary contrast

    Δ = ΔH_active − ΔH_sham,  where ΔH_arm = H_post(arm) − H_pre(arm)

is expected to be **negative** (active reduces entropy more than sham), and its magnitude is expected to **exceed the test–retest drift** of the entropy measure itself (the noise floor established from the sham-only group; see Sampling Plan and Analysis Plan). Direction and the magnitude bar are both registered in advance; "some change" is not the prediction.

**H0 (null / standard-neurology account — the prior we expect to hold).**
Active follicular clearance produces no change in intracranial-origin EEG entropy beyond that produced by the sham procedure: Δ = 0 within the noise floor. Under H0, any within-arm ΔH reflects arousal, relaxation, expectation, scalp-signal-quality change, and session-to-session drift — all of which the sham reproduces — because the elevated cortical entropy arises from E/I imbalance and has no follicular-photonic source.

**Explicit falsifier of the framework.**
If the active and sham arms move whole-scalp-averaged Rényi entropy statistically indistinguishably (the primary two-sided test does not reject Δ = 0, and/or |Δ| does not exceed the pre-registered noise floor), the biophoton-source claim for ASD EEG entropy is **falsified** at the effect size this study is powered to detect. The study is deliberately constructed to be able to return this outcome, and a null result will be published (see Other → Ethics; Analysis → Exploratory vs confirmatory).

**Honest prior.**
Our prior is that **H0 wins.** We are pre-registering and running the test anyway because (a) the framework's own honesty — it names the experiment and flags that it has never been run — is an invitation to run it cleanly, and (b) a pre-committed blinded null is the outcome that turns a narratable framework into a falsified one. A directional secondary endpoint ("movement toward H(1/φ)") is registered below but is explicitly *not* the basis on which the framework stands or falls.

---

## Design Plan

### Study type

**Experiment** — a controlled intervention with random assignment of condition order. The manipulated variable (active vs sham follicular clearance) is administered by the researchers; the dependent variable (resting-state EEG entropy) is measured.

### Blinding

**Three-way blinding.**

1. **Participant-blind.** The active and sham procedures are matched on duration, practitioner, chair, body position, tactile contact, product texture, product scent, and the participant's belief that "a scalp procedure was performed." Only the sebolytic/exfoliative action differs. Participants are told at consent that they will receive two scalp procedures, one active and one inactive, and will not learn which was which until the study ends (single-blind-to-arm, fully disclosed and debriefed — see Ethics).

2. **Technician-blind (EEG operator).** The person who applies the scalp procedure is *not* the person who records or handles the EEG. Arm assignment for each session is delivered in a sealed, sequentially numbered, opaque randomization envelope opened by a third party (the procedure practitioner) who never touches the EEG hardware, the EEG data, or the analysis. The EEG technician records only an arm-agnostic session code.

3. **Analyst-blind.** All entropy computation is performed on de-identified recordings labelled only with an arm-agnostic session code (e.g. A/B). The active/sham key is held by an independent custodian and is **not** broken until (i) the analysis pipeline is frozen, (ii) the positive-control gate has been evaluated, and (iii) the primary-analysis script has been run to produce arm-blind outputs. Unblinding is a single logged event.

### Is there a control / comparison condition?

**Yes — two, by design.**

- **Within-subjects sham control (primary comparison):** each participant undergoes a real follicular-clearance session and a procedurally identical sham session. The sham holds constant practitioner attention, tactile stimulation, relaxation/arousal, product scent and texture, time-of-day scheduling, and the participant's expectation that "something was done," isolating the sebolytic/photoreceptor-unblocking action as the *only* difference between arms. The primary endpoint is the active-minus-sham contrast, so every non-specific effect that moves resting EEG is subtracted at the participant level.

- **Between-subjects sham-only arm (drift / order control):** a separate group that receives *two* sham sessions on the same schedule. This group (i) establishes the entropy measure's session-to-session test–retest drift (the noise floor the active-minus-sham contrast must beat) and (ii) catches any pure order/practice effect of repeated EEG sessions independent of any active intervention.

### Study design

Mixed design.

- **Within-subjects factor: Arm** (active, sham), administered to the crossover group in counterbalanced order with a washout between sessions. Each crossover participant contributes one `ΔH_active` and one `ΔH_sham`.
- **Between-subjects factor: Group** (crossover vs sham-only). The sham-only group contributes two sham `ΔH` values on the identical schedule (yielding the drift estimate and the order-effect check).
- **Within-session structure:** resting-state EEG is recorded immediately **pre**-intervention and again in a fixed **post**-intervention window, identical epoch length and montage pre and post, so the unit of the dependent variable is the *change* `ΔH = H_post − H_pre`.
- **Positive control within every session:** an eyes-open vs eyes-closed resting-EEG block (a robust, well-documented alpha/entropy manipulation) is recorded each session and serves as a *gating criterion* for the pipeline's ability to resolve a known entropy shift (see Analysis Plan).

Active intervention = the defined scalp cleansing/exfoliation protocol that removes sebum from the follicle **without** altering scalp temperature or hydration and **without** applying any photoactive or sensitising agent. Sham = identical in duration, contact, chair, practitioner, scent, and product texture, but with **no** sebolytic action and **no** exfoliation. Both arms use only verified non-photoactive formulations (a photoactive residue would itself stimulate follicular photoreceptors and confound the mechanism).

### Randomization

- **Arm-order assignment (crossover group):** each participant is randomly assigned to active-first or sham-first via a computer-generated random allocation sequence (blocked to keep the two orders balanced across the completed sample), prepared by an independent party and delivered as sealed sequentially numbered opaque envelopes. The sequence is generated before enrolment and stored with the independent custodian.
- **Group assignment (crossover vs sham-only):** participants are randomly allocated to the crossover group or the sham-only group by the same independent-party sequence at enrolment, stratified to fill the target group sizes.
- **Session-time and analysis order** are fixed by protocol (not randomized) to control day-to-day variance; recordings are processed in a de-identified, arm-agnostic order.

---

## Sampling Plan

### Existing data

**No.** Registration is prior to any data collection. No EEG data for this study exist at the time of registration; recruitment and recording begin only after this pre-registration is posted.

### Data collection procedures

Autistic adults are recruited through clinical/community autism registries, specialist clinics, and self-referral in response to advertised study materials (accessible, plain-language). Inclusion: adults (≥18) with a documented clinical autism diagnosis, able to give informed consent (capacity assessment where relevant), able to tolerate a resting EEG cap and two scalp procedures. Exclusion: active scalp dermatological condition; photosensitising medication or condition; known cryptochrome/opsin-relevant confound where applicable; inability to complete both sessions of the assigned arm structure; EEG contraindication.

Each participant completes their assigned sessions (two for both groups) at a **fixed time of day**, with **standardised pre-session abstinence** (caffeine, and other pre-registered stimulants) and self-reported sleep on the prior night recorded as a covariate. Sessions are separated by a fixed **washout** interval (registered). At each session: (1) cap fitment to marked fiducials at identical electrode positions (measured cap; positions re-verified each session), (2) pre-intervention resting eyes-closed EEG + the eyes-open/eyes-closed positive-control block, (3) the assigned scalp procedure (active or sham) applied by the blinded practitioner, (4) post-intervention resting eyes-closed EEG + positive-control block in the fixed post window. Scalp temperature and hydration are measured pre and post as covariates and to verify the active protocol did not alter them.

### Sample size

- **Crossover group:** recruit **N = 40** autistic adults (target **34 completing both arms**, allowing ~15% attrition across the crossover).
- **Sham-only group:** recruit **~20** autistic adults (for the noise-floor / drift and order-effect estimates).
- **Total target enrolment: ~60.**

### Sample-size rationale (power calculation)

The primary test is a within-subjects paired comparison of the active-minus-sham contrast against zero. We power to detect a **medium** effect, on the reasoning that a follicular-photonic effect large enough to be clinically or theoretically meaningful should not be subtle.

- **Design/test:** two-tailed paired *t* (Wilcoxon signed-rank as the non-parametric fallback; see Analysis Plan).
- **Alpha:** 0.05 (two-tailed). **Power:** 0.80.
- **Target effect:** Cohen's *d* = 0.5 on the paired contrast → **N ≈ 34 completing both arms**. (For reference, at *d* = 0.6 → N ≈ 24; we power to the smaller, more conservative *d* = 0.5.)
- **Attrition:** recruiting 40 to retain ≥34 across the two-session crossover assumes ≤15% dropout.

The paired-*t* requirement for 80% power at two-tailed α = 0.05 is N = 34 for *d* = 0.5 (standard paired-design power tables; verify with the analysis software's power routine at protocol lock and record the exact call and output in the study file). If the confirmed analytic model is the mixed model (arm × order) rather than the simple paired test, the paired-*t* N is treated as the conservative floor and is not reduced.

**The magnitude bar (noise floor), not just significance.** Statistical significance of the paired contrast is necessary but not sufficient. The registered bar is that the active-minus-sham contrast must **exceed a pre-registered drift ceiling**, defined as **1.96 × the within-participant SD of the sham-only group's session-to-session `ΔH`** (a one-sided ~95% ceiling on pure test–retest drift; the SD is estimated across the two sham sessions in the sham-only group). A contrast that is "significant" but smaller than the sham-only drift is reported as **within measurement drift** and does **not** count as support for H1. This bar is fixed before unblinding.

### Stopping rule

**Fixed-N, no interim inferential peeks.** Data collection stops when the target completing sample is reached: **≥34 completing both arms** in the crossover group **and** **~20** in the sham-only group. There are no interim analyses of the primary endpoint and no data-dependent stopping for efficacy or futility; recruitment continues only to backfill attrition up to the enrolment ceiling. If, after exhausting the recruitment window and ceiling, fewer than 34 crossover completers are obtained, the shortfall and its impact on achieved power are reported, and the primary analysis is run as pre-registered (no post-hoc power re-labelling of a null as a positive). Blinding is not broken until the completing sample is reached and the pipeline is frozen.

---

## Variables

### Manipulated / independent variables

- **Arm (within-subjects):** `active` (defined follicular sebum-clearance protocol — sebum removed from the follicle; scalp temperature and hydration held constant; no photoactive/sensitising agent) vs `sham` (procedurally identical — same duration, practitioner, chair, contact, product scent and texture — with no sebolytic action and no exfoliation). This is the sole intended physical difference between arms.
- **Group (between-subjects):** `crossover` (one active + one sham session) vs `sham-only` (two sham sessions).
- **Order (within crossover group):** `active-first` vs `sham-first` (counterbalanced; entered as a factor to test/adjust for order and carryover).

### Measured / dependent variables

- **Primary DV:** `ΔH_Rényi` per arm = whole-scalp-averaged Rényi entropy at the fixed post window minus at pre, from resting-state eyes-closed EEG. The primary **contrast** is `Δ = ΔH_Rényi(active) − ΔH_Rényi(sham)`.
- **Secondary DVs (FDR-corrected, exploratory-labelled):** `ΔH_Tsallis` (whole-scalp-averaged Tsallis entropy — elevated in ASD in the anchor literature); `ΔLZ` (Lempel–Ziv complexity — note it runs *lower* in ASD, so both directions are tracked and reported); `ΔMSE` (multiscale sample entropy — the measure the framework's own document names); and the per-channel maps of Rényi entropy.
- **Secondary directional DV:** movement of whole-scalp-averaged Rényi entropy *toward the pre-registered reference value* `H(1/φ)` (defined operationally below).
- **Positive-control DV (gating):** the eyes-open-minus-eyes-closed difference in whole-scalp-averaged Rényi entropy within each session (must be resolvable — see Indices and Analysis Plan).
- **Covariates:** scalp temperature (pre, post), scalp hydration (pre, post), electrode-position verification, time-of-day (fixed by protocol), self-reported prior-night sleep, adherence to pre-session abstinence.

### Indices — operational definitions of every metric

Recording and preprocessing are identical across all sessions and arms; every parameter below is fixed here before any data are seen.

- **EEG acquisition.** Resting-state eyes-closed EEG on a high-density montage (**≥ 32 channels, 10–20 layout**), identical electrode positions across sessions via a measured cap with marked fiducials, identical reference, identical amplifier settings and sampling rate. Pre and post recordings use the same **5-minute** artefact-rejected epoch length.
- **Preprocessing / artefact rejection (frozen pipeline).** A single pre-registered pipeline — band-pass filter, line-noise removal, bad-channel handling, artefact rejection (e.g. ICA/threshold criteria), epoch selection rule, and re-referencing — is fixed in the analysis script before data collection. The epoch-selection rule (which clean epochs enter the entropy computation) and the artefact-rejection thresholds are mechanical, not analyst-chosen per recording.
- **Rényi entropy (primary).** Computed **per channel** on the frozen epochs with a fixed order parameter α and a fixed probability-estimation method (registered exactly), then **averaged across all channels** to yield the whole-scalp value used for the primary endpoint. The exact α, the discretization/binning or density-estimation scheme, and the epoch aggregation are recorded in the pre-registered parameter block.
- **Tsallis entropy (secondary).** Same per-channel-then-averaged procedure with a fixed entropic index q (registered).
- **Lempel–Ziv complexity (secondary).** Fixed binarization rule and normalization, per-channel then averaged.
- **Multiscale sample entropy (secondary/tertiary).** Fixed embedding dimension m, tolerance r (as a fraction of the signal SD), and the set of time scales, per-channel then averaged.
- **`H(1/φ)` — the secondary reference target, defined concretely BEFORE collection.** `1/φ = 0.6180339887…`. `H(1/φ)` is defined as the Rényi entropy (same α and estimator as the primary DV) of a **pre-registered reference probability distribution** whose retention/release split is fixed at the golden ratio: a two-outcome (Bernoulli) reference distribution with `p = 1/φ = 0.618034` and `1 − p = 0.381966`, giving `H(1/φ)` as the numeric Rényi entropy of that {0.618034, 0.381966} distribution at the registered α. This single number is computed and written into the study file at protocol lock, before any EEG data are seen. "Movement toward `H(1/φ)`" for a participant/arm is the signed reduction in `|H_post − H(1/φ)| − |H_pre − H(1/φ)|` (negative = moved closer). This endpoint is **secondary and directional only**; a free-floating target invites post-hoc curve-fitting, so it is fixed as a number here and never used as the primary.
- **Positive control (gating index).** Within each session, the eyes-open-minus-eyes-closed difference in whole-scalp-averaged Rényi entropy, using the identical pipeline and parameters. This is a within-subject sanity check that the instrument+pipeline can resolve a *known* entropy manipulation.

---

## Analysis Plan

### Statistical models

**Primary confirmatory analysis (single endpoint).**
Test the active-minus-sham contrast on whole-scalp-averaged Rényi entropy against zero, in the crossover completers.

- Primary model: a **linear mixed-effects model** on `ΔH_Rényi` with fixed effects of **Arm** (active vs sham) and **Order** (active-first vs sham-first) and their interaction (Arm × Order carryover check), and a random intercept per participant:

      ΔH_Rényi ~ Arm * Order + (1 | Participant)

  The **Arm** fixed effect here (equivalently the sign and significance of the active-minus-sham contrast) is evaluated alongside the powered paired test below and must agree with it. H1 predicts the active level lowers entropy relative to sham (a negative Arm contrast).
- **Powered confirmatory test of record: a two-tailed paired t-test** of `ΔH_Rényi(active)` vs `ΔH_Rényi(sham)` — this is the test the power analysis (N = 34 for *d* = 0.5) is built on, so the confirmatory claim rests on the test the study is actually powered for. The mixed-effects model above is a **pre-registered robustness check** (its role is the Arm × Order carryover check and per-participant structure), not a separately-powered primary; it must agree in sign and significance with the paired test. If the paired differences violate normality (Shapiro–Wilk pre-registered threshold), use the **Wilcoxon signed-rank** test as the pre-specified non-parametric substitute. Disagreement between the paired test and the mixed model is reported transparently and resolved in favour of the more conservative result.
- **Noise-floor gate (magnitude bar):** the estimated active-minus-sham contrast must **exceed the pre-registered drift ceiling** — **1.96 × the within-participant SD** of session-to-session `ΔH_Rényi` in the **sham-only** group (a one-sided ~95% drift ceiling). A contrast that is statistically significant but below this ceiling is reported as **within measurement drift** and does not support H1.

**Secondary analyses (all FDR-corrected, explicitly exploratory).**
- Repeat the Arm-effect test for `ΔH_Tsallis`, `ΔLZ`, `ΔMSE`, and the per-channel Rényi maps. Correct across this secondary family with **Benjamini–Hochberg FDR** at q = 0.05. All are labelled exploratory regardless of outcome. LZ is interpreted with its known ASD direction (lower in ASD) in mind, and both directions are reported.
- **Directional secondary:** test whether the active arm moves whole-scalp Rényi entropy toward the pre-registered `H(1/φ)` more than sham (one-sided, on the `|H − H(1/φ)|` reduction), reported as secondary/directional only.
- **Order/practice effect:** in the sham-only group, test session-2-minus-session-1 `ΔH` for a pure order/practice effect on entropy.

**Positive-control gate (pre-registered as a gating criterion — evaluated BEFORE the primary analysis, blind to arm).**
Confirm the pipeline resolves the eyes-open vs eyes-closed entropy manipulation at the group level (pre-registered: significant eyes-open-minus-eyes-closed difference in whole-scalp Rényi entropy in the expected direction, at the registered alpha). **If the positive control fails, the study is underpowered at the *measurement* level, not the biology level, and the primary analysis is not interpreted as a biological test** — any null would be uninterpretable, so a failed positive control is reported as a measurement-level negative result and the biological hypothesis is neither confirmed nor falsified. No positive control, no primary analysis.

### Transformations

- The dependent variable is a **change score** `ΔH = H_post − H_pre` per arm; the primary quantity is the **between-arm difference of change scores** `Δ = ΔH_active − ΔH_sham` (double difference), which removes stable per-participant baseline entropy.
- Entropy values are computed per channel and **averaged across channels** for whole-scalp endpoints (primary and secondary summaries) before modelling.
- Covariates (scalp temperature, hydration, sleep) enter as pre-registered nuisance covariates in a sensitivity version of the primary model; the confirmatory model is the covariate-light one specified above, with the covariate-adjusted model reported alongside.
- If the paired differences fail the pre-registered normality check, the Wilcoxon signed-rank test is used (no post-hoc choice of transformation to rescue a parametric test).

### Inference criteria

- **Primary alpha:** 0.05, **two-tailed**, on the single primary endpoint (Arm effect / active-minus-sham paired contrast on whole-scalp Rényi entropy). Two-tailed despite H1 being directional, so that a *reversed* effect (active raises entropy relative to sham) is also detectable and reportable.
- **Magnitude bar:** significant **and** contrast magnitude > sham-only test–retest drift → support for H1. Significant but below drift → "within measurement drift," not support.
- **Multiple comparisons:** exactly **one** primary endpoint is tested at α = 0.05, locked before unblinding. All other measures (Tsallis, LZ, MSE, per-channel maps, the `H(1/φ)` directional endpoint) are **secondary, Benjamini–Hochberg FDR-corrected (q = 0.05), and labelled exploratory**. No "some channel went significant" claim is made outside the FDR-corrected exploratory frame.
- **Positive-control gate** must pass (as above) for the primary analysis to be interpreted biologically.

### Data exclusion

- **Participant-level:** a participant is excluded from the crossover primary analysis if they do not complete both arms, if either session fails the pre-registered EEG data-quality criteria (excessive artefact leaving fewer than the registered minimum clean epochs; failed electrode-position verification), or if a documented protocol breach compromises blinding for that participant. Exclusions are counted and reported; the number needed to retain ≥34 completers drove the 40-recruitment target.
- **Epoch-level:** epochs are included/excluded by the frozen artefact-rejection and epoch-selection rules only — never by inspection of the resulting entropy value.
- **Session-quality floor:** a session yielding fewer than the pre-registered minimum clean epochs after artefact rejection is treated as missing for that arm (see Missing data).
- All exclusion rules are mechanical and fixed before data are seen; an exclusion decision is never conditioned on the entropy outcome or on arm.

### Missing data

- A crossover participant missing one arm's usable EEG (dropout or session-quality failure) is **excluded from the primary paired/mixed analysis** (which requires both arms). No imputation of the missing arm's entropy is performed for the confirmatory endpoint (imputing the dependent variable would fabricate the effect).
- In the mixed-effects model, participants with a missing arm contribute to any estimable random-effects structure only insofar as the model permits, but the confirmatory Arm contrast is computed on complete pairs; the complete-pair result is the registered primary.
- Missingness rates by arm and group are reported. Sensitivity analyses (e.g. the mixed model retaining partial data) are reported as secondary/exploratory, never as the primary result.

### Exploratory vs confirmatory

- **Confirmatory:** the single primary endpoint — active-minus-sham contrast on whole-scalp-averaged Rényi entropy, two-tailed α = 0.05, with the noise-floor magnitude bar and the positive-control gate — tests H1 vs H0 and constitutes the framework's falsifier.
- **Exploratory (all FDR-corrected, so-labelled):** Tsallis, Lempel–Ziv, multiscale sample entropy, per-channel maps, the directional `H(1/φ)` endpoint, covariate-adjusted and partial-data sensitivity models, and any subgroup or descriptive analyses.
- The result — **including a null** — is committed to publication in advance (see Other). A disconfirming outcome is reported as a falsification of the framework's follicular-photonic-source claim at the powered effect size, not narrated around; a confirming outcome is reported with the explicit caveat that a single blinded crossover is a first test requiring independent replication before any mechanistic or clinical claim.

---

## Other

### Ethics / IRB

The study requires prospective approval from an Institutional Review Board / Research Ethics Committee before recruitment. Key features:

- **Population:** autistic adults. Informed consent uses accessible, plain-language materials, with capacity assessment where relevant. Participants may withdraw at any time without penalty.
- **Intervention risk:** a benign topical scalp procedure using only **non-photoactive, non-sensitising** products, with pre-screening dermatological assessment to exclude active scalp conditions. No photoactive or sensitising agents are used in either arm.
- **EEG:** non-invasive, standard-risk resting-state recording.
- **Deception:** none beyond the sham procedure itself, which is **disclosed at consent** ("you will receive two scalp procedures, one active and one inactive, and will not be told which is which until the study ends") — an acceptable single-blind-to-arm design with **full debrief** at study end, including disclosure of each participant's arm assignment on request.
- **Data:** de-identified and arm-coded; the active/sham key is held by an independent custodian and broken only once, after the pipeline is frozen and the positive-control gate is evaluated.
- **Publication commitment:** the outcome, **including a null result**, is committed to publication in advance so a disconfirming finding cannot be buried. This commitment is itself part of what makes the study a genuine test rather than a narratable exercise.
- **Framing safeguard:** the study is a mechanism-falsification study of an EEG entropy measure. It does not test, claim, or imply that follicular clearance treats autism or alters any autistic trait, and consent and dissemination materials state this explicitly to avoid raising or exploiting therapeutic expectations. The registered prior is the null.

### Positive control (methods-reviewer hardening — restated as a first-class design element)

A null result only falsifies the framework if the measurement pipeline can detect a *known* entropy shift. Each session therefore includes an **eyes-open vs eyes-closed** resting-EEG block, a robust and well-documented alpha/entropy manipulation. The pipeline's ability to resolve this difference (group-level, in the registered direction, at the registered alpha) is a **gating criterion evaluated before the primary analysis**: if the positive control fails, the study is declared underpowered at the measurement level, any null is deemed uninterpretable as biology, and the primary endpoint is not interpreted as a biological test. This gate is pre-registered precisely so that "the instrument couldn't see anything" and "the biology isn't there" cannot be confused after the fact.

### Confound-control summary

| Confound | Threat to Δ | Control |
|---|---|---|
| Arousal/relaxation from being cleansed | Lowers resting entropy independent of any photonic effect | Sham arm reproduces the relaxation exactly; primary endpoint is active-minus-sham |
| Scalp temperature / hydration change | Alters skin impedance and EEG signal quality | Active protocol holds both constant; measured pre/post and entered as covariates |
| Electrode-position drift between sessions | Spurious per-channel entropy differences | Measured cap, marked fiducials, positions re-verified each session; whole-scalp averaging for the primary |
| Expectation / placebo ("I was treated, I feel calmer") | Belief alone shifts autonomic state and EEG | Three-way blinding; participant cannot tell active from sham |
| Practitioner / analyst bias | Unblinded scoring nudges the result | Technician-blind recording; analyst-blind entropy computation on arm-coded data; key broken post-lock |
| Time-of-day / caffeine / sleep | Large day-to-day EEG variance | Fixed session time, standardised pre-session abstinence, sleep self-report covariate |
| Order / practice effect on repeated EEG | Entropy drifts across sessions regardless of arm | Counterbalanced order + between-subjects sham-only group + Arm×Order term |
| Photoactive product residue | Would itself stimulate follicular photoreceptors, confounding the mechanism | Both arms use verified non-photoactive products |
| Multiple comparisons across channels/measures | "Some channel significant" almost guaranteed | One locked primary endpoint; all else Benjamini–Hochberg FDR-corrected and exploratory |
| Pipeline can't resolve entropy at all | Uninterpretable null | Eyes-open/eyes-closed positive-control gate before primary analysis |
| Free-floating "toward H(1/φ)" target | Post-hoc curve-fitting | `H(1/φ)` fixed as a concrete number pre-registration; secondary/directional only |

### Anchor citation

Higher Rényi and Tsallis entropy in ASD, attributed to increased neural noise (Lempel–Ziv complexity lower in ASD, reconciled as repetitive sharp oscillations): **Frontiers in Psychiatry (2025), PMC11832502** — https://pmc.ncbi.nlm.nih.gov/articles/PMC11832502/. This is the source of the entropy family used here (Rényi/Tsallis primary/secondary, LZ and MSE secondary/tertiary) so that results are directly comparable to the established ASD-entropy finding.

### Analytic-software note

At protocol lock, the exact power routine call (paired-*t*, two-tailed, α = 0.05, power = 0.80, *d* = 0.5 → N = 34) and its output, and the frozen preprocessing + entropy-parameter block (montage, reference, filter, artefact/epoch rules, Rényi α and estimator, Tsallis q, LZ binarization, MSE m/r/scales, and the computed numeric value of `H(1/φ)`), are written into the version-controlled analysis repository and time-stamped before any data are collected. The primary-analysis script is executed on arm-coded data to produce blind outputs; the active/sham key is applied only after those outputs and the positive-control gate result are locked.