import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break
    play_again()
    exit()
def play_again():
    play=input("do you want to play again=")
    if play.lower()=="yes":
        guess_the_number()
    elif play.lower()=="no":
        print("thank you for playing ")
    else:
        print("invalid choice")
        play_again()
guess_the_number()
