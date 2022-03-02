def fizz_buzz(number) -> str:
    """
    plays a game fizz buzz, substitudes divisible numbers by 3 and 5 with fizz and buzz
    :param top: highest number in the game
    :return:
    """
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 ==0:
        return "buzz"
    else:
        int_to_str = str(number)
        return int_to_str

def test_for_fizz_buzz(answer) -> str:
    if fizz_buzz(i) == answer:
        print("gut")
    else:
        print("wrong, you lost")
        quit()

for i in range(1, 101):
    if i % 2 != 0:
        print(fizz_buzz(i))
    else:
        answer = input("Player's turn: ")
        test_for_fizz_buzz(answer)
