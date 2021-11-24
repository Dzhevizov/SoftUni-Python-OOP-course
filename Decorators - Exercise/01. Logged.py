def logged(f):

    def wrapper(*args):
        func_name = f.__name__
        params = [str(x) for x in args]
        result = f(*args)
        return f"you called {func_name}({', '.join(params)})\nit returned {result}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
