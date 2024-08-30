import random as ran
from turtle import     *

def dice_roll():
    number =ran.randint(1,6)
    print("you rolled a " + str(number))
    return number

max_score = 20
max_trial = 7
 

def start_game():
    user_score = 0
    current_trial = 1 

    print("welcome to dodjo dice game")
    print("try to reach exactly " + str(max_score) + "points to win the game")
    input("Press Enter to begin")
    
    # while user_score < max_score and current_trial < max_trial:

           
           
    #         current_roll = dice_roll()
    #         user_score += current_roll
    #         current_trial += 1

            
    #         if user_score > max_score:
    #             print("your final score was " + str(user_score))
    #             print("you have excedded maximum score.")
    #             break
    #         elif user_score == max_score :
    #                 print("your final score was " + str(user_score))
    #                 print("congratulations, you have won")
    #                 break
    #         elif user_score < max_score:
    #             print("your final score was " + str(user_score))

    while True:

        input("press enter to roll")
        current_roll = dice_roll()
        user_score += current_roll
        current_trial += 1

        if user_score < max_score and current_trial < max_trial:
            print("your final score was " + str(user_score))
        elif user_score == max_score:
            print("your final score was " + str(user_score))
            print("congratulations, you have won")
            break
        elif user_score > max_score:
            print("your final score was " + str(user_score))
            print("you have excedded maximum score of 20.")
            break
        elif current_trial > max_trial:
            print("You have exceeded  your max trials of seven")
            print("Your final score is " + str(user_score))
            break
        else:
            print("you rolled a " + str(current_roll))
            ("your score is " + str(user_score))



        


start_game()



 