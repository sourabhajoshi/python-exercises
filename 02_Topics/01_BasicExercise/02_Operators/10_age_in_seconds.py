"""
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
"""
# Number of seconds in a day
seconds_in_a_day = 86400

# Number of days in a year (assuming 365 days per year)
days_in_a_year = 365

year = int(input("Enter number of year : "))
number_of_seconds = year * seconds_in_a_day * days_in_a_year

print(f"You have lived for {number_of_seconds} seconds.")
