const projects = [
  {
    title: 'Next-Gen Product Launch',
    description: 'A polished digital product experience focused on user engagement, accessibility, and measurable conversion uplift.',
    tags: ['Design System', 'Responsive UI', 'Performance'],
    image: 'CNDZ7537.JPG',
    link: '#contact'
  },
  {
    title: 'Customer Growth Dashboard',
    description: 'A modern analytics workspace designed to surface insights clearly for decision-makers and teams.',
    tags: ['Data Visualization', 'UX Strategy', 'Web App'],
    image: 'PPXG3701.JPG',
    link: '#contact'
  },
  {
    title: 'Brand Story Microsite',
    description: 'A storytelling-driven experience that combines immersive visuals with a crisp, responsive structure.',
    tags: ['Branding', 'Interaction', 'Copycraft'],
    image: 'profile%20photo.png',
    link: '#contact'
  }
];

const skills = [
  { name: 'Modern Front-End', level: 98 },
  { name: 'Product Strategy', level: 92 },
  { name: 'Design Systems', level: 90 },
  { name: 'Performance Optimization', level: 95 },
  { name: 'Responsive Layouts', level: 96 },
  { name: 'Client Collaboration', level: 93 }
];

function createProjectCard(project) {
  const card = document.createElement('article');
  card.className = 'project-card';
  card.innerHTML = `
    <img src="${project.image}" alt="${project.title}" />
    <div>
      <div class="project-meta">${project.tags.map(tag => `<span>${tag}</span>`).join('')}</div>
      <h3>${project.title}</h3>
      <p>${project.description}</p>
    </div>
    <a class="button button-outline" href="${project.link}">Discuss project</a>
  `;
  return card;
}

function createSkillCard(skill) {
  const card = document.createElement('article');
  card.className = 'skill-card';
  card.innerHTML = `
    <strong>${skill.name}</strong>
    <div class="skill-label">${skill.level}% confidence</div>
    <div class="skill-bar"><div class="skill-fill" style="width: ${skill.level}%"></div></div>
  `;
  return card;
}

function loadPortfolioContent() {
  const projectGrid = document.getElementById('projectGrid');
  const skillsGrid = document.getElementById('skillsGrid');

  projects.forEach(project => projectGrid.appendChild(createProjectCard(project)));
  skills.forEach(skill => skillsGrid.appendChild(createSkillCard(skill)));
}

function setupScrollReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('.project-card, .skill-card, .highlight-card, .hero-card, .stat-card, .contact-text, .contact-form').forEach((el) => {
    el.classList.add('reveal');
    observer.observe(el);
  });
}

function handleContactForm() {
  const form = document.getElementById('contactForm');
  const feedback = document.getElementById('formFeedback');

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    feedback.textContent = 'Thanks! Your message is ready to be emailed. I’ll follow up shortly.';
    form.reset();
  });
}

function init() {
  loadPortfolioContent();
  setupScrollReveal();
  handleContactForm();
}

window.addEventListener('DOMContentLoaded', init);