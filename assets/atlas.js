(() => {
  'use strict';
  const tabs = [...document.querySelectorAll('[data-signal]')];
  const panel = document.querySelector('#signal-panel');
  if (tabs.length && panel) {
    const signals = {
      imaging: { kicker: 'Structure & composition', title: 'More than an image.', description: 'Quantifying anatomy, tissue composition, and disease burden from imaging acquired during routine care.', image: 'ct', alt: 'Conceptual illustration of computational imaging', href: 'focus-areas.html#imaging', action: 'Explore imaging research' },
      ecg: { kicker: 'Electrical patterns & physiology', title: 'A signal with more to say.', description: 'Learning from ECG images, waveforms, and physiological signals to study subclinical disease and future cardiovascular outcomes.', image: 'ecg', alt: 'Schematic ECG waveforms, not a patient recording', href: 'focus-areas.html#ecg', action: 'Explore ECG research' },
      ehr: { kicker: 'Clinical history & trajectories', title: 'Health, over time.', description: 'Connecting diagnoses, laboratory results, medications, and clinical text to characterize how health changes across a person’s care journey.', image: 'ehr', alt: 'Conceptual longitudinal clinical trajectories', href: 'focus-areas.html#ehr', action: 'Explore EHR research' },
      environment: { kicker: 'Place & exposure', title: 'The world around the patient.', description: 'Linking clinical outcomes with air pollution, heat, greenspace, and neighborhood conditions to understand environmental influences on cardiometabolic health.', image: 'environment', alt: 'Conceptual environmental exposure map', href: 'focus-areas.html#exposome', action: 'Explore exposome research' }
    };
    function activate(tab, focus = false) {
      const signal = signals[tab.dataset.signal];
      tabs.forEach(item => {
        const active = item === tab;
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
      });
      panel.setAttribute('aria-labelledby', tab.id);
      document.querySelector('#signal-kicker').textContent = signal.kicker;
      document.querySelector('#signal-title').textContent = signal.title;
      document.querySelector('#signal-description').textContent = signal.description;
      const image = document.querySelector('#signal-image');
      image.src = 'assets/' + signal.image + '.svg';
      image.alt = signal.alt;
      const link = document.querySelector('#signal-link');
      link.href = signal.href;
      link.replaceChildren(document.createTextNode(signal.action + ' '));
      const arrow = document.createElement('span');
      arrow.setAttribute('aria-hidden', 'true');
      arrow.textContent = '↗';
      link.appendChild(arrow);
      if (focus) tab.focus();
    }
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => activate(tab));
      tab.addEventListener('keydown', event => {
        let next;
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = tabs.length - 1;
        if (next === undefined) return;
        event.preventDefault();
        activate(tabs[next], true);
      });
    });
  }
  const programs = [...document.querySelectorAll('.program-disclosure')];
  programs.forEach(disclosure => disclosure.addEventListener('toggle', () => {
    if (disclosure.open) programs.forEach(other => { if (other !== disclosure) other.open = false; });
  }));
  const stage = document.querySelector('.atlas-stage');
  const artwork = stage?.querySelector('.heart-art');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (stage && artwork && window.matchMedia('(pointer: fine)').matches) {
    stage.addEventListener('pointermove', event => {
      if (reducedMotion.matches) return;
      const box = stage.getBoundingClientRect();
      const x = (event.clientX - box.left) / box.width - .5;
      const y = (event.clientY - box.top) / box.height - .5;
      artwork.style.transform = `rotateY(${x * 8}deg) rotateX(${-y * 5}deg)`;
    });
    stage.addEventListener('pointerleave', () => { artwork.style.transform = ''; });
    reducedMotion.addEventListener('change', () => { artwork.style.transform = ''; });
  }
})();
