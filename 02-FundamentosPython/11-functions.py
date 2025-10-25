
# parametros
# def hello(greet = "Hela", name = "Invitado"):
#     print(f"{greet}, {name}!")


# # arguementos
# hello("Hela", "Cesar")
# hello("Ciao", "Fernando")
# hello()
# hello(name="Teddy", greet="Hello")


def big_function (*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs
    
print(big_function(1,2,3,4,5, num1=77, num2=100))



