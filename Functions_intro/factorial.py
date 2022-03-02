def factorial(number: int) -> int:
    """
    makes factorial function
    :param number: calculated factorial
    :return:
    """
    if number == 0:
        number = 1
    fact = number
    for i in range(1, number):
        init = i
        fact = fact * init
    return fact


for i in range(0, 10):
    print(i, factorial(i))

