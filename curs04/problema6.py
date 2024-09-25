lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n']
n = 3
a = len(lista_start)
lista_n = []

for i in range(n) :

    lista_micuta = []

    for j in range(a) :

        if j % n - i == 0 :
            lista_micuta.append(lista_start[j])

    lista_n.append(lista_micuta)

print(lista_n)