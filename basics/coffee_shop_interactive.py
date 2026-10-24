import menu
import want_more


#tracks total bill for the customer's order
total_bill = 0

# 1. We ask the user for their name and save it in a variable!
customer_name = input("Welcome to the Python Cafe! What is your name? ")

# 2. We use their name to greet them
print("Hello " + customer_name + "!")

# 3. We pause again to ask them what they want to order
drink_price = menu.ask_for_drink()
if drink_price is None:
    print("No problem! Have a great day!")
    exit()

#3.2. Ask if they want food and list the types
food_price = 0
if menu.add_food_to_order():
    order_food = input("What food item would you like?: ")
    position_of_food_price = -1
    for i in range(len(menu.food_items)):
        if menu.food_items[i].lower() == order_food.lower():
            position_of_food_price = i
            break

    if position_of_food_price != -1:
        food_price = menu.food_prices[position_of_food_price]
        print("You ordered a " + order_food + ".")
    else:
        print("Sorry, we don't have that food item.")

# 4. We add the prices of the drink and food to the total bill
total_bill += drink_price + food_price

while True:
    item_type = want_more.ask_for_more()
    if item_type is None:
        break

    if item_type == "food":
        print("Here are our food options:")
        for item, price in zip(menu.food_items, menu.food_prices):
            print(f"- {item}: ${price:.2f}")

        order_food = input("What food item would you like? ")
        if order_food.lower() in [item.lower() for item in menu.food_items]:
            position = next(
                i for i, item in enumerate(menu.food_items)
                if item.lower() == order_food.lower()
            )
            total_bill += menu.food_prices[position]
            print("You ordered a " + menu.food_items[position] + ".")
        else:
            print("Sorry, we don't have that food item.")
    else:
        drink_price = menu.ask_for_drink()
        if drink_price is None:
            print("No problem! Have a great day!")
            break
        total_bill += drink_price

#prints total bill to the customer
print("Your total is: $" + str(total_bill))
