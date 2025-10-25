
list_numbers = [1, 2, 3, 4, 2, 5, 2,2,2]
list_letters = ['a', 'b', 'c', 'd', 'e']
list_mix = [1, 'a', 2, True, 3, 'c']


shopping_cart = ['apple', 'banana', 'orange' "Cafe"]


print(type(list_mix))


#Metodos

#append
print(list_numbers)
list_numbers.append(100)
list_numbers.append(200)
print(list_numbers)


#remove
list_numbers.remove(4)
list_numbers.remove(100)
print(list_numbers)


#count
print(list_numbers.count(2))