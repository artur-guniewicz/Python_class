line = 'So close, no matter how far \n' \
       'Couldn\'t be much more from the heart \n' \
       'Forever trusting who we are \n' \
       'And nothing else matters'

length = [len(l) for l in line.split()]

print('a) the longest word: ', max(line.split(), key=len))
print('b) length of the longest word: ', max(length))