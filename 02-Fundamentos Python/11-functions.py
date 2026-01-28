
# # Parametros
# def hello(greet = "Hola", name = "Invitado"):
#     print(f"{greet}, {name}")



# # Cuando llamamos a una funcion que necesita parametros, nosotros le mandamo argumentos
# hello("Hola", "Cesar")
# hello("Ciao", "Eduardo")
# hello()
# hello(name = "Teddy", greet = "Hello")



def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs
    
print(big_function(1,2,3,4,5, num1=77, nm2=30))