import datetime

def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        if age < 0:
            print("It seems you've entered a future birth year. Please try again!")
        else:
            print(f"You are {age} years old.")
    except ValueError:
        print("Invalid input. Please enter a valid birth year.")

calculate_age()
