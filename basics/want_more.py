#asks if user wants to add more items to their order

def ask_for_more():
    wants_more = input("Want to order more? (yes/no) ")
    if wants_more.lower() == "yes":
        item_type = input("More food or drink? (food/drink) ")
        while item_type.lower() not in ["food", "drink"]:
            print("Please enter 'food' or 'drink'.")
            item_type = input("More food or drink? (food/drink) ")
        return item_type.lower()

    print("No problem! Your order is complete.")
    return None