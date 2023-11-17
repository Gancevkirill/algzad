# 1
class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_average_grade(self):
        return self.average_grade

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade
# 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
#пример
rectangle = Rectangle(5, 10)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
rectangle.set_length(7)
rectangle.set_width(12)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
# 3
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def display_info(self):
        print("Марка автомобиля:", self.brand)
        print("Модель автомобиля:", self.model)
        print("Год выпуска автомобиля:", self.year)
        print("Пробег автомобиля:", self.mileage)


car = Car("BMW", "M4", 2022, 11000)
car.display_info()
# 4
class BankAccount:
    def __init__(self, client_name, balance):
        self.client_name = client_name
        self.balance = balance

    def get_client_name(self):
        return self.client_name

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
#пример
account = BankAccount("Ганцев", 12000)
print(account.get_client_name())
print(account.get_balance())

account.deposit(400)
print(account.get_balance())

account.withdraw(300)
print(account.get_balance())

account.withdraw(3000)
print(account.get_balance())

# 5
import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side1(self):
        return self.side1

    def set_side1(self, side1):
        self.side1 = side1

    def get_side2(self):
        return self.side2

    def set_side2(self, side2):
        self.side2 = side2

    def get_side3(self):
        return self.side3

    def set_side3(self, side3):
        self.side3 = side3

    def get_type(self):
        if self.side1 == self.side2 == self.side3:
            return 'Равносторонний треугольник'
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return 'Равнобедренный треугольник'
        else:
            return 'Разносторонний треугольник'

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    triangle = Triangle(5, 5, 5);
    print(triangle.get_type())
    print(triangle.calculate_area())