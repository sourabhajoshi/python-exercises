"""
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""

length = int(input("Enter a length of rtectangle :"))
width = int(input("Enter a width of rectangle : "))

area_of_rect = (length * width)
perimeter_of_rect = (2 * length * width)

print(f"Area of rectangle : {area_of_rect} and Perimeter of rectangel is : {perimeter_of_rect}")