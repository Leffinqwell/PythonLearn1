shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("buy " + item)
#
# for item in shopping_list:
#     if item == "spam":
#         break
#
#     print("buy " + item)
#
# print("shoes")

itemToFind = "spam"
foundAt = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == itemToFind:
#         foundAt = index
#         break

if itemToFind in shopping_list:
    foundAt = shopping_list.index(itemToFind)

if foundAt is not None:
    print("item's posistion in list is {}".format(foundAt))
else:
    print("{} is not in the list".format(itemToFind))