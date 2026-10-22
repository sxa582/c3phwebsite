(() => {
  'use strict';
  const menu = document.querySelector('.menu-button');
  const nav = document.querySelector('#site-nav');
  const closeMenu = (returnFocus = false) => {
    nav.classList.remove('open');
    menu.setAttribute('aria-expanded', 'false');
    menu.textContent = 'Menu';
    if (returnFocus) menu.focus();
  };
  menu.addEventListener('click', () => {
    const expanded = menu.getAttribute('aria-expanded') !== 'true';
    nav.classList.toggle('open', expanded);
    menu.setAttribute('aria-expanded', String(expanded));
    menu.textContent = expanded ? 'Close' : 'Menu';
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('open')) closeMenu(true);
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.nav-shell')) closeMenu();
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  const desktop = window.matchMedia('(min-width: 961px)');
  desktop.addEventListener('change', () => closeMenu());
  document.querySelectorAll('[data-current-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  const filters = document.querySelector('#publication-filters');
  if (!filters) return;
  const search = document.querySelector('#publication-search');
  const topic = document.querySelector('#publication-topic');
  const year = document.querySelector('#publication-year');
  const cards = [...document.querySelectorAll('.pub-card')];
  const count = document.querySelector('#publication-count');
  const empty = document.querySelector('#publication-empty');
  const params = new URLSearchParams(location.search);
  search.value = params.get('q') || '';
  if ([...topic.options].some(option => option.value === params.get('topic'))) topic.value = params.get('topic');
  if ([...year.options].some(option => option.value === params.get('year'))) year.value = params.get('year');
  const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
  function filter(updateUrl = true) {
    const words = normalize(search.value).split(/\s+/).filter(Boolean);
    let visible = 0;
    cards.forEach(card => {
      const matches = (!topic.value || card.dataset.topic === topic.value) && (!year.value || card.dataset.year === year.value) && words.every(word => normalize(card.textContent).includes(word));
      card.hidden = !matches;
      if (matches) visible++;
    });
    count.textContent = `${visible} of ${cards.length} selected publications`;
    empty.hidden = visible !== 0;
    if (updateUrl) {
      const next = new URLSearchParams();
      if (search.value.trim()) next.set('q', search.value.trim());
      if (topic.value) next.set('topic', topic.value);
      if (year.value) next.set('year', year.value);
      const query = next.toString();
      history.replaceState(null, '', location.pathname + (query ? '?' + query : '') + location.hash);
    }
  }
  filters.addEventListener('submit', event => event.preventDefault());
  search.addEventListener('input', () => filter());
  topic.addEventListener('change', () => filter());
  year.addEventListener('change', () => filter());
  filters.addEventListener('reset', () => {
    search.value = ''; topic.value = ''; year.value = '';
    filter(); search.focus();
  });
  filter(false);
})();
