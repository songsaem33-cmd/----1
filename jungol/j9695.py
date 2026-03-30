class House:
    def __init__(self, location, bedrooms, bathrooms):
        self.location = location
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def print(self):
        print(f"location: {self.location}")
        print(f"bedrooms: {self.bedrooms}")
        print(f"bathrooms: {self.bathrooms}")

        
location, bedrooms, bathrooms = input().split()
p1 = House(location, bedrooms, bathrooms)
p1.print()