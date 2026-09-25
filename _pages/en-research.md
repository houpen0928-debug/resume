---
layout: single
title: "Projects & Applied Research"
permalink: /en/research/
author_profile: true
author: jason_en
resume_style: true
lang: en
locale: en
site_title: "Jason Hung | Plant Operations"
excerpt: "17+ years in electronics manufacturing, plant operations, entrepreneurship and AI transformation."
zh_url: /research/
en_url: /en/research/
---

<p class="executive-eyebrow">PROJECTS & APPLIED RESEARCH</p>
<p>Applied research across manufacturing, product development and business operations, exploring AI parameter optimization, IoT services and agentic workflows. Personal participation, team-reported outcomes and third-party study references are identified below.</p>

<nav class="executive-section-nav" aria-label="Research cases">
{% for project in site.data.cv_en.projects %}
<a href="#{{ project.id }}">{{ project.name }}</a><br>
{% endfor %}
</nav>

{% for project in site.data.cv_en.projects %}
<section class="executive-role" id="{{ project.id }}">
  <h2>{{ project.name }}</h2>
  <p class="executive-date">{{ project.category }}</p>
  <p><strong>{{ project.role }}</strong></p>
  <p>{{ project.summary }}</p>
  {% for detail in project.details %}
  <h3>{{ detail.title }}</h3>
  <p>{{ detail.text }}</p>
  {% endfor %}
  <p class="executive-date">Source: {{ project.source }}</p>
</section>
{% endfor %}

<p><a href="{{ '/en/cv/' | relative_url }}">Back to full resume</a></p>
