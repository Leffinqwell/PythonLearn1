menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


for meal in menu:
#    print(meal)
    length = len(meal)-1
    for index, value in enumerate(reversed(meal)):
        if meal[length - index] == "spam":
#            print(length - index, value)
            del(meal[length - index])
    print(", ".join(meal))
#    print(meal, end=" ")
#print(menu)