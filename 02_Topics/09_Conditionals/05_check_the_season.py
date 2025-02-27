"""
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""

month = input("Enter a month (e.g., January, February, etc.): ").strip().lower()

if month in ["september", "october", "november"]:
    print("Autumn")
elif month in ["december", "january", "february"]:
    print("Winter")
elif month in ["march", "april", "may"]:
    print("Spring")
elif month in ["june", "july", "august"]:
    print("Summer")
else:
    print("Invalid input. Please enter a valid month.")