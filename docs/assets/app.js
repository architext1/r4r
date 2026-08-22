/* ============================================================
   Regulus — instrument behaviours.
   No dependencies. Nothing leaves the browser.
   ============================================================ */
'use strict';

const PHI = (1 + Math.sqrt(5)) / 2;
const KAPPA = 1 / PHI;              // 0.6180339887…
const ALPHA = PHI + 2;              // 3.618…  convergence rate
const GAMMA = Math.pow(KAPPA, 5);   // 0.0902… noise amplitude
const BASIN_LO = Math.pow(KAPPA, 5);
const BASIN_HI = 1 - Math.pow(KAPPA, 5);

const STEPS = 620;
const DT = 0.008;

/* §3.3 prints the bracket as (κ − 1/φ), which repels the attractor the same
   section calls stable. Integrated here with the sign corrected — the full
   argument, Lyapunov function included, is E2 in ERRATA.md. β∇²κ is dropped:
   one well-mixed scalar has no neighbour to diffuse to. */
function drift(k) {
  return ALPHA * (KAPPA - k) * (1 - k) * k;
}

/* Deterministic pseudo-noise, so any redraw reproduces exactly. */
function noise(seed) {
  const s = Math.sin(seed * 12.9898) * 43758.5453;
  return (s - Math.floor(s)) - 0.5;
}

function clamp01(k) {
  if (k < 0.001) return 0.001;
  if (k > 0.999) return 0.999;
  return k;
}

function integrate(k0, seed) {
  const vals = [k0];
  let k = k0;
  for (let i = 1; i <= STEPS; i++) {
    k = clamp01(k + drift(k) * DT + GAMMA * noise(i + seed) * DT * 1.4);
    vals.push(k);
  }
  return vals;
}

/* ---------------- κ attractor instrument ---------------- */

function KappaPlot(canvas) {
  this.cv = canvas;
  this.ctx = canvas.getContext('2d');
  this.W = canvas.width;
  this.H = canvas.height;
  this.padL = 52; this.padR = 16; this.padT = 18; this.padB = 30;
  this.pw = this.W - this.padL - this.padR;
  this.ph = this.H - this.padT - this.padB;
  this.traces = [];
  this.live = null;
  this.raf = null;
  this.reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  this.onValue = null;
}

KappaPlot.prototype.y = function (k) { return this.padT + this.ph - k * this.ph; };
KappaPlot.prototype.x = function (i) { return this.padL + (i / STEPS) * this.pw; };

KappaPlot.prototype.drawBasin = function () {
  const c = this.ctx;
  c.fillStyle = 'rgba(168,199,255,0.045)';
  c.fillRect(this.padL, this.y(BASIN_HI), this.pw, this.y(BASIN_LO) - this.y(BASIN_HI));
};

KappaPlot.prototype.drawTicks = function () {
  const c = this.ctx, self = this;
  c.strokeStyle = '#232C3B';
  c.lineWidth = 1;
  c.font = '11px "Courier New", Courier, monospace';
  c.fillStyle = '#4C566A';
  c.textAlign = 'right';
  [0, 0.25, 0.5, 0.75, 1].forEach(function (v) {
    const yy = Math.round(self.y(v)) + 0.5;
    c.beginPath(); c.moveTo(self.padL, yy); c.lineTo(self.W - self.padR, yy); c.stroke();
    c.fillText(v.toFixed(2), self.padL - 9, yy + 4);
  });
};

KappaPlot.prototype.drawUnstable = function () {
  const c = this.ctx, self = this;
  c.setLineDash([3, 4]);
  c.strokeStyle = '#4C566A';
  [0, 1].forEach(function (v) {
    const yy = Math.round(self.y(v)) + 0.5;
    c.beginPath(); c.moveTo(self.padL, yy); c.lineTo(self.W - self.padR, yy); c.stroke();
  });
  c.setLineDash([]);
};

KappaPlot.prototype.drawAttractor = function () {
  const c = this.ctx;
  const ya = Math.round(this.y(KAPPA)) + 0.5;
  c.strokeStyle = '#E8B84B';
  c.lineWidth = 1.5;
  c.beginPath(); c.moveTo(this.padL, ya); c.lineTo(this.W - this.padR, ya); c.stroke();
  c.fillStyle = '#E8B84B';
  c.textAlign = 'left';
  c.fillText('κ* = 1/φ = 0.6180', this.padL + 8, ya - 8);
  c.textAlign = 'right';
  c.fillStyle = '#4C566A';
  c.fillText('time →', this.W - this.padR, this.H - 10);
};

KappaPlot.prototype.grid = function () {
  this.ctx.clearRect(0, 0, this.W, this.H);
  this.drawBasin();
  this.drawTicks();
  this.drawUnstable();
  this.drawAttractor();
};

KappaPlot.prototype.stroke = function (vals, upto, colour, width) {
  const c = this.ctx;
  c.strokeStyle = colour;
  c.lineWidth = width;
  c.lineJoin = 'round';
  c.beginPath();
  const last = Math.min(upto, vals.length - 1);
  for (let i = 0; i <= last; i++) {
    const px = this.x(i), py = this.y(vals[i]);
    if (i === 0) c.moveTo(px, py); else c.lineTo(px, py);
  }
  c.stroke();
};

KappaPlot.prototype.drawHead = function () {
  const c = this.ctx;
  const k = this.live.vals[Math.min(this.live.i, this.live.vals.length - 1)];
  c.fillStyle = '#A8C7FF';
  c.beginPath();
  c.arc(this.x(this.live.i), this.y(k), 3.5, 0, Math.PI * 2);
  c.fill();
  if (this.onValue) this.onValue(k);
};

KappaPlot.prototype.paint = function () {
  const self = this;
  this.grid();
  this.traces.forEach(function (t) { self.stroke(t, STEPS, 'rgba(168,199,255,0.30)', 1.2); });
  if (!this.live) return;
  this.stroke(this.live.vals, this.live.i, '#A8C7FF', 2);
  this.drawHead();
};

KappaPlot.prototype.finish = function () {
  this.live.i = STEPS;
  this.paint();
  this.traces.push(this.live.vals);
  if (this.traces.length > 7) this.traces.shift();
  this.live = null;
  this.raf = null;
};

KappaPlot.prototype.tick = function () {
  if (!this.live) return;
  this.live.i += this.reduced ? 40 : 6;
  if (this.live.i >= STEPS) { this.finish(); return; }
  this.paint();
  this.raf = requestAnimationFrame(this.tick.bind(this));
};

KappaPlot.prototype.release = function (k0) {
  if (this.raf) { cancelAnimationFrame(this.raf); this.raf = null; }
  this.live = { vals: integrate(k0, this.traces.length * 97 + 13), i: 0 };
  this.tick();
};

KappaPlot.prototype.clear = function () {
  if (this.raf) { cancelAnimationFrame(this.raf); this.raf = null; }
  this.traces = [];
  this.live = null;
  this.paint();
};

function revealOnce(el, fn) {
  if (!('IntersectionObserver' in window)) { fn(); return; }
  const io = new IntersectionObserver(function (entries) {
    const hit = entries.some(function (e) { return e.isIntersecting; });
    if (!hit) return;
    io.disconnect();
    fn();
  }, { threshold: 0.35 });
  io.observe(el);
}

function wireKappa() {
  const cv = document.getElementById('kappa');
  if (!cv) return;

  const plot = new KappaPlot(cv);
  const startEl = document.getElementById('kStart');
  const startOut = document.getElementById('kStartOut');
  const kOut = document.getElementById('kOut');

  plot.onValue = function (k) { kOut.textContent = k.toFixed(4); };

  startEl.addEventListener('input', function () {
    const v = parseFloat(startEl.value);
    startOut.textContent = v.toFixed(2);
    if (!plot.live) kOut.textContent = v.toFixed(4);
  });

  document.getElementById('kRun').addEventListener('click', function () {
    plot.release(parseFloat(startEl.value));
  });

  document.getElementById('kClear').addEventListener('click', function () {
    plot.clear();
    kOut.textContent = parseFloat(startEl.value).toFixed(4);
  });

  startOut.textContent = parseFloat(startEl.value).toFixed(2);
  plot.paint();
  revealOnce(cv, function () { plot.release(parseFloat(startEl.value)); });
}

/* ---------------- Ŝ / M̂ diagnostic ---------------- */

const VERDICTS = {
  clean: {
    line: 'Reads as Ŝ throughout.',
    sub: 'Bilateral, calming, and it survives the removal of every constraint. On this ' +
         'framework’s own criteria that is authentic binding — which it says costs 11.8% ' +
         'of your capacity and frees the rest.'
  },
  core: {
    line: 'Both load-bearing rows read as M̂.',
    sub: 'Only one of you is being changed, and your nervous system is more vigilant near them, ' +
         'not less. §9.1 treats that pair as the core signature: “you cannot fake vasodilation. ' +
         'You cannot fake the vagus.” Worth taking to a person rather than a page.'
  },
  unilateral: {
    line: 'Mixed — but the single metric reads M̂.',
    sub: '§9.2 puts all the weight on one question: who in this system is unchanged? Unilateral ' +
         'modification is extraction, the document argues, regardless of the story told about it.'
  }
};

function countMimic(answers) {
  return answers.filter(function (a) { return a === 'm'; }).length;
}

function partialVerdict(done, total, mimic) {
  return {
    line: done + ' of ' + total + ' answered',
    sub: 'Keep going — the reading needs the whole table. ' +
         (mimic > 0 ? mimic + ' so far point to M̂.' : 'Nothing points to M̂ so far.')
  };
}

function fullVerdict(answers) {
  const total = answers.length;
  const mimic = countMimic(answers);
  const unilateral = answers[1] === 'm';   // §9.2 — who in this system is unchanged
  const vigilant = answers[3] === 'm';     // §9.1 — the single metric, HRV-measurable

  if (mimic === 0) return VERDICTS.clean;
  if (unilateral && vigilant) return VERDICTS.core;
  if (mimic >= 4) {
    return {
      line: 'Most rows read as M̂.',
      sub: mimic + ' of ' + total + ' land on the mimic side. The behaviour of M̂ looks like love ' +
           'from outside — that similarity is precisely what makes it work.'
    };
  }
  if (unilateral) return VERDICTS.unilateral;
  return {
    line: 'Mixed reading.',
    sub: mimic + ' of ' + total + ' point to M̂, and the bilateral test passed. Mixed is ordinary — ' +
         '§7.3 is explicit that a real bond contains the discord mode too.'
  };
}

function Diagnostic(root) {
  this.rows = Array.prototype.slice.call(root.querySelectorAll('.drow'));
  this.answers = this.rows.map(function () { return null; });
  this.box = document.getElementById('verdict');
  this.lineEl = document.getElementById('vLine');
  this.subEl = document.getElementById('vSub');
}

Diagnostic.prototype.paintRow = function (idx) {
  const row = this.rows[idx];
  const chosen = this.answers[idx];
  row.querySelectorAll('button').forEach(function (b) {
    b.setAttribute('aria-pressed', String(b.getAttribute('data-v') === chosen));
  });
  row.classList.toggle('is-s', chosen === 's');
  row.classList.toggle('is-m', chosen === 'm');
};

Diagnostic.prototype.choose = function (idx, value) {
  this.answers[idx] = (this.answers[idx] === value) ? null : value;
  this.paintRow(idx);
  this.render();
};

Diagnostic.prototype.render = function () {
  const answered = this.answers.filter(Boolean).length;
  if (answered === 0) { this.box.hidden = true; return; }
  this.box.hidden = false;
  const v = (answered < this.rows.length)
    ? partialVerdict(answered, this.rows.length, countMimic(this.answers))
    : fullVerdict(this.answers);
  this.lineEl.textContent = v.line;
  this.subEl.textContent = v.sub;
};

Diagnostic.prototype.bindRow = function (row, idx) {
  const self = this;
  row.querySelectorAll('button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      self.choose(idx, btn.getAttribute('data-v'));
    });
  });
};

Diagnostic.prototype.bind = function () {
  const self = this;
  this.rows.forEach(function (row, idx) { self.bindRow(row, idx); });
};

function wireDiagnostic() {
  const root = document.getElementById('diag');
  if (!root) return;
  const d = new Diagnostic(root);
  d.bind();
}

/* ---------------- boot ---------------- */

wireKappa();
wireDiagnostic();
