line = 'So close, no matter how far \n' \
       'Couldn\'t be much more from the heart \n' \
       'Forever trusting who we are \n' \
       'And nothing else matters'

print('a) sorted alfabetically: ', sorted(line.split(), key=lambda x : x.lower()))
print('b) sorted by length: ', sorted(line.split(), key=len))