#!/usr/bin/env python3
"""Generate the Regulus site pages from their primary sources.

Every page except index.html is produced from a real file on disk, so the
site cannot drift from the documents it claims to present. Re-run after any
source changes:

    python3 docs/build.py                 # safe default: no spec page
    python3 docs/build.py --with-source   # adds source.html - see below

source.html reproduces Thomas's ASS-OS / Regulus specification in full, and
that document has not been published. It is therefore NOT built unless
--with-source is passed explicitly. Publishing a person's specification is
his call to make, not ours, and a public deploy must not depend on anyone
remembering a flag. (--no-source is still accepted; it is now a no-op, since
omitting the spec is what happens anyway.)

Requires: markdown (pip install markdown).
"""

from __future__ import annotations

import html
import pathlib
import sys

try:
    import markdown
except ImportError:  # pragma: no cover - operator-facing guard
    sys.exit("build.py needs the 'markdown' package: pip install markdown")

DOCS = pathlib.Path(__file__).resolve().parent
REPO = DOCS.parent

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list"]

NAV_BASE = [
    ("index.html", "Explainer"),
    ("primer.html", "Primer"),
    ("geometries.html", "Geometries"),
    ("gerald.html", "Gerald"),
    ("proof.html", "Proof"),
]

# Only ever appended when source.html is actually written. A nav link to a
# page that was not built is a broken site.
NAV_SOURCE = ("source.html", "Source")

HEAD = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} &middot; R4R</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="mast">
  <div class="wrap mast-in">
    <span class="sigil">&#945; Leonis &middot; <b>REGULUS</b></span>
    <nav class="mast-nav" aria-label="Primary">
      <span class="sigil r4r">R4R</span>
{nav}
    </nav>
  </div>
</header>
<main id="main">
<div class="wrap">
"""

FOOT = """</div>
</main>
<footer>
  <div class="wrap">
    <p class="cred">
      REGULUS / ASS-OS &mdash; Thomas (@ThomasTheTankEngineer), Konomi Systems<br>
      Explainer, appraisal and pre-registrations &mdash; V&gt;&gt;<br>
      With assistance of Claude Opus 5 &middot; <a href="https://github.com/teslasolar/eth">github.com/teslasolar/eth</a>
    </p>
    <p style="max-width:60ch">
      Written to be checked, not believed. This page is generated directly from its source
      file by <code>docs/build.py</code>, so it cannot drift from the document it presents.
    </p>
  </div>
</footer>
</body>
</html>
"""


Nav = list[tuple[str, str]]


def nav_html(current: str, nav: Nav) -> str:
    out = []
    for href, label in nav:
        mark = ' aria-current="page"' if href == current else ""
        out.append(f'      <a href="{href}"{mark}>{label}</a>')
    return "\n".join(out)


def page(current: str, title: str, desc: str, body: str, nav: Nav) -> str:
    return HEAD.format(title=title, desc=html.escape(desc, quote=True),
                       nav=nav_html(current, nav)) + body + FOOT



def _wrap_operators(markup: str) -> str:
    """Render M̂ and Ŝ in a font that composes the circumflex.

    Courier New carries U+0302 as a spacing glyph, so M̂ renders as "M^"
    and never falls through to a font that would stack it. See the .op
    rule in assets/style.css for the measurement.
    """
    import re as _re
    return _re.sub(r'(M\u0302|\u015C)', r'<span class="op">\1</span>', markup)


def md_to_html(text: str) -> str:
    return _wrap_operators(markdown.markdown(text, extensions=MD_EXTENSIONS, output_format="html5"))


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def hero(eyebrow: str, heading: str, standfirst: str) -> str:
    return (
        f'<div class="hero">\n'
        f'  <p class="eyebrow">{eyebrow}</p>\n'
        f'  <h1>{heading}</h1>\n'
        f'  <p class="standfirst">{standfirst}</p>\n'
        f"</div>\n"
    )


def section(body: str) -> str:
    return f'<section>\n<div class="doc col">\n{body}\n</div>\n</section>\n'


def verbatim(label: str, path: pathlib.Path, note: str) -> str:
    """Render a primary text verbatim inside a scrollable well."""
    if not path.exists():
        return (
            f'<div class="panel"><span class="panel-label">{label}</span>'
            f"<p>Not present at <code>{html.escape(str(path))}</code>.</p></div>"
        )
    body = html.escape(read(path))
    kb = path.stat().st_size / 1024
    return (
        f"<h3>{label}</h3>\n<p>{note}</p>\n"
        f'<p class="meta" style="font-family:var(--mono);font-size:0.7rem;'
        f'letter-spacing:0.1em;text-transform:uppercase;color:var(--dim)">'
        f"{html.escape(path.name)} &middot; {kb:.0f} KB</p>\n"
        f'<pre class="src">{body}</pre>\n'
    )


# --------------------------------------------------------------------------
# gerald.html
# --------------------------------------------------------------------------

def build_gerald(nav: Nav) -> None:
    src = REPO / "analysis" / "GERALD.md"
    if not src.exists():
        print("skip gerald.html — no GERALD.md")
        return
    body = hero(
        "Companion piece &middot; a cube who refuses to stay a box",
        "What does Gerald want?",
        "Thomas wrote a song about a cube that turns itself inside out. It reads as a joke "
        "for about thirty seconds, and then it turns out to obey the sin geometry in his own "
        "addendum, and to encode the framework&rsquo;s fixed point more precisely than the "
        "specification does.",
    ) + section(md_to_html(read(src)))
    (DOCS / "gerald.html").write_text(
        page("gerald.html", "What Does Gerald Want?",
             "A close reading of Thomas's Gerald song — the geometry, the sin addendum, "
             "and the duck standing on Regulus's coercion test.", body, nav),
        encoding="utf-8")
    print("wrote gerald.html")


# --------------------------------------------------------------------------
# primer.html
# --------------------------------------------------------------------------

def build_primer(nav: Nav) -> None:
    src = REPO / "analysis" / "REGULUS-FOR-DUMMIES.md"
    if not src.exists():
        print("skip primer.html — no REGULUS-FOR-DUMMIES.md")
        return
    body = hero(
        "The long version &middot; every claim tagged to its source",
        "Regulus, from the bottom",
        "The same walk as the explainer, at four times the depth. Each claim carries a tag "
        "back to the section it came from, and the ten marked <em>inference</em> are the "
        "author&rsquo;s to challenge first.",
    ) + section(md_to_html(read(src)))
    (DOCS / "primer.html").write_text(
        page("primer.html", "Regulus From the Bottom",
             "A full plain-English primer on Regulus / ASS-OS, with every claim tagged to "
             "the section of the source it came from.", body, nav),
        encoding="utf-8")
    print("wrote primer.html")


# --------------------------------------------------------------------------
# proof.html
# --------------------------------------------------------------------------

PROOF_INTRO = """
<p>
  A framework earns the word <em>theory</em> by naming the observation that would kill it.
  Regulus names two, and both are cheap. Neither had been run, so they were written up as
  formal pre-registrations &mdash; every procedure, parameter, sample size, blinding scheme
  and stopping rule fixed <strong>before</strong> any data is collected, so the result cannot
  be steered after the fact.
</p>
<p class="pull">
  We state the prior explicitly: we expect the null to win.
  <cite>Pre-registration 01 &middot; study description</cite>
</p>
<p>
  That sentence is the most important one on this site. A pre-committed, sham-controlled,
  blinded null is a real scientific result. A &ldquo;positive&rdquo; that turns out to be
  arousal, expectation or measurement drift is not, and both designs are built specifically
  to tell those apart.
</p>
"""


def build_proof(nav: Nav) -> None:
    one = REPO / "experiments" / "01-prereg-follicular-eeg.md"
    two = REPO / "experiments" / "02-prereg-geomagnetic-hrv.md"
    parts = [
        hero(
            "Two ready-to-file OSF pre-registrations",
            "The loops worth running",
            "Both of the framework&rsquo;s cheapest falsifiable predictions, written up so "
            "that they can fail.",
        ),
        section(PROOF_INTRO),
    ]
    for label, path, note in [
        ("01 &mdash; Follicular clearance and scalp-EEG entropy", one,
         "The framework&rsquo;s single cheapest prediction, and one it admits has never been "
         "run. Each participant is their own control across a real clearance session and a "
         "procedurally identical sham, order-counterbalanced, with a parallel sham-only group "
         "establishing the measure&rsquo;s own session-to-session drift."),
        ("02 &mdash; Geomagnetic activity and HRV coherence", two,
         "Bus D, tested directly: does an individual&rsquo;s HRV coherence differ between "
         "quiet days (Kp &le; 2) and storm days (Kp &ge; 5) by a margin a phase-shuffled "
         "negative control cannot reproduce? Exposure cannot be manipulated, so the entire "
         "evidential weight rests on the controls."),
    ]:
        if path.exists():
            parts.append(section(f"<h2>{label}</h2>\n" + md_to_html(read(path))))
        else:
            parts.append(section(f"<h2>{label}</h2>\n<p>Source file not found.</p>"))
    (DOCS / "proof.html").write_text(
        page("proof.html", "The Loops Worth Running",
             "Two ready-to-file OSF pre-registrations for Regulus's cheapest falsifiable "
             "predictions — both written to be capable of failing.",
             "".join(parts), nav),
        encoding="utf-8")
    print("wrote proof.html")


# --------------------------------------------------------------------------
# source.html
# --------------------------------------------------------------------------

SOURCE_INTRO = """
<p>
  Everything on the explainer page is traceable to the documents below. They are reproduced
  in full and unedited so that any claim can be checked against the author&rsquo;s own words
  rather than a summary of them.
</p>
<p>
  Where the explainer says something the source does not, it is marked as inference. Where
  the two disagree &mdash; as with the sign of the &sect;3.3 dynamical equation &mdash; the
  disagreement is stated rather than quietly corrected.
</p>
"""


def build_source(src_dir: pathlib.Path, nav: Nav) -> None:
    parts = [
        hero(
            "Primary text &middot; unabridged",
            "Read it yourself",
            "The specification, the appraisal and the addendum, in full.",
        ),
        section(SOURCE_INTRO),
    ]
    blocks = [
        ("ASS-OS / Regulus &mdash; specification", src_dir / "ass-os-regulus.txt",
         "The core document. Prime recursion spine, the convergence constant, the level "
         "architecture, the five buses, the seven love equations, and both operators."),
        ("Regulus addendum &mdash; the sins", src_dir / "regulus-addendum-sins.txt",
         "Seven geometries for the seven ways a system deforms when it runs alone. "
         "Binding is described here as the return to shape."),
        ("Catch-up and experiment design", REPO / "analysis" / "regulus-catchup-and-experiment.md",
         "The working document behind the two pre-registrations."),
        ("Measurement-first appraisal", REPO / "analysis" / "00-catch-up-and-appraisal.md",
         "An independent read of the framework, scored claim by claim &mdash; including the "
         "8/10 rating on the golden-ratio identification."),
    ]
    body = "".join(verbatim(label, path, note) for label, path, note in blocks)
    parts.append(f'<section>\n<div class="doc">\n{body}\n</div>\n</section>\n')
    (DOCS / "source.html").write_text(
        page("source.html", "Regulus Primary Text",
             "The ASS-OS / Regulus specification, the sins addendum, the experiment design "
             "and the appraisal — reproduced in full and unedited.",
             "".join(parts), nav),
        encoding="utf-8")
    print("wrote source.html")


USAGE = """usage: build.py [SRC_DIR] [--with-source] [--no-source]

  SRC_DIR        where the primary texts live (default: <repo>/sources)
  --with-source  also build source.html, which reproduces Thomas's ASS-OS /
                 Regulus specification in full. Off by default: that document
                 is unpublished, and the decision to publish it is his.
  --no-source    accepted, and does nothing. Omitting the spec is the default.
  --help, -h     print this and exit
"""

CONSENT_WARNING = (
    "build.py: WARNING - this build includes source.html, which reproduces an "
    "unpublished third-party specification in full. Do not deploy it publicly "
    "without the author's consent."
)

KNOWN_FLAGS = {"--with-source", "--no-source", "--help", "-h"}


def main() -> None:
    """Build the site. Run with --help for the flags."""
    flags = [a for a in sys.argv[1:] if a.startswith("-")]
    positional = [a for a in sys.argv[1:] if not a.startswith("-")]

    unknown = [f for f in flags if f not in KNOWN_FLAGS]
    if unknown:
        sys.exit(f"build.py: unknown flag {unknown[0]}\n\n{USAGE}")
    if {"--help", "-h"} & set(flags):
        print(USAGE, end="")
        return

    with_source = "--with-source" in flags
    src_dir = pathlib.Path(positional[0]) if positional else REPO / "sources"
    nav = (NAV_BASE + [NAV_SOURCE]) if with_source else list(NAV_BASE)

    build_gerald(nav)
    build_primer(nav)
    build_proof(nav)
    if with_source:
        print(CONSENT_WARNING, file=sys.stderr)
        build_source(src_dir, nav)
    else:
        # Delete rather than merely skip: a stale source.html left on disk from
        # an earlier build would still be served, flag or no flag.
        (DOCS / "source.html").unlink(missing_ok=True)
        print("omitted source.html (pass --with-source to include the spec)")


if __name__ == "__main__":
    main()
