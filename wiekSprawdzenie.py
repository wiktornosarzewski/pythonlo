w = int(input("Ile masz lat? "))
if w >= 18:
    print("możesz grać w gry dla dorosłych")
else:
    if w <= 17 and w >= 12:
        print("możesz grać w gry oznaczone jako PEGI-12")
    else:
        if w < 12:
            print("jesteś za mały na granie w gry")
