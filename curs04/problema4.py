s = input("Introduceti un string: ")
n = input("Introduceti un numar: ")

if n.isdigit() :
    n = int(n)
    s = s[n+1:]