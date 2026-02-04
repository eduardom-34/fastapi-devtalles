

def divide_numbers():
    
    try: 
        a = int(input("Ingresa el numerados: ")) # a / b
        b = int(input("Ingresa el denominador: "))
    
        result = a / b
    
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except ValueError:
        print("por favor, ingresa solo numeros")
    except Exception as error:
        print(type(error))
    else:
        print(result)
        return result
    finally:
        print("Gracias por usa nuestra calculadora.")


divide_numbers()
