input_string = input("Enter string: ")
n = int(input("Enter n: "))

#creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]   #-1 means right to left move, from end to start by 1-1 step back
dict1 = dict(zip(alphabets,reverse_alphabets)) #zip function used to create a dictionary from 2 differnet iterables like list 

#finding part of string on which we will do miror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding the mirror string
mirror =""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating final string
res = prefix + mirror
print("the result is :", res)
