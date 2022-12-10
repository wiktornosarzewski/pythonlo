#sprawdza czy wyraz czytany wspak jest taki sam
def czyPalindrom(slowo):
    slowo_inv = "".join(reversed(slowo))
    if(slowo == slowo_inv):
        return True
    return False
slowo = str(input("podaj slowo "))
odp = czyPalindrom(slowo)
if (odp):
    print("Tak")
else:
    print("Nie")
