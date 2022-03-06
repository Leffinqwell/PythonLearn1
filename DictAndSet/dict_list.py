choosable_computer_parts = {"1": "computer",
                            "2": "monitor",
                            "3": "keyboard",
                            "4": "mouse",
                            "5": "mouse mat",
                            "6": "hdmi Cable",
                            }

current_choice = None
chosen_computer_parts = []

while current_choice != "0":
    if current_choice in choosable_computer_parts:
        chosen_part = choosable_computer_parts[current_choice]
        if chosen_part in chosen_computer_parts:
            print("removing {}".format(current_choice))
            chosen_computer_parts.remove(chosen_part)
        else:
            print("adding {}".format(chosen_part))
            chosen_computer_parts.append(chosen_part)
        print(chosen_computer_parts)
    else:
        for key, value in choosable_computer_parts.items():
            print(key, value, sep=", ")




    current_choice = input("> ")

