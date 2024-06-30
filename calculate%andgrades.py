"""
81-100  Very good
61-80   Good
41-60   Average
<=40    Fail

"""

# percenatge_obtained = int(input("Enter the percentage: "))
#
# if percenatge_obtained >= 81:
#     print("The grade obtained is Very Good:")
# elif percenatge_obtained >= 61:
#     print("The Grade obtained is Good:")
# elif percenatge_obtained >= 41:
#     print("The Grade obtained is Average:")
# else:
#     print("The Grade obtained is failed:")
#

physics = int(input("Enter the physics marks out of 100: "))
chemistry = int(input("Enter the chemistry marks out of 100: "))
biology = int(input("Enter the biology marks out of 100: "))
english = int(input("Enter the english marks out of 100: "))
history = int(input("Enter the history marks out of 100: "))
computer_science = int(input("Enter the history marks out of 100: "))
botany = int(input("Enter the botany marks out of 100: "))

Total = physics + chemistry + biology + english + history + computer_science + botany
print("The total marks are: ", Total)

Average = (physics + chemistry + biology + english + history + computer_science + botany)/ 7
print("The Average marks are: ", Average)

percentage = Total / 700 * 100
print("The percentage is: ", percentage)

if percentage >= 81:
    print("The grade obtained is Very Good:")
elif percentage >= 61:
    print("The Grade obtained is Good:")
elif percentage >= 41:
    print("The Grade obtained is Average:")
else:
    print("The Grade obtained is failed:")



