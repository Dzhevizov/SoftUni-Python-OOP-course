def solution():

    def integers():
        integer = 1
        while True:
            yield integer
            integer += 1

    def halves():

        for i in integers():
            half = i / 2
            yield half

    def take(n, seq):
        result = []
        for i in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
