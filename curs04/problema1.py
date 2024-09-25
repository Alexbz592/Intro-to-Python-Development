a = input("Introduceti nr1: ")
b = input("Introduceti nr2: ")
rezultat = None
operatie = None

if a.isdigit() and b.isdigit() :
    a = int(a)
    b = int(b)
    if (rezultat := a * b) and rezultat <= 1000 :
        operatie = "produs"
    else :
        rezultat = a + b
        operatie = "suma"

            print(f"{operatie} este {rezultat} ")