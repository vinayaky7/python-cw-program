class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

def main():
    # Creating instances of different classes
    animal = Animal("Generic Animal")
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    # Using type() to get the exact class of an object
    print(f"Type of animal: {type(animal)}")  # Output: <class '__main__.Animal'>
    print(f"Type of dog: {type(dog)}")        # Output: <class '__main__.Dog'>
    print(f"Type of cat: {type(cat)}")        # Output: <class '__main__.Cat'>

    # Using isinstance() to check inheritance
    print(f"Is dog an Animal? {isinstance(dog, Animal)}")  # Output: True
    print(f"Is cat an Animal? {isinstance(cat, Animal)}")  # Output: True
    print(f"Is animal a Dog? {isinstance(animal, Dog)}")    # Output: False

if __name__ == "__main__":
    main()
