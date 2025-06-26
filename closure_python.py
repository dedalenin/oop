# Closure Замыкание


def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)  #
        return all_names  # return outter value

    return inner


def average():
    values = []

    def inner(value: int) -> float:
        values.append(value)
        return sum(values) / len(values)

    return inner



def create_counter(start: int):
    count = start

    def func_counter():
        nonlocal count
        count = count+1
        return count
    return func_counter

def pow_(base):
    def inner(value):
        return value**base
    return inner
if __name__ == "__main__":
    count = create_counter(7)
    print(count())
    print(count())
    print(count())
    print(count())
    print(count())
    print(count)

