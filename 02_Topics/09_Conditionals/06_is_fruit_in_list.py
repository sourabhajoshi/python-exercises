"""
The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""

fruit = input("Enter a fruit : ").strip().lower()

fruits_list = ['banana', 'orange', 'mango', 'lemon']

if fruit in fruits_list:
    print("That fruit already exist in the list")
else:
    fruits_list.append(fruit)
    print("Updated fruit list : ", fruits_list)