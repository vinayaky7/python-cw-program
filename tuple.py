# create a tuple
colours = ("red","yellow","green")
print(colours)

# creating tuple with 1 item, always give quamma
#fruit = ("apple",)
fruit = tuple(("apple",))
print(fruit)


# check type of tuple
print(type(colours))
print(type(fruit))

# check length of tuple
print(len(colours))
print(len(fruit))

# accessing items in tuple
print(colours[1]) # positive indexing
print(colours[-1]) # negative indexing
print(colours[1:3]) # range indexing 3 is last item to print+1
print(colours[-2:]) # negative range indexing here we didnt mentioned ending point

# check if an item exist in tuple
if "green" in colours:
    print("Green is part of tuple")

# traverse the tuple
for i in colours:
    print(i)

# concatinate 2 tuple
more_colours= ("blue", "brown")
colours = colours + more_colours
print(colours)

#unpacking a tuple
colour1, colour2, colour3 = colours
print(colour1,colour2,colour3)

