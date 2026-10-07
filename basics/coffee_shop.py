def welcome_customer(name):
    print("Hello " + name + "! Welcome to the Python Cafe.")

menu_items = ["Coffee", "Tea", "Muffin"]
prices = [3, 2, 4]
total_bill = 0

welcome_customer("Alex")

print("Here is what we have today:")
for item in menu_items:
    print("- " + item)

order = "Coffee"

if order in menu_items:
    print("You ordered a " + order + ".")
    total_bill = total_bill + 3
else:
    print("Sorry, we don't have that.")

print("Your total is: $" + str(total_bill))

