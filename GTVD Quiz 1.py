"""
Your first task is to create a function that returns your profile information
it should include name, age, birthday, amount of siblings, late (true/false), height in metres (an estimate is okay)
"""


def Student_Info():
    # complete code here then try running the program.

    return name, age, birthday, siblings, late, height


# Don't touch below this line
def Run_Checks(name, age, bday, siblings, late, height):
    score = 0
    if isinstance(name, str):
        print("name passed")
        score += 1
    else:
        print("Error: name wasn't a string.")
    if isinstance(age, int):
        print("age passed")
        score += 1
    else:
        print("Error: age wasn't an int.")
    if isinstance(bday, str):
        print("bday passed")
        score += 1
    else:
        print("Error: bday wasn't a string")
    if isinstance(siblings, int):
        print("siblings passed")
        score += 1
    else:
        print("Error")
    if isinstance(late, bool):
        print("late passed")
        score += 1
    else:
        print("Error: late wasn't a bool")
    if isinstance(height, float):
        print("height passed")
        score += 1
    else:
        print("Error: height wasn't a float")
    if score == 6:
        print(f"\nCongratulations a perfect score {score}/6\n")
    else:
        print(f"You scored {score}/6 check your code and try again.")


try:
    answers = Student_Info()
except Exception as e:
    print(e)

try:
    Run_Checks(answers[0], answers[1], answers[2], answers[3], answers[4], answers[5])
except Exception as e:
    print(e)
