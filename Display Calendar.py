import calendar

def display_calendar(year, month):
    # Display the calendar
    cal = calendar.month(year, month)
    return cal

# Example usage:
try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    if 1 <= month <= 12:
        print(f"\nCalendar for {calendar.month_name[month]} {year}:")
        print(display_calendar(year, month))
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
except ValueError:
    print("Please enter valid integers.")
