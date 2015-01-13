def rabbit_pairs(n: int, k: int) -> int:
    """

    :param n: Months
    :param k: Rabbits produced by every reproduction age pair every generation.
    :return: Rabbit population
    """

    if n <= 2:
        return 1

    return rabbit_pairs(n-1, k) + (k * rabbit_pairs(n-2, k))




assert rabbit_pairs(1, 3) == 1
assert rabbit_pairs(2, 3) == 1
assert rabbit_pairs(3, 3) == 4
assert rabbit_pairs(4, 3) == 7
assert rabbit_pairs(5, 3) == 19

print(rabbit_pairs(33, 4))