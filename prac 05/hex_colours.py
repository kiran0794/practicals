HEXA_COLOR_CODES = {"AliceBlue": "#f0f8ff","black": "#000000","brown": "#a52a2a",
               "CadetBlue": "#5f9ea0","coral": "#ff7f50","cyan1": "#00ffff",
               "DarkGreen": "#006400","DarkOrange": "#ff8c00",
               "DarkOrchid": "#9932cc","gold1": "#ffd700", }

color_name = input("Enter color name: ")
while color_name != "":
    if color_name in HEXA_COLOR_CODES:
        print(color_name, " hexa-color-code is", HEXA_COLOR_CODES[color_name])
    elif color_name == " ":
        break
    else:
        print("Invalid color name")
    color_name = input("Enter color name ")