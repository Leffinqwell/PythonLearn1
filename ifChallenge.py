age = int(input("please enter your age: "))
name = str(input("please enter your name: "))

if 18 <= age < 31:
    print("Welcome and happy holiday, {0}".format(name))
else:
    print("Sorry," + name + ", sucks to be you, no entry for kids and old people")
