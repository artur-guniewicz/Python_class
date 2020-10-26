line = 'So close, no matter how far \n' \
       'Couldn\'t be much more from the heart \n' \
       'Forever trusting who we are \n' \
       'And nothing else matters'

first_letters = [l[0] for l in line.split()]
last_letters = [l[len(l) - 1] for l in line.split()]
print('First letters: ', first_letters)
print('Last letters: ', last_letters)
