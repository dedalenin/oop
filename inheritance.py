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
        super().__init__(name, 45000, 15)  # Позволяет вызвать метод из класса родителя


class CEO(Employee):
    def __init__(self, name):
       super().__init__(name, 105000, 200)#Позволяет вызвать метод из класса родителя

def calc_bonuses(employees: list[Employee]):
    for employee in employees:
        print(f'Calc bonus for {employee.name}, it is = {employee.calculate_total_bonus()}')
if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    print(masha)
    grisha = Manager('Nikolai Petrovich')
    print(grisha)
    ivan = CEO('Ivan Pavlovich')
    print(ivan)
    a_list = [masha, grisha, ivan]
    calc_bonuses(a_list)