def typed(type_):# Декоратор с параметром
    def real_decorator(function):# Добавление еще одного уровня вложенности
        def wrapped(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'TYPE should be {type_}')

            return function(*args)

        return wrapped
    return real_decorator

def typed_int(function):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError('TYPE should be int')

        return function(*args)

    return wrapped

def typed_str(function):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError('TYPE should be str')

        return function(*args)

    return wrapped

#@typed(int) #real_decorator with int
def calculate(a, b, c):
    return a + b + c

@typed(str)
def convert(a, b):
    return a+b



if __name__ == '__main__':
    # calculate = typed_int(calculate)
    calculate = typed(int)(calculate) # Сначала вызывается функция и потом передается еще раз функция
    print(calculate(1, 2, 3))
    print(convert('None', ' hello'))
