import math


def least_common_multiple(a, b):
    return (a * b) / math.gcd(a, b)


def add_frac(x, y):
    denominator = least_common_multiple(x[1], y[1])
    nominator = x[0] * (denominator / x[1]) + y[0] * (denominator / y[1])
    return [nominator, denominator]


def sub_frac(x, y):
    denominator = least_common_multiple(x[1], y[1])
    nominator = x[0] * (denominator / x[1]) - y[0] * (denominator / y[1])
    return [nominator, denominator]


def mul_frac(x, y):
    denominator = x[1] * y[1]
    nominator = x[0] * y[0]
    gcd = math.gcd(nominator, denominator)
    return [nominator / gcd, denominator / gcd]


def div_frac(x, y):
    return mul_frac(x, y[::-1])


def is_positive(x):
    return (x[0] > 0 and x[1] > 0) or (x[0] < 0 and x[1] < 0)


def is_zero(x):
    return x[0] == 0


def cmp_frac(x, y):
    denominator = least_common_multiple(x[1], y[1])
    nominator1 = x[0] * (denominator / x[1])
    nominator2 = y[0] * (denominator / y[1])

    if nominator1 == nominator2:
        return 0
    elif nominator1 < nominator2:
        return -1
    else:
        return 1


def frac2float(x):
    return x[0] / x[1]
