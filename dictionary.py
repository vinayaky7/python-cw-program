# creating dictionary
phones = {
    "John": 982628,
    "Ria": 468201,
    "Joy": 126830
}

# # printing the dict
# print(phones)
#
# # checking types of dict
# print(type(phones))
#
# #check length of dict
# print(len(phones))
#
# #access items of dict
# print(phones["John"])
# print(phones.get("John"))

# print(phones.keys())

# #update value in dict
# phones["John"] = 777777
# print(phones)
#
# #add elements in dict
# phones["Kia"] = 26589
# print(phones)

# more_phones = {
#     "Kia" : 256483
# }
# phones.update(more_phones)
# print(phones)
#
# # remove element in dict
# phones.pop("John")
# print(phones)
#
#
# phones.popitem()    #this will remove last added element
# print(phones)
#
#
# phones.clear()  # this will empty the dict
# print(phones)

# #printing values of dict
# for x in phones:
#     print(phones[x])

#printing elements of dict
for x,y in phones.items():
    print(x,y)

#nested dict
phones = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2" : {
        "a" : 3,
        "b" : 4,
        "c" : 5
    }
}


print(phones["Area2"]["c"])

print(phones["Area1"]["y"])



