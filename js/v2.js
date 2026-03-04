/* =============================================
   LP V2 — Scroll Animations & Interactions
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  // --- Intersection Observer for scroll animations ---
  const animElements = document.querySelectorAll('[data-anim]');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Stagger the animation for elements that appear together
        const delay = entry.target.dataset.animDelay || 0;
        setTimeout(() => {
          entry.target.classList.add('is-visible');
        }, delay);
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  // Add stagger delays to grouped elements
  const groups = {};
  animElements.forEach((el) => {
    const parent = el.parentElement;
    if (!groups[parent]) {
      groups[parent] = [];
    }
    groups[parent].push(el);
  });

  Object.values(groups).forEach((group) => {
    group.forEach((el, i) => {
      el.dataset.animDelay = i * 120;
    });
  });

  animElements.forEach((el) => observer.observe(el));

  // --- Smooth scroll for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // --- Parallax effect on hero (subtle) ---
  const hero = document.querySelector('.hero');
  if (hero) {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      if (scrolled < window.innerHeight) {
        hero.style.backgroundPositionY = `${scrolled * 0.4}px`;
      }
    }, { passive: true });
  }

});
