# let's create a program for the monty hall problem/paradox

# There are 3 doors
# User selects a door
# A separate door is opened out of the 3 doors
# The user is given a chance to switch doors
# Examine the wins/losses

import random

def main():
    doors = ["1", "2", "3"]
    
    prize_door = random.choice(doors)
    
    while True:
        try:
            pick_door = int(input("Pick a door (1, 2, 3): "))
            if 1 <= pick_door <= 3:
                str_pick_door = str(pick_door)
                break
            print("Pick a number between 1 and 3.")

        except ValueError:
            print("Pick a number.")
            
    if str_pick_door == prize_door:
        temp_doors = [door for door in doors if door != str_pick_door]
        
        random_empty_door = random.choice(temp_doors)
        
        print(f"Door {random_empty_door} is opened and is empty.")
        while True:
            choice_to_switch = input("Do you wish to switch doors? (y/n): ").lower()
            
            if choice_to_switch == 'n':
                print(f"You won! The prize was in door {prize_door}.")
                print("You didn't switch and you WON.")
                break
            elif choice_to_switch == 'y':
                print(f"Sorry, the prize was in door {prize_door}.")
                print("You switched and you LOST.")
                break
            else:
                print("Pick between y or n.")
    
    else:
        for door in doors:
            if door != prize_door and door != str_pick_door:
                print(f"Door {door} is opened and is empty.")
                break
        while True:
            choice_to_switch = input("Do you wish to switch doors? (y/n): ").lower()
            
            if choice_to_switch == 'n':
                print(f"Sorry, the prize was in door {prize_door}.")
                print("You didn't switch and you LOST.")
                break
            elif choice_to_switch == 'y':
                print(f"You won! The prize was in door {prize_door}.")
                print("You switched and you WON.")
                break
            else:
                print("Pick between y or n.")
    
if __name__ == "__main__":
    main()
