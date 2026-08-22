# R4R — project instructions

ultrathink++

This is a **research corpus, not a codebase**. There is no application to run, no test
suite, and no deploy. The work is reading carefully, computing rather than recalling, and
being exact about who said what. Optimise for that.

Register: measurement-first, no sycophancy. The framework's author tags his own seams
(*"DEFINED not MEASURED… a map, not the territory"*) and is better served by someone who
respects that than by someone who smooths it over. Praise what is earned, and say plainly
what is not.

---

## PARAMOUNT — attribution is the primary failure mode

This repository holds two people's work and the boundary is load-bearing, not cosmetic.

| Path | Owner | Rule |
|---|---|---|
| `sources/**` (gitignored, local only) | **Thomas Frumkin** (@teslasolar) | His, unpublished. Never edit. Never commit — this repo is PUBLIC. Not covered by its licence. |
| `analysis/**`, `experiments/**`, `docs/**`, `ERRATA.md` | V>> | CC BY 4.0 |

Three things follow, and none of them are optional:

1. **Never edit anything in `sources/`.** Corrections go in `ERRATA.md` as a documented
   erratum with the arithmetic, never as a silent fix to his text.
2. **Never commit `sources/`.** This repository is PUBLIC. The spec is gitignored and lives
   only on local machines; `git add -f` on it would publish an unpublished work irreversibly.
   The default build already omits `source.html`; keep it that way. Consent is Thomas's to
   give, and he has not given it.
3. **Never attribute across the line.** The specification and Addendum A are his. The
   appraisal, the pre-registrations, the primer, the Gerald reading and the site are V>>'s.
   Conflating them is the single most damaging mistake available here.

## PARAMOUNT — compute, do not recall

Every number in this corpus is checkable, and several published claims about it have already
turned out to be wrong on checking. When you state a figure:

- **Re-derive it.** `κ*² = 1 − κ*`, `709` being the 127th prime, `2047 = 23 × 89`, the growth
  ratios of the prime spine — all of these are one line of Python. Run the line.
- **Cite the section.** `[R §7.4]`, `[A §A2]`, `[P1]`, `[Read]` — the primer uses this
  convention with 139 tags. Follow it.
- **Mark inference as inference.** The primer carries ten `[inference]` tags precisely so
  Thomas can challenge those first. That is a feature; keep it.

Two transcription errors were found this way and are recorded in `ERRATA.md`. Both were
invisible to reading and obvious to arithmetic.

## The name

Thomas named this project himself when he reviewed it, and the name is his word about his
own work. Use **R4R** in every page title, heading, `<title>` tag and nav label.

- **Do not spell the expansion out in page chrome or `<title>` tags.** R4R stands alone
  there.
- Where the expansion appears in body copy it must be clearly in Thomas's own voice, quoted
  and attributed to him. It is quoted exactly once, in `README.md`. Do not add a second.
- **ASS-OS / Regulus** remains the framework's formal name. R4R is the explainer and the
  apparatus around it; Regulus is the thing being explained. Do not swap them.

He is autistic and reclaiming the word deliberately. Two ways to get this wrong, and both
are worse than getting it slightly awkward: sanitising the project's voice into corporate
mush, and performing edginess with it. Plain, warm, direct. His register, not a costume.

## PARAMOUNT — the layering is the achievement. STOP SIMPLIFYING.

The framework's author reviewed this site and named the structure, not the plainness, as
what works:

> *"The structure is perfect. Four sentences -> five paragraphs -> full math -> diagnostic
> -> proof. Layered depth. Somebody can read the top. A mathematician can read the bottom.
> Nobody has to read more than they want."*

That is a **depth gradient**, and every layer has to keep its own register:

| Layer | Page | Register |
|---|---|---|
| 1 | `index.html` TL;DR | four sentences, no symbols |
| 2 | `index.html` on-ramp | five paragraphs, still no symbols |
| 3 | `index.html` body, `geometries.html` | the mathematics, explained |
| 4 | `primer.html` | the full walk, every claim tagged |
| 5 | `brief.html`, `proof.html` | technical. Deliberately does NOT simplify. |

Three rules follow:

1. **Do not run another plain-language pass.** Grade 8 was the target and four pages are at
   or under it. Going further flattens the gradient, and the gradient is the product.
2. **Never simplify layer 5.** `brief.html` and the pre-registrations are the bottom of the
   ladder. A reader who reaches them wants the depth. `proof.html` reads at grade 13 on
   purpose — the protocols must stay filable as formal documents.
3. **New technical findings go DOWN the ladder, not across it.** An equation audit or a
   methodological correction belongs in the brief, not spread through the explainer.

He also named, unprompted, what he valued beyond the writing: the seven-button diagnostic
running locally with nothing sent anywhere, the bullshit-meter score published against his
own constant with the arithmetic shown, the errata surfaced publicly rather than fixed
silently, and the consent flag in the build script. Those are integrity features. Do not
quietly trade any of them away for polish.

## The framework, briefly

**ASS-OS** maps consciousness onto ISA-95 (Purdue levels), ISA-88 (PACK-ML state machine)
and ISA-18.2 (alarm management). Its skeleton is the Prime Recursion Spine —
`p^k(1) = {1, 2, 3, 5, 11, 31, 127, 709}` — giving seven levels whose costs accelerate
super-linearly. Its attractor is `κ* = 1/φ = 0.618…`, the point at which a system keeps
61.8% and releases 38.2%.

**Regulus** (α Leonis, Heart of the Lion) extends that base with three things the original
lacks, and this is where the value is concentrated:

- **Ŝ** — the binding operator. Two states become one non-separable state; remove B and you
  do not recover the original A. Threshold `|δΨ_crit| = κ*² = 0.382`. Requires **bilateral**
  modification (§8.5).
- **M̂** — the mimic operator. Coercion wearing love's behaviour, distinguished by opposite
  physiology and by one question: *who in this system is unchanged?*
- **The love field equations** (§7.1–7.7) — recognition, attraction, resonance,
  vulnerability, pair entropy, speed, persistence.

**Addendum A** classifies seven chronic stress patterns as geometric deformations away from
1/φ, isomorphic to the seven deadly sins — structurally, explicitly not morally — all
corrected by Ŝ, because Ŝ addresses their shared root: isolation.

## Document map

```
sources/     ass-os-regulus.txt          the specification (17 sections)
             regulus-addendum-sins.txt   Addendum A, seven stress geometries
analysis/    REGULUS-FOR-DUMMIES.md      the primer, 139 source tags
             00-catch-up-and-appraisal.md  claim-by-claim appraisal with scores
             regulus-catchup-and-experiment.md  the brief behind the experiments
             GERALD.md                   close reading of the Gerald song
experiments/ 01-prereg-follicular-eeg.md    the §12.1 falsifier, made runnable
             02-prereg-geomagnetic-hrv.md   Bus D, quiet days versus storm days
docs/        the R4R site + build.py
ERRATA.md    two verified corrections, with the full proofs
```

## Where a proof belongs

`ERRATA.md` is the canonical home of the full working — the §3.3 stability argument lives
there in its entirety, four independent routes and a runnable integration included.
Everything else points at it and stays short: `docs/assets/app.js` carries a brief note at
`drift()`, and the explainer shows the two corrected lines in a table.

This is a placement rule, not a rigour rule. Never thin the argument to make a page read
better — move it to `ERRATA.md` and link. A reader who wants the proof will follow the link;
a reader who does not should not have to step over it.

## Working on the site

```bash
python3 docs/build.py                 # the default, and the safe one — no source.html
python3 docs/build.py --with-source   # …and also build source.html
python3 -m http.server 4173 --directory docs
```

**The default build is the safe build.** `source.html` reproduces Thomas's unabridged
specification, so it is only built when explicitly requested, and only ever for a private
copy. The default does not merely skip it — it deletes a stale copy from an earlier build,
because a page left on disk is a page that gets served. Before any public deployment, run
the plain `python3 docs/build.py` and confirm `docs/source.html` is absent. Never invert
this default back.

`index.html` and `geometries.html` are hand-written because they carry interactive
instruments. Everything else is generated from a file in this repo, so **edit the source
document, not the HTML** — a hand-edit to a generated page is erased by the next build.

The site commits to a single dark theme deliberately (it is styled as a control-room
instrument panel) and paints every colour explicitly rather than inheriting. Palette, type
and layout tokens are at the top of `docs/assets/style.css`.

**No external font dependencies.** Type is set in `"Courier New", Courier, monospace` — one
token at the top of `style.css`, with the display and body faces aliased to it. A page that
phones a font CDN to render a control-room readout has its priorities backwards, and
Thomas's own SCADA pages load zero external fonts. This applies to every page including the
hand-written ones, which do not go through `build.py` and so will not be fixed for you: if
you touch `index.html` or `geometries.html`, check the `<head>` for a stylesheet link to a
font host before you finish.

## Quality roadmap

Real gaps, in the order they are worth closing:

1. **The Ŝ/M̂ discrimination study does not exist.** It is the cheapest study in the whole
   framework — saliva cortisol and HRV, about £30 a participant — and it tests the claim
   that carries the most weight. `experiments/` should have a third pre-registration.
2. **§9.3's inoculation claim is untested and falsifiable.** It predicts that people with a
   prior secure bond detect coercive dynamics faster. That is a straightforward study.
3. **Neither pre-registration has been filed.** They are ready; OSF is the next step.
4. **Addendum A's counter-sequences (R0–R6) are unspecified as protocols.** They are named
   but not operationalised, so nobody could replicate them.
5. **§12.2's eight fault mappings re-describe rather than predict** — V>>'s argument, not
   independently assessed. Worth a proper look.

## Writing conventions

British English. Numbers verbatim, never rounded in a claim. Section references in the
`§n.n` form the documents use. When quoting the specification, quote it exactly — its
phrasing is often better than a paraphrase, and *"the integral was always computable, you
just hadn't run the calculation until she showed up"* is not improvable.

## Code quality, where code appears

There is little of it, but `docs/build.py` and `docs/assets/app.js` are real. Correct by
construction as written: dispatch tables over if/else chains, helpers extracted on first
duplication rather than third, functions under 30 lines, no dependency hardcoded that could
be passed. Do not add a build system, a framework or a package manager to a site that
currently needs none — their absence is a feature, and the review said so twice.
