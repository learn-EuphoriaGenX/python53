class Car:
    # constructor method
    def __init__(self, color, model, name ):
        self.color = color # features / property
        self.model = model
        self.name = name
    
    # method / functions
    def move_forward(self):
        print(f'{self.name} is moving forward...⬆️')

    def move_backward(self):
        print(f'{self.name} is moving backward...⬇️')
    
    # magic/dunder method
    def __str__(self):
        return f"{self.color} : {self.model}: {self.name}"

    
c1 = Car("Blue", "ABC", "Volvo1") # object initialization
c2 = Car("Red", "DEF", "Volvo2")
# print(f'C1 -> {c1.color} : {c1.model}: {c1.name}')
# c1.move_forward()
# print(f'C2 -> {c2.color} : {c2.model}: {c2.name}')
# c2.move_forward()

print(c1)
print(c2)

# class Human
        