directions = ["up", "down", "left", "right"]
curses = ["fuck", "suck", ]

choice_dir = ""

while choice_dir.casefold() not in directions:
    choice_dir = input("where you wanna go?")
    if choice_dir.casefold() in curses:
        print("you have lost the game")
        break

print("you went {}".format(choice_dir))