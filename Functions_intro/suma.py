def sum_numbers(*numbers: int) -> int:
    """
    calculates sum of numbers
    :param numbers:
    :return:
    """
    result = 0
    for x in numbers:
        result = result + x
    return result


print(sum_numbers(999907, 744753, 655931, 243533, 361310, 852087, 686306, 880531))