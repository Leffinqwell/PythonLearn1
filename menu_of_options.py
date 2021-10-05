options = ["spam", "eggs", "buns", "ham", "mustard"]
choice = "-"

while choice != 0:
    i = 0
    if choice in range(1,6):
        choice = int(input("what do you choose?"))
        print("You choose {}!".format(choice))
    else:
        for itter in options:

            i += 1
            print(f"{i}.\t" + itter)
        else:
            print(f"{0}.\tExit")
            choice = 1
else:
    print("game over")