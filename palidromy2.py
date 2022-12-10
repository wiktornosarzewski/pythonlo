#ok dziala palidromy to np. kajak, oko, sos, zakaz
def czyPal(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i -1]:
            return False
    return True
slowo = str(input("podaj slowo: "))
odp = czyPal(slowo)
if(odp):
    print("Tak")
else:
    print("Nie")
