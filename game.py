secret = 50
attempts = 0  

while True:
    guess = int(input("Guess the number (0-100): "))
    attempts += 1 

    if guess > 100:
        print("Enter a smaller number")
    elif guess < 0:
        print("Enter a higher number")
    elif guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break  
