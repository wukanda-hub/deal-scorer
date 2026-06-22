print("=== Should I Pursue This Deal? ===\n")

industry = input("1. What industry are they in? (e.g. tech, healthcare, retail): ")
size = input("2. How big is the company? (small / medium / large): ")
urgency = input("3. Do they have an urgent need? (yes / maybe / no): ")
budget = input("4. Any budget signals? (confirmed / likely / unknown): ")
access = input("5. Do you have a direct contact? (yes / no): ")

score = 0

if size.lower() == "large":
    score += 3
elif size.lower() == "medium":
    score += 2
else:
    score += 1

if urgency.lower() == "yes":
    score += 3
elif urgency.lower() == "maybe":
    score += 2
else:
    score += 0

if budget.lower() == "confirmed":
    score += 3
elif budget.lower() == "likely":
    score += 2
else:
    score += 1

if access.lower() == "yes":
    score += 2
else:
    score += 0

max_score = 11

if score >= 9:
    verdict = "🔥 Strong Pursue — prioritize this one."
    advice = "High potential. Move fast and personalize your outreach."
elif score >= 6:
    verdict = "⚡ Worth Exploring — but qualify further."
    advice = "Solid signals, but clarify budget and urgency before investing heavy time."
elif score >= 3:
    verdict = "🤔 Proceed with Caution — low priority."
    advice = "Thin signals. A quick touch is fine, but don't over-invest yet."
else:
    verdict = "❌ Skip for Now — not worth your time."
    advice = "Too many unknowns. Park this and revisit later."

print("\n===========================")
print(f"LEAD: {industry.upper()} company")
print(f"SCORE: {score} / {max_score}")
print(f"\nVERDICT: {verdict}")
print(f"ADVICE: {advice}")
print("===========================\n")
