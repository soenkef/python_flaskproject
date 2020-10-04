def repeat(n):
    def deco(func):
        def inner():
            for i in range(0, n):
                func(i)

        return inner
    return deco

@repeat(5)
def do_something(x):
    print("do something() wurde ausgeführt: "  + str(x))

do_something()