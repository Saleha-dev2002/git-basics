# Secret Text Cleaner & Formatter

text = "Agentic-AI-Secret"

for char in text:
    # Rule 1: Agar dash '-' aaye toh skip kar do
    if char == "-":
        continue

    # Rule 2: Agar 'S' aaye toh loop wahin rok do
    if char == "S":
        break

    # Rule 3: Baqi har character ko upper case karke '*' ke sath print karo
    print(char.upper() + "*")


