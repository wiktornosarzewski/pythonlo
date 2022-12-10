lista = [0] * 8
#lista = [0,0,0,0,0,0,0,0]
for i in range(8):
    lista[i] = int(input("podaj kolejna liczbe "))#nadpisuje
for j in reversed(lista): #czytane w odwrotnej kolejnosci
    print(j)
