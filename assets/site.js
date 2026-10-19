(function () {
  var root = document.documentElement;

  // ---- theme: auto (system) until the user picks; choice persists
  function systemDark() { return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches; }
  function current() { return root.dataset.theme || (systemDark() ? 'dark' : 'light'); }
  function setTheme(t) {
    root.dataset.theme = t;
    try { localStorage.setItem('theme', t); } catch (e) {}
    var meta = document.querySelectorAll('meta[name="theme-color"]');
    meta.forEach(function (m) { m.setAttribute('content', t === 'dark' ? '#16161a' : '#fbfbfa'); });
  }
  document.querySelectorAll('.themebtn').forEach(function (b) {
    b.addEventListener('click', function () { setTheme(current() === 'dark' ? 'light' : 'dark'); });
  });

  // ---- mobile drawer
  var side = document.getElementById('side'), scrim = document.getElementById('scrim'), btn = document.getElementById('menuBtn');
  function drawer(open) {
    document.body.classList.toggle('nav-open', open);
    if (btn) btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (btn) btn.addEventListener('click', function () { drawer(!document.body.classList.contains('nav-open')); });
  if (scrim) scrim.addEventListener('click', function () { drawer(false); });
  if (side) side.addEventListener('click', function (e) { if (e.target.closest('a') && innerWidth <= 1020) drawer(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { drawer(false); closeLb(); } });

  // keep the active nav item visible in the sidebar
  var on = side && side.querySelector('nav a.on');
  if (on && on.scrollIntoView) on.scrollIntoView({ block: 'center' });

  // ---- "On this page" scroll-spy
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  var targets = links.map(function (a) { return document.getElementById(decodeURIComponent(a.hash.slice(1))); });
  if (links.length && 'IntersectionObserver' in window) {
    var visible = new Set();
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) { en.isIntersecting ? visible.add(en.target) : visible.delete(en.target); });
      var idx = -1;
      targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top < innerHeight * 0.35) idx = i; });
      links.forEach(function (a, i) { a.classList.toggle('on', i === idx); });
    }, { rootMargin: '0px 0px -60% 0px' });
    targets.forEach(function (t) { if (t) io.observe(t); });
  }

  // ---- show / hide all solutions
  document.querySelectorAll('[data-sol]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.dataset.sol === 'open';
      document.querySelectorAll('details.solution').forEach(function (d) { d.open = open; });
    });
  });

  // ---- figure lightbox
  var lb = document.getElementById('lightbox');
  function closeLb() { if (lb && !lb.hidden) { lb.hidden = true; document.body.classList.remove('lb-open'); } }
  document.addEventListener('click', function (e) {
    var z = e.target.closest('a.zoom');
    if (z && lb) {
      e.preventDefault();
      lb.querySelector('img').src = z.getAttribute('href');
      lb.querySelector('img').alt = (z.querySelector('img') || {}).alt || '';
      lb.hidden = false; document.body.classList.add('lb-open');
    } else if (lb && !lb.hidden && (e.target === lb || e.target.closest('.lb-close') || e.target.tagName === 'IMG')) closeLb();
  });
})();

// ---- Source-material reader (PDF.js, loaded only when the section comes near the screen)
(function () {
  var viewers = document.querySelectorAll('.src-viewer');
  if (!viewers.length) return;
  var PDFJS = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/';
  var libPromise = null;
  function loadLib() {
    if (libPromise) return libPromise;
    libPromise = new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = PDFJS + 'pdf.min.js';
      s.onload = function () { window.pdfjsLib.GlobalWorkerOptions.workerSrc = PDFJS + 'pdf.worker.min.js'; res(window.pdfjsLib); };
      s.onerror = rej;
      document.head.appendChild(s);
    });
    return libPromise;
  }
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }

  viewers.forEach(function (v) {
    var sources = [];
    try { sources = JSON.parse(v.dataset.sources || '[]'); } catch (e) {}
    if (!sources.length) return;
    var tabs = el('div', 'src-tabs'); tabs.setAttribute('role', 'tablist');
    var bar = el('div', 'src-bar');
    var title = el('div', 'src-title');
    var actions = el('div', 'src-actions');
    var openA = el('a', 'src-btn', 'Open in new tab'); openA.target = '_blank'; openA.rel = 'noopener';
    var dlA = el('a', 'src-btn', 'Download'); dlA.setAttribute('download', '');
    var fsB = el('button', 'src-btn', 'Full screen'); fsB.type = 'button';
    actions.append(openA, dlA, fsB); bar.append(title, actions);
    var pagesBox = el('div', 'src-pages'); pagesBox.tabIndex = 0;
    v.append(tabs, bar, pagesBox);

    var current = -1, token = 0, observer = null;
    sources.forEach(function (s, i) {
      var b = el('button', 'src-tab', s.title); b.type = 'button'; b.setAttribute('role', 'tab');
      b.addEventListener('click', function () { show(i); });
      tabs.appendChild(b);
    });

    function show(i) {
      if (i === current) return;
      current = i; var my = ++token; var s = sources[i];
      tabs.querySelectorAll('.src-tab').forEach(function (b, j) { b.classList.toggle('on', j === i); b.setAttribute('aria-selected', j === i); });
      title.textContent = s.title; openA.href = s.url; dlA.href = s.url;
      pagesBox.innerHTML = '<div class="src-msg">Loading…</div>'; pagesBox.scrollTop = 0;
      if (observer) observer.disconnect();
      loadLib().then(function (lib) { return lib.getDocument(s.url).promise; }).then(function (pdf) {
        if (my !== token) return;
        pagesBox.innerHTML = '';
        title.textContent = s.title + ' · ' + pdf.numPages + ' page' + (pdf.numPages > 1 ? 's' : '');
        observer = new IntersectionObserver(function (ents) {
          ents.forEach(function (en) { if (en.isIntersecting) { observer.unobserve(en.target); render(pdf, en.target, my); } });
        }, { root: pagesBox, rootMargin: '600px 0px' });
        pdf.getPage(1).then(function (p1) {
          var vp = p1.getViewport({ scale: 1 }), ratio = vp.height / vp.width;
          for (var n = 1; n <= pdf.numPages; n++) {
            var holder = el('div', 'src-page'); holder.dataset.n = n;
            holder.style.aspectRatio = (1 / ratio).toFixed(4);
            holder.appendChild(el('span', 'src-pno', n));
            pagesBox.appendChild(holder); observer.observe(holder);
          }
        });
      }).catch(function () {
        if (my !== token) return;
        pagesBox.innerHTML = '<div class="src-msg">Could not display this PDF here. <a href="' + s.url + '" target="_blank" rel="noopener">Open it in a new tab</a>.</div>';
      });
    }

    function render(pdf, holder, my) {
      pdf.getPage(+holder.dataset.n).then(function (page) {
        if (my !== token) return;
        var w = holder.clientWidth || pagesBox.clientWidth;
        var base = page.getViewport({ scale: 1 });
        var dpr = Math.min(window.devicePixelRatio || 1, 2);
        var vp = page.getViewport({ scale: (w / base.width) * dpr });
        var c = document.createElement('canvas'); c.width = vp.width; c.height = vp.height;
        page.render({ canvasContext: c.getContext('2d'), viewport: vp }).promise.then(function () {
          if (my === token) { holder.insertBefore(c, holder.firstChild); holder.classList.add('ready'); }
        });
      });
    }

    fsB.addEventListener('click', function () {
      var on = !v.classList.contains('full');
      v.classList.toggle('full', on); document.body.classList.toggle('lb-open', on);
      fsB.textContent = on ? 'Exit full screen' : 'Full screen';
      // re-render at the new width
      if (current >= 0) { var i = current; current = -1; show(i); }
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && v.classList.contains('full')) fsB.click(); });

    // start loading the first source only when the reader approaches the viewport
    function start() { if (current < 0) show(0); }
    var io = new IntersectionObserver(function (ents) {
      if (ents[0].isIntersecting) { io.disconnect(); start(); }
    }, { rootMargin: '400px 0px' });
    io.observe(v);
    if (location.hash === '#source-material') start();
    window.addEventListener('hashchange', function () { if (location.hash === '#source-material') start(); });
  });
})();
