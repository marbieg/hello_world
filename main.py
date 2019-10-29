print("Hello world!")

lista = [1, 2, 3, 4, 5]
l1 = lista.copy()  # performs deep copy
l1[0] = 100
print(lista)

l2 = lista  # performs shallow copy
l2[0] = 100
print(lista)