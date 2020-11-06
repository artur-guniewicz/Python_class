def factorial(n):
    output = 1

    for i in range(1, n + 1):
        output *= i

    return output


number = int(input('Enter the number: '))
print(number, '! = ', factorial(number))
