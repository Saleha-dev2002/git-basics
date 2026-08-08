# Iterating through Lists

# 1. Direct Iteration
print("--- Direct Iteration ---")
tech_stack = ["Python", "Git", "Docker", "Agentic-AI"]

for tech in tech_stack:
    if tech == "Docker":
        continue  # Skip Docker
    print(f"Learning: {tech}")

# 2. Enumerate Iteration (With Index)
print("\n--- Enumerate Iteration ---")
milestones = ["Setup Environment", "Learn Strings", "Learn Loops", "Build Projects"]

for index, step in enumerate(milestones, start=1):
    print(f"Step {index}: {step}")
    