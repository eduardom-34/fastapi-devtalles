
#el ciclo for solo se utiliza cuando sabes que lo que evaluas tiene un limite y no es infinito, como una lista o tupla


my_list = [1, 2, 3, 4, 5]

addition = 0

for number in my_list:
    # print(number)
    addition += number

# print(addition)


#el list crea una lista
#el enumerate le da un indice a cada value de la lista
for index, number in enumerate(list(range(100))):
    print(index, number * 2)
    

   
