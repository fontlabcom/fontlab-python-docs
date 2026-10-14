// this_file: scripts/a11y_checks.js
() => {
  const failures = [], focus = [], needs_manual = [];
  const selector = e => {
    const parts = [];
    while (e && e.nodeType === 1) {
      const index = e.parentElement ? 1 + [...e.parentElement.children].filter(x => x.localName === e.localName).indexOf(e) : 1;
      parts.unshift(`${e.localName}:nth-of-type(${index})`);
      e = e.parentElement;
    }
    return parts.join(' > ');
  };
  const fail = (check, e, measured) => failures.push({check, selector: e ? selector(e) : null, ...measured});
  const rendered = e => {
    if (!e.getClientRects().length || getComputedStyle(e).visibility !== 'visible' || e.closest('[hidden], [inert]')) return false;
    return true;
  };
  const visible = e => {
    if (!rendered(e)) return false;
    for (let p = e; p; p = p.parentElement) if (Number(getComputedStyle(p).opacity) === 0) return false;
    return true;
  };
  const style = e => {
    const s = getComputedStyle(e);
    const shadowVisible = s.boxShadow.split(/,(?![^()]*\))/).some(shadow => {
      const color = shadow.match(/rgba?\([^)]+\)/)?.[0];
      if (!color || color.endsWith(', 0)')) return false;
      return (shadow.replace(color, '').match(/-?[\d.]+px/g) || []).some(n => parseFloat(n) !== 0);
    });
    return {outline: `${s.outlineStyle} ${s.outlineWidth} ${s.outlineColor}`, shadow: s.boxShadow,
      outlineVisible: s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0 && !s.outlineColor.endsWith(', 0)'),
      shadowVisible};
  };
  const oldTabindex = document.body.getAttribute('tabindex');
  document.body.tabIndex = -1; document.body.focus();
  if (oldTabindex === null) document.body.removeAttribute('tabindex');
  else document.body.setAttribute('tabindex', oldTabindex);
  window.scrollTo(0, 0);
  const baseline = new Map([...document.querySelectorAll('*')].map(e => [e, style(e)]));
  window.a11yFocus = async () => {
    // Focus-triggered transitions can start with opacity zero (MaterialX skip).
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    const animations = [];
    for (let p = document.activeElement; p; p = p.parentElement) animations.push(...p.getAnimations());
    await Promise.race([
      Promise.all(animations.map(a => a.finished.catch(() => {}))),
      new Promise(resolve => setTimeout(resolve, 700))
    ]);
    const e = document.activeElement;
    if (!e || e === document.body || e === document.documentElement) return null;
    const before = baseline.get(e), after = style(e);
    const rect = e.getBoundingClientRect();
    const inViewport = rect.width > 0 && rect.height > 0 && rect.right > 0 && rect.bottom > 0 && rect.left < innerWidth && rect.top < innerHeight;
    return {selector: selector(e), before, after, inViewport, rendered: !!rendered(e), visible: !!visible(e),
      ...(e.matches(controls) ? {accessible_name: name(e)} : {}),
      indicator: !!before && !!visible(e) && inViewport &&
      ((after.outlineVisible && after.outline !== before.outline) || (after.shadowVisible && after.shadow !== before.shadow))};
  };
  const width = document.scrollingElement.scrollWidth;
  if (width > innerWidth + 1) fail('overflow', document.scrollingElement, {scrollWidth: width, innerWidth, tolerance: 1});
  const headings = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')];
  const h1 = document.querySelectorAll('h1').length;
  if (h1 !== 1) fail('h1', document.body, {count: h1, expected: 1});
  let previous = 0;
  for (const e of headings) {
    const level = Number(e.tagName[1]);
    if (level > previous + 1) fail('heading_order', e, {previous, level});
    previous = level;
  }
  for (const e of document.images) if (!e.hasAttribute('alt')) fail('image_alt', e, {alt: null});
  const name = e => {
    const refs = (e.getAttribute('aria-labelledby') || '').split(/\s+/).filter(Boolean);
    const labelled = refs.map(id => document.getElementById(id)?.textContent || '').join(' ').trim();
    if (labelled) return labelled;
    const labels = [...new Set([...(e.labels || []), ...[...document.querySelectorAll('label[for]')].filter(label => label.htmlFor === e.id && e.id)])];
    return [e.getAttribute('aria-label'), labels.map(x => x.textContent).join(' '),
      labels.map(x => x.getAttribute('aria-label') || x.title || '').join(' '),
      e.matches('button,[role="button"]') ? e.textContent : '',
      e.matches('input[type="submit"],input[type="reset"],input[type="button"]') ? e.value : '',
      e.matches('input[type="submit"],input[type="reset"]') && !e.hasAttribute('value') ? (e.type === 'submit' ? 'Submit' : 'Reset') : '',
      e.matches('input[type="image"]') ? e.alt : '', e.title
    ].map(value => (value || '').trim()).find(Boolean) || '';
  };
  const controls = 'input:not([type="hidden"]),select,textarea,button,[role="button"]';
  const keyboardFocusable = e => rendered(e) && e.tabIndex >= 0 && !e.matches(':disabled');
  for (const e of document.querySelectorAll(controls)) {
    if ((rendered(e) || keyboardFocusable(e)) && !name(e)) fail('accessible_name', e, {name: ''});
  }
  const rgba = value => {
    const m = value.match(/^rgba?\(([^)]+)\)$/);
    if (!m) return null;
    const a = m[1].split(',').map(Number);
    return [a[0], a[1], a[2], a.length === 4 ? a[3] : 1];
  };
  const over = (front, back) => [...front.slice(0, 3).map((c, i) => c * front[3] + back[i] * (1 - front[3])), 1];
  const luminance = rgb => rgb.slice(0, 3).map(c => c / 255).map(c => c <= .04045 ? c / 12.92 : ((c + .055) / 1.055) ** 2.4)
    .reduce((sum, c, i) => sum + c * [.2126, .7152, .0722][i], 0);
  const checked = new Set();
  const canvas = document.createElement('span');
  canvas.style.backgroundColor = 'Canvas';
  document.documentElement.append(canvas);
  const canvasColor = rgba(getComputedStyle(canvas).backgroundColor);
  canvas.remove();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const node = walker.currentNode, e = node.parentElement;
    if (!node.textContent.trim() || checked.has(e) || !visible(e) || e.closest('script,style,noscript')) continue;
    checked.add(e);
    const ancestors = []; let unsupported = null;
    for (let p = e; p; p = p.parentElement) {
      const s = getComputedStyle(p);
      if (s.backgroundImage !== 'none' || Number(s.opacity) !== 1 || s.mixBlendMode !== 'normal') unsupported = 'background image, opacity or blending';
      ancestors.unshift(rgba(s.backgroundColor));
    }
    const foreground = rgba(getComputedStyle(e).color);
    if (foreground?.[3] === 0 && getComputedStyle(e).textShadow === 'none') {
      fail('contrast', e, {foreground, background: null, ratio: 1, minimum: 4.5,
        reason: 'fully transparent text', kind: e.closest('code,pre') ? 'code' : e.closest('a') ? 'link' : 'body'});
      continue;
    }
    if (unsupported || !foreground || !canvasColor || ancestors.some(x => !x)) {
      needs_manual.push({check: 'contrast_unmeasurable', selector: selector(e),
        reason: unsupported || 'unsupported color syntax'}); continue;
    }
    const background = ancestors.reduce((back, front) => over(front, back), canvasColor);
    const ink = over(foreground, background), a = luminance(ink), b = luminance(background);
    const ratio = (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    if (ratio < 4.5) fail('contrast', e, {foreground, background, ratio, minimum: 4.5,
      kind: e.closest('code,pre') ? 'code' : e.closest('a') ? 'link' : 'body'});
  }
  const skip = document.querySelector('.md-skip,a[href^="#"][class*="skip"],a[href^="#"][id*="skip"]') ||
    [...document.querySelectorAll('a[href^="#"]')].find(e => /skip/i.test(e.textContent));
  const searchCandidates = [...document.querySelectorAll('input[type="search"],.md-search__input,[data-md-component="search-query"],[role="searchbox"],button[aria-label*="Search"],a[aria-label*="Search"],label[for="__search"][tabindex]')];
  const search = searchCandidates.find(keyboardFocusable) || searchCandidates.find(rendered) || searchCandidates[0];
  const navLinks = [...document.querySelectorAll('nav a[href], [role="navigation"] a[href]')];
  let nav = navLinks.find(rendered), navPanel = null;
  if (!nav) {
    // Closed mobile navigation is reached through a keyboard opener that controls it.
    const opener = [...document.querySelectorAll('[aria-controls]')].find(e => {
      const panel = document.getElementById(e.getAttribute('aria-controls'));
      return keyboardFocusable(e) && panel && navLinks.some(a => panel.contains(a));
    });
    if (opener) { nav = opener; navPanel = '#' + CSS.escape(opener.getAttribute('aria-controls')); }
  }
  return {failures, focus, needs_manual, scrollWidth: width, innerWidth, text_elements: checked.size,
    tab_budget: document.querySelectorAll('a,button,input,select,textarea,[tabindex],label').length + 2,
    reach_budget: 40, nav_panel: navPanel,
    targets: {...(skip ? {skip: selector(skip)} : {}), search: search ? selector(search) : null, nav: nav ? selector(nav) : null}};
}
