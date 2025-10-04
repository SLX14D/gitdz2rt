# #Задание 1
# class Animal:
#     def speak(self):
#         raise NotImplementedError("Метод speak() должен быть переопределён в подклассе")

#     def describe(self):
#         print(f"This is a {self.__class__.__name__}")

# class Dog(Animal):
#     def speak(self):
#         print("Собака говоритЖ гав,гав!")

# class Cat(Animal):
#     def speak(self):
#         print("Кошка говорит: мяу!")

# class Parrot(Animal):
#     def speak(self):
#         print("Попугай говоритт: Я Пират аa Я пират!")

# dog = Dog()
# cat = Cat()
# parrot = Parrot()

# dog.speak()
# cat.speak()
# parrot.speak()

#Задание 2
# import inspect

# def who_am_i(obj):
#     print(f"\nОбъект: {obj}")
#     print(f"Тип: {type(obj)}")
#     print(f"Атрибуты и методы: {dir(obj)}")
#     if type(obj).__module__ == 'builtins':
#         print("Это встроенный тип Python")
#     else:
#         print("Это пользовательский или импмортированный тип")

# who_am_i(123)
# who_am_i("hello")
# who_am_i([1, 2, 3])

#Задание 3
# import sys

# print("\n--- Информация о Python ---")
# print(f"Версия Python: {sys.version}")
# print(f"Путь к интерпретатору: {sys.executable}")
# print(f"Аргументы комалндной строки: {sys.argv}")
# print(f"Платформа: {sys.platform}")

#Задание 4
print("\n--- Простой калькулятор ---")

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    op = input("Введите операцию (+, -, *, /): ")

    if op == '+':
        print("Результат:", a + b)
    elif op == '-':
        print("Результат:", a - b)
    elif op == '*':
        print("Результат:", a * b)
    elif op == '/':
        print("Результат:", a / b)
    else:
        print("Ошибка: неизвестная операция!")

except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except Exception as e:
    print(f"Произошла непредвиденнач ошибка: {e}")
