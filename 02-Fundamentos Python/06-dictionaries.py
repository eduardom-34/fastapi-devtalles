

# no se hace de forma ordenda, sino de clave y valor, en otros lenguajes se les conoce como JSON
user = {
    "name": "Cesar",
    "age": 24,
    "email": "cesar@email.com",
    "active": True,
    (19.12, -98.32): "Cancun Mexicco"   
}

# El diccionario si es mutable, pero las llaves (el primer valor de los dos) tiene que ser inmutable
# por eso solo acepta, string, numero y tuplas como llave, porque son inmutables

user["name"] = "Eduardo"
user["age"] = 27
user["country"] = "Mexico"
# print(user[(19.12, -98.32)])


# vaues, items, keys
print(user)