# creating a set
names = {"Sia", "Mia", "Tia"}

# # print set
# print(names)
#
# # check length of set
# print(len(names))
#
# # check datatype of set
# print(type(names))
#
# # access items of set
# for x in names:
#     print(x)

# #check if item exists in set
# if "Sia" in names:
#     print("Sia is in the set")

# # add element in set
# names.add("ria")
# print(names)

# # add another sequence in set
# names_list = ["Ria", "Kia"]
# names.update(names_list)
# print(names)

# for removing element from set
names.remove("Tia")    # this function will throw error if value is not present in set
names.discard("Ria")    # this function will not throw error if value is not present in set
print(names)

# joining 2 sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}

# s3 = s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

# keep only duplicate while joining (put values in same variable)
# s1.intersection_update(s2)
# print(s1)

# keep all values except duplicates
# s1.symmetric_difference_update(s2)
# print(s1)


