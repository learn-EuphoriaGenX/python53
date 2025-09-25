hangman_stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        =========
        """,
        """
           ------
           |    |
           |   DEAD  
           |    
           |    
           |
        =========
        """
    ]
import random
random_num = random.randint(1, 10)
stages = 6
current_stage = 0
print(hangman_stages[0])
while True:
    userChoice = int(input("Choose a number (1-10) "))

    if (current_stage < stages):
        if (random_num > userChoice):
            print("Choose Grater than ", userChoice)
            print(hangman_stages[current_stage+1])
        elif (random_num < userChoice):
            print("Choose Less than ", userChoice)
            print(hangman_stages[current_stage+1])
        else:
            print("You Win in ", current_stage+1, " stage")
            break
    else:
        print("You Loose ")
        print(hangman_stages[current_stage+1])
        break

    current_stage += 1
      
    

