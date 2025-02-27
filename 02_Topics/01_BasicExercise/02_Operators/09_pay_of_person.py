"""
Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
"""

hours = int(input("Enter a hours : "))
rate_per_weak = int(input("Enter a rate per weak : "))

weekly_earning = hours * rate_per_weak

print("Your weekly earning is ", weekly_earning)