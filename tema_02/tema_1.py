print("Alegeți o problemă de rezolvat:")
alegere = input("Introduceți numărul problemei (1-5): ")

if alegere == '1':
    nume = input("Introduceți numele dvs.: ")
    text = input("Introduceți un text: ")
    if text.isalpha():
        print(f"Sirul de caractere a fost gasit de {nume}")
    elif text.isdigit():
        print("Ați introdus un șir de numere")
    else:
        print("Ați introdus un șir mixt de caractere și numere")

elif alegere == '2':
    numar = int(input("Introduceți un număr: "))
    if numar % 2 == 0:
        print("Numărul este par")
    else:
        print("Numărul este impar")

elif alegere == '3':
    an = int(input("Introduceți un an: "))
    if an % 4 == 0:
        print("Anul este bisect")
    else:
        print("Anul nu este bisect")

elif alegere == '4':
    numar = float(input("Introduceți un număr: "))
    if numar > 0:
        if numar < 10:
            print("Numărul este pozitiv și mai mic decât 10")
        else:
            print("Numărul este pozitiv")
    elif numar == 0:
        print("Numărul este 0")
    else:
        print(f"Numărul transformat în pozitiv este: {abs(numar)}")

elif alegere == '5':
    print("""
    1 – Afisare lista de cumparaturi
    2 – Adaugare element
    3 – Stergere element
    4 – Sterere lista de cumparaturi
    5 - Cautare in lista de cumparaturi
    """)
    optiune = input("Alegeți o opțiune (1-5): ")
    if optiune == '1':
        print("Afisare lista de cumparaturi")
    elif optiune == '2':
        print("Adaugare element")
    elif optiune == '3':
        print("Stergere element")
    elif optiune == '4':
        print("Sterere lista de cumparaturi")
    elif optiune == '5':
        print("Cautare in lista de cumparaturi")
    else:
        print("Alegerea nu exista. Reincercati")

else:
    print("Alegere invalidă. Vă rugăm să alegeți un număr între 1 și 5.")