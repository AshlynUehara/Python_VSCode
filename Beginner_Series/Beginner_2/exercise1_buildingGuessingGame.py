secret_number = 9

guess_count = 0
while guess_count < 3:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You win!")
        break
    else:
        guess_count = guess_count + 1
else:
    print("Sorry, you failed!")
