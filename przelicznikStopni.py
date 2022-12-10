while True:
    c = 0.0
    f = 0.0
    c = float(input("Podaj temperature w oC: "))
    #temp = (f-32*5/9)
    #c = temp
    f = 32.0 + 1.8 * c
    print("w stopniach F to: " ,f,)
