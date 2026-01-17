# Sample Coding Questions 01 Week 01
# Anthony Huete-Jacobs

# Defining Variables
arr = [1, 4, 7, 9]

# Order of Operations
a, b, c, d = 1, 2, 3, 4

# Fully-bracketed version of:
# e = a - b ** c // d + a % c
# is:
# e = (a - ((b ** c) // d)) + (a % c)
e = (a - ((b ** c) // d)) + (a % c)

# Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))
