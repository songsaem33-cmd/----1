class Building:
    def __init__(self, years, price):
        self.years = years
        self.price = price

    def print(self, Y, P):
        if Y <= self.years and P >= self.price:
            print(f"{self.years} {self.price}")

N = int(input())
building = []

for _ in range(N):
    years, price = map(int,input().split())
    building.append(Building(years, price))

Y, P = map(int, input().split())

for b in building:
    b.print(Y, P)