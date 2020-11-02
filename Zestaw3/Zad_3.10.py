def isCorrect(roman_nb):
    counter = 1

    correctChars = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

    for i in roman_nb:
        if i not in correctChars:
            return False

    for i, val in enumerate(roman_nb):
        if (i + 1) < len(roman_nb) and val == roman_nb[i + 1] and val in ('I', 'X', 'C', 'M'):
            counter = counter + 1
        else:
            counter = 1

        if counter > 3:
            return False

        if (i + 1) < len(roman_nb) and val in ('V', 'L', 'D') and roman_nb[i + 1] in ('V', 'L', 'D'):
            return False

        return True


def roman2int():
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0

    while True:
        roman_nb = input('Enter the number in the Roman numeral system: ')

        if isCorrect(roman_nb):
            for i in range(len(roman_nb)):
                if i > 0 and values[roman_nb[i]] > values[roman_nb[i - 1]]:
                    output += values[roman_nb[i]] - 2 * values[roman_nb[i - 1]]
                else:
                    output += values[roman_nb[i]]

            print(roman_nb, "in the decimal system: ", output)
            break
        else:
            print('Incorrect number! Try again...')


roman2int()
