class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point() # creates object
point1.draw() # returns draw

point1.x = 10
point1.y = 20
print(point1.x) # returns 10

point2 = Point()
