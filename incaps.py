class Person:
    def __init__(self, first_name, last_name, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self._age = age
    def get_age(self, age): # в
        return self._age # возвращает значение атрибута _age

    def describe(self) -> None:
        print(f' I am {self.first_name} {self.last_name}, i am {self.age} years old ')


if __name__ == '__main__':
    ivan = Person('Ivan', 'Naumoff', 12)
    ivan.set_age(0)
    ivan.describe()
