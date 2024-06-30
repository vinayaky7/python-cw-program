# reverse a tuple
# reversed(): used to iterate through a sequence in reversed order
# put tuple elements in list in reverse order
# then use typecast from list to tuple

input_tuple = (1, 2, 3, 4, 5, 6)

list = []

# add reversed values in a list
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)   # type cast into tuple
print(output_tuple)


