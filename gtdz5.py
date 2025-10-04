x = [1, 2, 3]
print("type(x):", type(x))           # <class 'list'>
print("id(x):", id(x))               # id оюъекта в памяти
print("dir(x):", dir(x))             # список доступных методов
print("isinstance(x, list):", isinstance(x, list))  # True

class Human:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Привет, меня зовут {self.name}")

a = Human("John")
print("hasattr(a, 'name'):", hasattr(a, "name"))    # True
print("getattr(a, 'name'):", getattr(a, "name"))    # John

def printMas():
    print("hi")

print("callable(printMas):", callable(printMas))  # True
print("callable('hi'):", callable("hi"))          # False

import inspect
print("\nИсходный код класса Human:")
print(inspect.getsource(Human))

print("Сигнатура метода introduce:", inspect.signature(a.introduce))

import sys
b = 10
print("\nВерсия Python:", sys.version)
print("Размер числа в памяти:", sys.getsizeof(b), "байт")

print("\nДоступные builtins:")
print(dir(__builtins__))
