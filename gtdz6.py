result = []

def divider(a, b):
    if a < b:
        raise ValueError("Первое число < второго")
    if b > 100:
        raise IndexError("Второе число > 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  

for key in data:
    try:
        res = divider(int(key), data[key]) 
        result.append(res)
    except ZeroDivisionError:
        print(f"Ошибка: деление на ноль при key = {key}")
    except ValueError as e:
        print(f"Ошибка ValueError: {e} (key = {key})")
    except IndexError as e:
        print(f"Ошибка IndexError: {e} (key = {key})")
    except TypeError as e:
        print(f"Ошибка TypeError: {e} (key = {key})")
    except Exception as e:
        print(f"Другая ошибка: {e} (key = {key})")

print("\nРезультаааты делений:", result)
