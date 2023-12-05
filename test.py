def alg(x: list):
    n = len(x)
    for i in range(n):
        swap = False
        for j in range(n - i):
            if (j + 1) not in range(len(x)):
                continue
            if x[j + 1] < x[j]:
                swap_items(x, j, j + 1)
                swap = True
        if not swap:
            return  # Everything is in order!


def swap_items(x: list, i: int, j: int):
    x[i], x[j] = x[j], x[i]