class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(f"{self.name}({self.age}) : child")
        print(f"{self.name}({self.age}) : adult")
        if self.age >= 18:
            print("child")
        else:
            print("adult")

name, age = input().split()
age = int(age)
p1 = Person(name, age)
p1.print()
        