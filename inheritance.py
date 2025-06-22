class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):  # Метод делает красивый вывод в консоль
        return f'{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}%, total bonus={self.calculate_total_bonus()}'


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)  # Позволяет вызвать метод из класса родителя


class Manager(Employee):# Так происходит наследование
    def __init__(self, name):
        super().__init__(name, 45000, 10000)  # Позволяет вызвать метод из класса родителя


class CEO(Employee):
    def __init__(self, name):
       super().__init__(name, 105000, 20000)#Позволяет вызвать метод из класса родителя

    def calculate_total_bonus(self):# Позволяет переписать метод предка
        return 2000000
if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    print(masha)
    grisha = Manager('Nikolai Petrovich')
    print(grisha)
    ivan = CEO('Ivan Pavlovich')
    print(ivan)