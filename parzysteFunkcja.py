#parzyste cyfry wybrane z funkcji (DOWOLNY ZBIOR)
def parz(a,b):
    for i in range(a+1 if a%2 else a, b+1, 2):
        #range(1,101,2)
        print(i, end = " ")
parz(1,100)
#parz(45,450)
#parz(80,100)
