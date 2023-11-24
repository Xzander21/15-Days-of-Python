# PART 2: READING DIFFERENT TYPES OF INPUT

# Use the input() function to get input from the user
name = input("Enter your name: ")

# Reading a character (first character of the entered string)
middle_initial = input("Enter your middle name: ")[0]

# Use int() to convert the input to an integer
age = int(input("Enter your age: "))

# Use float() to convert the input to a float
height = float(input("Enter your height in meters: "))

# Reading a boolean (using lower() to handle case-insensitive input) and check if the lowercase user input is equal to "yes"
is_cloudArchitect = input("Are you a member of the AWS Cloud Club - Department of Cloud Computing? (yes/no): ").lower() == "yes"







