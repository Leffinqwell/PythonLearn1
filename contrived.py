numbers = [1, 45, 31, 16, 60]


# for number in numbers:
#     if number %8 ==0:
#         print("the numbers are unccaptable")
#         break
# else:
#     print("the numbers are fine")

for i in range (1,11):
    if i == 10:
        print("Outrageous!")
        break
    elif i % 2 == 0:
        print("fine")
    else:
        print("not fine")

else:
    print("done")