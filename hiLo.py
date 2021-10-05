low = 1
high = 1000

print("please think number between {}-{}".format(low, high))
input("press enter to start")

guesses = 1
while low != high:
    print("guessing in {} to {}". format(low, high))
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. Should i guess higher or lower?"
                     "H for higher, L for lower, C for correct"
                     .format(guess).casefold())
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("enter h, l or c")

   #guesses = guesses + 1
    guesses += 1

else:
    print ("your number was no.{}".format(low))
    print ("I got it in {}".format(guesses))
