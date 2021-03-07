def my_add(*args):
    # print(args[0])
    total = 0
    for num in args:
        total += num
    return total

print(my_add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="현대", model="아이오닉5")
print(my_car.make)
print(my_car.model)

my_car2 = Car()
print(my_car2.model)