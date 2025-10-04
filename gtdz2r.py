class Student:
    Uni = "KBTU"

    def __init__(self, name="Unknown", group="Unknown", studID=0, gpa=1.0, money= int):
        self.name = name
        self.group = group
        self.studentID = studID
        self.gpa = gpa
        self.money = money

    def __bool__(self):
        return self.gpa >= 2.0

    def __str__(self):
        return f"Student {self.name} have GPA {self.gpa} money {self.money}"

    def sayHello(self):
        print(f"Hello, my name is {self.name} I study  in {self.group} group")

    def Info(self):
        print("Name: ", self.name)
        print("Group: ", self.group)
        print("ID: ", self.studentID)
        print("University: ", self.Uni)
        print("Money:", self.money, "₸")

    def spend_money(self, amount):
        if amount > self.money:
            print(f"{self.name} не хватает денег! У него только {self.money}₸.")
        else:
            self.money -= amount
            print(f"{self.name} потратил {amount}₸. Осталось {self.money}₸.")

    def earn_money(self, amount):
        if amount <= 0:
            print("Нельзя заработать отрицательную сумму!")
        else:
            self.money += amount
            print(f"{self.name} заработал {amount}₸. Теперь у него {self.money}₸.")

    def check_balance(self):
        print(f"У {self.name} сейчас {self.money}₸.")

s1 = Student("Mansur", "GE84932", 12, 2.5, 100000)
s1.Info()
s1.spend_money(67000)
s1.earn_money(25000)
s1.check_balance()

print(bool(s1))
print(s1)