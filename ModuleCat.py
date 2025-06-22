class Cat:
    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    def __add__(self, other):  # Переписали Для плюсика
        if isinstance(other, Cat):
            return Cat('Ginger', 0)

    def __str__(self):  # Переписали для принта
        return (f'Meow. My full name is{self.name} and i am {self.age} years old')

    def about(self) -> None:
        print(f'Hi! My name is {self.name}. I am {self.age} years old')
