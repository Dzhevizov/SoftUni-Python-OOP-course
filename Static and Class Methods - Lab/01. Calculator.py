class Calculator:
    @staticmethod
    def add(*args):
        result = args[0]
        for arg in args[1:]:
            result += arg
        return result

    @staticmethod
    def multiply(*args):
        result = args[0]
        for arg in args[1:]:
            result *= arg
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
