import unicodedata

# Map of country ISO codes to printable names
countries = {"US": "USA", "GB": "UK", "JP": "Japan", "FR": "France", "CA": "Canada"}

for code, country_name in countries.items():
    # Convert letters to their corresponding regional indicator symbols
    name1 = unicodedata.name(
        code[0].upper().replace(code[0], chr(ord(code[0]) + 127397))
    )
    name2 = unicodedata.name(
        code[1].upper().replace(code[1], chr(ord(code[1]) + 127397))
    )

    # Construct the flag string
    flag_emoji = f"\\N{{{name1}}}\\N{{{name2}}}"
    actual_flag = (
        code.upper().encode("ascii").decode("unicode_escape")
    )  # standard resolution

    print(f"{country_name:<8}: {flag_emoji}")


# Let's check how flag names and food names are formatted in unicodedata
# Often flags are "REGIONAL INDICATOR SYMBOL LETTER X" or named like "FLAG FOR UNITED STATES"
# Food items usually have clear names. Let's see some samples.
try:
    print(unicodedata.name("🍕"))
    print(unicodedata.name("🇺🇸"))
except Exception as e:
    print(e)
