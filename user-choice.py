# let's create a program for the monty hall problem/paradox

# There are 3 doors
# User selects a door
# A separate door is opened out of the 3 doors
# The user is given a chance to switch doors
# Examine the wins/losses

import random

def main():
    prior_doors = ["1", "2", "3"]
    final_doors = []
    
    try:
        pick_door = int(input("Pick a door (1, 2, 3): "))
        
        if not (1 <= pick_door <= 3):
            print("Pick a number between 1 and 3.")
            return
            
        for door in prior_doors:
            if str(pick_door) == door:
                final_doors.append(door)
                prior_doors.remove(door)
                #print(prior_doors)
                break
        
        random_empty_door = random.choice(prior_doors)
        print(f"Door {random_empty_door} is opened and is empty.")
        for door in prior_doors:
            if random_empty_door == door:
                prior_doors.remove(door)
                continue
            final_doors.append(door)
        
        random_prize_door = random.choice(final_doors)
        while True:
            choice_to_switch = input("Do you wish to switch doors? (y/n): ").lower().strip()
            
            if choice_to_switch == 'n':
                if random_prize_door == str(pick_door):
                    print(f"You won! The prize was in door {pick_door}.")
                    print("You didn't switch and you WON.")
                else:
                    for door in final_doors:
                        if pick_door == door:
                            final_doors.remove(door)
                            print(final_doors)
                            break
                    
                    print(f"Sorry, the prize was in door {door}.")
                    print("You didn't switch and you LOST.")
                break
            elif choice_to_switch == 'y':
                if random_prize_door == str(pick_door):
                    print(f"Sorry, the prize was in door {pick_door}.")
                    print("You switched and you LOST.")
                else:
                    for door in final_doors:
                        if random_prize_door == door:
                            final_doors.remove(random_prize_door) 
                            break
                    
                    print(f"You won! The prize was in door {door}.")
                    print("You switched and you WON.")
                break
            else:
                print("Pick between y or n.")
        
    except ValueError:
        print("Pick a number.")
    
if __name__ == "__main__":
    main()
