import unicodedata

x = [
    "Emojis & Smileys",
    "Grinning Face: \N{GRINNING FACE} ➔ 😀",
    "Thumbs Up: \N{THUMBS UP SIGN} ➔ 👍",
    "Sparkles: \N{SPARKLES} ➔ ✨",
    "Rocket: \N{ROCKET} ➔ 🚀",
    "Fire: \N{FIRE} ➔ 🔥",
    "Snake: \N{SNAKE} ➔ 🐍",
    "Currency Symbols",
    "Euro: \N{EURO SIGN} ➔ €",
    "Pound: \N{POUND SIGN} ➔ £",
    "Yen / Yuan: \N{YEN SIGN} ➔ ¥",
    "Cent: \N{CENT SIGN} ➔ ¢",
    "Rupee: \N{INDIAN RUPEE SIGN} ➔ ₹",
    "Math & Logic",
    "Infinity: \N{INFINITY} ➔ ∞",
    "Square Root: \N{SQUARE ROOT} ➔ √",
    "Partial Differential: \N{PARTIAL DIFFERENTIAL} ➔ ∂",
    "Summation: \N{N-ARY SUMMATION} ➔ ∑",
    "Not Equal: \N{NOT EQUAL TO} ➔ ≠",
    "Plus-Minus: \N{PLUS-MINUS SIGN} ➔ ±",
    "Typography & Symbols",
    "Bullet: \N{BULLET} ➔ •",
    "Trademark: \N{TRADE MARK SIGN} ➔ ™",
    "Registered: \N{REGISTERED SIGN} ➔ ®",
    "Copyright: \N{COPYRIGHT SIGN} ➔ ©",
    "Section: \N{SECTION SIGN} ➔ §",
    "Degree: \N{DEGREE SIGN} ➔ °",
    "Weather & Sky",
    "Snowman: \N{SNOWMAN} ➔ ☃",
    "Sun: \N{BLACK SUN WITH RAYS} ➔ ☀️",
    "Cloud: \N{CLOUD} ➔ ☁️",
    "Umbrella: \N{UMBRELLA} ➔ ☂",
    "Rain: \N{UMBRELLA WITH RAIN DROPS} ➔ ☔",
    "Thunderstorm: \N{THUNDERSTORM} ➔ ☈",
    "100 points: \N{HUNDRED POINTS SYMBOL} ➔ 💯",
    "pizza slice: \N{SLICE OF PIZZA} ➔ 🍕",
]
for item in x:
    print(item)

# Get the name of a character
print(unicodedata.name("A"))  # Output: LATIN CAPITAL LETTER A
print(unicodedata.name("🍕"))  # Output: SLICE OF PIZZA
print(unicodedata.name("⛈"))  # Output: THUNDER CLOUD AND RAIN

# Look up a character by its official Unicode name
print(unicodedata.lookup("EURO SIGN"))  # Output: €
