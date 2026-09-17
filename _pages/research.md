---
layout: single
title: "專案與工作研究經驗"
permalink: /research/
author_profile: true
resume_style: true
lang: zh-TW
locale: zh-TW
zh_url: /research/
en_url: /en/research/
---

<p class="executive-eyebrow">PROJECTS & APPLIED RESEARCH</p>
<p>結合製造現場、產品研發與企業營運，持續研究 AI 參數最佳化、IoT 服務系統及智能體工作流。以下依個人參與、團隊報告與研讀資料說明。</p>

<nav class="executive-section-nav" aria-label="研究案例">
{% for project in site.data.cv.projects %}
<a href="#{{ project.id }}">{{ project.name }}</a><br>
{% endfor %}
</nav>

{% for project in site.data.cv.projects %}
<section class="executive-role" id="{{ project.id }}">
  <h2>{{ project.name }}</h2>
  <p class="executive-date">{{ project.category }}</p>
  <p><strong>{{ project.role }}</strong></p>
  <p>{{ project.summary }}</p>
  {% for detail in project.details %}
  <h3>{{ detail.title }}</h3>
  <p>{{ detail.text }}</p>
  {% endfor %}
  <p class="executive-date">資料依據：{{ project.source }}</p>
</section>
{% endfor %}

<p><a href="{{ '/cv/' | relative_url }}">返回完整履歷</a></p>
