import os

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Thatha Chenchaiah | VLSI Aspirant &amp; Automation Tester</title>
<meta name="description" content="Portfolio of Thatha Chenchaiah - B.Tech ECE student specializing in VLSI design, digital electronics, and Selenium automation testing."/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#050b14;--bg2:#080f1c;
  --cyan:#00d4ff;--teal:#00ffb2;--purple:#7c3aed;--purple-lt:#a78bfa;--gold:#fbbf24;
  --text:#e2e8f0;--text-dim:#94a3b8;
  --border:rgba(0,212,255,0.15);--glass:rgba(13,24,39,0.7);
  --glow:0 0 30px rgba(0,212,255,0.2);--radius:16px;
  --transition:all 0.35s cubic-bezier(0.4,0,0.2,1)
}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6}
::selection{background:rgba(0,212,255,0.3)}
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--cyan);border-radius:3px}
#circuit-canvas{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;opacity:0.4}
nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:1rem 6%;backdrop-filter:blur(20px);background:rgba(5,11,20,0.85);border-bottom:1px solid var(--border);transition:var(--transition)}
.nav-logo{font-family:'JetBrains Mono',monospace;font-size:1.2rem;font-weight:600;color:var(--cyan);text-decoration:none}
.nav-logo span{color:var(--teal)}
.nav-links{display:flex;gap:2rem;list-style:none}
.nav-links a{color:var(--text-dim);text-decoration:none;font-size:0.875rem;font-weight:500;transition:var(--transition);position:relative}
.nav-links a::after{content:'';position:absolute;bottom:-4px;left:0;right:0;height:2px;background:var(--cyan);transform:scaleX(0);transition:transform 0.3s ease}
.nav-links a:hover{color:var(--cyan)}
.nav-links a:hover::after{transform:scaleX(1)}
.nav-cta{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#fff !important;padding:0.5rem 1.25rem;border-radius:8px;font-weight:600 !important}
.nav-cta::after{display:none !important}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer}
.hamburger span{width:25px;height:2px;background:var(--cyan);border-radius:2px;transition:var(--transition)}
main{position:relative;z-index:1}
section{padding:6rem 6%}
.section-tag{font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--cyan);letter-spacing:0.2em;text-transform:uppercase;margin-bottom:0.5rem}
.section-title{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:800;line-height:1.2;margin-bottom:1rem}
.section-title span{background:linear-gradient(135deg,var(--cyan),var(--purple-lt));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.section-divider{width:60px;height:3px;background:linear-gradient(to right,var(--cyan),var(--purple));border-radius:2px;margin-bottom:3rem}
#hero{min-height:100vh;display:flex;align-items:center;padding:6rem 6% 4rem;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;width:100%}
.hero-badge{display:inline-flex;align-items:center;gap:0.5rem;background:rgba(0,212,255,0.08);border:1px solid rgba(0,212,255,0.25);border-radius:50px;padding:0.35rem 1rem;font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--cyan);margin-bottom:1.5rem}
.hero-badge::before{content:'';width:8px;height:8px;background:var(--teal);border-radius:50%;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.5;transform:scale(0.8)}}
.hero-name{font-size:clamp(2.5rem,6vw,4.5rem);font-weight:800;line-height:1.1;margin-bottom:1rem}
.hero-name .first{color:var(--text)}
.hero-name .last{background:linear-gradient(135deg,var(--cyan) 0%,var(--teal) 50%,var(--purple-lt) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-typed-wrapper{font-size:clamp(1rem,2vw,1.3rem);color:var(--text-dim);margin-bottom:1.5rem;height:2rem;display:flex;align-items:center;gap:0.5rem}
.typed-prefix{color:var(--cyan);font-family:'JetBrains Mono',monospace}
#typed-text{color:var(--teal);font-weight:600}
.cursor{display:inline-block;width:2px;height:1.2em;background:var(--cyan);margin-left:2px;animation:blink 1s step-end infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.hero-bio{color:var(--text-dim);font-size:0.95rem;max-width:500px;margin-bottom:2rem;line-height:1.8}
.hero-btns{display:flex;gap:1rem;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:0.5rem;padding:0.8rem 1.8rem;border-radius:10px;font-weight:600;font-size:0.9rem;text-decoration:none;transition:var(--transition);cursor:pointer;border:none}
.btn-primary{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#fff;box-shadow:0 4px 20px rgba(0,212,255,0.3)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(0,212,255,0.5)}
.btn-outline{background:transparent;border:1px solid var(--border);color:var(--text)}
.btn-outline:hover{border-color:var(--cyan);color:var(--cyan);transform:translateY(-2px)}
.hero-stats{display:flex;gap:2.5rem;margin-top:2.5rem;flex-wrap:wrap}
.stat{text-align:center}
.stat-num{font-size:1.8rem;font-weight:800;background:linear-gradient(135deg,var(--cyan),var(--teal));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-label{font-size:0.75rem;color:var(--text-dim)}
.hero-visual{display:flex;justify-content:center;align-items:center;position:relative}
.hero-chip{width:320px;height:320px;position:relative}
.chip-svg{width:100%;height:100%;animation:float 5s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-15px) rotate(2deg)}}
.chip-ring{position:absolute;inset:-20px;border-radius:50%;border:2px dashed rgba(0,212,255,0.2);animation:spin 20s linear infinite}
.chip-ring-2{position:absolute;inset:-40px;border-radius:50%;border:1px dashed rgba(124,58,237,0.2);animation:spin 30s linear infinite reverse}
@keyframes spin{to{transform:rotate(360deg)}}
#about{background:var(--bg2)}
.about-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:4rem;align-items:start}
.about-card{background:var(--glass);border:1px solid var(--border);border-radius:var(--radius);padding:2rem;backdrop-filter:blur(20px)}
.about-avatar{width:100px;height:100px;background:linear-gradient(135deg,var(--cyan),var(--purple));border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.4rem;font-weight:800;color:#fff;margin:0 auto 1.5rem;box-shadow:0 0 40px rgba(0,212,255,0.3)}
.about-info{text-align:center}
.about-info h3{font-size:1.3rem;font-weight:700;margin-bottom:0.25rem}
.about-info .role-tag{color:var(--cyan);font-size:0.85rem;margin-bottom:1.5rem;font-family:'JetBrains Mono',monospace}
.info-list{text-align:left}
.info-item{display:flex;align-items:flex-start;gap:0.75rem;padding:0.6rem 0;border-bottom:1px solid rgba(255,255,255,0.05);font-size:0.85rem}
.info-item:last-child{border-bottom:none}
.info-icon{color:var(--cyan);flex-shrink:0;margin-top:2px}
.info-label{color:var(--text-dim);width:80px;flex-shrink:0}
.info-val{color:var(--text);font-weight:500}
.about-text p{color:var(--text-dim);margin-bottom:1rem;line-height:1.8;font-size:0.95rem}
.highlight{color:var(--cyan);font-weight:600}
.social-links{display:flex;gap:1rem;margin-top:1.5rem;flex-wrap:wrap;justify-content:center}
.social-link{display:inline-flex;align-items:center;gap:0.5rem;background:rgba(0,212,255,0.08);border:1px solid rgba(0,212,255,0.2);color:var(--cyan);padding:0.5rem 1rem;border-radius:8px;font-size:0.85rem;text-decoration:none;font-weight:500;transition:var(--transition)}
.social-link:hover{background:rgba(0,212,255,0.15);transform:translateY(-2px)}
#skills{background:var(--bg)}
.skills-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.skill-category{background:var(--glass);border:1px solid var(--border);border-radius:var(--radius);padding:1.75rem;backdrop-filter:blur(20px);transition:var(--transition)}
.skill-category:hover{border-color:var(--cyan);box-shadow:var(--glow);transform:translateY(-4px)}
.skill-cat-header{display:flex;align-items:center;gap:0.75rem;margin-bottom:1.25rem}
.skill-cat-icon{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem}
.icon-vlsi{background:rgba(0,212,255,0.15)}
.icon-sw{background:rgba(124,58,237,0.15)}
.icon-hw{background:rgba(0,255,178,0.15)}
.skill-cat-title{font-weight:700;font-size:1rem}
.skill-tags{display:flex;flex-wrap:wrap;gap:0.5rem}
.skill-tag{font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:500;padding:0.35rem 0.75rem;border-radius:6px;border:1px solid rgba(0,212,255,0.2);color:var(--text-dim);transition:var(--transition)}
.skill-tag.cyan{background:rgba(0,212,255,0.08);color:var(--cyan);border-color:rgba(0,212,255,0.3)}
.skill-tag.purple{background:rgba(124,58,237,0.08);color:var(--purple-lt);border-color:rgba(124,58,237,0.3)}
.skill-tag.teal{background:rgba(0,255,178,0.08);color:var(--teal);border-color:rgba(0,255,178,0.3)}
#projects{background:var(--bg2)}
.projects-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:1.75rem}
.project-card{background:var(--glass);border:1px solid var(--border);border-radius:var(--radius);padding:1.75rem;backdrop-filter:blur(20px);transition:var(--transition);position:relative;overflow:hidden}
.project-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(to right,var(--cyan),var(--purple));transform:scaleX(0);transition:transform 0.4s ease}
.project-card:hover::before{transform:scaleX(1)}
.project-card:hover{border-color:rgba(0,212,255,0.3);transform:translateY(-6px);box-shadow:var(--glow)}
.project-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:1rem;gap:1rem}
.project-icon{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;flex-shrink:0}
.project-title{font-size:1.05rem;font-weight:700;margin-bottom:0.25rem}
.project-desc{color:var(--text-dim);font-size:0.875rem;line-height:1.7;margin-bottom:1rem}
.project-tech{display:flex;flex-wrap:wrap;gap:0.4rem;margin-bottom:1rem}
.tech-tag{font-family:'JetBrains Mono',monospace;font-size:0.7rem;padding:0.25rem 0.6rem;border-radius:4px;background:rgba(124,58,237,0.1);color:var(--purple-lt);border:1px solid rgba(124,58,237,0.2)}
.project-link{display:inline-flex;align-items:center;gap:0.4rem;color:var(--cyan);font-size:0.82rem;text-decoration:none;font-weight:600;transition:var(--transition)}
.project-link:hover{gap:0.8rem}
.project-num{font-family:'JetBrains Mono',monospace;font-size:2rem;font-weight:800;color:rgba(0,212,255,0.08);position:absolute;top:1rem;right:1.25rem;line-height:1}
#experience{background:var(--bg)}
.timeline{position:relative;padding-left:2rem}
.timeline::before{content:'';position:absolute;left:0;top:0;bottom:0;width:2px;background:linear-gradient(to bottom,var(--cyan),var(--purple),transparent)}
.timeline-item{position:relative;margin-bottom:2.5rem}
.timeline-dot{position:absolute;left:-2.4rem;top:0.3rem;width:14px;height:14px;border-radius:50%;background:var(--bg);border:2px solid var(--cyan);box-shadow:0 0 10px rgba(0,212,255,0.5)}
.timeline-card{background:var(--glass);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;backdrop-filter:blur(20px);transition:var(--transition)}
.timeline-card:hover{border-color:var(--cyan);transform:translateX(6px)}
.timeline-header{display:flex;align-items:flex-start;justify-content:space-between;gap:1rem;margin-bottom:0.5rem}
.timeline-role{font-size:1rem;font-weight:700;color:var(--text)}
.timeline-company{font-size:0.875rem;color:var(--cyan);font-weight:600;margin-bottom:0.25rem}
.timeline-date{font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--text-dim);background:rgba(0,212,255,0.08);border:1px solid rgba(0,212,255,0.2);padding:0.2rem 0.6rem;border-radius:4px;white-space:nowrap;flex-shrink:0}
.timeline-desc{color:var(--text-dim);font-size:0.875rem;line-height:1.7}
#certifications{background:var(--bg2)}
.cert-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.25rem}
.cert-card{background:var(--glass);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;backdrop-filter:blur(20px);transition:var(--transition);display:flex;gap:1rem;align-items:flex-start}
.cert-card:hover{border-color:var(--gold);transform:translateY(-4px);box-shadow:0 0 20px rgba(251,191,36,0.15)}
.cert-icon{width:44px;height:44px;border-radius:10px;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.25);display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0}
.cert-title{font-size:0.9rem;font-weight:700;margin-bottom:0.25rem}
.cert-issuer{font-size:0.8rem;color:var(--text-dim)}
#achievements{background:var(--bg)}
.achievements-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.25rem}
.achievement-card{background:var(--glass);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;backdrop-filter:blur(20px);transition:var(--transition);position:relative;overflow:hidden}
.achievement-card:hover{border-color:var(--gold);transform:translateY(-4px)}
.prize-badge{display:inline-flex;align-items:center;gap:0.4rem;padding:0.3rem 0.8rem;border-radius:50px;font-size:0.75rem;font-weight:700;margin-bottom:0.75rem}
.prize-1{background:rgba(251,191,36,0.15);color:var(--gold);border:1px solid rgba(251,191,36,0.3)}
.prize-2{background:rgba(148,163,184,0.15);color:#94a3b8;border:1px solid rgba(148,163,184,0.3)}
.achievement-title{font-size:0.9rem;font-weight:700;margin-bottom:0.25rem}
.achievement-venue{font-size:0.8rem;color:var(--text-dim);line-height:1.5}
#contact{background:var(--bg2)}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start}
.contact-info h3{font-size:1.4rem;font-weight:700;margin-bottom:1rem}
.contact-info p{color:var(--text-dim);font-size:0.95rem;line-height:1.8;margin-bottom:2rem}
.contact-links{display:flex;flex-direction:column;gap:1rem}
.contact-link-item{display:flex;align-items:center;gap:1rem;text-decoration:none;color:var(--text);background:var(--glass);border:1px solid var(--border);border-radius:12px;padding:1rem 1.25rem;transition:var(--transition);backdrop-filter:blur(20px)}
.contact-link-item:hover{border-color:var(--cyan);color:var(--cyan);transform:translateX(6px)}
.contact-link-icon{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0}
.contact-link-text strong{display:block;font-size:0.85rem;font-weight:600}
.contact-link-text span{font-size:0.78rem;color:var(--text-dim)}
.contact-form{display:flex;flex-direction:column;gap:1rem}
.form-group{display:flex;flex-direction:column;gap:0.4rem}
.form-group label{font-size:0.82rem;color:var(--text-dim);font-weight:500}
.form-group input,.form-group textarea{background:rgba(13,24,39,0.8);border:1px solid var(--border);border-radius:10px;padding:0.85rem 1rem;color:var(--text);font-family:'Inter',sans-serif;font-size:0.9rem;transition:var(--transition);outline:none}
.form-group input:focus,.form-group textarea:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,212,255,0.1)}
.form-group textarea{resize:vertical;min-height:120px}
.form-submit{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#fff;border:none;border-radius:10px;padding:0.9rem 2rem;font-size:0.9rem;font-weight:600;cursor:pointer;transition:var(--transition);display:flex;align-items:center;justify-content:center;gap:0.5rem}
.form-submit:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(0,212,255,0.4)}
footer{background:var(--bg);border-top:1px solid var(--border);padding:2rem 6%;text-align:center;position:relative;z-index:1}
.footer-text{color:var(--text-dim);font-size:0.85rem}
.footer-span{color:var(--cyan);font-family:'JetBrains Mono',monospace}
.reveal{opacity:0;transform:translateY(30px);transition:opacity 0.7s ease,transform 0.7s ease}
.reveal.visible{opacity:1;transform:translateY(0)}
@media(max-width:900px){
  .hero-grid{grid-template-columns:1fr;text-align:center}
  .hero-bio{max-width:100%;margin:0 auto 2rem}
  .hero-btns{justify-content:center}
  .hero-stats{justify-content:center}
  .hero-visual{display:none}
  .about-grid{grid-template-columns:1fr}
  .contact-grid{grid-template-columns:1fr}
  .nav-links{display:none}
  .hamburger{display:flex}
}
@media(max-width:600px){
  section{padding:4rem 5%}
  .projects-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<canvas id="circuit-canvas"></canvas>
<nav id="navbar">
  <a href="#hero" class="nav-logo">TC<span>.portfolio</span></a>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#certifications">Certs</a></li>
    <li><a href="#achievements">Awards</a></li>
    <li><a href="#contact" class="nav-cta">Contact</a></li>
  </ul>
  <div class="hamburger" id="hamburger"><span></span><span></span><span></span></div>
</nav>
<main>
<section id="hero">
  <div class="hero-grid">
    <div class="hero-content">
      <div class="hero-badge">Available for Internship and Placement Opportunities</div>
      <h1 class="hero-name">
        <span class="first">Thatha </span><br/>
        <span class="last">Chenchaiah</span>
      </h1>
      <div class="hero-typed-wrapper">
        <span class="typed-prefix">&gt;&gt; </span>
        <span id="typed-text"></span>
        <span class="cursor"></span>
      </div>
      <p class="hero-bio">4th-year B.Tech ECE student at <strong>PBR Visvodaya Institute of Science and Technology</strong>, passionate about VLSI design, digital systems, and software automation. Building real-world hardware and software solutions. From Kavali, Andhra Pradesh.</p>
      <div class="hero-btns">
        <a href="#projects" class="btn btn-primary">View Projects</a>
        <a href="#contact" class="btn btn-outline">Get in Touch</a>
      </div>
      <div class="hero-stats">
        <div class="stat"><div class="stat-num">5+</div><div class="stat-label">Projects</div></div>
        <div class="stat"><div class="stat-num">3</div><div class="stat-label">Internships</div></div>
        <div class="stat"><div class="stat-num">6</div><div class="stat-label">Certifications</div></div>
        <div class="stat"><div class="stat-num">4</div><div class="stat-label">Awards</div></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-chip">
        <div class="chip-ring"></div>
        <div class="chip-ring-2"></div>
        <svg class="chip-svg" viewBox="0 0 320 320" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs><linearGradient id="cg" x1="0" y1="0" x2="320" y2="320" gradientUnits="userSpaceOnUse"><stop offset="0%" stop-color="#00d4ff" stop-opacity="0.3"/><stop offset="100%" stop-color="#7c3aed" stop-opacity="0.3"/></linearGradient></defs>
          <rect x="80" y="80" width="160" height="160" rx="12" fill="url(#cg)" stroke="#00d4ff" stroke-width="1.5"/>
          <rect x="100" y="100" width="120" height="120" rx="6" fill="rgba(0,212,255,0.05)" stroke="rgba(0,212,255,0.4)" stroke-width="1"/>
          <line x1="140" y1="100" x2="140" y2="220" stroke="rgba(0,212,255,0.15)" stroke-width="0.5"/>
          <line x1="160" y1="100" x2="160" y2="220" stroke="rgba(0,212,255,0.15)" stroke-width="0.5"/>
          <line x1="180" y1="100" x2="180" y2="220" stroke="rgba(0,212,255,0.15)" stroke-width="0.5"/>
          <line x1="100" y1="140" x2="220" y2="140" stroke="rgba(0,212,255,0.15)" stroke-width="0.5"/>
          <line x1="100" y1="160" x2="220" y2="160" stroke="rgba(0,212,255,0.15)" stroke-width="0.5"/>
          <line x1="100" y1="180" x2="220" y2="180" stroke="rgba(0,212,255,0.15)" stroke-width="0.5"/>
          <rect x="120" y="120" width="80" height="80" rx="4" fill="rgba(124,58,237,0.2)" stroke="#a78bfa" stroke-width="1"/>
          <text x="160" y="168" text-anchor="middle" fill="#00d4ff" font-family="monospace" font-size="12" font-weight="bold">VLSI</text>
          <rect x="110" y="68" width="8" height="14" rx="2" fill="#00d4ff" opacity="0.7"/>
          <rect x="130" y="68" width="8" height="14" rx="2" fill="#00d4ff" opacity="0.7"/>
          <rect x="150" y="68" width="8" height="14" rx="2" fill="#00d4ff" opacity="0.7"/>
          <rect x="170" y="68" width="8" height="14" rx="2" fill="#00d4ff" opacity="0.7"/>
          <rect x="190" y="68" width="8" height="14" rx="2" fill="#00d4ff" opacity="0.7"/>
          <rect x="110" y="238" width="8" height="14" rx="2" fill="#00ffb2" opacity="0.7"/>
          <rect x="130" y="238" width="8" height="14" rx="2" fill="#00ffb2" opacity="0.7"/>
          <rect x="150" y="238" width="8" height="14" rx="2" fill="#00ffb2" opacity="0.7"/>
          <rect x="170" y="238" width="8" height="14" rx="2" fill="#00ffb2" opacity="0.7"/>
          <rect x="190" y="238" width="8" height="14" rx="2" fill="#00ffb2" opacity="0.7"/>
          <rect x="68" y="110" width="14" height="8" rx="2" fill="#a78bfa" opacity="0.7"/>
          <rect x="68" y="130" width="14" height="8" rx="2" fill="#a78bfa" opacity="0.7"/>
          <rect x="68" y="150" width="14" height="8" rx="2" fill="#a78bfa" opacity="0.7"/>
          <rect x="68" y="170" width="14" height="8" rx="2" fill="#a78bfa" opacity="0.7"/>
          <rect x="68" y="190" width="14" height="8" rx="2" fill="#a78bfa" opacity="0.7"/>
          <rect x="238" y="110" width="14" height="8" rx="2" fill="#fbbf24" opacity="0.7"/>
          <rect x="238" y="130" width="14" height="8" rx="2" fill="#fbbf24" opacity="0.7"/>
          <rect x="238" y="150" width="14" height="8" rx="2" fill="#fbbf24" opacity="0.7"/>
          <rect x="238" y="170" width="14" height="8" rx="2" fill="#fbbf24" opacity="0.7"/>
          <rect x="238" y="190" width="14" height="8" rx="2" fill="#fbbf24" opacity="0.7"/>
          <circle cx="92" cy="92" r="4" fill="#00d4ff" opacity="0.5"/>
        </svg>
      </div>
    </div>
  </div>
</section>
<section id="about">
  <div class="reveal">
    <p class="section-tag">01 / About Me</p>
    <h2 class="section-title">The <span>Person</span> Behind the Circuits</h2>
    <div class="section-divider"></div>
  </div>
  <div class="about-grid reveal">
    <div class="about-card">
      <div class="about-avatar">TC</div>
      <div class="about-info">
        <h3>Thatha Chenchaiah</h3>
        <p class="role-tag">ECE Student | VLSI Aspirant</p>
        <div class="info-list">
          <div class="info-item"><span class="info-icon">&#127891;</span><span class="info-label">Institute</span><span class="info-val">PBR Visvodaya Institute of Science and Technology</span></div>
          <div class="info-item"><span class="info-icon">&#128203;</span><span class="info-label">Roll No.</span><span class="info-val">2373A04069 (R23)</span></div>
          <div class="info-item"><span class="info-icon">&#128197;</span><span class="info-label">Graduation</span><span class="info-val">2027 | B.Tech ECE</span></div>
          <div class="info-item"><span class="info-icon">&#128205;</span><span class="info-label">Location</span><span class="info-val">Kavali, Andhra Pradesh</span></div>
          <div class="info-item"><span class="info-icon">&#127760;</span><span class="info-label">Languages</span><span class="info-val">Telugu, English</span></div>
        </div>
        <div class="social-links">
          <a href="mailto:thathachenchaiah506@gmail.com" class="social-link">Email</a>
          <a href="https://www.linkedin.com/in/thatha-chenchaiah-99254634a/" target="_blank" class="social-link">LinkedIn</a>
          <a href="https://github.com/Chenchaiah143" target="_blank" class="social-link">GitHub</a>
        </div>
      </div>
    </div>
    <div class="about-text">
      <p>Hi, I am <span class="highlight">Thatha Chenchaiah</span> - a driven electronics engineering student with a deep passion for <span class="highlight">VLSI/digital design</span>, <span class="highlight">embedded systems</span>, and <span class="highlight">software test automation</span>.</p>
      <p>My core interests lie at the intersection of hardware and software. On the hardware side, I design sequential circuits using <span class="highlight">Verilog HDL</span> - including FSM-based traffic light controllers and matrix keypad scanners targeting FPGA. On the software side, I build automation test frameworks using <span class="highlight">Selenium in Java</span>.</p>
      <p>I have also ventured into creative web development - building a browser-based GTA-style game Vice Circuit using HTML5 and Three.js, and a Logic Circuit Lab web app with SVG schematics and an ML-based logic gate predictor built with Antigravity AI.</p>
      <p>I have completed internship training with <span class="highlight">Sri Shasha Prayathi Technologies</span>, <span class="highlight">SkillDzire Technologies</span>, and industrial exposure at <span class="highlight">Daikin Airconditioning India</span>. Actively preparing for campus placements and VLSI-focused career opportunities.</p>
    </div>
  </div>
</section>
<section id="skills">
  <div class="reveal">
    <p class="section-tag">02 / Tech Stack</p>
    <h2 class="section-title">Skills and <span>Expertise</span></h2>
    <div class="section-divider"></div>
  </div>
  <div class="skills-grid">
    <div class="skill-category reveal">
      <div class="skill-cat-header"><div class="skill-cat-icon icon-vlsi">&#9889;</div><div class="skill-cat-title">VLSI and Hardware</div></div>
      <div class="skill-tags">
        <span class="skill-tag cyan">Verilog HDL</span>
        <span class="skill-tag cyan">Digital Design</span>
        <span class="skill-tag cyan">FSM Design</span>
        <span class="skill-tag cyan">FPGA</span>
        <span class="skill-tag cyan">Digital Electronics</span>
        <span class="skill-tag cyan">Analog Electronics</span>
        <span class="skill-tag cyan">Network Analysis</span>
        <span class="skill-tag cyan">Low Power VLSI</span>
        <span class="skill-tag cyan">Embedded Systems</span>
      </div>
    </div>
    <div class="skill-category reveal">
      <div class="skill-cat-header"><div class="skill-cat-icon icon-sw">&#129514;</div><div class="skill-cat-title">Software and Automation</div></div>
      <div class="skill-tags">
        <span class="skill-tag purple">Selenium WebDriver</span>
        <span class="skill-tag purple">Java</span>
        <span class="skill-tag purple">Test Automation</span>
        <span class="skill-tag purple">Python Basics</span>
        <span class="skill-tag purple">JavaScript</span>
        <span class="skill-tag purple">HTML5 and CSS3</span>
        <span class="skill-tag purple">scikit-learn Basics</span>
      </div>
    </div>
    <div class="skill-category reveal">
      <div class="skill-cat-header"><div class="skill-cat-icon icon-hw">&#128300;</div><div class="skill-cat-title">Tools and Other</div></div>
      <div class="skill-tags">
        <span class="skill-tag teal">MATLAB Basics</span>
        <span class="skill-tag teal">Three.js</span>
        <span class="skill-tag teal">SVG and Canvas</span>
        <span class="skill-tag teal">GitHub Pages</span>
        <span class="skill-tag teal">IoT</span>
        <span class="skill-tag teal">HVAC Systems</span>
        <span class="skill-tag teal">Google Cloud</span>
      </div>
    </div>
  </div>
</section>
<section id="projects">
  <div class="reveal">
    <p class="section-tag">03 / Portfolio</p>
    <h2 class="section-title">Featured <span>Projects</span></h2>
    <div class="section-divider"></div>
  </div>
  <div class="projects-grid">
    <div class="project-card reveal">
      <div class="project-num">01</div>
      <div class="project-header"><div><div class="project-title">Logic Circuit Predictor</div></div><div class="project-icon" style="background:rgba(0,212,255,0.12)">&#128300;</div></div>
      <p class="project-desc">Browser-based logic gate simulator with SVG schematics, interactive truth tables, and an ML prediction API for circuit behavior. Built using Antigravity AI.</p>
      <div class="project-tech"><span class="tech-tag">JavaScript</span><span class="tech-tag">SVG</span><span class="tech-tag">Python</span><span class="tech-tag">scikit-learn</span><span class="tech-tag">ML Backend</span></div>
      <a href="https://chenchaiah143.github.io/logic_circuit_pridicter/" target="_blank" class="project-link">Live Demo &rarr;</a>
    </div>
    <div class="project-card reveal">
      <div class="project-num">02</div>
      <div class="project-header"><div><div class="project-title">Traffic Light Controller</div></div><div class="project-icon" style="background:rgba(251,191,36,0.12)">&#128678;</div></div>
      <p class="project-desc">Sequential traffic light controller using Moore FSM with 13 states for a two-road intersection. Priority logic gives Street A default green, Street B triggers switching when vehicles are detected, with extendable timing.</p>
      <div class="project-tech"><span class="tech-tag">Verilog HDL</span><span class="tech-tag">FSM 13 states</span><span class="tech-tag">FPGA</span><span class="tech-tag">Moore Machine</span></div>
    </div>
    <div class="project-card reveal">
      <div class="project-num">03</div>
      <div class="project-header"><div><div class="project-title">4x3 Matrix Keypad Scanner</div></div><div class="project-icon" style="background:rgba(124,58,237,0.12)">&#9110;</div></div>
      <p class="project-desc">Matrix keypad scanner with debouncing and decoding - scans rows and columns, generates 5-bit binary code for pressed key, outputs valid signal for one clock cycle with 2-stage flip-flop debounce circuit.</p>
      <div class="project-tech"><span class="tech-tag">Verilog HDL</span><span class="tech-tag">FSM 6 states</span><span class="tech-tag">FPGA</span><span class="tech-tag">Debounce Circuit</span></div>
    </div>
    <div class="project-card reveal">
      <div class="project-num">04</div>
      <div class="project-header"><div><div class="project-title">Facebook Signup Automation</div></div><div class="project-icon" style="background:rgba(0,255,178,0.12)">&#129302;</div></div>
      <p class="project-desc">End-to-end automated Facebook signup and login flow testing covering form validation, account creation, and authentication workflows using Selenium WebDriver.</p>
      <div class="project-tech"><span class="tech-tag">Selenium</span><span class="tech-tag">Java</span><span class="tech-tag">WebDriver</span><span class="tech-tag">Test Automation</span></div>
    </div>
    <div class="project-card reveal">
      <div class="project-num">05</div>
      <div class="project-header"><div><div class="project-title">Clap Switch Mini Project</div></div><div class="project-icon" style="background:rgba(251,191,36,0.1)">&#128079;</div></div>
      <p class="project-desc">Sound-activated electronic switch circuit that turns devices ON or OFF on detecting a clap. Demonstrates analog signal processing and relay control for home automation applications.</p>
      <div class="project-tech"><span class="tech-tag">Analog Electronics</span><span class="tech-tag">Circuit Design</span><span class="tech-tag">Home Automation</span></div>
    </div>
  </div>
</section>
<section id="experience">
  <div class="reveal">
    <p class="section-tag">04 / Experience</p>
    <h2 class="section-title">Internships and <span>Training</span></h2>
    <div class="section-divider"></div>
  </div>
  <div class="timeline">
    <div class="timeline-item reveal">
      <div class="timeline-dot"></div>
      <div class="timeline-card">
        <div class="timeline-header"><div><div class="timeline-role">Advanced VLSI and Chip Design Intern</div><div class="timeline-company">SkillDzire Technologies Pvt. Ltd.</div></div><span class="timeline-date">Recent</span></div>
        <p class="timeline-desc">In-depth training on advanced VLSI concepts and chip design methodologies. Covered RTL design, synthesis flows, and modern chip design practices used in the semiconductor industry.</p>
      </div>
    </div>
    <div class="timeline-item reveal">
      <div class="timeline-dot"></div>
      <div class="timeline-card">
        <div class="timeline-header"><div><div class="timeline-role">VLSI Signal Processing with FPGA Intern</div><div class="timeline-company">Sri Shasha Prayathi Technologies</div></div><span class="timeline-date">Recent</span></div>
        <p class="timeline-desc">Hands-on FPGA-based signal processing internship. Implemented digital signal processing algorithms in Verilog HDL and deployed on FPGA development boards.</p>
      </div>
    </div>
    <div class="timeline-item reveal">
      <div class="timeline-dot"></div>
      <div class="timeline-card">
        <div class="timeline-header"><div><div class="timeline-role">Industrial Training - HVAC Systems</div><div class="timeline-company">Daikin Airconditioning India Pvt. Ltd.</div></div><span class="timeline-date">Dec 2025</span></div>
        <p class="timeline-desc">HVAC Skill Enhancement Program - industrial exposure to Heating, Ventilation, and Air Conditioning systems, product training, and energy efficiency concepts at Daikin facilities.</p>
      </div>
    </div>
  </div>
</section>
<section id="certifications">
  <div class="reveal">
    <p class="section-tag">05 / Credentials</p>
    <h2 class="section-title">Certifications and <span>Courses</span></h2>
    <div class="section-divider"></div>
  </div>
  <div class="cert-grid">
    <div class="cert-card reveal"><div class="cert-icon">&#127981;</div><div><div class="cert-title">HVAC Skill Enhancement Program</div><div class="cert-issuer">Daikin Airconditioning India Pvt. Ltd. | Dec 2025</div></div></div>
    <div class="cert-card reveal"><div class="cert-icon">&#9889;</div><div><div class="cert-title">VLSI Signal Processing with FPGA</div><div class="cert-issuer">Sri Shasha Prayathi Technologies</div></div></div>
    <div class="cert-card reveal"><div class="cert-icon">&#128300;</div><div><div class="cert-title">Advanced VLSI and Chip Design</div><div class="cert-issuer">SkillDzire Technologies Pvt. Ltd.</div></div></div>
    <div class="cert-card reveal"><div class="cert-icon">&#128013;</div><div><div class="cert-title">Python for Data Science</div><div class="cert-issuer">NPTEL | IIT</div></div></div>
    <div class="cert-card reveal"><div class="cert-icon">&#128187;</div><div><div class="cert-title">Computer Architecture and Organization</div><div class="cert-issuer">NPTEL | IIT</div></div></div>
    <div class="cert-card reveal"><div class="cert-icon">&#9925;</div><div><div class="cert-title">Google Cloud - Hack2skill</div><div class="cert-issuer">Google Cloud | Hack2skill</div></div></div>
  </div>
</section>
<section id="achievements">
  <div class="reveal">
    <p class="section-tag">06 / Recognition</p>
    <h2 class="section-title">Awards and <span>Achievements</span></h2>
    <div class="section-divider"></div>
  </div>
  <div class="achievements-grid">
    <div class="achievement-card reveal"><span class="prize-badge prize-1">1st Prize</span><div class="achievement-title">Technical Quiz Competition</div><div class="achievement-venue">Geethanjali College of Engineering and Technology</div></div>
    <div class="achievement-card reveal"><span class="prize-badge prize-2">2nd Prize</span><div class="achievement-title">Circuit Debugging Competition</div><div class="achievement-venue">Geethanjali College of Engineering and Technology</div></div>
    <div class="achievement-card reveal"><span class="prize-badge prize-2">2nd Prize</span><div class="achievement-title">Circuit Debugging Competition</div><div class="achievement-venue">Audisankara College of Engineering and Technology</div></div>
    <div class="achievement-card reveal"><span class="prize-badge prize-2">2nd Prize</span><div class="achievement-title">Quiz Competition</div><div class="achievement-venue">St. Ann's College of Engineering and Technology</div></div>
  </div>
</section>
<section id="contact">
  <div class="reveal">
    <p class="section-tag">07 / Contact</p>
    <h2 class="section-title">Let's <span>Connect</span></h2>
    <div class="section-divider"></div>
  </div>
  <div class="contact-grid">
    <div class="contact-info reveal">
      <h3>Open to Opportunities</h3>
      <p>Actively looking for <strong>VLSI internships</strong>, <strong>automation testing roles</strong>, and <strong>campus placement opportunities</strong>. Whether you have a project, an internship, or just want to connect - my inbox is always open!</p>
      <div class="contact-links">
        <a href="mailto:thathachenchaiah506@gmail.com" class="contact-link-item"><div class="contact-link-icon" style="background:rgba(0,212,255,0.1)">&#128231;</div><div class="contact-link-text"><strong>Email</strong><span>thathachenchaiah506@gmail.com</span></div></a>
        <a href="https://www.linkedin.com/in/thatha-chenchaiah-99254634a/" target="_blank" class="contact-link-item"><div class="contact-link-icon" style="background:rgba(0,119,181,0.1)">&#128188;</div><div class="contact-link-text"><strong>LinkedIn</strong><span>thatha-chenchaiah-99254634a</span></div></a>
        <a href="https://github.com/Chenchaiah143" target="_blank" class="contact-link-item"><div class="contact-link-icon" style="background:rgba(255,255,255,0.05)">&#128025;</div><div class="contact-link-text"><strong>GitHub</strong><span>Chenchaiah143</span></div></a>
      </div>
    </div>
    <form class="contact-form reveal" onsubmit="handleFormSubmit(event)">
      <div class="form-group"><label for="contact-name">Your Name</label><input type="text" id="contact-name" placeholder="John Doe" required/></div>
      <div class="form-group"><label for="contact-email">Your Email</label><input type="email" id="contact-email" placeholder="john@example.com" required/></div>
      <div class="form-group"><label for="contact-subject">Subject</label><input type="text" id="contact-subject" placeholder="Internship / Collaboration / Connect" required/></div>
      <div class="form-group"><label for="contact-message">Message</label><textarea id="contact-message" placeholder="Write your message here..." required></textarea></div>
      <button type="submit" class="form-submit" id="form-submit-btn"><span id="submit-text">Send Message</span></button>
    </form>
  </div>
</section>
</main>
<footer><p class="footer-text">Designed and Built by <span class="footer-span">Thatha Chenchaiah</span> | <span class="footer-span">ECE | VLSI | Automation</span> | 2025</p></footer>
<script>
(function(){
var canvas=document.getElementById('circuit-canvas');
var ctx=canvas.getContext('2d');
var w,h,nodes,particles;
function resize(){w=canvas.width=window.innerWidth;h=canvas.height=window.innerHeight;initNodes();}
function initNodes(){
  nodes=[];
  var count=Math.floor((w*h)/30000);
  for(var i=0;i<count;i++){nodes.push({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-0.5)*0.3,vy:(Math.random()-0.5)*0.3,r:Math.random()*3+1});}
  particles=[];
  for(var j=0;j<5;j++){particles.push({src:Math.floor(Math.random()*nodes.length),dst:Math.floor(Math.random()*nodes.length),t:Math.random(),speed:0.003+Math.random()*0.004});}
}
function draw(){
  ctx.clearRect(0,0,w,h);
  nodes.forEach(function(n){n.x+=n.vx;n.y+=n.vy;if(n.x<0||n.x>w)n.vx*=-1;if(n.y<0||n.y>h)n.vy*=-1;});
  for(var i=0;i<nodes.length;i++){for(var j=i+1;j<nodes.length;j++){var dx=nodes[i].x-nodes[j].x;var dy=nodes[i].y-nodes[j].y;var dist=Math.sqrt(dx*dx+dy*dy);if(dist<180){ctx.strokeStyle='rgba(0,212,255,'+(1-dist/180)*0.15+')';ctx.lineWidth=0.5;ctx.beginPath();ctx.moveTo(nodes[i].x,nodes[i].y);ctx.lineTo(nodes[j].x,nodes[j].y);ctx.stroke();}}}
  nodes.forEach(function(n){ctx.fillStyle='rgba(0,212,255,0.4)';ctx.beginPath();ctx.arc(n.x,n.y,n.r,0,Math.PI*2);ctx.fill();});
  particles.forEach(function(p){p.t+=p.speed;if(p.t>=1){p.t=0;p.src=p.dst;p.dst=Math.floor(Math.random()*nodes.length);}var src=nodes[p.src];var dst=nodes[p.dst];var x=src.x+(dst.x-src.x)*p.t;var y=src.y+(dst.y-src.y)*p.t;ctx.fillStyle='rgba(0,255,178,0.9)';ctx.beginPath();ctx.arc(x,y,3,0,Math.PI*2);ctx.fill();ctx.fillStyle='rgba(0,255,178,0.3)';ctx.beginPath();ctx.arc(x,y,7,0,Math.PI*2);ctx.fill();});
  requestAnimationFrame(draw);
}
window.addEventListener('resize',resize);
resize();draw();
})();
(function(){
var texts=['VLSI Aspirant','Digital Designer','Selenium Tester','Verilog Developer','ECE Engineer','FSM Architect'];
var idx=0,charIdx=0,deleting=false;
var el=document.getElementById('typed-text');
function type(){var current=texts[idx];if(!deleting){el.textContent=current.slice(0,charIdx+1);charIdx++;if(charIdx===current.length){deleting=true;setTimeout(type,1800);return;}}else{el.textContent=current.slice(0,charIdx-1);charIdx--;if(charIdx===0){deleting=false;idx=(idx+1)%texts.length;}}setTimeout(type,deleting?60:100);}
type();
})();
(function(){
var reveals=document.querySelectorAll('.reveal');
var observer=new IntersectionObserver(function(entries){entries.forEach(function(entry,i){if(entry.isIntersecting){setTimeout(function(){entry.target.classList.add('visible');},i*80);}});},{threshold:0.12});
reveals.forEach(function(r){observer.observe(r);});
})();
window.addEventListener('scroll',function(){var nav=document.getElementById('navbar');nav.style.background=window.scrollY>60?'rgba(5,11,20,0.97)':'rgba(5,11,20,0.85)';});
function handleFormSubmit(e){e.preventDefault();var btn=document.getElementById('form-submit-btn');var txt=document.getElementById('submit-text');btn.disabled=true;txt.textContent='Sending...';setTimeout(function(){txt.textContent='Message Sent!';setTimeout(function(){txt.textContent='Send Message';btn.disabled=false;e.target.reset();},2500);},1200);}
document.getElementById('hamburger').addEventListener('click',function(){var links=document.querySelector('.nav-links');if(links.style.display==='flex'){links.style.display='none';}else{links.style.display='flex';links.style.flexDirection='column';links.style.position='absolute';links.style.top='70px';links.style.left='0';links.style.right='0';links.style.background='rgba(5,11,20,0.98)';links.style.padding='1.5rem';links.style.gap='1.25rem';links.style.borderBottom='1px solid rgba(0,212,255,0.15)';links.style.backdropFilter='blur(20px)';}});
</script>
</body>
</html>"""

path = r'C:\Users\THATHA CHENCHAIAH\.gemini\antigravity\scratch\portfolio\index.html'
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
size = os.path.getsize(path)
print(f'SUCCESS: Portfolio written to {path}')
print(f'File size: {size} bytes ({size/1024:.1f} KB)')
