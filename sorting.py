pangram = "The quick brown fox jumps over he lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

print(sorted(numbers))
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The Real stuff goes around",
                        key=str.casefold)
print(missing_letter)

names = ["Graham", "John", "terry", "eric", "Terry", "micheal"]
names.sort(key=str.casefold)
print(names)