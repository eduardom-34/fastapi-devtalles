
# Las listadas son ordenadas, o sea, cada quien tiene un índice, comenzando desde el cero
list_numbers = [1,2,3,4,5,2,2,2,2]


list_letters = ['a', 'b', 'c']

list_mix = [2, 'z,', True, [1, 2, 3, 4], 5.5]


shopping_cart = ['Laptop', 'Silla Gamer', "Cafe"]


print(type(list_mix))

# Metodos de las listas, se escribe el nombre de la lista y luego el nombre del metodo a utilizar

# append
print(list_numbers)
list_numbers.append(100)
list_numbers.append(200)
print(list_numbers)


# remove, se elimina el valor que pongamos, se evalua el valor, no el índice
list_numbers.remove(4)
list_numbers.remove(100)
print(list_numbers)


# count
print(list_numbers.count(2))


# .copy()  copia una lista
# .cort()  ordena una lista





