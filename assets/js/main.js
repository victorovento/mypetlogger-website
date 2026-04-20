// MyPetLogger — marketing site interactions

(() => {
  'use strict';

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

  // Parallax on bloom backgrounds
  if (!reduce) {
    const blooms = document.querySelectorAll('.bloom');
    let ticking = false;
    const onParallax = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const y = window.scrollY;
        blooms.forEach((b, i) => {
          const speed = (i % 3 === 0) ? 0.15 : (i % 3 === 1 ? -0.12 : 0.08);
          const scale = 1 + (Math.sin((y + i * 80) / 900) * 0.05);
          b.style.transform = `translate3d(0, ${y * speed}px, 0) scale(${scale})`;
        });
        ticking = false;
      });
    };
    window.addEventListener('scroll', onParallax, { passive: true });
    onParallax();

    // Phone tilt on scroll
    const phones = document.querySelectorAll('.phone[data-parallax]');
    const onPhoneTilt = () => {
      const cy = window.innerHeight / 2;
      phones.forEach(p => {
        const rect = p.getBoundingClientRect();
        const mid = rect.top + rect.height / 2;
        const d = (mid - cy) / window.innerHeight;
        const base = p.dataset.rotate ? parseFloat(p.dataset.rotate) : 0;
        p.style.transform = `rotate(${base + d * -4}deg) translateY(${d * -10}px)`;
      });
    };
    window.addEventListener('scroll', onPhoneTilt, { passive: true });
    onPhoneTilt();
  }
})();
