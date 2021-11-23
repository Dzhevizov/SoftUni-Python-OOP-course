class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.number:
            raise StopIteration

        result = self.sequence[self.index]
        self.index += 1
        if self.index == len(self.sequence):
            self.index = 0
        self.count += 1

        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
