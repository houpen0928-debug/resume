---
layout: "journal"
title: "The Wishing Well Was Always There — the Bill Just Arrived Late"
date: "2026-11-08"
lang: "en"
locale: "en"
author_profile: true
resume_style: true
description: "A MES support engineer once told me: don't treat your system vendor like a wishing well. Half of that was true. But what AI agents actually change is not whether software can be built — it's when the price shows up."
---

> Published as a professional article on 2026-11-08. Also available in [Traditional Chinese]({{ '/blog/2026-11-08-wishing-well-bill-arrived-late/' | relative_url }}).

![Illustration: on the left, a hand drops a coin into a stone wishing well, its bottom glittering with sunken coins; a ribbon of coins rises from the rim, arcs across the frame and funnels into the coin slot of a vending machine on the right, where a packaged item is sliding out of the delivery slot — the same wish, unpriced on one side, price-tagged on the other]({{ '/images/journal/wishing-well-vending-machine-2026-11-08.jpg' | relative_url }})

Over a decade in factories, I've watched a lot of systems go live. The words that sting most were never "that can't be done." They were these:

> "Sir, we gave you a system — the same one everyone else gets. Why does your site have so many issues? Change this, change that — how many engineers do you expect us to assign? We're losing money on your account. Don't treat your system vendor like a wishing well."

My first reaction was anger: I'm describing real production problems, and as my supplier you're scolding me for making wishes?

Later I ran systems myself, and spent time on the vendor side of the table. Gradually I admitted it: half of that sentence was true — genuinely true.

## First, Let Me Make Their Case for Them

To most clients, a "change" is just a sentence.

Inside the vendor, that sentence has to travel a full assembly line:

Clarify the requirement → Impact analysis → Solution design → Development → Unit testing → Regression testing → Documentation update → Version control → Post-release support.

The killer isn't development. It's regression.

Because an MES isn't built for you alone. Your warehouse, your process routes, your production reporting rules run on the same codebase as everyone else's. One sentence from you can touch logic another customer has had running stably for two years.

So the real cost of "just change one thing" was never those few dozen lines of code — it's where the regression boundary sits. And the fuzzier that boundary, the less anyone dares to quote.

And when nobody dares to quote? You say yes first, lose money later, and end the call with "don't treat your system vendor like a wishing well."

That sentence isn't arrogance. It's a cost sheet nobody wanted to show you.

## What a Wishing Well Really Is

I eventually worked one thing out.

**A wishing well is called a wishing well not because it's free, but because you don't pay at the moment you make the wish.**

One coin in, and the wish can be as large as you like. That is the real root of runaway customization — not too many demands, but demands whose price is invisible at the moment they are raised.

Which pushes client and vendor into a bet built on asymmetric information:

- The client doesn't know what one change actually costs, so they ask — freely, willingly, necessarily.
- The vendor doesn't dare to quote: high and the deal dies, low and they eat the loss. So they stay vague.
- And once vague enough, it turns into "don't treat your system vendor like a wishing well."

This isn't a question of anyone's character. It's a missing pricing mechanism.

Custom software carries another, colder truth: it has almost no economies of scale. In manufacturing, the millionth unit costs far less than the first. In custom software, the hundredth customer's hundredth change costs exactly what the first one did.

So a vendor has two paths: lock down a standard product and ignore you, or take project work and slowly go broke.

"We're losing money" isn't an emotion. It's a financial statement.

## What AI Actually Changes Isn't Whether It Can Be Built

Here is the point I want to make.

Now that AI agents have matured, many people assume what changed is how fast software can be built. Wrong.

**What changed is when the price appears.**

The old loop:

> You raise a request → wait a week for an assessment → receive a quote → push back on price → reassess → a month has passed → the requirement has changed → start over.

The loop today:

> You raise a request → the agent reads your system configuration, your codebase, your ticket history and change log → and tells you **on the spot**: this touches three modules, roughly 2.5 person-days, affects logic two other customers depend on, requires 12 regression checks, medium risk, this much cost, earliest delivery date.

So where is the difference?

**Not in time. In this: at the moment you make the wish, you can see the price.**

That is the real distinction between a wishing well and a vending machine —

**not whether there are wishes, but whether the wishes carry a price.**

## What Happens When Wishes Carry a Price

**For the client — the role I usually play — three things change.**

First, making requests becomes "expensive." Not because you are charged, but because you can finally see the price. You used to ask freely because it looked free.

Second, "just change one thing" becomes "is this one thing worth it?" That is a normal commercial conversation — not that it cannot be done, but let us look together at what this change actually buys.

Third, for the first time you see the strata of wishes:

- **Cheap** wishes: add a field, adjust a report, change a display, add a validation.
- **Middling** wishes: integrate an interface, add an approval step, build a dashboard.
- **Absurdly expensive** wishes: process re-engineering, cross-system integration, data governance.

And the most expensive wish is usually not on the requirements list at all. Its name is: **"from now on, everyone works this new way."**

Code was never the expensive part. Getting people to work differently is where the real bill lands.

**For the vendor, one thing changes too.**

You can no longer hide behind "we're losing money." When cost can be calculated, it should be calculated in front of the customer.

The confidence to say no should not come from a complaint. It should come from a cost sheet that adds up.

## A Bucket of Cold Water: What AI Won't Fix

I don't want to make this sound prettier than it is. Cheaper wishes do not mean easy wishes. Four things AI will not fix:

**Accountability.** When a system causes a production incident, who signs? An algorithm does not sign.

**Data.** The dirty records in your MES, the part numbers that don't reconcile, the process routes nobody maintains — AI won't rescue those. It will just amplify the errors faster.

**Integration.** Legacy PLCs, undocumented equipment, an interface written ten years ago by an engineer who has since left. That is human work.

**Organization.** I have seen too many failed system rollouts. Eight in ten were not software problems — nobody wanted to work the new process.

So my conclusion is not "AI makes wishes free."

**AI makes wishes priced. Those are two very different things.**

## Closing

That engineer was right to push back. In a world with only people, "don't treat your system vendor like a wishing well" was the only rational advice.

But that conclusion is going out of date.

The wishing well does not disappear. It becomes a vending machine — **price marked, coin in, product out.**

So for those of us in this generation of factory people, what has to change is not the wishes. It is the habit:

**Wish away. Just be ready to read the bill.**

A mature partnership was never about the client asking for nothing while the vendor claims no losses.

It is this: **every wish, with its price visible to both sides.**

---

*This piece is drawn from my own experience. I have carried that engineer's words for years. Today I am handing half of them back.*
