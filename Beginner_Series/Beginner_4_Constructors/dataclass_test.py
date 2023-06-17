from dataclasses import dataclass

@dataclass
class Student:

    name: str
    age: int
    ID_number: int

student1 = Student("Ashlyn", 18, 488)
student2 = Student("Amy", 19, 127)

print(student1) # returns Student(name='Ashlyn', age=18, ID_number=488)
print(student2) # returns Student(name='Amy', age=19, ID_number=127)
print(student1.name)

print()

print("Data in student1 and student2 are same?", student1 == student2)