# parrot = "Norwegian blue"
#
# for character in parrot:
#     print(character)
#**************************************
# for i in range (10, 0, -2):
#     print("i is now: {}".format(i))
#**************************************
for i in range (1,13):
    for j in range(1,13):
        print("{0} x {1} = {2}".format(j, i, j * i))
    print("-"*20)