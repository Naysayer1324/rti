def decor(func):
    def wrapper(*args, **kwargs):
        res = func(*args)
        res = res * 2
        return res
    return wrapper

@decor
def som(a):
    return a**3


print(som(3))

