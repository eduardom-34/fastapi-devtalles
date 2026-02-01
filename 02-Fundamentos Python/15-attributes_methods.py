

class Person:
    species = "Humano"
     
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100
        self.__password = "1234"
    
        
    def work(self):
        return f"{self.name} está trabajando duro."
    
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return f"Energía restante de {self.name}: {self._energy}"
    
    def __generate_pasword(self):
        return f"$${self.name}{self.age}$$"
    

person1 = Person("Cesar", 29)
person2 = Person("Eduardo", 16)

print(person1.work())
print(person1._waste_energy(10))
print(person2.work())