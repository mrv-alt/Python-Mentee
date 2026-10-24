#praticing using seperate files

#drink types
menu_items = ["Coffee", "Tea", "Matcha"]
prices = [3, 2, 4]

#milk types
milk_items = ["Oat", "2%", "Whole", "Almond", "Soy"]
milk_prices = [.50, .20, .40, .60, .70]

#food items
food_items = ["Muffin", "Bagel", "Croissant", "Scone", "Danish"]
food_prices = [4, 3, 5, 4, 6]


def ask_for_drink():
    print("Here are our drink options:")
    for item, price in zip(menu_items, prices):
        print(f"- {item}: ${price:.2f}")

    order = input("What drink would you like? ")
    if order.lower() == "nothing":
        return None

    position = next(
        (i for i, item in enumerate(menu_items) if item.lower() == order.lower()),
        -1,
    )
    if position == -1:
        print("Sorry, we don't have that drink.")
        return 0

    milk_price = 0
    order_milk = ""
    if order.lower() in ["coffee", "tea"] and ask_for_milk():
        order_milk = input("What type of milk would you like?: ")
        milk_price = add_milk_to_order(order_milk)

    if order_milk:
        print("You ordered a " + menu_items[position] + " with " + order_milk + " milk.")
    else:
        print("You ordered a " + menu_items[position] + ".")
    return prices[position] + milk_price


#asks user if they want milk and lists the types

def ask_for_milk():
    wants_milk = input("Would you like milk with your order? (yes/no) ")
    if wants_milk.lower() == "yes":
        for item, price in zip(milk_items, milk_prices):
            print(f"- {item}: ${price:.2f}")
        return True
    else:
        print("No problem!")
        return False

def add_milk_to_order(milk_type):
    position_of_price = -1
    for i in range(len(milk_items)):
        if milk_items[i].lower() == milk_type.lower():
            position_of_price = i
            break

    if position_of_price != -1:
        return milk_prices[position_of_price]
    else:
        print("Sorry, we don't have that type of milk.")
        return 0

def add_food_to_order():
    wants_food = input("Would you like to add a food item to your order? (yes/no) ")
    if wants_food.lower() == "yes":
        for item, price in zip(food_items, food_prices):
            print(f"- {item}: ${price:.2f}")
        return True
    else:
        print("No problem!")
        return False