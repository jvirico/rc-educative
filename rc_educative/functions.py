from rc_educative import F


def multiplication(n1: int, n2: int) -> int:
    return n1 * n2


def calculator(operation: F, n1: int, n2: int) -> int:
    return operation(n1, n2)


print(calculator(lambda n1, n2: n1 * n2, 10, 10))
print(calculator(multiplication, 100, 10))


num_list = [0, 1, 2, 3]
print(list(map(lambda n: n+10, num_list)))
print(list(filter(lambda n: n>1, num_list)))
