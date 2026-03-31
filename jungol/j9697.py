class Person:
    def __init__(self, name, bat, hit):
        self.name = name
        self.bat = bat
        self.hit = hit
        self.avg = hit / bat

    def print(self):
        print(f"name:{self.name}, AVG:{self.avg:.3f}, AB:{self.bat}, H:{self.hit}")

name, bat, hit = input().split()
bat = int(bat)
hit = int(hit)
p1 = Person(name, bat, hit)

name, bat, hit = input().split()
bat = int(bat)
hit = int(hit)
p2 = Person(name, bat, hit)

p1.print()
p2.print()