##Задание 1
# class ReverseIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data) - 1 

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= 0:
#             value = self.data[self.index]
#             self.index -= 1
#             return value
#         else:
#             raise StopIteration


# lst = [5, 10, 15]
# for item in ReverseIterator(lst):
#     print(item)

#Задание 2
def before_and_after(func):
    def wrapper():
        print("Нааало")
        func()
        print("Конец")
    return wrapper

@before_and_after
def say_hi():
    print("Hi!")

say_hi()