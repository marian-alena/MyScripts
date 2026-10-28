import unicodedata

# 1. Broad keywords to search for within official Unicode names
FOOD_KEYWORDS = [
    "POTATO",
    "BURGER",
    "PIZZA",
    "TACO",
    "SUSHI",
    "DONUT",
    "APPLE",
    "BANANA",
    "COOKIE",
    "CHERRY",
]
FLAG_KEYWORDS = ["PIRATE FLAG", "CHECKERED FLAG", "TRIANGULAR FLAG", "CROSSSED FLAGS"]

# 2. Add full country flag lookups (Note: individual country flags like 🇺🇸 or 🇯🇵 are pairs of regional
# indicator symbols in Python, but distinct standalone flag emojis can be looked up directly)
KEYWORDS = FOOD_KEYWORDS + FLAG_KEYWORDS

print(f"{'Emoji':<6} | {'Python \\N{...} Syntax':<40} | {'Official Unicode Name'}")
print("-" * 85)

# 3. Loop through a large range of the emoji Unicode block (U+1F300 to U+1F9FF)
for codepoint in range(0x1F300, 0x1F9FF):
    char = chr(codepoint)
    try:
        name = unicodedata.name(char)
        if name == "SYRINGE":
            print(f"{char:<6} | \\N{{{name:<36}}} | {name}")
        # Check if the character name contains any of our food or flag keywords
        if any(keyword in name for keyword in KEYWORDS):
            # Print the emoji, the ready-to-copy code format, and the name
            print(f"{char:<6} | \\N{{{name:<36}}} | {name}")
        print(f"{char:<6} | \\N{{name:<36}} | {name}")
    except ValueError:
        # Codepoint has no assigned name, skip it
        continue
