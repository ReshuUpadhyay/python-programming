name = input("Enter your name: ")
age = int(input("enter your age="))
print("your age =",age)
if (18<=age <=110):
        print("You are eligible to vote.")
        code=int(input("enter your voter code "))
        state = input("Enter your state: ")
        print("chose any one :- a=bjp,b=inc,c=aap,d=none of them,e =other candidate")
        vote=input("enter your choice=")
        if vote.lower() == 'a' or vote.lower() == 'A':
                print("Voted for BJP")
        elif vote.lower() == 'b' or vote.lower() == 'B':
                print("Voted for INC")
        elif vote.lower() == 'c' or vote.lower() == 'C':
                print("Voted for AAP")
        elif vote.lower() == 'd' or vote.lower() == 'D':
                print("Voted for none of the above")
        elif vote.lower() == 'e' or vote.lower() == 'E':
                your_candidate = input("Enter the name of your candidate: ")
                print("Voted for", your_candidate)
        else:
                print("Invalid choice. Please rerun the code.")
        print("Thank you for voting!")
        print("Voter Information:")
        print("Name:", name)
        print("Age:", age)
        print("State:", state)

else:
        print("Sorry, you are not eligible to vote.")
