# a)

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;

# Kod jest poprawny pod wzgledem poprawnosci jednak mozna pozbyc sie srednikow i nawiasow
# poprawiona wersja:

x = 2
y = 3
if x > y:
    result = x
else:
    result = y

# b)

# for i in "qwerty": if ord(i) < 100: print (i)

# Kod nie jest poprawny i nie skompiluje sie. Musimy przeniesc funkce if do nowej linii i zachowac skladnie
# poprawiona wersja:

for i in "qwerty":
    if ord(i) < 100:
        print(i)

# c)

# for i in "axby": print (ord(i) if ord(i) < 100 else i)

# Kod jest poprawny pod wzgledem funkcjonalnosci i skompiluje sie. Mozna jednak przeniesc
# wnetrze petli for do nowej linii
# poprawiona wersja:

for i in "axby":
    print(ord(i) if ord(i) < 100 else i)