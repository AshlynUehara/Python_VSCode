i = 1

while i == 1:
    line = input(">")
    if line == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif line == "start":
        print("Car started...Ready to go!")
    elif line == "stop":
        print("Car stopped.")
    elif line == "quit":
        i = -1
    else:
        print("I don't understand that...")
