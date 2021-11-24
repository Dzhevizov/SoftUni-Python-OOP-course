class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            func_name = self.function.__name__
            result = self.function(*args, **kwargs)
            file.write(f"Function '{func_name}' was called. Result: {result}")
            file.write("\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
