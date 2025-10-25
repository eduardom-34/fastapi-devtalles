

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self):
        return f"{self.name} está trabajando."


person1 = Person("Cesar", 24)
person2 = Person("Fernando", 16)

print(person1.work())
print(person2.work())