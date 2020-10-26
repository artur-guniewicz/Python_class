line = 'So close, no matter how far \n' \
       'Couldn\'t be much more from the heart \n' \
       'Forever trusting who we are \n' \
       'And nothing else matters'

length = 0

for l in line.split():
    length += len(l)

print('Sum of letters in line: ', length)
