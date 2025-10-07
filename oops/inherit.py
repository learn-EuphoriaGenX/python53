class Animal: # parent class
    def __init__(self, name, sound, type ):
        self.name = name
        self.sound = sound
        self.type = type

    def produce_sound(self):
        print(f"{self.name} is produce sound...")


class Dog(Animal):
    def __init__(self, name, sound, type, loyal=True ):
            super().__init__(name, sound, type)
            self.loyal = loyal
    
    def produce_sound(self): # method overriding
        print(f"{self.name} is {self.sound}...")
    
    def save_human(self):
        print(f"{self.name} save 4 human.")

class Lion(Animal):
     def __init__(self, name, sound, type, lives="Forest" ):
            super().__init__(name, sound, type)
            self.lives = lives

     def produce_sound(self): # method overriding
            print(f"{self.name} is {self.sound}ing...")

# a1 = Animal("animal1", "sound1", "Type1")
# a1.save_human()

# d1 = Dog("pogo", "vow vow", "Veg")
# d1.produce_sound()
# d1.save_human()
# print(d1.loyal)

sheru = Lion("Sheru", "Roar", "Non Veg")
sheru.produce_sound()
print(sheru.lives)


