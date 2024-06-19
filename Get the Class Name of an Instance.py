##############Using type()#################
class MyClass:
    pass

# Create an instance of MyClass
obj = MyClass()

# Get the class name using type() and __name__
class_name = type(obj).__name__

print(f"Class name of obj: {class_name}")


# #########Using __class__ Attribute####################################
# class MyClass:
#     pass
#
# # Create an instance of MyClass
# obj = MyClass()
#
# # Get the class name using __class__ and __name__
# class_name = obj.__class__.__name__
#
# print(f"Class name of obj: {class_name}")
