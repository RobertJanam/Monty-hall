import random
import time
import csv
import os

sum_reports = []

counter = 0
tester1_victory = 0
tester2_victory = 0

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_test = os.path.join(script_dir, "monty-hall_results.csv")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_report = os.path.join(script_dir, "monty-hall_report.csv")

test_header = ["Tester 1", "Tester 2"]
report_header = ["Category", "Tester 1", "Tester 2"]

def initialize_csv():
    os.makedirs(os.path.dirname(csv_file_path_test), exist_ok=True)
    
    if not os.path.exists(csv_file_path_test) or not os.path.exists(csv_file_path_report):
        with open(csv_file_path_test, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)
            
        with open(csv_file_path_report, mode='w', newline='')as csv_file:
            csv_writer = csv.writer(csv_file)

def save_to_csv():
    try:
        with open(csv_file_path_test, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(test_header)
            csv_writer.writerow([
                f"{tester1_victory} / {test_samples}",
                f"{tester2_victory} / {test_samples}"
            ])
            
            prob_tester1 = round((tester1_victory * 100) / test_samples)
            prob_tester2 = round((tester2_victory * 100) / test_samples)
            
            csv_writer.writerow([
                f"{prob_tester1}%",
                f"{prob_tester2}%"
            ])
                    
        #with open(csv_file_path_report, mode='w', newline='') as csv_file:
        #            csv_writer = csv.writer(csv_file)
        #            csv_writer.writerow(report_header)
        #            if sum_reports:
        #                for report in sum_reports:
        #                    csv_writer.writerow(report)
    except Exception as e:
        print(f"An error occurred: {e}")
    
def main():
    global counter
    global tester1_victory
    global tester2_victory
    
    while True:
        #time.sleep(0.5)
        print("==================================================================")
        counter += 1
        if counter > test_samples:
            counter = 0
            tester1_victory = 0
            tester2_victory = 0
            break
      
        doors = ["1", "2", "3"]
        prize_door_tester1 = random.choice(doors)
        prize_door_tester2 = random.choice(doors)

        """We have two testers. One always goes for yes, meaning they switch doors while
        the other always goes for no, meaning they stick to their previous choice.
        """
        
        # Door selection for both tester 1 and 2
        print("Pick a door (1, 2, 3): ")
        pick_door_tester1 = random.choice(doors)
        pick_door_tester2 = random.choice(doors)
        
        print(f"Tester 1 chose door {pick_door_tester1}")
        print(f"Tester 2 chose door {pick_door_tester2}")

        # Host reveals an empty door for tester 1
        if pick_door_tester1 == prize_door_tester1:
            temp_doors_tester1 = [door for door in doors if door != pick_door_tester1]
            random_empty_door_tester1 = random.choice(temp_doors_tester1)
        else:
            for door in doors:
                if door != prize_door_tester1 and door != pick_door_tester1:
                    random_empty_door_tester1 = door
                    break

        print(f"Door {random_empty_door_tester1} is opened and is empty.")
        
        # Host reveals an empty door for tester 2
        if pick_door_tester2 == prize_door_tester2:
            temp_doors_tester2 = [door for door in doors if door != pick_door_tester2]
            random_empty_door_tester2 = random.choice(temp_doors_tester2)
        else:
            for door in doors:
                if door != prize_door_tester2 and door != pick_door_tester2:
                    random_empty_door_tester2 = door
                    break
        
        print(f"Door {random_empty_door_tester2} is opened and is empty.")

        # Switch choice 
        print("Do you wish to switch doors? (y/n): ")

        # Evaluate outcome for the testers
        if pick_door_tester1 == prize_door_tester1:
            print("[-----Tester 1-----]")
            print(f"Sorry, the prize was in door {prize_door_tester1}.")
        else:
            print("[-----Tester 1-----]")
            print(f"You won! The prize was in door {prize_door_tester1}.")
            tester1_victory += 1
            save_to_csv()
            
        print("-----------------------------------------------")
        
        if pick_door_tester2 == prize_door_tester2:
            print("[-----Tester 2-----]")
            print(f"You won! The prize was in door {prize_door_tester2}.")
            tester2_victory += 1
            save_to_csv()

        else:
            print("[-----Tester 2-----]")
            print(f"Sorry, the prize was in door {prize_door_tester2}.")
    
if __name__ == "__main__":
    if os.path.exists(csv_file_path_test) and os.stat(csv_file_path_test).st_size > 0:
        os.remove(csv_file_path_test)
    
    while True:
        try:
            test_samples = int(input("How many test samples: "))
            if 0 <= test_samples <= 10000:
                main()
                break
            print("Pick again.")
                
        except ValueError:
            print("Enter a valid number.")