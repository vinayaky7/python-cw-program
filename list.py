# check python collections file for theory
#
fruits = ["apple","mango","cherry","banana"]    # create a list
print(fruits)   # print a list
print(type(fruits))     # check type of list
print(len(fruits))  # check length of list

# # checking if an item present in list
# if "banana" in fruits:
#     print("banana is part of list")
# if "kiwi" not in fruits:
#     print("kiwi is not part of list")
#


# #indexing in list
# print(fruits[1])    # mango
# print(fruits[-3])   # mango
#
# print(fruits[1:3])  #[mango, cherry]
# print(fruits[-3,-1]) #[mango, cherry] for counting from -, 1 not consider 1st count.


# adding elements to list
# fruits.append("kiwi")
# print(fruits)

# fruits.insert(2, "kiwi")
# print(fruits)

# more_fruits= ["kiwi","papaya"]
# fruits.extend(more_fruits)
# print(fruits)

# # removing element from list
# fruits.remove("banana")
# print(fruits)
#
# fruits.pop()    # remove item at last
# print(fruits)
#
# fruits.pop(1)   # remove item at index 1
# print(fruits)



# #changing items in list
# fruits[1] = "kiwi"
# print(fruits)
#
# fruits[1:3]= ["papaya"]
# print(fruits)


# sorting a list
# fruits.sort()   # by default ascending way sort
# print(fruits)

# fruits.sort(reverse=True) # descending order sort
# print(fruits)

# fruits.reverse()   #reverse the order of list
# print(fruits)

# #   list comprehension
# new_fruits= [fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)


# # copy a list
# new_fruits = fruits.copy()
# print(new_fruits)
#
# # to concatinate two lists
# new_fruits = fruits + new_fruits
# print(new_fruits)


# nested list
fruits.insert(2,["kiwi", "papaya"])
print(fruits)
print(fruits[2][0])



