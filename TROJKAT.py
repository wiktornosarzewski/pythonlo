#trojkat pro
while True:
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    if a>b and a > c:
        p = a
        a = c
        c = p
    else:
        if b > c:
            p = b
            b = c
            c = p

    if a+b > c:
        print("TAK.")
    else:
        print("Nie.")
