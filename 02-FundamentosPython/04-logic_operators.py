
# and
from turtle import Turtle


age = 25
licensed = True

if (age >= 18 and licensed):
    print("Puedes conducir")
    
    
# or
is_student = False
membership = False

if (is_student or membership):
    print("Tienes descuento")


# not
is_admin = False

if not is_admin:
    print("Acceso denegado")
    
# short circuiting
name = "Cesar"
print(name and name.upper())