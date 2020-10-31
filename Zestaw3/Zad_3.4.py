while True:
    txt = input('Enter number or "stop" to exit: ')

    if txt == "stop":
        print("ending...")
        break
    try:
        nb = int(txt)
    except ValueError:
        print('I said enter NUMBER!')
    else:
        print(nb, '^ 3 = ', nb**3)