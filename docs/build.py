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
    ("brief.html", "Brief"),
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
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta name="theme-color" content="#0B0E14">
<meta property="og:type" content="article">
<meta property="og:site_name" content="R4R">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://architext1.github.io/r4r/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://architext1.github.io/r4r/assets/og.png">
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




def _wrap_tables(markup: str) -> str:
    """Put every generated table inside a horizontal scroller.

    A markdown table has no width limit, and on a 390px phone the ones in the
    pre-registrations render 542px wide and push the whole document sideways.
    A CSS child-combinator fallback misses any table nested below the section,
    so the wrap is done structurally here instead — measured on proof.html,
    which overflowed by 124px before this.
    """
    import re as _re
    return _re.sub(r'<table>', '<div class="tw"><table>', markup).replace('</table>', '</table></div>')


def _wrap_operators(markup: str) -> str:
    """Render M̂, Ŝ and σ̂ in a font that composes the circumflex.

    Courier New carries U+0302 as a spacing glyph, so M̂ renders as "M^"
    and never falls through to a font that would stack it. See the .op
    rule in assets/style.css for the measurement.

    The hazard is the combining mark, not the letter it sits on, so the
    statistical σ̂ in the brief needs the same treatment as the two
    Regulus operators. Any further base letter that acquires a U+0302
    must be added here, or it silently renders as "x^".
    """
    import re as _re
    return _re.sub(r'(M\u0302|\u015C|\u03C3\u0302)', r'<span class="op">\1</span>', markup)


def md_to_html(text: str) -> str:
    return _wrap_tables(_wrap_operators(markdown.markdown(text, extensions=MD_EXTENSIONS, output_format="html5")))


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
# brief.html
# --------------------------------------------------------------------------

def build_brief(nav: Nav) -> None:
    """The expert brief — the technical read, for someone who wants the depth.

    Deliberately the one page that does not simplify. Everything else on the
    site works to be followable by a newcomer; this one assumes you have read
    them and want the architecture, the operators worked properly, and an
    honest methodologist's view of the two pre-registrations.
    """
    src = REPO / "analysis" / "REGULUS-BRIEF.md"
    if not src.exists():
        print("skip brief.html — no REGULUS-BRIEF.md")
        return
    body = hero(
        "The technical read &middot; for after the explainer",
        "Regulus, examined",
        "The one page here that does not simplify. Architecture, the three operators worked "
        "in full, what is derived against what is merely defined, and both pre-registrations "
        "assessed the way a hostile reviewer would.",
    ) + section(md_to_html(read(src)))
    (DOCS / "brief.html").write_text(
        page("brief.html", "Regulus Examined",
             "A technical brief on ASS-OS / Regulus: the architecture, the three operators, "
             "and a methodologist's assessment of both pre-registrations.", body, nav),
        encoding="utf-8")
    print("wrote brief.html")


# --------------------------------------------------------------------------
# finding.html
# --------------------------------------------------------------------------

def build_finding(nav: Nav) -> None:
    """The §3.4 scale finding — deliberately not in the nav.

    It belongs at the bottom of the depth ladder with the brief, not spread
    across the explainer, so it is reached from there rather than from the
    masthead. See the layering note in .claude/CLAUDE.md.
    """
    src = REPO / "analysis" / "FINDING-ODDS-VS-FRACTION.md"
    if not src.exists():
        print("skip finding.html — no FINDING-ODDS-VS-FRACTION.md")
        return
    body = hero(
        "A correction to &sect;3.4 &middot; companion to the brief",
        "The right number, the wrong scale",
        "The specification&rsquo;s one piece of empirical confirmation compares a measured "
        "<em>odds</em> against a constant defined as a <em>fraction</em> &mdash; and the "
        "framework&rsquo;s own &sect;3.5 gets the distinction right three lines later.",
    ) + section(md_to_html(read(src)))
    (DOCS / "finding.html").write_text(
        page("finding.html", "The Right Number, The Wrong Scale",
             "Regulus §3.4 compares a coherence odds against a retention fraction. The scale "
             "error is confirmed; what it points at instead is not.", body, nav),
        encoding="utf-8")
    print("wrote finding.html")


# --------------------------------------------------------------------------
# audit.html
# --------------------------------------------------------------------------

def build_audit(nav: Nav) -> None:
    """The equation sweep. Bottom of the ladder, no nav entry."""
    src = REPO / "analysis" / "EQUATION-AUDIT.md"
    if not src.exists():
        print("skip audit.html — no EQUATION-AUDIT.md")
        return
    body = hero(
        "Every checkable number &middot; companion to the brief",
        "The arithmetic is sound",
        "Two errors were found in this specification by computing rather than reading, which "
        "raised the obvious question of how many more there were. This is the sweep. About "
        "twenty-five quantities, and the answer is none.",
    ) + section(md_to_html(read(src)))
    (DOCS / "audit.html").write_text(
        page("audit.html", "The Arithmetic Is Sound",
             "A systematic check of every computable quantity in the Regulus specification — "
             "the prime spine, all eight derived constants, and the golden-ratio algebra.", body, nav),
        encoding="utf-8")
    print("wrote audit.html")


# --------------------------------------------------------------------------
# corrections.html
# --------------------------------------------------------------------------

def build_corrections(nav: Nav) -> None:
    """Drop-in fixes for the two pre-registration defects."""
    src = REPO / "analysis" / "PREREG-CORRECTIONS.md"
    if not src.exists():
        print("skip corrections.html — no PREREG-CORRECTIONS.md")
        return
    body = hero(
        "Before either study is filed &middot; companion to the proof page",
        "Two corrections",
        "Both protocols are ready to file and each has one defect that would waste the "
        "study. Neither is a design flaw. Here is the arithmetic and the replacement text; "
        "the registered values remain the author&rsquo;s to set.",
    ) + section(md_to_html(read(src)))
    (DOCS / "corrections.html").write_text(
        page("corrections.html", "Two Corrections",
             "Drop-in fixes for two defects in the Regulus pre-registrations: a magnitude bar "
             "on the wrong scale, and a permutation null that over-rejects.", body, nav),
        encoding="utf-8")
    print("wrote corrections.html")


# --------------------------------------------------------------------------
# proof.html
# --------------------------------------------------------------------------

PROOF_CORRECTIONS_NOTE = (
    '<p class="col" style="margin:-1rem 0 2rem"><strong>Before filing:</strong>\n'
    '  <a href="corrections.html">Two corrections</a> &mdash; a magnitude bar on the wrong scale,\n'
    '  and a permutation null measured over-rejecting at 13% against a nominal 5%.</p>\n\n'
)

PROOF_INTRO = """
<p>
  A framework earns the word <em>theory</em> by naming the thing that would prove it wrong.
  Regulus names two. Both are cheap to run, and neither had been run. So both were written
  up as pre-registrations and locked.
</p>
<p>
  A pre-registration is a study plan filed in public <strong>before</strong> the work starts.
  Every choice is nailed down in advance. How many people. What gets measured. What counts
  as a result, and when to stop. Lock the rules first and you cannot bend them later to fit
  whatever turns up.
</p>
<p class="pull">
  We state the prior explicitly: we expect the null to win.
  <cite>Pre-registration 01 &middot; study description</cite>
</p>
<p>
  Read that line again. The people who wrote these two studies are saying, in advance and in
  writing, that they expect their own idea to lose. The null is the boring answer: nothing
  happened, no effect, go home.
</p>
<p>
  That is the strongest move a scientist can make. It is worth being clear about why.
</p>
<p>
  Predict you will win, then win, and nobody has learned much. You wanted that answer. You
  went looking for it. You found it. People are very good at finding what they set out to
  find, without meaning to and without noticing.
</p>
<p>
  Write down <em>I expect to be wrong</em> and you take that escape route away. You cannot
  claim afterwards that the result was the one you were hoping for. You cannot quietly move
  the goalposts either, because you already drove them into the ground where everyone can
  see them. If the idea wins anyway, it has won against the house. The people running the
  test were betting the other way.
</p>
<p>
  And if it loses, nothing is wasted. A clean <em>no</em> is a real finding. It closes a
  question that was open, and it saves the next person a year. Both studies below are built
  so that <em>no</em> is an answer they can actually reach.
</p>
<p>
  There is a catch, and both designs take it seriously. A <em>yes</em> can be manufactured by
  accident. Nerves can do it. So can expectation. So can a measuring instrument that drifts
  between one day and the next. Each study is built to tell a real <em>yes</em> apart from
  those three impostors. That is why so much of the machinery below is spent on the fake
  version of the procedure rather than the real one.
</p>
"""

# The plain-English panels. These sit ABOVE each pre-registration and explain, in
# ordinary words, what the experiment does. The formal document below them is left
# exactly as filed: it has to stay a document an ethics committee would accept, and
# rewriting it to read more easily would destroy it. So the reading level is fixed
# the other way round - by putting a grade-7 explanation in front of it, not by
# simplifying a grade-16 document that has to keep every parameter it states.

PLAIN_01 = """
<h3>What they think is going on</h3>
<p>
  Autistic brains are noisier at rest. That is not a figure of speech. Hook someone up to an
  EEG, which reads brain waves through the scalp, and the trace from an autistic adult
  carries measurably more disorder than average. Scientists have a name for how much disorder
  sits in a signal. They call it entropy. Most brain scientists put the extra entropy down to
  an imbalance between the brain&rsquo;s own accelerator and its brake &mdash; the excitatory
  and inhibitory signals.
</p>
<p>
  Regulus offers a different source for the same noise. It says hair follicles work as light
  sensors, all over the body. It points at two light-catching proteins found in them: OPN3,
  and the cryptochromes CRY1 and CRY2. It says your body gives off a faint light of its own,
  called biophotons. And it says that when oil blocks a follicle, that sensor starts
  misreading your own faint light as a message coming in. The brain is then flooded with
  signals that mean nothing.
</p>
<p>
  If that is right, unblocking the pores should quieten the brain. Nobody has ever checked.
</p>

<h3>What they will actually do</h3>
<p>
  Take autistic adults. Give each one a real scalp-clearing session that lifts the oil out of
  the follicles. On another day, give the same person a fake one. Which comes first is
  decided at random, so the order cannot skew the answer.
</p>
<p>
  The fake is the whole trick. Same length, same chair, same person doing it. Same touch,
  same smell, same feel of the product on the skin. One thing is missing: it does not shift
  the oil. Nobody in the room knows which session is which &mdash; not the person in the
  chair, not the technician running the EEG, not the analyst who later crunches the numbers.
  Who got what is sealed in an envelope and held by someone outside the study.
</p>
<p>
  Brain waves are recorded for five minutes with eyes closed, on at least thirty-two points
  around the head. Once before each session, once after. So every person is their own
  comparison: real day against fake day. The number being watched is a measure of disorder
  called R&eacute;nyi entropy, averaged across the whole scalp.
</p>
<p>
  A second group of about twenty people gets two fake sessions and nothing else. They answer
  a dull but vital question. How far does this measurement wander on its own, from one day to
  the next, when nothing has been done at all?
</p>
<p>
  Forty people in the main group, hoping thirty-four finish both days. About twenty in the
  fake-only group. Roughly sixty in all. That size is chosen to catch a middling effect and
  no smaller. If the effect is real but tiny, this study will miss it, and it says so.
</p>

<h3>How they will know if they are wrong</h3>
<p>
  Two hurdles, both fixed before anyone collects a number.
</p>
<p>
  First, the real session has to beat the fake one. If both move the entropy reading by about
  the same amount, the claim is dead.
</p>
<p>
  Second &mdash; and this is the hurdle that catches wishful thinking &mdash; the gap has to
  be bigger than the wobble. The fake-only group tells you how far the reading drifts by
  itself. The bar is set at 1.96 times that drift, near enough two of them. A real-minus-fake
  gap that comes in under the bar is written up as noise, not as a result, even when the
  statistics call it significant.
</p>
<p>
  There is a check on the kit as well. Every session records the brain with eyes open and
  then with eyes closed, which is a known and reliable shift. If the equipment cannot pick
  that up, it cannot be trusted to pick up anything smaller. No verdict on the biology is
  drawn either way.
</p>

<h3>Why this one is worth doing</h3>
<p>
  It is the framework&rsquo;s cheapest claim and its boldest. Regulus admits as much itself:
  this experiment has never been run.
</p>
<p>
  One thing needs saying plainly, because the design says it plainly too. This is not a
  treatment. Nobody is testing whether washing your scalp helps autism, and nothing here
  should be read that way. The question is narrow. Does clearing the pores move one
  brain-wave number more than a fake does?
</p>
"""

PLAIN_02 = """
<h3>What they think is going on</h3>
<p>
  Regulus claims the Earth&rsquo;s magnetic field reaches into your body and nudges your
  heart.
</p>
<p>
  The mechanism it offers goes like this. The gap between the ground and the upper atmosphere
  rings like a bell, struck all day by lightning around the world, at a base note near 7.83
  times a second. The framework calls this a channel the body listens to, and names it Bus D.
  If it is real, then the part of your nervous system that sets your heart rhythm without
  asking you should shift when that field turns rough.
</p>
<p>
  The study Regulus leans on, by McCraty and colleagues in 2017, found exactly that. But that
  study only watched. It changed nothing. It used a small group of volunteers who were easy
  to recruit, and it was paid for by the organisation whose idea it was. The wider field has
  a poor record here. Results keep appearing, then failing to turn up again once somebody
  accounts for the seasons.
</p>

<h3>What they will actually do</h3>
<p>
  You cannot switch the Earth off. So nothing gets changed. They watch instead, and put the
  whole weight of the answer on the controls.
</p>
<p>
  Forty healthy adults, spread across at least two places far apart. Every morning for sixty
  days, each one sits still for five minutes wearing a chest strap that reads the heart
  directly. Same window of the clock each day. A wrist tracker will not do, because it is not
  accurate enough to catch the fine detail. They also log sleep, coffee, alcohol, illness and
  exercise. Local weather is pulled in for each site.
</p>
<p>
  What gets measured is the gap between one heartbeat and the next. Those gaps are never
  quite even, and the pattern in them is called heart rate variability. When the pattern
  settles into one smooth, steady wave, that is what the study means by coherence. Coherence
  is the number being watched.
</p>
<p>
  The magnetic weather comes from a public government feed, on a fixed scale called Kp. What
  counts as quiet and what counts as stormy is written down here, before anyone looks. Quiet
  means the day peaks at 2 or below. Stormy means 5 or above. Days in the middle are set
  aside from the main comparison. A person&rsquo;s data only enters that comparison if they
  caught at least six quiet days and at least six stormy ones.
</p>
<p>
  The people taking part are never told the study is about magnetism. If they knew, somebody
  might start breathing calmly on days they guessed were stormy, and manufacture the result
  by hand. The analyst does not know which days are which either.
</p>
<p>
  Sixty days each, forty people. Up to 2,400 person-days of recording, with thirty people
  expected to finish holding enough of both kinds of day.
</p>

<h3>How they will know if they are wrong</h3>
<p>
  Here is the part doing the real work.
</p>
<p>
  Any two things that both drift with the seasons will look connected even when neither
  touches the other. The Sun turns on a rhythm of about twenty-seven days. So does a good
  deal of human biology. Lay those two side by side and you get a handsome correlation that
  means nothing at all.
</p>
<p>
  So they break the link on purpose. They take the record of magnetic storms and slide it
  along in time, more than a thousand different ways. That keeps its shape but destroys its
  line-up with the real days. Then they run the whole analysis again on every shuffled
  version. It tells you what size of effect pure coincidence can produce.
</p>
<p>
  The real answer only counts if it beats almost all of those thousand fakes. A result that
  clears the usual statistics bar but not this one is written up as nothing.
</p>
<p>
  There is a second test, and it is the harder one to fake. Take strangers in different
  places, who have never met and share no weather, no household and no habits. If one global
  field is pushing on all of them, they should still move together day by day. Their days get
  shuffled a thousand times too.
</p>
<p>
  If both tests come back empty, then Bus D is a metaphor and not a channel. The
  pre-registration says so in those words.
</p>

<h3>Why this one is worth doing</h3>
<p>
  Because the honest version of this question has never been asked. The evidence that exists
  is the weak kind. Watched rather than tested, and gathered by people who wanted a
  particular answer.
</p>
<p>
  The authors expect a null here as well, or an effect so small it hardly matters. Published
  results in this area report correlations of about 0.1 to 0.2. That is faint enough that
  seasonal drift alone could produce them. If a real effect does survive the shuffle test, it
  would be a genuine surprise, and worth everyone&rsquo;s attention.
</p>
"""


def plain_panel(body: str) -> str:
    """The grade-7 explanation that sits above an untouched formal document."""
    return (
        f'<div class="panel">\n'
        f'<span class="panel-label">In plain English &middot; the formal document follows</span>\n'
        f"{body}"
        f"</div>\n"
    )


def build_proof(nav: Nav) -> None:
    one = REPO / "experiments" / "01-prereg-follicular-eeg.md"
    two = REPO / "experiments" / "02-prereg-geomagnetic-hrv.md"
    parts = [
        hero(
            "Two ready-to-file study plans &middot; OSF pre-registrations",
            "The loops worth running",
            "The two cheapest claims Regulus makes that could be shown false &mdash; written "
            "up so that they can fail.",
        ),
        # Rendered here rather than hand-added to the built file: a note edited
        # into proof.html directly is silently deleted by the next rebuild.
        PROOF_CORRECTIONS_NOTE,
        section(PROOF_INTRO),
    ]
    for label, path, plain in [
        ("01 &mdash; Follicular clearance and scalp-EEG entropy", one, PLAIN_01),
        ("02 &mdash; Geomagnetic activity and HRV coherence", two, PLAIN_02),
    ]:
        head = f"<h2>{label}</h2>\n" + plain_panel(plain)
        # The pre-registration is rendered verbatim. It is a filable scientific
        # document, and every parameter in it is load-bearing.
        rest = md_to_html(read(path)) if path.exists() else "<p>Source file not found.</p>"
        parts.append(section(head + rest))
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
    build_brief(nav)
    build_finding(nav)
    build_audit(nav)
    build_corrections(nav)
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
