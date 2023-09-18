# DRY: Do not Repeat Yourself
from data_manager import save_to_csv
from products import Products
from electronics import Electronics
from grocery import Grocery
from furniture import Furniture
from toys import Toys
from cloths import Cloths

while True:
    print("Enter:\n1 to add new product to inventory")
    print("2 to delete a product")
    print("3 to view a product details")
    print("4 to edit a product details")
    print("5 to view the entire inventory")

    print("9 to exit\n")
    op = int(input())
    if op == 1:
            item_type = int(input())    
            lookup = {
                1: Electronics.addNewItem,
                2: Furniture.addNewItem,
                3: Grocery.addNewItem,
                4: Cloths.addNewItem,
                5: Toys.addNewItem
            }
            new_item = lookup[item_type]()
            save_to_csv()

    elif op == 2:
        pass

    elif op == 3:
        index = Products.showInventory()
        Products.all_products[index].show_details()

    elif op == 4:
            index = Products.showInventory()
            Products.all_products[index].editDetails()
            save_to_csv()

    elif op == 5:
        pass

    elif op == 9:
        break

    else:
        print("Invalid operation, please try again...")
