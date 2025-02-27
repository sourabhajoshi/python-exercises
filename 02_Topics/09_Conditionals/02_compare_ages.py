"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
"""

my_age = 30
your_age = int(input("Enter your age : "))

if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print(f"You are {age_diff} year younger than me.")
    else:
        print(f"You are {age_diff} years younger than me.")

elif my_age < your_age:
    age_diff =  abs(my_age - your_age)
    if age_diff == 1:
        print(f"You are {age_diff} year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")

else:
    print("We are same age")