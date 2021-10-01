import random

highest = 10
answer = random.randint(1, highest)
print(answer)

guess = int
print("Please guess a numebr between 1-{}".format(highest))

while answer != guess:

    guess = int(input())
    if guess == 0 or guess > 10:
        print("You can't read, game over")
        break
    elif guess < answer:
        print("wrong, guess higher")
    elif guess > answer:
        print("wrong, guess lower")
    else:
        print("correct")



