from pathlib import Path

base = Path(r'c:/Users/Public/wanaemicv')

files = {}

files['index.html'] = base / 'index.html'
files['styles.css'] = base / 'styles.css'
files['script.js'] = base / 'script.js'

for name, path in files.items():
    text = path.read_text(encoding='utf-8')
    if name == 'index.html':
        text = text.replace(
            '<meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <title>Wanaemic Portfolio</title>\n  <link rel="preconnect" href="https://fonts.googleapis.com" />',
            '<meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <meta name="description" content="Wanaemic is a modern portfolio showcasing product design, front-end engineering, and cloud-ready delivery." />\n  <title>Wanaemic Portfolio</title>\n  <link rel="icon" href="profile%20photo.png" type="image/png" />\n  <link rel="preconnect" href="https://fonts.googleapis.com" />'
        )
        text = text.replace(
            '          <div class="hero-actions">\n            <a class="button button-primary" href="#work">View Work</a>\n            <a class="button button-outline" href="#about">Learn More</a>\n          </div>\n          <div class="hero-tags">',
            '          <div class="hero-actions">\n            <a class="button button-primary" href="#work">View Work</a>\n            <a class="button button-outline" href="#about">Learn More</a>\n            <a class="button button-secondary" href="Copy of cv.pdf" target="_blank" rel="noreferrer noopener">Download CV</a>\n          </div>\n          <div class="hero-tags">'
        )
        if 'id="process"' not in text:
            text = text.replace(
                '      </section>\n\n      <section id="work" class="section section-work">',
                '      </section>\n\n      <section id="process" class="section section-process">\n        <div class="section-header">\n          <span>Process</span>\n          <h2>How I turn strategy into sleek, launch-ready products.</h2>\n        </div>\n        <div class="process-grid">\n          <div class="process-step">\n            <span class="step-number">01</span>\n            <h3>Align</h3>\n            <p>Understand the business goals, audience needs, and product vision first.</p>\n          </div>\n          <div class="process-step">\n            <span class="step-number">02</span>\n            <h3>Design</h3>\n            <p>Create polished visual systems and intuitive interactions for every screen.</p>\n          </div>\n          <div class="process-step">\n            <span class="step-number">03</span>\n            <h3>Build</h3>\n            <p>Develop fast, resilient interfaces with modern web technologies and clean structure.</p>\n          </div>\n          <div class="process-step">\n            <span class="step-number">04</span>\n            <h3>Launch</h3>\n            <p>Deploy with certainty, iterate quickly, and keep every experience performing beautifully.</p>\n          </div>\n        </div>\n      </section>\n\n      <section id="work" class="section section-work">'
            )
        )
    elif name == 'styles.css':
        text = text.replace(
            '\n.hero {\n  display: grid;\n  grid-template-columns: 1.4fr 1.1fr;\n  gap: 40px;\n  align-items: center;\n  min-height: calc(100vh - 120px);\n  padding-top: 40px;\n}\n\n.section-glow {\n',
            '\n.hero {\n  display: grid;\n  grid-template-columns: 1.4fr 1.1fr;\n  gap: 40px;\n  align-items: center;\n  min-height: calc(100vh - 120px);\n  padding-top: 40px;\n  position: relative;\n}\n\n.hero::before {\n  content: "";\n  position: absolute;\n  top: 10%;\n  right: -5%;\n  width: 420px;\n  height: 420px;\n  border-radius: 50%;\n  background: radial-gradient(circle, rgba(124, 103, 255, 0.18), transparent 55%);\n  filter: blur(60px);\n  pointer-events: none;\n}\n\n.section-glow {\n'
        )
        text = text.replace(
            '\n.hero-card-photo {\n  position: relative;\n  min-height: 390px;\n}\n\n.hero-card-photo img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n}\n',
            '\n.hero-card-photo {\n  position: relative;\n  min-height: 390px;\n  overflow: hidden;\n}\n\n.hero-card-photo::after {\n  content: "";\n  position: absolute;\n  inset: 10px;\n  border-radius: 28px;\n  box-shadow: inset 0 0 0 1px rgba(124, 103, 255, 0.18);\n}\n\n.hero-card-photo img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n}\n'
        )
        text = text.replace(
            '\n.hero-tags span {\n  padding: 12px 18px;\n  border-radius: 999px;\n  background: rgba(255, 255, 255, 0.06);\n  color: var(--text);\n  font-size: 0.95rem;\n}\n\n.hero-visual {\n',
            '\n.hero-tags span {\n  padding: 12px 18px;\n  border-radius: 999px;\n  background: rgba(255, 255, 255, 0.06);\n  color: var(--text);\n  font-size: 0.95rem;\n}\n\n.hero-actions .button-secondary {\n  border-color: rgba(255, 255, 255, 0.18);\n  background: rgba(255, 255, 255, 0.07);\n}\n\n.hero-actions .button-secondary:hover {\n  background: rgba(255, 255, 255, 0.12);\n}\n\n.hero-visual {\n'
        )
        text = text.replace(
            '\n.contact-list strong {\n  font-size: 0.95rem;\n}\n\n.contact-form {\n',
            '\n.contact-list strong {\n  font-size: 0.95rem;\n}\n\n.section-process {\n  padding-top: 24px;\n}\n\n.process-grid {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: 20px;\n}\n\n.process-step {\n  padding: 28px;\n  border-radius: 28px;\n  background: rgba(255, 255, 255, 0.04);\n  border: 1px solid rgba(255, 255, 255, 0.08);\n  transition: transform 200ms ease, border-color 200ms ease, background 200ms ease;\n}\n\n.process-step:hover {\n  transform: translateY(-4px);\n  border-color: rgba(124, 103, 255, 0.25);\n  background: rgba(124, 103, 255, 0.08);\n}\n\n.step-number {\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n  width: 46px;\n  height: 46px;\n  border-radius: 16px;\n  background: rgba(124, 103, 255, 0.18);\n  color: #fff;\n  font-weight: 700;\n  margin-bottom: 18px;\n}\n\n.process-step h3 {\n  margin: 0 0 10px;\n}\n\n.contact-form {\n'
        )
    elif name == 'script.js':
        text = text.replace(
            '  return card;\n}\n\nfunction loadPortfolioContent() {\n',
            '  return card;\n}\n\nfunction animateCounter(card) {\n  const span = card.querySelector(\'span\');\n  const target = Number(card.dataset.target || 0);\n  const suffix = card.dataset.suffix || \''\';\n  if (!span || !target) return;\n  let current = 0;\n  const step = Math.max(1, Math.round(target / 60));\n  const interval = setInterval(() => {\n    current += step;\n    if (current >= target) {\n      span.textContent = `${target}${suffix}`;\n      clearInterval(interval);\n    } else {\n      span.textContent = `${current}${suffix}`;\n    }\n  }, 16);\n}\n\nfunction loadPortfolioContent() {\n'
        )
        text = text.replace(
            '  document.querySelectorAll(\'.project-card, .skill-card, .highlight-card, .hero-card, .stat-card, .contact-text, .contact-form\').forEach((el) => {\n    el.classList.add(\'reveal\');\n    observer.observe(el);\n  });\n}\n',
            '  document.querySelectorAll(\'.project-card, .skill-card, .highlight-card, .hero-card, .stat-card, .contact-text, .contact-form, .process-step\').forEach((el) => {\n    el.classList.add(\'reveal\');\n    observer.observe(el);\n  });\n}\n'
        )
        text = text.replace(
            '      if (entry.isIntersecting) {\n        entry.target.classList.add(\'visible\');\n        observer.unobserve(entry.target);\n      }\n',
            '      if (entry.isIntersecting) {\n        entry.target.classList.add(\'visible\');\n        if (entry.target.classList.contains(\'stat-card\')) {\n          animateCounter(entry.target);\n        }\n        observer.unobserve(entry.target);\n      }\n'
        )
    path.write_text(text, encoding='utf-8')
    print(f'Updated {name}')
