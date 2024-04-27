import random
def rock_paper_scissors():
    choices = {1:'rock',2:'paper',3:'scissors'}
    list_of_dic=list(choices)
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = int(input("Enter your choice (rock=1/paper=2/scissors=3): "))
    if user_choice in list_of_dic:
        computer_choice=random.choice(list_of_dic)
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
            (user_choice == 2 and computer_choice == 1) or \
            (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print( "Computer wins!")
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        play_again()
    else:
        print("Invalid choice! Please enter 'rock=1', 'paper=2', or 'scissors=3'.")
        rock_paper_scissors()
def play_again():
    play = input("do you want to play again yes=y,no=n")
    if play.lower() == "y":
        rock_paper_scissors()
    elif play.lower() == "n":
        print("thank you for playing ")
    else:
        print("invalid choice")
        play_again()

rock_paper_scissors()
