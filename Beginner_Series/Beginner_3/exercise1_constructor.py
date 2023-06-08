class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
print(john.name) # returns John Smith
john.talk() # returns Hi, I am John Smith

bob = Person("Bob Smith")
bob.talk() # returns Hi, I am Bob Smith