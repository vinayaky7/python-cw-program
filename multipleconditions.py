eng_marks = int(input("Enter marks in english: "))
math_marks = int(input("Enter marks in math: "))

#if both are more than 80 then print A grade
if eng_marks > 80 and math_marks > 80:
    print("A grade")
#if either of marks are more than 80 than print B grade
elif eng_marks > 80 or math_marks > 80:
    print("B grade")
# if neither of marks more than 80
else:
    print("C grade")
