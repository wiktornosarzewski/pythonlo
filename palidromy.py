def czyPal(slowo):
    return slowo == slowo[::-1]
slowo = str(input("Podaj slowo: "))
odp = czyPal(slowo)
if odp:
    print(slowo, "jest palidromem")
else:
    print(slowo, "nie jest")
    
