---
layout: "journal"
title: "You Already Have MES. Why Do You Still Need a Quality System? — From Tracking Things to Tracking Closure"
date: "2026-11-18"
lang: "en"
locale: "en"
author_profile: true
resume_style: true
description: "The first internal control system a company builds is almost always MES: incoming material, manufacturing, shipment. The overlooked second layer is the quality system — it does not track where goods are, but whether problems are accumulated, analyzed, traced and closed."
---

> Published as a professional article on 2026-11-18. Also available in [Traditional Chinese]({{ '/blog/2026-11-18-quality-system-beyond-mes/' | relative_url }}).

One Excel file dropped into a WeChat group every day, titled "11/17 Quality Anomalies." By the next morning it is buried under new messages. The same defect occurred on the same line last week, and nobody remembers.

This is not because the shop floor is careless. It is because **the second layer of the system is missing**.

![Concept diagram: the blue upper band is Layer 1 MES, with four boxes — INCOMING → MANUFACTURING → INSPECTION → SHIPMENT — in a one-way line ending at a red dot labelled "RECORD ENDS: ends at shipment"; two grey arrows lead down into the orange Layer 2 quality system, whose five boxes DETECT → TRACE → HANDLE → ANALYZE → DESIGN REC. run left to right, with a feedback arc from DESIGN REC. back to DETECT closing the loop, labelled "Design feedback → specs · process parameters · inspection standards → the next lot"; the closing line reads "MES governs this lot. A quality system governs the next one."]({{ '/images/journal/mes-vs-quality-loop-2026-11-18-en.jpg' | relative_url }})

## 1. The Order of Internal Control Systems: MES Always Comes First

Open any MES architecture diagram on the market and the stack is drawn the same way, bottom to top: incoming material, warehouse, work orders, stations, equipment, operators, WIP, finished goods, shipment. Its core is **tracking things** — where a lot came from, which station it is at now, who ran it, under which parameters, and which customer it shipped to.

This layer has to exist first. Without MES, you cannot even answer "which lot had the problem"; traceability falls back to paper records and asking the veteran operator. So nobody argues against MES. It is usually the first internal control system a company builds — and very often the only one that ever gets built.

That "only" is exactly the problem.

## 2. The Overlooked Second Layer: The Quality System

MES answers **where things are**. It does not answer **why they broke again**.

A quality system governs an entirely different set of objects:

- **Accumulation** of problems — not a single anomaly, but the *nth* occurrence of the same class
- **Analysis** — root cause, correlation, cross-lot comparison
- **Tracing and closure** — who handled the ticket, was the fix verified, did it recur
- **People control** — who judges, who releases, authority and recusal
- **Inspection methods and standards** — SIP, sampling levels, acceptance limits, standard revisions

In one sentence: **MES tracks *things*; a quality system tracks *closure across every layer*.** It lifts tracking from the flow of material to the flow of problems, decisions, accountability and standards.

| | MES | Quality System |
|---|---|---|
| Tracks | Material, work orders, stations | Problems, judgments, dispositions, standards |
| Timeline | Incoming → shipment | Anomaly → analysis → design recommendation → no recurrence |
| Core action | Record flow | Accumulate experience, close the loop |
| Record is most valuable | Right now | Three months later, at the next similar problem |
| Without it | Broken traceability | Re-learning the same lesson every day |

The decisive difference: **an MES record ends the moment the goods ship; the value of a quality system begins the moment an anomaly occurs.**

## 3. That 10% Used to Be the Strongest Objection

In the past, any proposal to implement a quality system ran into the same line:

> "We run high-mix, low-volume production. Product types keep changing, inspection standards have to change with them — roughly 10% variability. A system simply cannot be pinned down."

Back then, this was **a valid argument**, not an excuse.

Traditional systems were static: one specification table, one inspection procedure, one hardcoded set of decision rules. Change the product or revise the standard, and someone had to edit configurations, forms and code. Ten percent sounds small — multiplied by dozens of product types and hundreds of inspection items, maintenance becomes a full-time job that always lags behind the shop floor.

So the quality system stayed on "next quarter" forever, and the shop floor kept using Excel. **Using 10% to reject a quality system was, at the time, sound engineering judgment.**

## 4. AI Turns That 10% From a Blocker Into a Ticket to Entry

Today only one thing has changed: **dynamic, real-time baseline judgment is no longer a barrier.**

- Bring in the product type and the matching standard revision, sampling level and acceptance limits come with it — nobody picks a table by hand
- Anomaly descriptions are classified automatically and matched against historical cases: "does this look like that lot three weeks ago?"
- When a standard changes, the system follows — no waiting for an IT ticket

To be precise: **AI does not make the QC judgment.** Final acceptance still belongs to a person, with a signature. What AI does is turn "standards must follow the product" — previously a manual maintenance burden — into a baseline capability of the system.

So that 10% is no longer a reason to say no. **What remains is not a technical problem. It is whether we are willing to change how we think.**

## 5. The Real Cost of a Daily Excel File Is Not "No Records"

To be fair: an Excel file in a group chat *is* a record. The problem is not that nothing is recorded — it is that **records cannot accumulate**.

Three concrete losses:

**First, the fifth occurrence of the same problem is still treated as a new one.** Nobody knows it is the fifth, so every time the investigation starts from zero and a fresh 8D is written. The organization pays tuition five times and buys one lesson.

**Second, judgment walks out with the person.** A veteran QC takes one look and knows "this kind of contamination usually means the cleaning bath changeover cycle." That sentence lives in no system. On the day they leave, the company loses a set of criteria — and nobody notices.

**Third, the most valuable thing is never computed.** Every production day generates real experience: which product type combined with which supplier's material tends to deform, which line sees contamination spike during which shift, which combination of process parameters fails three months later. Those correlations sit scattered across hundreds of spreadsheets and have never been cross-matched.

**The factory pays tuition every single day and never receives a diploma.**

What a quality system must catch is not "a better-looking report." It is turning each day's anomalies into experience that can be found next time.

## 6. Where Exactly Should the Loop Close?

The most common way to build a quality system badly is to build an *anomaly logging system* — open a ticket, fill the fields, close it, archive it. It looks complete, and the problem recurs anyway.

A real closed loop has to reach the final step:

**Detect → Trace → Handle → Analyze → Design Recommendation**

Most systems cover the first four. The fifth is the rare one. **If analysis never feeds back into design specs, process parameters or inspection standards, it is just bookkeeping.**

An example: for one product, the welding stage reports 15% VC incoming deformation, while the assembly stage reports 16.67% missing substrate and fin deformation. MES faithfully records two unrelated anomalies and files them separately. A quality system must collide them into one problem chain — and then feed back into incoming acceptance limits or fixture design. **Two numbers from the same lot only speak when they are connected.**

Add two layers MES usually does not govern: **people control** (who has release authority, when recusal applies) and **inspection method** (if two inspectors judge the same defect differently, the standard has not actually landed).

## Closing

The order of internal control systems is actually quite clear:

**MES first, to know where the goods went. A quality system second, to remember what was learned.**

Almost every company builds the first layer, because it maps directly to shipments, customer audits and financial reporting. The second layer mostly still lives in WeChat groups, because its return is not today — it is "not breaking again next time."

**MES governs this lot. A quality system governs making sure the next lot does not break the same way.**

Tooling stopped being the barrier a while ago. What blocks it now is simply whether someone is willing to replace that daily Excel file with a loop that accumulates on its own. Staying with Excel is not fatal — it is just a pity that the real value accumulated on the shop floor every day keeps sinking, one day at a time, into a chat history.

---

*Further reading: [Factory AI Adoption: The Data Foundation Is the First Barrier]({{ '/blog/2026-10-15-factory-ai-data-foundation-en/' | relative_url }}) — the earlier stretch of the same road: data must get in before dynamic judgment is possible.*
*[Organizations Don't Remember, So They Start Over]({{ '/blog/2026-11-12-organization-doesnt-remember/' | relative_url }}) (in Chinese) — the same problem on the R&D side.*
