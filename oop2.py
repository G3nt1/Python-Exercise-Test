class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I speak a delphin language")



class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and i have color  {self.color}")


    def speak(self):
        print("I make meow")
    
class Dog(Pet):
    def speak(self):
        print("I make bark")
    
p = Pet("Tim", 22)
p.show()
p.speak()
c = Cat("pupi", 5, "Broun")
c.show()
c.speak()
d = Dog("lupi", 11)
d.show()
d.speak()