class MyList(list):
    def __str__(self):# Переопределяем метод __str__ в классе list
        return super().__str__().replace(',', ',\n')


if __name__ == '__main__':
    print([1,2,3])
    my_list = MyList([1,2,3])
    print(my_list)
    print(dir(MyList))