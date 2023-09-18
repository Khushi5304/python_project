from data_manager import save_to_csv
from products import Electronics, Furniture, Grocery, Toys, Cloths, Products

def main():
    while True:
        print("Enter:")
        print("1 to add a new product to inventory")
        print("2 to delete a product")
        print("3 to view a product details")
        print("4 to edit a product details")
        print("5 to view the entire inventory")
        print("9 to exit")

        op = int(input())

        if op == 1:
            # Option 1: Add a new product to inventory
            item_type = int(input())
            lookup = {
                1: Electronics.addNewItem,
                2: Furniture.addNewItem,
                3: Grocery.addNewItem,
                4: Cloths.addNewItem,
                5: Toys.addNewItem
            }
            lookup[item_type]()

            # Save data to CSV file after adding a product
            save_to_csv()

        elif op == 2:
            # Option 2: Delete a product
            index = Products.showInventory()
            deleted_product = Products.all_products.pop(index)
            print(f"Deleted product: {deleted_product.name}")

            # Save data to CSV file after deleting a product
            save_to_csv()

        elif op == 3:
            # Option 3: View a product details
            index = Products.showInventory()
            Products.all_products[index].show_details()

        elif op == 4:
            # Option 4: Edit a product details
            index = Products.showInventory()
            Products.all_products[index].editDetails()

            # Save data to CSV file after editing a product
            save_to_csv()

        elif op == 5:
            # Option 5: View the entire inventory
            for product in Products.all_products:
                product.show_details()
        
        elif op == 9:
            break

        else:
            print("Invalid operation, please try again...")

if __name__ == '__main__':
    main()
