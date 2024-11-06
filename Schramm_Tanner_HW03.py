# Tanner Schramm
# COSC 1010
# Homerwork 7
# Lab Section 10
# 11/5/2024
# Sources, help given to, recieved: I have used Chat GPT to get my code to work and run correctly. I was unable to get my code to runa nd Chat GPT gave me the main function block to help me work the code. 

DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
DAYS_IN_MONTH_LEAP = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
def is_leap_year(year):
    """Check if the year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

def day_of_week_jan_1(year):
    """Calculate the day of the week for January 1st of a given year using the formula."""
    y = year - 1
    return (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7

def is_valid_date(month, day, year):
    """Check if the given month, day, and year represent a valid date."""
    if month < 1 or month > 12:
        return False
    if is_leap_year(year):
        days_in_month = DAYS_IN_MONTH_LEAP
    else:
        days_in_month = DAYS_IN_MONTH
    if day < 1 or day > days_in_month.get(month, 31):
        return False
    return True

def calculate_day_of_week(month, day, year):
    """Calculate the day of the week for a given date."""
    jan_1st_day = day_of_week_jan_1(year)
    days_in_month = DAYS_IN_MONTH_LEAP if is_leap_year(year) else DAYS_IN_MONTH
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month[m]
    total_days += day
    return DAYS_OF_WEEK[(jan_1st_day + total_days - 1) % 7]

def get_user_input():
    """Get the date input from the user and validate it."""
    while True:
        user_input = input("Enter a date (MM/DD/YYYY): ")
        parts = user_input.split("/")
        
        if len(parts) != 3:
            print(f"{user_input} Invalid Date")
            continue
        month, day, year = parts
        if not (month.isdigit() and day.isdigit() and year.isdigit()):
            print(f"{user_input} Invalid Date")
            continue
        
        month, day, year = int(month), int(day), int(year)
        
        if not is_valid_date(month, day, year):
            print(f"{user_input} Invalid Date")
        else:
            day_of_week = calculate_day_of_week(month, day, year)
            print(f"{user_input} {day_of_week}")
            break  
def main():
    """Main function to run the program."""
    get_user_input()

if __name__ == "__main__":
    main()
