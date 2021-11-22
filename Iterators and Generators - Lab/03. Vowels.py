class vowels:
    __vowels = ['a', 'o', 'e', 'i', 'u', 'y']

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration

        while True:
            letter = self.string[self.index]
            if letter.lower() in self.__vowels:
                self.index += 1
                return letter
            self.index += 1


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
