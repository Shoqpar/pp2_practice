# class_variables.py

class Car:
    wheels = 4  # переменная класса

    def __init__(self, brand):
        self.brand = brand  # переменная объекта

car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.wheels)
print(car2.wheels)