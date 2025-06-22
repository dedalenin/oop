import ModuleCat
from ModuleCat import Cat
if __name__ == "__main__":
    leopold = Cat('Leopold', 13)
    angela = Cat('Angela', 10)
    print(leopold.name)
    leopold.about()
    print(leopold)
    print(Cat)
    ginger = leopold+angela
    print(ginger)
    # print(dir(leopold))
