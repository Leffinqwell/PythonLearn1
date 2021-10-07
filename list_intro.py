computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

another_list = computer_parts
a = b = c = computer_parts
computer_parts += ["repro"]
b.append("mic")

print(computer_parts)
print(a)



# result = True
# another_result = result
#
# print(id(result))
# print(id(another_result))
