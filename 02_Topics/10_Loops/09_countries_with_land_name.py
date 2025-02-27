"""
Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
"""

import sys

sys.path.append(r'C:\Appl\SelfLearning\Python\python-exercises\02_Topics\data')

try:
    from countries import countries

    new_country_list = []
    for country in countries:
        if "land" in country.lower():
            new_country_list.append(country)

    print(new_country_list)

    alter_country_list = [country for country in countries if "land" in country.lower()]
    print(alter_country_list)
except ImportError as e:
    print(f"Error: {e}")
