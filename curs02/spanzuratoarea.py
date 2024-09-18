cuvant = 'onomatopee'
cuvant_de_inlocuit = ''
for i in cuvant :
    if i != cuvant[0] and i != cuvant [-1] :
        cuvant_de_inlocuit = cuvant_de_inlocuit + '_'
    else :
        cuvant_de_inlocuit = cuvant_de_inlocuit + i
print (cuvant_de_inlocuit)
while cuvant_de_inlocuit != cuvant :
    caracter_cerut = input("Alege o litera: ")
    print(caracter_cerut)
    if caracter_cerut in cuvant :

