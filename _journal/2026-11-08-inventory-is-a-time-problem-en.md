---
layout: "journal"
title: "Inventory Isn't Arithmetic — It's Time"
date: "2026-11-08"
lang: "en"
locale: "en"
author_profile: true
resume_style: true
description: "On the surface inventory is arithmetic. Underneath, it's time. From quote to delivery an order has exactly two windows where you can still act — everything after that is cleanup."
---

> Published as a professional article on 2026-11-08. Also available in [Traditional Chinese]({{ '/blog/2026-11-08-inventory-is-a-time-problem/' | relative_url }}).

![Illustration: an antique brass hourglass sits on a wooden crate in a dim warehouse aisle lined with steel shelving and cartons; the glass holds no sand but fine silver powder and small silver ingots trickling through the waist, catching a single warm light from the right]({{ '/images/journal/inventory-time-hourglass-2026-11-08.jpg' | relative_url }})

Over the years I've read a fair amount of management philosophy from people who built successful companies. Toyota in Japan, Formosa Plastics in Taiwan, Amazon in the United States — manufacturing or online retail, once production is involved, you cannot walk around inventory.

Finished goods, work in progress, raw material: all of it is moving. It moves with the business cycle, with exchange rates, with freight, with tariffs — and with a customer saying "can we hold off on this month." The number that looks healthy in the warehouse today can be dead stock on the books and a pile-up on the floor tomorrow.

Here's the thing. On the surface, inventory is arithmetic. Underneath, it's time.

Silver went up not long ago. In manufacturing that isn't news. It's a Tuesday.

When an order is quoted, silver is one number. When it ships, it's another. Across those three months, nobody books the difference. Finance has aging reports, purchasing has delivery schedules, production has attainment rates — but nobody can answer the question: how much silver am I actually exposed to across all my open orders, and how much margin do I lose if it goes up another ten percent?

What stings more is that you know the order doesn't make money, and you take it anyway. The customer wants the date, the line can't stop, the penalty clause is right there. So you eat the loss. And then you eat it again.

The reason it happens "again and again" is that it never became a decision. It stayed an understanding. Nobody signed anything, so nobody owns it. There's no limit, so there's always room to lose once more.

And it isn't that purchasing doesn't know how to buy. It's that prices now move faster than people can decide. Silver used to move ten percent in a year; now it moves fifteen in a week. The monthly review stops being a decision meeting and becomes a post-mortem.

Which is where I'll be blunt: AI cannot predict the silver price. Neither can anyone else. Pinning your plan on getting the forecast right means pinning your margin on a variable you don't control.

So the thing to work on isn't the price. It's time — and the only place you can still act is the short window between quoting and locking.

## Two Windows, and They Close

From quote to delivery, an order gives you exactly two moments where you can still do something. At the quote, you can still negotiate terms. At material prep, you can still lock a price or split the buy. Once it hits production, material becomes work in progress and the cost is fixed. By delivery, all that's left is booking it and reviewing it.

**Exposure is created at the quote and sealed at material prep. Everything after that is cleanup.**

So there are five things to do, in order.

**One: build a metal-content ledger.** Convert the BOM into grams. Convert orders into exposure. Without this ledger you don't even know what you're exposed to.

**Two: put a raw-material clause in the quote.** A base price plus an adjustment band, renegotiated beyond plus or minus five percent. This isn't pushing risk onto the customer; it's turning a one-sided bet into a two-sided one. The ones willing to sign are your real long-term customers.

**Three: lock the price instead of predicting it.** Negotiate fixed or tiered pricing upstream, or split purchases to average out. Convert uncertainty into a known cost, even if the cost is a little higher.

**Four: give loss-making orders a loss budget.** It isn't that you can't lose money. It's that you can't make a habit of it. Set a limit by month and by customer, with sign-off above the line.

**Five: generate the renegotiation packet automatically.** When the price falls past a threshold, produce the file: our volumes, the last base price, the current market price, the contract terms.

The fifth looks like the least of the five and is worth the most. On a falling price, what matters isn't whether you know — it's how fast. Whoever walks in with the data has the leverage. A week late, the supplier's own costs have already come down, but he won't volunteer that.

Of these five, only the first and the fifth need AI. The other three are policy.

## Where AI Actually Sits

So what does AI do? It doesn't forecast the price. What it does is re-run the books every morning: every part number, every open order, recomputed at today's price and exchange rate for theoretical margin — and any order that just went from black to red gets named that same day. Management shifts from a periodic report to an exception trigger.

Two things need saying plainly. AI gives you options and tripwires, not decisions; the last signature is still a person's, because inventory is cash that's been tied up. And it will only compute garbage faster — if the BOM is wrong, receipts arrive late, scrap never gets booked, then AI just helps you make the wrong call sooner and with more confidence.

## The Sixteen-Hour Day Doesn't Disappear

The older generation of founders worked sixteen-hour days. They weren't watching one company; they were watching a country, and the whole world. Those sixteen hours don't disappear — they get reallocated. Pulling data, reconciling, chasing, piecing things together goes back to the machine. What's left is the trade-off: whether to give that five percent when you're sitting across from the customer.

Purchasing isn't getting harder. It's getting more dependent on information speed. Supervision doesn't need to be stricter — it needs to be finer. Fine enough to reach every gram of silver, every open order, every price you haven't locked yet.

That's what this round of AI actually changes in production management. It doesn't decide for you. It makes sure you know while there's still time.
