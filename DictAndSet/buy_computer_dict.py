choosable_computer_parts = {"1": "computer",
                            "2": "monitor",
                            "3": "keyboard",
                            "4": "mouse",
                            "5": "mouse mat",
                            "6": "hdmi Cable",
                            }

current_choice = None

while current_choice != "0":
    if current_choice in choosable_computer_parts:
        chosen_part = choosable_computer_parts[current_choice]
        print(f"adding {chosen_part}")
    else:
        for key, value in choosable_computer_parts.items():
            print(key, value, sep=", ")

    current_choice = input("> ")

