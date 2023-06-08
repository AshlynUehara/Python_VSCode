course = "Python for Beginners"
print(course) # returns Python for Beginners
print(course.upper()) # returns PYTHON FOR BEGINNERS
print(course.find("y")) # returns 1
print(course.find("Y")) # returns -1
print(course.find("for")) # returns 7
print(course.replace("for", "4")) # returns Python 4 Beginners

print("Python" in course) # returns True