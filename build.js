// Static site builder: content/*.md  ->  _site/*.html
// Markdown via marked, maths via KaTeX (rendered at build time), ::: containers for callouts.
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');
marked.setOptions({ breaks: true });
const katex = require('katex');

const ROOT = __dirname;
const OUT = path.join(ROOT, '_site');

// ---------------------------------------------------------------- navigation
const site = require('./site.json');

function flatPages(nav, parent = null, acc = []) {
  for (const item of nav) {
    if (item.file) acc.push({ ...item, parent });
    if (item.children) flatPages(item.children, item, acc);
  }
  return acc;
}
const pages = flatPages(site.nav);

// ---------------------------------------------------------------- markdown helpers
function slugify(s) {
  return s.toLowerCase().replace(/<[^>]+>/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function renderMath(tex, display) {
  try {
    return katex.renderToString(tex, { displayMode: display, throwOnError: false, strict: false, trust: true,
      macros: { '\\R': '\\mathbb{R}', '\\bm': '\\boldsymbol{#1}', '\\T': '^{\\top}' } });
  } catch (e) {
    return `<code class="math-error">${tex}</code>`;
  }
}

// Replace maths and code with placeholders so marked does not touch them.
function protect(src, store) {
  // fenced code
  src = src.replace(/```[\s\S]*?```/g, m => { store.push({ raw: m }); return `\uE000${store.length - 1}\uE000`; });
  // display math $$...$$
  src = src.replace(/\$\$([\s\S]+?)\$\$/g, (m, t) => { store.push({ html: renderMath(t.trim(), true) }); return `\uE000${store.length - 1}\uE000`; });
  // inline code
  src = src.replace(/`[^`\n]+`/g, m => { store.push({ raw: m }); return `\uE000${store.length - 1}\uE000`; });
  // inline math $...$ (not $$, not escaped \$)
  src = src.replace(/(^|[^\\$])\$([^\s$](?:[^$\n]*?[^\s\\$])?)\$(?!\d)/g, (m, pre, t) => {
    store.push({ html: renderMath(t, false) }); return `${pre}\uE000${store.length - 1}\uE000`;
  });
  return src.replace(/\\\$/g, '$');
}

function restore(html, store) {
  // raw items go back through marked inline (code) - simplest: restore raw then let marked handle
  return html.replace(/\uE000(\d+)\uE000/g, (m, i) => store[+i].html !== undefined ? store[+i].html : store[+i].raw);
}

const LABELS = {
  def: 'Definition', thm: 'Theorem / Key result', example: 'Worked example', warn: 'Common trap',
  ml: 'Where this shows up in AI', remember: 'Remember', note: 'Note', exam: 'Exam pattern',
  check: 'Check yourself', proof: 'Derivation', intuition: 'Intuition', slide: 'From the slides',
};

// Parse ::: containers (nestable) into HTML, rendering inner markdown recursively.
function renderBlocks(src, store) {
  const lines = src.split('\n');
  const out = [];
  let buf = [];
  const stack = [];
  const flush = () => { if (buf.length) { out.push({ md: buf.join('\n') }); buf = []; } };
  // build a tree
  const root = { children: [] };
  let cur = root;
  for (const line of lines) {
    const open = line.match(/^:::\s*([a-z]+)\s*(.*)$/);
    if (open && open[1]) {
      cur.children.push({ md: buf.join('\n') }); buf = [];
      const node = { type: open[1], title: open[2].trim(), children: [], parent: cur };
      cur.children.push(node); cur = node;
    } else if (/^:::\s*$/.test(line) && cur !== root) {
      cur.children.push({ md: buf.join('\n') }); buf = [];
      cur = cur.parent;
    } else buf.push(line);
  }
  cur.children.push({ md: buf.join('\n') });
  const emit = node => node.children.map(c => {
    if (c.md !== undefined) return c.md.trim() ? restore(marked.parse(c.md), store) : '';
    const inner = emit(c);
    const title = c.title ? restore(marked.parseInline(c.title), store) : '';
    if (c.type === 'solution' || c.type === 'answer' || c.type === 'hint') {
      const lab = { solution: 'Solution & marking', answer: 'Answer', hint: 'Hint' }[c.type];
      return `<details class="solution ${c.type}"><summary>${title || lab}</summary><div class="sol-body">${inner}</div></details>`;
    }
    if (c.type === 'figs') {
      const items = c.children.map(x => x.md || '').join('\n').split('\n').map(l => l.trim()).filter(Boolean);
      return `<div class="figs">${items.map(l => { const [f, cap] = l.split('|');
        return `<figure><a href="assets/fig/${f}.jpg" class="zoom"><img src="assets/fig/${f}.jpg" alt="${cap || ''}" loading="lazy" decoding="async"></a><figcaption>${f.replace(/^m(\d+)-p0*(\d+).*$/, 'Module $1 notes · PDF p.$2')} — ${cap || ''}</figcaption></figure>`; }).join('')}</div>`;
    }
    if (c.type === 'background' || c.type === 'derive') {
      const lab = c.type === 'background' ? 'Background you need' : 'Where does this come from?';
      const icon = c.type === 'background' ? '\u{1F9E9}' : '\u{1F50D}';
      return `<details class="explain ${c.type}"><summary><span class="ex-icon">${icon}</span><span class="ex-lab">${lab}</span>${title ? `<span class="ex-title">${title}</span>` : ''}</summary><div class="ex-body">${inner}</div></details>`;
    }
    if (c.type === 'orig') {
      return `<div class="orig-q"><div class="oq-head"><span class="oq-lab">\u{1F4C4} Original question</span>${title ? `<span class="oq-src">${title}</span>` : ''}</div><div class="oq-body">${inner}</div></div><div class="oq-sol">Worked solution</div>`;
    }
    if (c.type === 'origc') {
      return `<details class="orig-q oq-fold"><summary><span class="oq-lab">\u{1F4C4} Original question</span>${title ? `<span class="oq-src">${title}</span>` : ''}<span class="oq-hint">tap to show</span></summary><div class="oq-body">${inner}</div></details>`;
    }
    if (c.type === 'question') {
      return `<section class="question"><div class="q-head">${title}</div>${inner}</section>`;
    }
    const lab = LABELS[c.type] || c.type;
    return `<div class="callout ${c.type}"><div class="callout-title">${lab}${title ? ': ' + title : ''}</div>${inner}</div>`;
  }).join('\n');
  return emit(root);
}

function mdToHtml(src) {
  const store = [];
  src = protect(src, store);
  // raw code placeholders must be parsed by marked as code: restore them before block parse
  src = src.replace(/\uE000(\d+)\uE000/g, (m, i) => store[+i].raw !== undefined ? store[+i].raw : m);
  let html = renderBlocks(src, store);
  // headings ids
  const toc = [];
  html = html.replace(/<h([23])>([\s\S]*?)<\/h\1>/g, (m, lvl, inner) => {
    const id = slugify(inner.replace(/<span class="katex[\s\S]*?<\/span>\s*<\/span>\s*<\/span>/g, '')) || 'sec';
    let uid = id, k = 2; while (toc.find(t => t.id === uid)) uid = id + '-' + k++;
    toc.push({ lvl: +lvl, id: uid, text: inner });
    return `<h${lvl} id="${uid}"><a class="anchor" href="#${uid}" aria-hidden="true">#</a>${inner}</h${lvl}>`;
  });
  html = html.replace(/<table>/g, '<div class="tbl"><table>').replace(/<\/table>/g, '</table></div>');
  return { html, toc };
}

// ---------------------------------------------------------------- template
function navHtml(current) {
  const item = it => {
    if (it.section) return `<div class="nav-section">${it.section}</div>`;
    if (it.children) {
      const open = it.children.some(c => c.id === current.id);
      return `<details class="grp"${open ? ' open' : ''}><summary>${it.title}</summary>${it.children.map(c =>
        `<a href="${c.id}.html"${c.id === current.id ? ' class="on" aria-current="page"' : ''}>${c.title}</a>`).join('')}</details>`;
    }
    return `<a href="${it.id}.html"${it.id === current.id ? ' class="on" aria-current="page"' : ''}>${it.title}</a>`;
  };
  return site.nav.map(item).join('\n');
}

const plain = s => s.replace(/<[^>]+>/g, '');
const THEME_BOOT = `(function(){try{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.dataset.theme=t;}catch(e){}})();`;

function page(p, body, toc) {
  const idx = pages.findIndex(x => x.id === p.id);
  const prev = pages[idx - 1], next = pages[idx + 1];
  const h2 = toc.filter(t => t.lvl === 2);
  const tocHtml = h2.length > 1
    ? `<div class="toc"><div class="toc-title">On this page</div>${toc.map(t => `<a href="#${t.id}" class="${t.lvl === 3 ? 'h3' : ''}">${t.text}</a>`).join('')}</div>` : '';
  const isQuiz = /quiz|mock|answers|practice/i.test(p.id);
  const crumb = p.parent && p.parent.title ? p.parent.title : '';
  const label = (x) => x.parent && x.parent.title ? `${x.parent.title.split(' · ')[0]} · ${x.title}` : x.title;
  return `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${plain(crumb ? crumb + ' — ' + p.title : p.title)} · ${site.short}</title>
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#fbfbfa" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#16161a" media="(prefers-color-scheme: dark)">
<script>${THEME_BOOT}</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<link rel="stylesheet" href="assets/style.css">
</head><body>
<header class="topbar">
  <button class="iconbtn" id="menuBtn" aria-label="Open contents" aria-expanded="false"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
  <a class="topbrand" href="index.html">${site.short}<span>${plain(crumb || p.title)}</span></a>
  <button class="iconbtn themebtn" aria-label="Toggle dark mode"><svg class="i-moon" viewBox="0 0 24 24" width="19" height="19"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="currentColor"/></svg><svg class="i-sun" viewBox="0 0 24 24" width="19" height="19"><circle cx="12" cy="12" r="4.5" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></g></svg></button>
</header>
<div class="scrim" id="scrim"></div>
<div class="wrap">
<aside class="side" id="side">
  <div class="side-head">
    <a class="brand" href="index.html">${site.short} — ${site.title}<span>${site.subtitle}</span></a>
    <button class="iconbtn themebtn" aria-label="Toggle dark mode"><svg class="i-moon" viewBox="0 0 24 24" width="17" height="17"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="currentColor"/></svg><svg class="i-sun" viewBox="0 0 24 24" width="17" height="17"><circle cx="12" cy="12" r="4.5" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></g></svg></button>
  </div>
  <nav>${navHtml(p)}</nav>
  ${tocHtml}
</aside>
<main>
  ${crumb ? `<div class="crumb">${crumb}</div>` : ''}
  ${isQuiz ? `<div class="quiz-tools"><button data-sol="open">Show all solutions</button><button data-sol="close">Hide all</button><button onclick="window.print()">Print</button></div>` : ''}
  ${body}
  <nav class="pagenav">
    ${prev ? `<a class="pv" href="${prev.id}.html">← Previous<b>${label(prev)}</b></a>` : '<span></span>'}
    ${next ? `<a class="nx" href="${next.id}.html">Next →<b>${label(next)}</b></a>` : '<span></span>'}
  </nav>
  <div class="foot">${site.short} · Fall 2026 · study notes</div>
</main>
</div>
<div class="lightbox" id="lightbox" hidden><img alt=""><button class="iconbtn lb-close" aria-label="Close">✕</button></div>
<script src="assets/site.js" defer></script>
</body></html>`;
}

// ---------------------------------------------------------------- build
fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(path.join(OUT, 'assets'), { recursive: true });
fs.cpSync(path.join(ROOT, 'assets'), path.join(OUT, 'assets'), { recursive: true });
fs.cpSync(path.join(ROOT, 'pdfs'), path.join(OUT, 'pdfs'), { recursive: true });
fs.cpSync(path.join(ROOT, 'files'), path.join(OUT, 'files'), { recursive: true });
fs.writeFileSync(path.join(OUT, '.nojekyll'), '');

let n = 0;
for (const p of pages) {
  const file = path.join(ROOT, 'content', p.file);
  if (!fs.existsSync(file)) { console.warn('missing', p.file); continue; }
  let src = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
  // Source material: collect the PDFs linked at the top of the page and append a reader at the bottom
  const chips = (src.match(/<div class="pdf-links">([\s\S]*?)<\/div>/) || [])[1] || '';
  const sources = [...chips.matchAll(/<a href="(pdfs\/[^"]+\.pdf)">([^<]+)<\/a>/g)].map(m => ({ url: m[1], title: m[2].replace(/&amp;/g, '&') }));
  if (sources.length && /-notes$/.test(p.id)) {
    const enc = JSON.stringify(sources).replace(/'/g, '&#39;');
    src = src.replace(/(<div class="pdf-links">[\s\S]*?)(<\/div>)/, '$1<a class="jump" href="#source-material">Read them all on this page ↓</a>\n$2');
    src += `\n\n## Source material\n\nThe original documents behind these notes. Pick a tab to read it here, page by page, or open it in a new tab.\n\n<div class="src-viewer" data-sources='${enc}'></div>\n`;
  }
  const { html, toc } = mdToHtml(src);
  fs.writeFileSync(path.join(OUT, p.id + '.html'), page(p, html, toc));
  n++;
}
console.log(`built ${n} pages -> _site/`);

// ---------------------------------------------------------------- cheat sheet (print, 2 A4 sheets, 2 columns)
if (fs.existsSync(path.join(ROOT, 'content', 'cheatsheet.md'))) {
  const CS_PT = process.env.CS_PT || '9.9';
  const { html } = mdToHtml(fs.readFileSync(path.join(ROOT, 'content', 'cheatsheet.md'), 'utf8'));
  const body = html.replace(/<h1[^>]*>[\s\S]*?<\/h1>/, '');
  fs.writeFileSync(path.join(OUT, 'cheatsheet-print.html'), `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI 500 Revision Sheet</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<style>
@page { size: A4; margin: 6mm 6.5mm; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #fff; color: #111; }
body { font: ${CS_PT}pt/1.22 "Segoe UI", Calibri, Arial, sans-serif; }
.hd { display: flex; justify-content: space-between; border-bottom: 1.2px solid #1d4ed8; margin-bottom: 1.5pt; font-size: 1.05em; }
.hd b { color: #1d4ed8; }
.cols { column-count: 2; column-gap: 4mm; column-rule: .5pt solid #bbb; column-fill: auto; height: auto; }
h2 { font-size: 1.12em; margin: 2.2pt 0 .8pt; padding: .6pt 3pt; background: #1d4ed8; color: #fff; border-radius: 2pt; break-after: avoid; }
ul { margin: 0; padding-left: 8pt; }
li { margin: 0 0 .5pt; }
li::marker { color: #1d4ed8; }
p { margin: 0 0 1pt; }
strong { color: #9a1b1b; }
.katex { font-size: 1.04em; }
.anchor { display: none; }
.katex-display { margin: 1pt 0; }
@media screen { body { max-width: 210mm; margin: 0 auto; padding: 6mm; } }
</style></head><body>
<div class="hd"><span><b>AI 500 · Foundations of AI</b> — Revision sheet (Modules 1–2)</span><span>Fall 2026 · Quiz 2 / Mid</span></div>
<div class="cols">${body}</div>
</body></html>`);
  console.log('built cheatsheet-print.html @ ' + CS_PT + 'pt');
}
