import random

def get_integer(prompt):
    """
     ´ss´
    :param prompt:
    :return:
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("wut?")


highest = 10
answer = random.randint(1, highest)

print("Please guess a numebr between 1-{}".format(highest))
guess = get_integer(" : ")

if guess == answer:
    print("well done")
elif guess < answer:
    print("guess higher")
    guess = get_integer(" : ")
    if guess == answer:
        print("well done, on second time")
    else:
        print("too bad, loser")
else:
    print("guess lower")
    guess = get_integer(" : ")
    if guess == answer:
        print("well done, on second time")
    else:
        print("too bad, loser")

print(answer) #TODO: remove this line

# if guess != answer:
#     if guess < answer:
#         print("please guess higher")
#     else:
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, correct")
#     else:
#         print("wrong, too bad")




# if guess < answer:
#     print("please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("got it for second try, you added right")
#     elif guess < answer:
#         print("wrong, not enough")
#     else:
#         print("Wrong, too much")
# elif guess > answer:
#     print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("got it for second try, took away just right")
#     elif guess < answer:
#         print("wrong, took away too much")
#     else:
#         print("wrong, didn't take away enough")
# else:
#     print("you got it for first try")


# x=15
# y=15
# if x>y:
#     print("x is greater than y")
# elif x<y:
#     print("x is smaller than y")
# else:
#     print("x equals y")