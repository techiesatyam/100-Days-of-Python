import sys
import random
from pyfiglet import Figlet

def follow():
    text = input("Input: ")
    figure = Figlet(font = "banner")

    if len(sys.argv) == 1:
         figure.setFont(font=random.choice(figure.getFonts()))

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid user input!")
        try:
            figure.setFont(font=sys.argv[2])
        except:
            sys.exit("Invalid font")

    else:
        sys.exit("Invalid usage")
    print(figure.renderText(text))

follow()