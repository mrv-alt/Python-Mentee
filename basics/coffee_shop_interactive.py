# The menu and prices stay the same
menu_items = ["Coffee", "Tea", "Muffin"]
prices = [3, 2, 4]
total_bill = 0

# 1. We ask the user for their name and save it in a variable!
customer_name = input("Welcome to the Python Cafe! What is your name? ")

# 2. We use their name to greet them
print("Hello " + customer_name + "!")

print("Here is what we have today:")
for item in menu_items:
    print("- " + item)

# 3. We pause again to ask them what they want to order
order = input("What would you like to order? ")

# 4. The program checks their exact input against the menu
position_of_price = -1
for i in range(len(menu_items)):
    if menu_items[i].lower() == order.lower():
        position_of_price = i
        break

if position_of_price != -1:
    total_bill = total_bill + prices[position_of_price]

print("Your total is: $" + str(total_bill))