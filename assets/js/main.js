// MyPetLogger — marketing site interactions

(() => {
  'use strict';

  // ---- Theme toggle (light / dark, persisted) ----
  const STORAGE_KEY = 'mpl-theme';
  const root = document.documentElement;
  const mql = window.matchMedia('(prefers-color-scheme: dark)');

  // For each <picture> with a dark <source media="(prefers-color-scheme: dark)">,
  // we flip the source's media attribute so the picture element reflects the chosen theme
  // instead of the system preference.
  const swapSources = document.querySelectorAll('picture > source[media*="prefers-color-scheme"]');

  const applyTheme = (theme) => {
    if (theme === 'light' || theme === 'dark') {
      root.setAttribute('data-theme', theme);
    } else {
      root.removeAttribute('data-theme');
    }
    const effective = theme || (mql.matches ? 'dark' : 'light');
    swapSources.forEach(s => {
      if (theme === 'dark')      s.media = 'all';
      else if (theme === 'light') s.media = 'not all';
      else                        s.media = '(prefers-color-scheme: dark)';
    });
    root.style.colorScheme = effective;
  };

  const stored = (() => { try { return localStorage.getItem(STORAGE_KEY); } catch { return null; } })();
  applyTheme(stored);

  document.querySelectorAll('.theme-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const current = root.getAttribute('data-theme') || (mql.matches ? 'dark' : 'light');
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem(STORAGE_KEY, next); } catch {}
    });
  });

  // Follow system if user hasn't picked
  mql.addEventListener?.('change', () => {
    const explicit = (() => { try { return localStorage.getItem(STORAGE_KEY); } catch { return null; } })();
    if (!explicit) applyTheme(null);
  });

  // Scroll-aware nav
  const nav = document.querySelector('.nav');
  if (nav) {
    const onScroll = () => {
      if (window.scrollY > 8) nav.classList.add('is-scrolled');
      else nav.classList.remove('is-scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Mobile nav toggle
  const burger = document.querySelector('.nav__burger');
  const links = document.querySelector('.nav__links');
  if (burger && links) {
    burger.addEventListener('click', () => {
      const open = links.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => links.classList.remove('is-open'));
    });
  }

  // Reveal on scroll
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-visible'));
  }

  // Parallax + tilt — skip on touch devices (jank > value on mobile)
  const coarse = window.matchMedia('(pointer: coarse)').matches;
  if (!reduce && !coarse) {
    const blooms = document.querySelectorAll('.bloom');
    const phones = document.querySelectorAll('.phone[data-parallax]');
    let ticking = false;
    const tick = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const y = window.scrollY;
        blooms.forEach((b, i) => {
          const speed = (i % 3 === 0) ? 0.15 : (i % 3 === 1 ? -0.12 : 0.08);
          const scale = 1 + (Math.sin((y + i * 80) / 900) * 0.05);
          b.style.transform = `translate3d(0, ${y * speed}px, 0) scale(${scale})`;
        });
        const cy = window.innerHeight / 2;
        phones.forEach(p => {
          const rect = p.getBoundingClientRect();
          const mid = rect.top + rect.height / 2;
          const d = (mid - cy) / window.innerHeight;
          const base = p.dataset.rotate ? parseFloat(p.dataset.rotate) : 0;
          p.style.transform = `rotate(${base + d * -4}deg) translateY(${d * -10}px)`;
        });
        ticking = false;
      });
    };
    window.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('resize', tick, { passive: true });
    tick();
  }
})();
