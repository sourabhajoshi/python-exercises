"""
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

for i in range(0, 9):
    for j in range(0, 9):
        print("#", end=" ")
    print()