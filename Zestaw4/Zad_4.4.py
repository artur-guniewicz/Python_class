def fibonacci(n):
    if n == 0:
        return 0

    prev_n = 0
    curr_n = 1

    for i in range(1, n):
        prev_prev_n = prev_n
        prev_n = curr_n
        curr_n = prev_prev_n + prev_n

    return curr_n


number = int(input('Enter the number: '))
print(number, 'number of Fibonacci Sequence is: ', fibonacci(number))
