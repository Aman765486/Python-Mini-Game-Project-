# Restaurant Order System

# Define the menu with item names as keys and their prices as values
menu = {
    "Pizza": 199,
    "Burger": 149,
    "Pasta": 179,
    "Salad": 99,
    "Soda": 49,
    "Coffee": 79,
    "Dessert": 129,
    "Fries": 89,
    "Briyani": 249,
    "Cold Drink": 59,
}
menu_lower = {item.lower(): item for item in menu}

# Start of the program
print("Welcome to the Restaurant!")
print("Here is the menu\nPizza - Rs199\nBurger - Rs149\nPasta - Rs179\nSalad - Rs99\nSoda - Rs49\nCoffee - Rs79\nDessert - Rs129\nFries - Rs89\nBriyani - Rs249\nCold Drink - Rs59")

order_total = 0

# Take the first order
Item_1 = input("Enter the name of item you want to order:- ")
if Item_1 in menu:
    order_total += menu[Item_1]
    print(f"{Item_1} added to your order. Price is Rs{menu[Item_1]}")
else:
    print(f"{Item_1} is not available in the menu.")

# Ask if the user wants to order anything else
more_order = input("Do you want to order anything else? (yes/no): ")
if more_order.lower() == "yes":
    Item_2 = input("Enter the name of the item: ")
    if Item_2 in menu:
        order_total += menu[Item_2]
        print(f"{Item_2} added to your order. Price is Rs{menu[Item_2]}")
    else:
        print(f"{Item_2} is not available in the menu.")

print(f"Your total order amount is Rs {order_total}. \nThank you for dining with us!")
# End of the program

