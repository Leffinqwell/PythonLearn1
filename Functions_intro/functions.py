def multiply(x: float, y: float) -> float:
    """
    multiplies x by y
    :param x:
    :param y:
    :return:
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    single word validation for palindromity
    :param string:
    :return:
    """
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()
    # return string[::-1] == string


def palindrome_sentence(string: str) -> bool:
    """
    Whole sentence validation for palindromity
    :param string:
    :return:
    """
    string1 = ""
    for char in string:
        if char.isalnum():
            string1 = string1 + char
    print(string1)
#    return string1.casefold()[::-1] == string1.casefold()
    return is_palindrome(string1)


def fibonacci(n: int) -> int:
    """
    return the 'n'th number of fibonacci number, for positive 'n'
    :param n:
    :return:
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(-10):
    print(i, fibonacci(i))


# word = input("enter your word: ")
# if palindrome_sentence(word):
#      print("'{}' is a palindrome".format(word))
# else:
#      print("'{}' is not a palindrome".format(word))


# word = input("enter your word: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


# answer = multiply(10.5, 4)
# print(answer)
#
# for z in range(1,5):
# #    print (multiply(z, 2))
#     a = multiply(z, 2)
#     print(a)