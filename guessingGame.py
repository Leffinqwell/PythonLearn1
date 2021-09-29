answer = 5

print("Please guess a numebr between 1-10")
guess = int(input())
if guess < answer:
    print("please guess higher")
    guess = int(input())
    if guess == answer:
        print("got it for second try, you added right")
    elif guess < answer:
        print("wrong, not enough")
    else:
        print("Wrong, too much")
elif guess > answer:
    print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("got it for second try, took away just right")
    elif guess < answer:
        print("wrong, took away too much")
    else:
        print("wrong, didn't take away enough")
else:
    print("you got it for first try")


# x=15
# y=15
# if x>y:
#     print("x is greater than y")
# elif x<y:
#     print("x is smaller than y")
# else:
#     print("x equals y")