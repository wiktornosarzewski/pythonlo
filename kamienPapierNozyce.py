while True:
    in1 = input("GRACZ 1: wpisz: papier LUB kamien LUB nozyce: ")
    print("WPROWADZONO: Gracz 1")
    in2 = input("GRACZ 2: wpisz: papier LUB kamien LUB nozyce: ")
    print("WPROWADZONO: Gracz 2")
    print("-----------------------------------------")
    print("WERDYKT")
    
    if in1 == in2:
        print("REMIS: " ,in1,)
    """
    if in1 == "papier" or in2 == "papier":
        print("Wygrywa: " ,in1,)
    if in1 == "nozyce" or in2 == "nozyce":
        print("Wygrywa: " ,in2,)
    if in1 == "kamien" or in2 == "kamien":
        print("Wygrywa: " ,in1,)
    """  
    if in1 == "papier" and in2 == "kamien":
        print("Wygrywa Gracz1 : " ,in1,)
    if in1 == "papier" and in2 == "nozyce":
        print("Wygrywa Gracz 2: " ,in2,)
        
    if in1 == "kamien" and in2 == "nozyce":
        print("Wygrywa Gracz1 : " ,in1,)
    if in1 == "nozyce" and in2 == "kamien":
        print("Wygrywa Gracz 2: " ,in2,)
        

    if in2 == "papier" and in1 == "kamien":
        print("Wygrywa Gracz2 : " ,in1,)
    if in2 == "papier" and in1 == "nozyce":
        print("Wygrywa Gracz 2: " ,in2,)
    
    #special check
        """
        if in1 != "papier" or in1 != "kamien" or in1 != "nozyce":
            print("Gracz 1 wprowadzil bledna wartosc !")
        if in2 != "papier" or in2 != "kamien" or in2 != "nozyce":
            print("Gracz 2 wprowadzil bledna wartosc !")
        """
