# Day 1: Variables and Data Types
# AI Architect Journey - Phase 0

# My Profile
name = "Aryan KC"
country = "Nepal"
goal = "AI Architect"
current_phase  = "Phase 0 : Foundations"

# My Commitment
hours_per_day = 2.5
days_total = 14*30  # 14 months
total_hours = hours_per_day*days_total

# data types demo
age = 23
is_true =True
skills = ["Python","Math","ML","System Design"]
profile = {
    "name":name,
    "goal" : goal,
    "country":country,
    "hours_per_day":hours_per_day
}

# Print Statements
print("="*50)
print("AI Architect Journey - Day 1")
print("="*50)
print(f"Name: {name}")
print(f"Country: {country}")
print(f"Goal: {goal}")
print(f"Current Phase: {current_phase}")
print()
print(f"Commitment: {hours_per_day} hours/day")
print(f"Total time commitment: {total_hours} hours over 14 months")
print()
print(f"Skills to learn: {skills}")
print()
print("Profile:")
for key, value in profile.items():
    print(f"  {key}: {value}")
print()
print("Ready to build? ", is_true)
print("=" * 50)


