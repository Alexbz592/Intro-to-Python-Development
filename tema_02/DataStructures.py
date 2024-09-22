lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Lista inițială:", lista_initiala)
print("Lista ordonată ascendent:", sorted(lista_initiala))
print("Lista ordonată descendent:", sorted(lista_initiala, reverse=True))
lista_ordonata = sorted(lista_initiala)
numere_pare = lista_ordonata[1::2]
print("Numerele pare din lista ordonată:", numere_pare)
numere_impare = lista_ordonata[::2]
print("Numerele impare din lista ordonată:", numere_impare)
multipli_3 = lista_ordonata[2::3]
print("Multiplii de 3 din lista ordonată:", multipli_3)