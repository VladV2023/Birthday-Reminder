import datetime
from datetime import datetime

# Dictionary with names as keys and birthdates as values
b_dates = {
    "Rena": "01-01",
    "Aure": "08-08",
    "Astic": "08-20",
    "Darkz": "08-15",
    "Iori": "08-29",
    "Floofie": "08-02",
}

# Date format to use
date_format = "%m-%d"
today = datetime.now().date()

# List to hold the names of people who have birthdays today
birthday_names = []

for name, date_str in b_dates.items():
    # Convert the date string to a datetime object, but without the year
    date_obj = datetime.strptime(date_str, date_format).date()
    
    # Compare month and day only, ignore the year
    if date_obj.month == today.month and date_obj.day == today.day:
        birthday_names.append(name)

# Print the names of people who have birthdays today
if birthday_names:
    for name in birthday_names:
        print(f"ATTENTION!!! TODAY IS {name}'s BIRTHDAY!!! GO CONGRATULATE THEM!!!")
else:
    print("There are no birthdays today")

# Pause to keep the window open
input("Press Enter to exit...")
