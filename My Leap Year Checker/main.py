print("Welcome To My Leap Year Checker")
# Year entry
try:
    year = int(input("Please enter year: "))
except ValueError:
    print("invalid value, please enter a number")
# verification
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False 
        else:
            return True
    else:
        return False

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")