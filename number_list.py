empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for number in number_list:
        print(number)


# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
#
# digits = sorted("432985617")
# digits_list = list("432985617")
# print(digits)
# print(digits_list)
#
# #more_numbers = list(numbers)
# #more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
#
# print(numbers is more_numbers)
# print(numbers == more_numbers)

# even.extend(odd)
# print(even)
#
#
# even.sort(reverse=True)
# print(even)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print(len(even))
# print(len(odd))
#
# print("mississippi".count("issi"))