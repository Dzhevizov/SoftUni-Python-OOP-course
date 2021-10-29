def create_rhombus_of_stars(count):
    star = "*" + " "
    for i in range(1, count):
        print(" " * (count - i), end="")
        print(star * i)
    for i in range(count, 0, -1):
        print(" " * (count - i), end="")
        print(star * i)


num = int(input())
create_rhombus_of_stars(num)
