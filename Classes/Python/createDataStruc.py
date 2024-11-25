# Create a program that will serve as a grocery list

# This program should ask the user to enter what they want to add to their list. 
# It should also contain an option to print the list (first printing some header, for example *** YOUR LIST ***).

# At the end you should have an option to exit the program.

        # Welcome user to the store 

        # Show the user the current store inventory 

        # Ask the user if they would like purchase an item

            # If the user wants to add items to their cart 
                # Ask the user what they would like to add to their cart 
                    # If item is sold in store and currently in stock
                        # Add to the user's cart for checkout 
                        # Reduce the amount in inventory 

                    # If item is sold in in store but not in stock 
                        # Apologize to the user letting them know it's currently not in stock

                    # If the item is not sold in the store 
                        # Apologize to the user letting them know the item isn't sold at the store 

            # Ask the user if they would like to add more items to their cart 
                # If the user wants to add more items to their cart 
                    # Ask the user what they would like to add to their cart 

            # If the user doesn't want to add more items to their cart 
                        # Show the user the items in their cart 

        # If the user doesn't want to purchase anything
            # Thank them for coming to the store 
            # End program 

# showInventory(storeInventory)
# Function that prints out the items inside the storeInventory 
def showInventory(storeInventory): 

    print("****************************************")
    print("")

    print("Our current inventory is:")
    for key, value in storeInventory.items(): 
        print(f"    - {key}: {value}")

    print("")

    print("****************************************")
    print("")

def userDecisionValidation(purchaseDecision): 
    while True:

        if purchaseDecision == 'Yes': 
            print("TEST - User wants to make a purchase")
            return True
        
        elif purchaseDecision == 'No': 
            print("TEST - User doesn't want to make a purchase")
            return False
        
        else: 
            print("Please enter Yes or No")


def purchaseItems(): 
    
    cart = []

    addItem = 'Yes'

    while addItem == 'Yes': 

        # Ask the user what item they would like to add to their cart 
        print("What item would you like to add to your cart?")
        selectedItem = input()

        # If we don't have the selected item in the store 
        if selectedItem not in storeInventory: 

            print("")

            print(f"Sorry, we don't sell {selectedItem} at the store.")
        elif storeInventory[selectedItem] == 0:

            print("")

            print(f"Sorry, we don't have {selectedItem} currently in stock.")
        elif selectedItem not in cart: 

            cart.append(selectedItem)

        else: 
            
            print("")

            print(f"You already have {selectedItem} in your cart.")

        print("")

        print("You currently have these items in your cart:")
        for item in cart: 
            print(f"    - {item}")

            # Updating the inventory to reduce the amount of items the user purchased by 1 
            storeInventory[item] -= 1 

        print("")

        print("Would you like to add another item to your cart?")
        print("Please enter Yes or No. ")
        addItem = input()

        print("")

    print("You've added the following items to your cart:")
    for item in cart: 
        print(f"    - {item}")

    print("Please proceed to the register for payment.")

    print("")


# Inventory 
storeInventory = {
    "Apples" : 10 ,
    "Oil" : 8 ,
    "Chicken": 25 ,
    "Cereal" : 0 ,
    "Soda" : 3 , 
    "Juice" : 5 ,
    "Avocado" : 1
} 

purchaseDecision = 'Yes'

print("")
print("****************************************")

# Welcome message
print("Welcome to the Python Deli Grocery Store!")

print("****************************************")


# Ask if user wants to make a purchase
print("Would you like to make a purchase today?")
print("Please enter Yes or No")
purchaseDecision = input()

# Validate the users input for userDecision 
userDecisionValidation(purchaseDecision) 

while purchaseDecision == 'Yes': 

    # Print inventory list
    showInventory(storeInventory)

    # User buys items 
    purchaseItems()

    # Ask user if they want to make another purchase
    print("Would you like to make another purchase?")
    print("Please enter Yes or No")
    purchaseDecision = input()

    userDecisionValidation(purchaseDecision)

    print("")

print("")

# Thank user for coming to the store 
print("Thank you for coming to the store!")

print("")