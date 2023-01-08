"""
Hexadecimal colour lookup

Based on the state name example program above,
create a program that allows you to look up hexadecimal colour codes like those at
http://www.color-hex.com/color-names.html

Use a constant dictionary of about 10 colour names and write a program that
allows a user to enter a name and get the code, e.g.,
entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.

"""
COLOR_HEX = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "Zomp": "#39a78e",
    "Zaffre": "#0014a8",
    "YellowGreen": "#9acd32",
    "Yellow Pantone": "#fedf00",
    "Xanadu": "#738678",
    "Wisteria": "#c9a0dc",
    "Wine": "#722f37",
    "White": "#ffffff"
}

def main():
    """
    The program takes input from the user and returns the corresponding hexadecimal color code.
    """
    color_name = input("Color name: ").strip()
    while color_name != "":
        # TODO

main()
