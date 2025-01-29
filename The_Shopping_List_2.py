# Task 1: Write a function that lets the user add items to a list.
shopping_list = []


def user_items():
    while True:
        item = input("Would you like to add to your shopping list? If you are done type (quit):").strip()
        if item == "quit":
            print("Your shopping list is complete.")
            print(shopping_list)
            break
        elif item: # Makes sure the list is not empty.
            shopping_list.append(item) #adds to list from users input
            print(f" You have added {item} to your shopping list.") # Task prints out list as is.
        else:
            print("There are no items added to your list.") # task if no items is listed
# Task 2: Include a function to remove items from the list.
def user_remove_item():
    item = input("What items would you like to remove?:")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"You have removed {item} form your shopping list")
    else:
        ("This item {item} is not in your shopping list.")

#Task 3: Add a function that prints out the entire list in a formatted way.
user_items()
print("Current shopping list:",shopping_list)



        
        

