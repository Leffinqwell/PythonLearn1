def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()
    # return string[::-1] == string


def palindrome_sentence(string):
    string1 = ""
    for char in string:
        if char.isalnum():
            string1 = string1 + char
    print(string1)
#    return string1.casefold()[::-1] == string1.casefold()
    return is_palindrome(string1)

word = input("enter your word: ")
if palindrome_sentence(word):
     print("'{}' is a palindrome".format(word))
else:
     print("'{}' is not a palindrome".format(word))


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