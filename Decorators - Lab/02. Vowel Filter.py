def is_vowel(x):
    vowels = 'aeiouy'
    if x in vowels:
        return True
    return False


def vowel_filter(function):

    def wrapper():

        seq = function()
        result = [x for x in seq if is_vowel(x)]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
