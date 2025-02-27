"""
Calculate the slope, x-intercept and y-intercept of y = 2x -2
"""

# Define the equation parameters
slope = 2
intercept = -2

# Slope
print("Slope (m):", slope)

# X-intercept (set y = 0 and solve for x)
x_intercept = -intercept / slope
print("X-intercept:", (x_intercept, 0))

# Y-intercept (set x = 0 and solve for y)
y_intercept = intercept
print("Y-intercept:", (0, y_intercept))
