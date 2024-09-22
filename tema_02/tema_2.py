a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

elemente_comune = []
for element in a:
    if element in b and element not in elemente_comune:
        elemente_comune.append(element)
elemente_comune.sort()

print("Elementele comune sunt:")
print(elemente_comune)