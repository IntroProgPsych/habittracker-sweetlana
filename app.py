#import all the modules you need, below this line
"""
If I am not mistaken, the module is an external file that helps the program run.
My code is written without use of any modules.
Even though some of the functions from here could be indeed collected in 1 file.
"""

#write any functions you need, below this line

def interpret_habit_score(total):
    if total >= 12:
        return "High"
    elif 6 <= total <= 11:
        return "Moderate"
    else:
        return "Low"

def get_valid_input (question_text):
    while True:
        try:
            value = int(input(question_text))

            if value < 0 or value > 7:
                print("Error: please enter a number from 0 to 7")
            else:
                return value 
            
        except ValueError:
            print("Error: please enter a valid number")


#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")
    
    questions = [

        {"text":"How many days per week do you go to bed at a consistent hour? ", "habit": "SleepRoutine"},
        {"text":"How many days per week do you sleep for 8 hours? ", "habit": "SleepRoutine"},
        {"text":"How many days per week do you get up right after you heard the alarm? ", "habit": "SleepRoutine"},
       
        {"text":"How many days per week do you exercise? ", "habit": "PhysicalActivity"},
        {"text":"How many days per week do you go for a walk? ", "habit": "PhysicalActivity"},
        {"text":"How many days per week do you exercise with weights? ", "habit": "PhysicalActivity"},
       
        {"text":"How many days per week do you eat at least one healthy meal? ", "habit": "HealthyEating"},
        {"text":"How many days per week do you eat vegetables? ", "habit": "HealthyEating"},
        {"text":"How many days per week do you eat fruits? ", "habit": "HealthyEating"},
       
        {"text":"How many days per week do you practice mindfulness or relaxation? ", "habit": "Mindfulness"},
        {"text":"How many days per week do you analyze your behavior? ", "habit": "Mindfulness"},
        {"text":"How many days per week do you journaling? ", "habit": "Mindfulness"},
       
        {"text":"How many days per week do you meet with your friends? ", "habit": "SocialConnection"},
        {"text":"How many days per week do you talk to your family? ", "habit": "SocialConnection"},
        {"text":"How many days per week do you go on public places to socialize? ", "habit": "SocialConnection"},

    ]
    
    
    totals = {

     "SleepRoutine" : 0,   
     "PhysicalActivity" : 0,
     "HealthyEating" : 0,
     "Mindfulness" : 0,
     "SocialConnection" : 0 
    }
    
    for question in questions:
        answer = get_valid_input(question["text"])
        habit_type = question["habit"]
        totals[habit_type] += answer
        
    print("\nWeekly habit summary: ")

    for habit in totals:
        total = totals[habit]
        label = interpret_habit_score(total)
        print(f"{habit}: Score {total} -> {label}")

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()
