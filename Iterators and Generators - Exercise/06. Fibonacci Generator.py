def fibonacci():
    fib0 = 0
    yield fib0
    fib1 = 1
    yield fib1

    while True:
        fibn = fib0 + fib1
        yield fibn
        fib0, fib1 = fib1, fibn


generator = fibonacci()
for i in range(5):
    print(next(generator))
generator = fibonacci()
for i in range(1):
    print(next(generator))
