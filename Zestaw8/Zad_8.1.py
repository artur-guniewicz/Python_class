def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0:
        if b == 0:
            if c == 0:
                print('Nieskończenie wiele rozwiązań')
            else:
                print('Brak rozwiązań')
        else:
            if c == 0:
                print('y = 0')
            else:
                print('y =', -c / b)
    else:
        if b == 0:
            if c == 0:
                print('x = 0')
            else:
                print('x =', -c / a)
        else:
            if c == 0:
                print('y =', -a / b, '* x')
            else:
                print('y =', -a / b, "* x +", -c / b)


print('2x + 4y - 2 = 0')
solve1(-2, 4, -2)
