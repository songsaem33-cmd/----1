class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        if self.age >= 18:
            print(f"{self.name}({self.age}) : adult")
        else:
            print(f"{self.name}({self.age}) : child")

name, age = input().split()
age = int(age)
p1 = Person(name, age)

name, age = input().split()
age = int(age)
p2 = Person(name, age)

p1.print()
p2.print()