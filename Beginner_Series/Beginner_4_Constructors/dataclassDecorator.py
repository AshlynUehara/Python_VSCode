from dataclasses import dataclass

class Student:
    
    StudentName: str
    rollNumber: str

    def move(self):
        print("move")

    def sit(self):
        print("sit")

    def print_name(self, StudentName):
        print(StudentName)

    def print_rollNumber(self, rollNumber):
        print(rollNumber)


student1 = Student()

print(type(student1.rollNumber))

# print(student1.rollNumber) # AttributeError: 'Student' object has no attribute 'rollNumber'
student1.rollNumber = 6
print(student1.rollNumber) # returns 6

student1.print_rollNumber("45") # returns 45
print(student1.rollNumber) # returns 6


student2 = Student()
#print(student2.rollNumber)

