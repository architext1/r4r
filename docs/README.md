# Regulus site

A dependency-free static site for GitHub Pages. Four pages, one stylesheet, one script,
no build step at serve time and no framework.

| Page | Source of truth |
|---|---|
| `index.html` | hand-written explainer; every claim traceable to the spec |
| `gerald.html` | generated from `GERALD.md` |
| `proof.html` | generated from the two `*-prereg-*.md` files in the repo root |
| `source.html` | generated from the primary texts, reproduced unabridged |

## Rebuild

```bash
python3 docs/build.py /path/to/regulus-src            # full site
python3 docs/build.py /path/to/regulus-src --no-source # omit the spec
```

`--no-source` drops `source.html`. **Use it for any public deployment until Thomas has
agreed to his full specification being published** — that page reproduces the unabridged
ASS-OS / Regulus document, and that consent is his to give.

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
