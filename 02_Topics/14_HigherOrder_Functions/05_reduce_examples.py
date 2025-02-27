import functools

list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use reduce to sum all the numbers in the numbers list.
add_list = functools.reduce(lambda a, b : a+b, list_of_nums)
print("Sum of list : ", add_list)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia'
]

concat_str = functools.reduce(lambda acc, country: acc + ", " + country, countries)
print(concat_str)