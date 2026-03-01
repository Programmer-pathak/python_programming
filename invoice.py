#.Invoice Generator
#Write a Python program to generate an invoice for a customer including item names, quantity, price, and total amount.

def invoice():
    items = {
        "Apple" : {"serial-no": 1,  "price": 10},
        "Banana": {"serial-no": 2, "price": 5},
        "Orange": {"serial-no": 3, "price": 8},
        "Grapes": {"serial-no": 4, "price": 15}  }
    
    items_purchased = input("Enter items you want to purchased ")
    correct_item_name=items_purchased.capitalize()

    for item in items.keys():
        if correct_item_name == item:
            print(f"{correct_item_name} is available in the inventory.")
            break
        else:
            print(f"{correct_item_name} is not available in the inventory.")
            return
    quantity = int(input("Enter quantity of items "))
    if correct_item_name in items:
        price = items[correct_item_name]["price"]
        total_amount = price * quantity

    name=input("Enter your name ")
    address=input("Enter your address ")
    DOP=input("Enter date of purchase ")

    print("\n \n")
    print("----- Invoice -----")
    print(f"Customer Name: {name}")
    print(f"Address: {address}")
    print(f"Date of Purchase: {DOP}")
    print(f"Item: {correct_item_name}")   
    print(f"Quantity: {quantity}")
    print(f"Serial No: {items[correct_item_name]['serial-no']}")
    print(f"Price per item: {price}")
    print(f"Total Amount: {total_amount}")

    return

invoice()