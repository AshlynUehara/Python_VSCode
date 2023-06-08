class Mammal:
    def walk(self):
            print("walk")

class Dog(Mammal): # Dog class will inherit methods of Mammal class    
    def bark(self):
         print("bark")

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk() # returns walk
dog1.bark() # returns bark

cat1 = Cat()
cat1.walk() # returns walk

