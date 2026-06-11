// Ruen Bongkot — interactions

// Sticky nav background on scroll
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const burger = document.getElementById('burger');
const navLinks = document.getElementById('navLinks');
burger.addEventListener('click', () => {
  burger.classList.toggle('is-open');
  navLinks.classList.toggle('is-open');
});
navLinks.querySelectorAll('a').forEach((link) =>
  link.addEventListener('click', () => {
    burger.classList.remove('is-open');
    navLinks.classList.remove('is-open');
  })
);

// Menu tabs
const tabs = document.querySelectorAll('.tab');
const panels = document.querySelectorAll('.panel');
tabs.forEach((tab) =>
  tab.addEventListener('click', () => {
    tabs.forEach((t) => t.classList.remove('is-active'));
    panels.forEach((p) => p.classList.remove('is-active'));
    tab.classList.add('is-active');
    const panel = document.getElementById(`panel-${tab.dataset.tab}`);
    panel.classList.add('is-active');
    // dishes inside a freshly shown panel should appear immediately
    panel.querySelectorAll('.reveal').forEach((el) => el.classList.add('is-visible'));
  })
);

// Scroll-reveal animations
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);
document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

// Footer year
document.getElementById('year').textContent = new Date().getFullYear();
