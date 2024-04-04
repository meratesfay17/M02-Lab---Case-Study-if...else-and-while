# Author: Merhawi Gebrehiwot
# File Name: dean_honor_roll_checker.py
# Description: This Python app accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.
#              It prompts the user to enter student information until 'ZZZ' is entered as the last name to stop processing.
#              For each student, it checks if their GPA qualifies them for the Dean's List (3.5 or greater) or the Honor Roll (3.25 or greater).
def main():
    # Print welcome message and instructions
    print("Welcome to the Dean's List and Honor Roll Checker!")
    print("Enter 'ZZZ' as the last name to stop processing student records.")
    print("")

    while True:
        try:
            # Prompt for last name
            last_name = input("Enter student's last name / Enter 'ZZZ' to Exit: ")
            # Check if user wants to exit
            if last_name.upper() == 'ZZZ':
                print("Exiting program...")
                break

            # Prompt for first name
            first_name = input("Enter student's first name: ")

            # Prompt for GPA and convert it to float
            gpa = float(input("Enter student's GPA: "))

            # Check if student qualifies for Dean's List
            if gpa >= 3.5:
                print("{} {} has made the Dean's List!".format(first_name, last_name))
            # Check if student qualifies for Honor Roll
            elif gpa >= 3.25:
                print("{} {} has made the Honor Roll!".format(first_name, last_name))
            # Otherwise, student does not qualify for Dean's List or Honor Roll
            else:
                print("{} {} does not qualify for Dean's List or Honor Roll.".format(first_name, last_name))
            print("")
        except ValueError:
            print("Invalid input! Please enter a valid GPA as a number.")
            print("")

if __name__ == "__main__":
    main()
