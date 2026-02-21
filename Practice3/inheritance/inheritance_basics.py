# inheritance_basics.py

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()