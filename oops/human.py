class Human:
     # constructor method
    def __init__(self, hname, hage, hcolor ):
        self.name = hname # features / property
        self.age = hage
        self.color = hcolor

    def running(self, dis):
        print(f"{self.name} with {self.age} age is running {dis} KM...")

    def eating(self, name):
        print(f"{self.name} with {self.color} color is eating {name}...")

    def __str__(self):
        return f"My name is : {self.name}\nMy age is : {self.age}\nMy Color is : {self.color}"   

# object instansiate
raghu = Human("Raghu", 24, "Brown")
shyam = Human("Shyam", 30, "Black")
ram = Human("Ram", 12, "White")

print(raghu)
print(shyam)
print(ram)