"""
#import all needed modules here
import unittest
from app import interpret_habit_score

#write all your tests below this line
def test_low_score():
    assert interpret_habit_score(5) == "Low"
def test_moderate_score():
    assert interpret_habit_score(11) == "Moderate"
def test_high_score():
    assert interpret_habit_score(13) == "High"

#write your test suite here, in the main() function
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")

    test_low_score()
    test_moderate_score()
    test_high_score()

    print("All tests have been finished.")
    
#please do not change the lines below
if __name__ == "__main__":
    main()
#NOT FINISHED!!!! broken test, needs to be fixed 
"""

from app import interpret_habit_score

def test_interpret_habit_score():
    assert interpret_habit_score(0) == "Low"
    assert interpret_habit_score(5) == "Low"
    assert interpret_habit_score(6) == "Moderate"
    assert interpret_habit_score(11) == "Moderate"
    assert interpret_habit_score(12) == "High"
    assert interpret_habit_score(14) == "High"

def main():
    print("Starting tests suite...")
    test_interpret_habit_score()
    print("All tests have been finished.")

if __name__ == "__main__":
    main()
