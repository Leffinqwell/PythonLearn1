current_choice = "-"

choosable_computer_parts = ["computer",
                            "monitor",
                            "keyboard",
                            "mouse",
                            "mouse mat",
                            "hdmi Cable"
                            ]
valid_choices = []
for i in range(1, len(choosable_computer_parts) + 1):
    valid_choices.append(str(i))


chosen_computer_parts = []

while current_choice != 665:
    i = 0
    if current_choice in range(0, len(choosable_computer_parts) + 1):
        ind = int(current_choice) - 1
        x = choosable_computer_parts[ind]
        if x in chosen_computer_parts:
            print("removing {}".format(current_choice))
            chosen_computer_parts.remove(choosable_computer_parts[ind])
        else:
            print("adding {}".format(current_choice))
            chosen_computer_parts.append(choosable_computer_parts[ind])
        print(chosen_computer_parts)
    else:
        print("add options from list below")
        #        for itter in choosable_computer_parts:
        for index_positon, object_in_list in enumerate(choosable_computer_parts):
            i += 1
            #            print(f"{i}.\t" + itter)
            #            print("{0}. {1}".format(choosable_computer_parts.index(itter) + 1, itter))
            print("{0}. {1}". format(index_positon + 1, object_in_list))
        print("0. for exit")
    current_choice = int(input())

print("shopping over")
print(chosen_computer_parts)
