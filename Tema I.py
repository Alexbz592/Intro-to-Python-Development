lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Lista inițială:", lista_initiala)
print("Lista ordonată ascendent:", sorted(lista_initiala))
print("Lista ordonată descendent:", sorted(lista_initiala, reverse=True))

lista_ordonata = sorted(lista_initiala)
lista_pare = lista_ordonata[1::2]
print("Lista cu numerele pare:", lista_pare)

lista_impare = lista_ordonata[::2]
print("Lista cu numerele impare:", lista_impare)

lista_multipli_3 = lista_ordonata[2::3]
print("Lista cu multiplii de 3:", lista_multipli_3)
