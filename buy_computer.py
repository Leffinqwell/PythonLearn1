current_choice = "-"

choosable_computer_parts = ["computer",
                            "monitor",
                            "keyboard",
                            "mouse",
                            "mouse mat"
                            ]

chosen_computer_parts = []

while current_choice != 665:
    i = 0
    if current_choice in range(0,len(choosable_computer_parts)):
        print("adding {}".format(current_choice + 1))
        chosen_computer_parts.append(choosable_computer_parts[current_choice])
        print(chosen_computer_parts)
        current_choice = int(input()) - 1
    else:
        print("add options from list below")
        for itter in choosable_computer_parts:
            i += 1
            print(f"{i}.\t" + itter)
        print("666.for exit")
        current_choice = int(input()) - 1

print("shopping over")

