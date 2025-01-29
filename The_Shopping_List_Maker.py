#2. The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.
shopping_list = [] # This your empty list that items (values) can be stored in.
# This function allows you to added items to your list
# The input line allows users to write in there items(type).
def user_list(): #
    item = input( "What would you like to add to your shopping list?:").strip() # strip() removes spaces that a user may 
    if item: # Checks to see if the list is empty. If you are going to have an empty list there needs to be a way to check the list.
        shopping_list.append(item)#The .append allows you to add to the list. that you have empty form the items list by the user. In parentheses tell the it where the list is pulling from.
        print(f' "{item}" has been added to you list,')
    else:
        print("List cant be empty")
#Task 2: Include a function to remove items from the list.
def remove_list(): #same as the above function but intended to remove the list.
   item = input("Is there an item you would like to remove from the list?: ").strip #  Allows you to input items they would like to revome.
   if item in shopping_list:
       shopping_list.remove(item)
       print(f' "You have removed "{item}" from your list.')
   else:
      print(f"{item} is not in your current shopping list.")
#Task 3: Add a function that prints out the entire list in a formatted way.
def print_user_list():
    if shopping_list:
        print(f" Here is your shopping list: {shopping_list}")
    else:
        print(f" You dont have a shopping list.")
#Loop statment
print("")
#Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.

# NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

#he goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.