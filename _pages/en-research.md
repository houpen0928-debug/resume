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

## Factory AI Landing Framework | From Station to ROI

Driving AI on the shop floor is less about how strong the model is, and more about whether it can plug into the line, connect across systems, and produce quantifiable value. Below is the four-layer structure and the four selection questions I use when assessing and driving factory AI projects.

### The Four Layers

**Layer 1 | Shop Floor Stations** — SMT placement, AOI inspection, ICT/FCT test, FATP assembly, packing and shipping. Every station is an intake point for AI.

**Layer 2 | AI Capabilities** — Visual inspection (defect classification/localization), time-series anomaly (test data/vibration/temperature drift), knowledge Q&A (SOP/complaints/equipment manuals), predictive maintenance (bearings/motors/aging trends). Capabilities only move things once they connect to systems.

**Layer 3 | Systems & Data** — MES, WMS, ERP, QMS, SCADA/PLC, test equipment, equipment logs (CAN/RS232), quality databases.

**Layer 4 | Business Value** — Yield, OEE, released manpower, fewer customer complaints. Ultimately it must land on quantifiable outcomes.

### The Four Selection Questions

1. **Can it take the input?** Does it support your testers, PLCs and legacy equipment (RS232, CAN, Modbus)?
2. **Can it run the process?** Can it carry an end-to-end flow across MES/QMS/ERP, not just answer a single point question?
3. **Can it be governed?** Are there permissions, logs, approvals and traceability? A line cannot have parameters changed at will.
4. **Can it create ROI?** Can it be quantified in yield/OEE/manpower, rather than "feels intelligent"?

If any of the four cannot be answered, that AI is not ready for the line. The real question a factory should ask is not "which model is strongest", but "which AI can plug into my line and explain why it judged this piece NG" — accurate is not enough; it must be explainable.

## Research Cases

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
