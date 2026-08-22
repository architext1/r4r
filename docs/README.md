# Regulus site

A dependency-free static site for GitHub Pages. Six pages, one stylesheet, one script,
no build step at serve time and no framework.

| Page | Source of truth |
|---|---|
| `index.html` | hand-written explainer; every claim traceable to the spec |
| `primer.html` | generated from `analysis/REGULUS-FOR-DUMMIES.md` |
| `geometries.html` | hand-written from Addendum A |
| `brief.html` | generated from `analysis/REGULUS-BRIEF.md` |
| `gerald.html` | generated from `analysis/GERALD.md` |
| `proof.html` | generated from the two `experiments/*-prereg-*.md` files |
| `source.html` | generated from the primary texts, reproduced unabridged. **Not built unless you ask for it.** |

## Rebuild

```bash
python3 docs/build.py                  # the safe default: no source.html
python3 docs/build.py --with-source    # …and also build source.html
```

**The default build is the safe build.** `source.html` reproduces the unabridged
ASS-OS / Regulus document, and that consent is Thomas's to give, so it is built only
when `--with-source` is passed. The default also *deletes* a stale `source.html` left
on disk by an earlier build, because a file that is merely skipped is still served.

`--no-source` is still accepted and now does nothing — omitting the spec is what
happens anyway. Do not rely on it; rely on the default.

## Enabling Pages

Settings → Pages → Source: *Deploy from a branch* → `master` / `/docs`.
A private repo needs GitHub Pro or Team for Pages; a public repo does not.

## Moving it to another repo

Every path is relative and nothing assumes a repo name, so the whole `docs/` folder can be
copied into another repository's `docs/` and served as-is.

## Honesty notes carried in the site

- §3.3's dynamical equation is printed with a sign that makes κ\* **unstable**, contradicting
  its own stability analysis. The site integrates the intended dynamics and says so.
- The κ\* = 1/φ identification is scored 8/10 on the appraisal's bullshit meter: the
  HeartMath window is 0.05 wide and |1/φ − 5/8| is 0.0070, so nothing yet distinguishes them.
- Claims are tagged established / measured / chosen / untested throughout.
