# 🔥 Should I Pursue This? — AI-Powered Deal Scorer

A simple command-line tool that helps sales and consulting professionals quickly decide whether a lead is worth their time — built with Python.

---

## What It Does

Every salesperson knows the feeling: you have a list of leads and not enough hours in the day. This tool asks you 5 fast questions about a prospect, scores them based on key signals (urgency, budget, company size, and access), and gives you a straight verdict:

- 🔥 **Strong Pursue** — drop everything and call them
- ⚡ **Worth Exploring** — dig a little deeper first
- 🤔 **Proceed with Caution** — don't over-invest yet
- ❌ **Skip for Now** — park it and move on

No spreadsheets. No gut second-guessing. Just a score and a recommendation in under 30 seconds.

---

## How to Run It

You don't need to install anything fancy. Here's how to get it running in two ways:

### Option 1: Run it in your browser (easiest)
1. Go to [replit.com](https://replit.com) and create a free account
2. Click **"Create Repl"** and choose **Python**
3. Copy and paste the code from `deal_scorer.py` into the editor
4. Click the green **Run** button
5. Answer the 5 questions and get your verdict

### Option 2: Run it on your computer
1. Make sure Python is installed — download it at [python.org](https://python.org) if not
2. Download this project by clicking the green **Code** button above, then **Download ZIP**
3. Unzip the folder and open your terminal (search "Terminal" on Mac or "Command Prompt" on Windows)
4. Navigate to the folder by typing: `cd path/to/folder`
5. Run the tool by typing: `python deal_scorer.py`

---

## Example Output

```
=== Should I Pursue This Deal? ===

1. What industry are they in? tech
2. How big is the company? large
3. Do they have an urgent need? yes
4. Any budget signals? confirmed
5. Do you have a direct contact? yes

===========================
LEAD: TECH company
SCORE: 11 / 11

VERDICT: 🔥 Strong Pursue — prioritize this one.
ADVICE: High potential. Move fast and personalize your outreach.
===========================
```

---

## What I Learned Building This

I built this project as my first real coding experience — no CS degree, no bootcamp, just curiosity and a real problem I wanted to solve.

Here's what clicked for me:

**Variables are just labeled boxes.** When I type `urgency = input("Do they have an urgent need?")`, the program saves my answer in a box called `urgency` so it can use it later. That's it. Not scary at all.

**If/elif/else is how programs make decisions.** It's the same logic as "if it's raining, take an umbrella — otherwise, don't." I used this to assign points based on each answer, and it made complete sense once I saw it that way.

**Scoring systems are just addition.** The whole "AI" behind this tool is honestly just math — adding up points based on what you type. That realization made me feel like I could build a lot more than I thought.

**Programs talk to users with `print()` and `input()`.** These two commands handle almost all of the interaction in this tool. `print()` shows something on screen. `input()` waits for you to type something back. Once I understood that, reading the code got a lot easier.

**Starting small is the right move.** I didn't build a web app or a database on day one. I built something that runs in a terminal, solves a real problem I have, and that I can actually explain. That felt like a real win.

---

## What's Next

Here are some features I'm planning to add:

- [ ] Save results to a CSV file so I can track leads over time
- [ ] Score multiple leads in one session without restarting
- [ ] Build a web version so I can share it with teammates
- [ ] Add a notes field so I can log context about each lead

---

## Built With

- **Python 3** — the only tool used. No external libraries required.

---

## About

Built by a sales and consulting professional learning to code — proving that you don't need a technical background to build tools that solve real problems.
# deal-scorer
A simple command line tool that helps sales and consulting professionals quickly decide whether a lead is worth their time - built with Python.
