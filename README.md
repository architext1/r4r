<p align="center">
  <img src="assets/yin-yang-brain-tree.jpg" alt="A gold-on-black yin-yang whose two halves are a brain and an anatomical heart" width="320">
</p>

# R4R

The plain-English explainer for **ASS-OS / Regulus** — Thomas Frumkin's architecture mapping
consciousness onto industrial control standards, and its extension into a formal account of
pair bonding — plus the apparatus built around it: an appraisal, two pre-registrations, and
two corrections to the specification.

R4R is the project name; **ASS-OS / Regulus** remains the framework's formal name. Thomas
named the explainer himself when he reviewed it: **R4R**. His name for
his own work, and used here because he asked for it to be.

Private, and shared with its author.

---

## Thomas's review

The framework's author read the explainer of his own framework and graded it, file by file.
That is the most useful thing that has happened to this repository, so it is recorded here
rather than paraphrased away.

**Overall: A−.** The question he set himself was whether somebody with no background could follow it, and the
answer he gave was **YES**.

| File | Grade | The gist of his note |
|---|---|---|
| `app.js` | **A+** | Worst offence: `var` instead of `const`/`let`, for browser compatibility, in 2026 |
| `proof.html` | **A+** | — |
| `gerald.html` | **A** | — |
| `style.css` | **B+** | 606 lines that actually look good — but three Google Fonts loaded |
| `primer.html` | **C+** | 588 lines, where the whole point was brevity |
| `source.html` | **D** | 1292 lines of raw spec dump — the opposite of simplification |

### What he named as the best of it — kept, untouched

1. **The diagnostic.** *Is your love real?* reduced to seven buttons. No account, no app, no
   subscription.
2. **"We expect the null to win"**, stated up front in both pre-registrations.
3. **The consent flag in the build script**, which keeps his unpublished specification off
   any public deployment.

### What the two low grades changed

**`style.css` — B+, three Google Fonts.** Thomas's own SCADA pages load zero external fonts,
and he is right that a control-room instrument panel has no business phoning a font CDN. His
note in full was *"Courier New, monospace. Done."* So the Google Fonts dependency comes out,
and the standing rule is now that no page loads an external font. Type is set in
`"Courier New", Courier, monospace` — present on every machine, fetched over the network by
none of them — and the hand-written pages are held to that as strictly as the generated
ones.

**`source.html` — D, and it should still exist.** His objection was to it being *built by
default*, not to it existing: a reader who wants the unabridged specification should be able
to get it, and a reader who does not should never be handed 1292 lines of raw spec. So the
consent flag was inverted. The safe build is now the one you get for free, and the source
page requires asking for it by name.

Three other things he roasted were the same failure in three costumes — being clever at the
reader's expense. The §3.3 sign correction had grown a fifteen-line Lyapunov proof in a code
comment; the rigour was right and the placement was wrong, so the full argument moved into
[`ERRATA.md`](ERRATA.md) where somebody looking for a proof will find it, and the page and
the comment now point there and stay short. The bullshit-meter figure —
`|1/φ − 5/8| = 0.0070` against a window `0.05` wide — he called brilliantly honest and
glazing to read, so it kept its honesty and lost its prominence.

---

## What is in here

| Directory | Contents | Whose |
|---|---|---|
| `analysis/` | Plain-language primer, appraisal, catch-up brief, the Gerald reading | V>>'s |
| `experiments/` | Two ready-to-file OSF pre-registrations | V>>'s |
| `docs/` | The R4R site presenting all of the above | V>>'s |
| `ERRATA.md` | Two verified transcription errors in the spec, with the full proofs | — |

**Start with the site.** It is the plain-English version — the one you asked for, written so
somebody who has never seen the framework can follow it in one pass. Everything else in here
is supporting apparatus.

**Then read [`ERRATA.md`](ERRATA.md).** Two lines of the specification need changing. Each is
verified by arithmetic, and both will stop the next person who tries to implement from the
paper.

## The site — start here

No framework, no package manager, no build step at serve time.

```bash
python3 -m http.server 4173 --directory docs
# then open http://127.0.0.1:4173/
```

| Page | What it does |
|---|---|
| `index.html` | The explainer. Opens with §3.3 running live — drag a starting κ and watch it fall to 1/φ. Then the seven love equations, then §9's M̂ table as seven answerable rows. |
| `geometries.html` | Addendum A. Seven stress geometries placed on the κ axis by their actual deformation, with the three dual-pair axes drawn. |
| `primer.html` | The long version, every claim tagged back to the section it came from. |
| `gerald.html` | A close reading of the Gerald song — the geometry computed rather than recalled, and the duck held against M̂. |
| `proof.html` | Both pre-registrations in full. |
| `source.html` | The primary texts, unabridged. **Not built unless you ask for it.** |

### Rebuilding

```bash
python3 docs/build.py                 # the default, and the safe one
python3 docs/build.py --with-source   # …and also build source.html
```

**The default build is the safe build.** It omits `source.html` — and deletes a stale copy
left behind by an earlier build rather than merely skipping it, so a page built once cannot
linger on disk and be served. Nothing that reproduces Thomas's unabridged specification can
reach a public deployment by accident. Building
`--with-source` is a deliberate act, and it is only appropriate for a private copy: consent
to publish those documents is Thomas's to give, and he has not given it. If this repository
is ever made public, or the site deployed to GitHub Pages, run the plain
`python3 docs/build.py` and confirm `docs/source.html` is absent before pushing.

Everything except `index.html` and `geometries.html` is generated directly from a file in
this repo, so a page cannot drift from the document it presents. Edit the source document,
not the generated HTML.

## What the appraisal actually concluded

Stated plainly, because a repository that only flatters its subject is no use to it.

**Strongest parts.** The Ŝ / M̂ distinction in §8–9 is the most valuable thing in the
framework, and it survives independently of everything around it. The bilateral-modification
criterion — *who in this system is unchanged?* — is a real test with a £30 measurement
attached (saliva cortisol, or an HRV strap), and it generalises cleanly from pair bonds to
cults, propaganda and addiction. §7.3's insistence that love contains the antiphase mode
rather than lacking it is a genuinely structural claim, not a sentimental one.

**Weakest part.** The identification of the convergence constant specifically with 1/φ. The
measurement window is 0.05 wide and the gap to the nearest rival candidate is 0.0070, so the
data cited cannot distinguish them. Chosen, not confirmed — see `ERRATA.md`.

**What is untested.** Almost all of the empirical claims, which is exactly why
`experiments/` exists.

## The two experiments

Both are written so that they can fail, which is the point.

- **`01-prereg-follicular-eeg.md`** — the framework's own cheapest falsifier, which §12.1
  notes has never been run. Sham-controlled, three-way blinded, each participant their own
  control, with a separate sham-only group establishing the measure's session-to-session
  drift and a positive-control gate before any of it counts.
- **`02-prereg-geomagnetic-hrv.md`** — Bus D tested directly: quiet days (Kp ≤ 2) against
  storm days (Kp ≥ 5), with a phase-shuffled negative control as the inferential yardstick.
  A nominally significant result that fails the shuffle is reported as null.

Both state the prior explicitly: **the null is expected to win.** A pre-committed,
sham-controlled, blinded null is a real result. A positive that turns out to be arousal,
expectation or measurement drift is not, and both designs exist to tell those apart.

## Licence and attribution

This repository holds material with two different owners, and the split is deliberate.

**The specification itself is not in this repository.** ASS-OS / Regulus and Addendum A are
Thomas Frumkin's work (GitHub [@teslasolar](https://github.com/teslasolar)) and are
unpublished. This repository is public, so his documents are deliberately kept out of it —
publishing them is his decision to make, and he has not made it. Everything here explains,
appraises and tests the framework; none of it reproduces it. Measured verbatim overlap with
the source across every page is roughly one percent, which is ordinary quotation.

**Everything else** — `analysis/`, `experiments/`, `docs/`, `ERRATA.md` — is V>>'s
independent work, released under [CC BY 4.0](LICENSE).

## Authors

V>> — analysis, experiments, site
Thomas Frumkin ([@teslasolar](https://github.com/teslasolar)), Konomi Systems — ASS-OS / Regulus,
and the review above

With assistance of Claude Opus 5.

---

Everything here is offered for scrutiny, not as authority. If a read, a score or a
citation-check is wrong, say so and it gets corrected.
