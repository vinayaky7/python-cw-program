# string
name = "Isha"
print(type(name))

profession = "Student"
print(type(profession))

# interger
roll_number = 17
print(type(roll_number))

# floating number
percentage = 95.8
print(type(percentage))

# boolean
is_student = True
print(type(is_student))

print(name, roll_number, percentage, is_student)

percentage = 94

print(name, roll_number, percentage, is_student)

# concatination
# can only concatenate str (not "int") to str
print("My name is " + name + " My profession is " + profession)
print("My name is " + name + "My roll number is ", roll_number)

print("I scored ", percentage, "% in my final exams. I am a student is ", is_student)

# print expressions
print("My percentage has changed to ", percentage - 1.0)

# print with seperator
print(name, roll_number, percentage, is_student, sep="-")
x = 1
y = 2 
z = 3
print(x,y,z,sep="->")


