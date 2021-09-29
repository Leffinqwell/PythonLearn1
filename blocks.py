# for i in range(1, 13):
#    print("No. {} squared {} and cubed is{:4}". format(i, i**2, i**3))
# print("*" * 80)

name = input("Please enter your name:")
age = int(input("how old are you, {0}?".format(name)))
print(age)

if age < 18:
    print("please come back in {} years".format(18-age))
elif age == 900:
    print("You're Yoda")
else:
    print("You're old enough to vote")
