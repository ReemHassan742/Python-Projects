import random
import os 
from game_data import data
from art import logo 
from art import vs


def clear():
    os.system('cls')


def assign():
    return random.choice(data)


def compare(p1, p2,user_input):
    sum1 = p1['follower_count']
    sum2 = p2['follower_count']
    max  = ""
    
    if sum1 > sum2:
        max = p1['name']
    elif sum1 > sum2 : 
        max = p2['name']
    
    if max == user_input :
        return True 
    else :
        return False 
    
def  play_higher_lower():
    playling_game = True 
    while playling_game:
        score = 0
        still_guessing = True
        while still_guessing:
            clear()
            print(logo)
            
            
            person1 = assign()
            person2 = assign()
            
            if person1 == person2 : 
                person2 = assign()
                
            print(f"Name: {person1['name']}, Desc: {person1['description']}")
            print(vs)
            print(f"Name: {person2['name']}, Desc: {person2['description']}")
            print("---------------------------------------------")
            print(f"Your current score is: {score}")
            print("---------------------------------------------")
            
            guess = input("Enter name of person with Higher Followers: ")
            
            if compare(person1, person2, guess):
                score += 1
            
            else: 
                still_guessing = False
                
        play_again = input("Want to play Again? (Y/N)").lower
        
        if play_again == "y":
            continue
        elif play_again  == 'n':
            playling_game = False
            clear()
            print("Game Exited Successfully")
        else:
            playling_game = False
            print("Invalid Input Taken as no.")
            
if __name__ == "__main__":
    want_to_play = input("Do you want to play Higher Lower? (Y/N)\n").lower()
    if want_to_play == 'y':
        clear()
        play_higher_lower()
    elif want_to_play == "n":
        print("Program Exit Successful")
    else:
        print("Intalid Input, Program Exited.")