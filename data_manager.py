import csv
from products import Products, Electronics, Furniture, Grocery, Toys, Cloths

def save_to_csv():
    with open('inventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Cost Price', 'MRP', 'Quantity', 'Barcode', 'Category', 'Additional Info'])

        for product in Products.all_products:
            if isinstance(product, Electronics):
                category = 'Electronics'
                additional_info = product.power_option
            elif isinstance(product, Furniture):
                category = 'Furniture'
                additional_info = product.material
            elif isinstance(product, Grocery):
                category = 'Grocery'
                additional_info = product.exp_date
            elif isinstance(product, Toys):
                category = 'Toys'
                additional_info = product.age_group
            elif isinstance(product, Cloths):
                category = 'Cloths'
                additional_info = product.size
            else:
                category = 'Unknown'
                additional_info = 'N/A'

            writer.writerow([product.name, product._Products__cost_price, product._mrp, product.quantity, product.barcode, category, additional_info])
