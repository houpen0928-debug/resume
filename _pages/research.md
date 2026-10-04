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

## 工廠 AI 落地框架｜從工站到 ROI

在製造現場推動 AI，關鍵不在模型強弱，而在能否接進產線、串起系統、並產出可量化的價值。以下為我評估與推動工廠 AI 專案時採用的四層結構與選型四問。

### 四層落地結構

**第一層｜工站層（Shop Floor）** 　SMT 貼片、AOI 光學檢測、ICT／FCT 測試、FATP 整機組裝、包裝出貨——每一個工站都是 AI 的接料口。

**第二層｜AI 能力層（Capabilities）** 　視覺檢測（缺陷分類／定位）、時序異常（測試數據／振動／溫漂）、知識問答（SOP／客訴／設備手冊）、預測維護（軸承／電機／老化趨勢）——能力要接到系統才動得了。

**第三層｜系統與資料層（Systems & Data）** 　MES、WMS、ERP、QMS、SCADA／PLC、測試機台、設備日誌（CAN／RS232）、品質資料庫。

**第四層｜價值輸出（Business Value）** 　良率提升、OEE 提升、人力釋放、客訴下降——最終必須落到可量化的成果。

### 選型四問

1. **能不能接料？** 支援你廠的測試機／PLC／老設備嗎（RS232、CAN、Modbus）？
2. **能不能跑流程？** 能不能跨 MES／QMS／ERP 走完整到端流程，而不是單點問答？
3. **能不能被治理？** 有沒有權限、日誌、審批、追溯？產線不能亂改參數。
4. **能不能造 ROI？** 能不能量化到良率／OEE／人力，而不是「感覺很智能」？

四問任一答不出來，這個 AI 就還不能進產線。工廠真正該問的不是「哪個模型最強」，而是「哪個 AI 能接進我的產線，並且講清楚為什麼判這片是 NG」——判得準不夠，還要判得能解釋。

## 研究案例

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
