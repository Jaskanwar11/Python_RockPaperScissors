import random

comp_score = 0 
user_score = 0

options = ['rock', 'paper', 'scissors']

def winner():
    global comp_score, user_score

    if comp_choice == 'rock' and choice == 'p':
        print("You won ")
        user_score += 1

    elif comp_choice == 'paper' and choice == 's':
        print("You won ")
        user_score += 1
        
    elif comp_choice == 'scissors' and choice == 'r':
        print("You won ")
        user_score += 1
        
    elif comp_choice == 'rock' and choice == 's':
        print("You lost ")
        comp_score += 1

    elif comp_choice == 'scissors' and choice == 'p':
        print("You lost ")
        comp_score += 1

    elif comp_choice == 'paper' and choice == 'r':
        print("You lost ")
        comp_score += 1

    else:
        print("It is a draw")

    print("Your score is: ", user_score)
    print("Computer's score is: ", comp_score)

print("Hello")
print("Welcome to the game of rock paper scissors")

while True:        
    user_input = input("-----Choose-----\n'r' for rock\n'p' for paper\n's' for scissors\nor press q to quit the game: ")
    choice = user_input.lower()
    if choice.lower() == 'q':
        print("Thank you for playing the game\nGoodBye!")
        quit()

    if choice not in ['r', 's', 'p']:
        print("Wrong input!")
        continue

    comp_choice = random.choice(options)

    print("Computer chose: " + comp_choice)
    winner()