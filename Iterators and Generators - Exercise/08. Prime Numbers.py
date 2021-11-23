def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    n = num // 2
    for i in range(2, n + 1):
        if num % i == 0:
            return False
    return True


def get_primes(list_of_num):
    for el in list_of_num:
        if is_prime(el):
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
