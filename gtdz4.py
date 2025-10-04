class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def info(self):
        print(f"Транспорт: {self.brand}, скорость {self.speed} км/ч")


class Car(Transport):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)
        self.model = model
    def info(self):
        super().info()
        print(f"Это легковая машина, модель: {self.model}")


class Bus(Transport):
    def __init__(self, brand, speed, capacity):
        super().__init__(brand, speed)
        self.capacity = capacity
        self.routes = []
    def add_route(self, route):
        self.routes.append(route)
        print(f"Маршрут {route} доюавлен.")
    def info(self):
        super().info()
        print(f"Это автобус, вместимость: {self.capacity} человек")
        if self.routes:
            print("Автобус ездит на этих маршшрутах:")
            for r in self.routes:
                print(r)


bmw = Car("BMW", 220, "M5")
bmw.info()

print()

bus1 = Bus("Mercedes", 120, 50)
bus1.add_route("number1 — Аэропорт Нурсултан Назарбаев → Нұрлы жол")
bus1.add_route("number2 — Университет Назарбаева → Косшы")
bus1.info()