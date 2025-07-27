
import random as rd 

print("Let's start the ROCK, PAPER, SCISSOR game")

list = ['Rock','Paper','Scissor']


user_points=0
computer_points= 0
draw_points = 0 
counter = 1

while counter <= 5:
    print (f'Round {counter}')
    user_choice = input("Select one [ROCK/PAPER/SCISSOR]=").strip().capitalize()
    if user_choice == 'Exit':
        print("Thanks for Playing")
        break
    if user_choice not in list:
        print("Invalid input! Please select ROCK/PAPER/SCISSOR")
        continue

    computer_choice = rd.choice(list)

    print (f'Your choice is {user_choice}')
    print (f'Computer choice is {computer_choice}')
    
    if computer_choice == user_choice:
            print ("Match draw as both choose same")
            draw_points+=1

    elif user_choice == 'Rock':
        if computer_choice=='Paper':
            print("Computer won as Paper covers Rock")
            computer_points+=1
        else:
            print("Hurry!!you won as Rock wins over Scissor")
            user_points+=1

    elif user_choice=='Paper':
        if computer_choice=='Rock':
            print("Hurry!!you won as paper covers rock")
            user_points+=1
        else:
            print('Computer won as scissor cuts paper')
            computer_points+=1
    elif user_choice=='Scissor':
        if computer_choice=='Paper':
            print("Hurry!!you won as Scissor cuts the paper")
            user_points+=1
        else:
            print('Computer won as Rock wins over scissor')
            computer_points+=1
    

    counter+=1 

    

print("\n🎉 Game Over 🎉")
print(f"Total Rounds Played: {counter - 1 if user_choice == 'Exit' else counter}")
print(f"Final Scores -> You: {user_points} | Computer: {computer_points} | Draws: {draw_points}")





