# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def exe_3(a = int(input('Enter a ')), b = int(input('Enter b ')), c = int(input('Enter c '))):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


print(exe_3())