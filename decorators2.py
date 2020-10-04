
def outer(func):
    cached = {}
    def inner(x):
        if x in cached:
            return cached[x]
        result = func(x)
        cached[x] = result
        return result

    return inner

@outer
def calulate_something(x):
    print("calculate_something(" + str(x) + ")")
    return x * x

print(calulate_something(5))
print(calulate_something(5))

