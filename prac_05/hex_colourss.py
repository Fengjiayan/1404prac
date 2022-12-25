COLOR_NAMES = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
               "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
               "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}

color_name = input("Enter color name: ").upper()
while color_name != "":
    try:
        print(color_name, "is", COLOR_NAMES[color_name])
    except Exception:
        print("Invalid color name.")
    state_code = input("Enter color name: ").upper()
