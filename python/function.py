# def print_pattern(n): # parameter
#     for i in range(n, 0, -1):
#         for j in range(i):
#             print(i, end=" ")
#         print("")

# while True:
#     n = int(input("Enter No of Lines: "))
#     print_pattern(n) # argument

#     choice = input("Want To Continue (y/n): ")
#     if (choice == 'n' or choice == 'N'):
#         print("Thanks For Playing.")
#         break



# Rock, Paper, Scissor
import random

def random_choice():
    choices = ["Rock", "Paper", "Scissor"]
    selected = random.choice(choices)
    return selected

def calculate_win(user, computer):
    if computer > user:
        print(f"Computer WIN! com:({computer}) | you:({user})")
    elif user > computer:
        print(f"You WIN! you:({user}) | com:({computer})")
    else:
        print(f"DRAW! you:({user}) | com:({computer})")

while True:
    m_points = int(input("Max Points: "))
    us_point = 0
    com_point = 0

    for i in range(1, m_points+1):
        user_choice = input("Rock (r)/ Paper (p)/ Scissor (s): ")
        computer_choice = random_choice()

        if user_choice == 'r' and computer_choice == 'Rock':
            print("Same Selection, DRAW")
        elif user_choice == "p" and computer_choice == 'Rock':
            print("You WIN!")
            us_point += 1
        elif user_choice == "s" and computer_choice == 'Rock':
            print("Computer WIN!")
            com_point += 1
        elif user_choice == 'r' and computer_choice == 'Paper':
            print("Computer WIN!")
            com_point += 1
        elif user_choice == 'p' and computer_choice == 'Paper':
            print("Same Selection, DRAW")
        elif user_choice == 's' and computer_choice == 'Paper':
            print("You WIN!")
            us_point += 1
        elif user_choice == 'r' and computer_choice == 'Scissor':
            print("You WIN!")
            us_point += 1
        elif user_choice == 'p' and computer_choice == 'Scissor':
            print("Computer WIN!")
            com_point += 1
        elif user_choice == 's' and computer_choice == 'Scissor':
            print("Same Selection, DRAW")
        else:
            print("Wrong Selection Type")

    calculate_win(user=us_point, computer=com_point)

    choice = input("Want To Continue (y/n): ")
    if (choice == 'n' or choice == 'N'):
        print("Thanks For Playing.")
        break






