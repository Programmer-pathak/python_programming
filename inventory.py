#.Inventory Management System
#Create a program to manage stock of items in a company. The program should allow adding new items, updating stock, and checking availability.

def Inventory(items):
    check_item = input("Enter the item to check availability: ")
    if check_item in items:
        print(f"{check_item} is available in stock.")
        print("You want to update the stock of this item.")
        update_stock = input("yes/No:- ")

        if update_stock.lower() == "yes":
            k=items.index(check_item)
            update=input("Enter the new item to replace the old one: ")
            items[k]=update
            print(f"The item has been updated. New inventory list is:-")
            print(items)

    else:
        print(f"{check_item} is not available in stock.")
        print("you want to add that item to the inventory.")
        new_item = input("yes/No:- ")
        
        if new_item.lower() == "yes":
            items.append(check_item)
            print(f"{check_item} has been added to the inventory and new list is:- \n {items}")
    return 

item=["book","pen","notebook","eraser","pencil","marker","stapler","folder"]
Inventory(item)