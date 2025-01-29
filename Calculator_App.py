#1Task 1: Create functions for each arithmetic operation.
# Define arithmetic functions
def add(a, b):
    return a + b

def sub(c, d):
    return c - d

def multi(e, f):
    return e * f
#Task 3: Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
def div(g, h):
    if h == 0:  # Handle division by zero
        return "Division by zero is not allowed."
    return g / h
# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Ask the user what operation they want to perform
operations = input("What type of problem would you like to solve? (add, sub, multi, div): ").lower()

# Ask for numbers (using float for precision)
try:
    num_1 = float(input("What number would you like to use first: "))
    num_2 = float(input("What number would you like to use second?: "))
except ValueError:
    print("Invalid input! Please enter valid numbers.")
    exit()  # Stop the program if inputs are invalid

# Perform the selected operation
if operations == "div":
    print(div(num_1, num_2))
elif operations == "multi":
    print(multi(num_1, num_2))
elif operations == "sub":
    print(sub(num_1, num_2))
elif operations == "add":
    print(add(num_1, num_2))
else:
    print("Invalid. Please choose add, sub, multi, or div.")
