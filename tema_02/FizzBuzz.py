numar = int(input("Introduceți un număr: "))
if numar % 3 == 0 and numar % 5 == 0:
    rezultat = "FizzBuzz"
elif numar % 3 == 0:
    rezultat = "Fizz"
elif numar % 5 == 0:
    rezultat = "Buzz"
else:
    rezultat = str(numar)
print(f"{numar} - {rezultat}")