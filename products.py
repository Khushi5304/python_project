import datetime
from abc import ABC, abstractmethod

class Products(ABC):
    all_products = []
    country = "India"

    def __init__(self, name: str, cost_price, mrp, quantity: int):
        assert isinstance(name, str), "Name should be a string..."
        self.name = name

        assert isinstance(cost_price, float), "Cost Price should be a Float..."
        self.__cost_price = cost_price
        assert isinstance(mrp, float) or isinstance(mrp, int), "MRP should be a Float..."
        self._mrp = mrp

        assert isinstance(quantity, int), "Quantity should be an integer."
        assert quantity > 0, "Quantity should be greater than 0!"
        self.quantity = quantity
        Products.all_products.append(self)
        self.generateBarcode()

    def generateBarcode(self):
        purchase_year = datetime.datetime.today().year
        purchase_month = datetime.datetime.today().month
        index = str(len(Products.all_products) + 100)
        self.barcode = str(purchase_year) + str(purchase_month).zfill(2) + self.category_code + index

    @staticmethod
    @abstractmethod
    def addNewItem():
        print("Enter the following details:")
        name = input("Name: ")
        cost_price = float(input("Cost Price: "))
        mrp = float(input("MRP: "))
        quantity = int(input("Quantity: "))
        return name, cost_price, mrp, quantity

    @staticmethod
    def showInventory():
        print("SrNo\t\tItem Name")
        for item in Products.all_products:
            print(f"{item.barcode}\t{item.name}")
        barcode = input("Enter barcode no: ")
        index = int(barcode[-3:]) - 101
        return index

    def editDetails(self):
        print("Enter new details (Press 'Enter' to keep old detail):")
        print("Field\tOld Value\tNew Value".expandtabs(20))
        name = input(f"Name\t{self.name}:\t".expandtabs(20))
        if name != "":
            self.name = name

        cost_price = input(f"Cost price\t{self.cost_price}:\t".expandtabs(20))
        if cost_price != "":
            self.cost_price = float(cost_price)

        mrp = input(f"MRP\t{self.mrp}:\t".expandtabs(20))
        if mrp != "":
            self.mrp = float(mrp)

        quantity = input(f"Stock\t{self.quantity}:\t".expandtabs(20))
        if quantity != "":
            self.quantity = int(quantity)

        month = input(f"Month\t{self.barcode[4 : 6]}:\t".expandtabs(20)).zfill(2)
        if month != "":
            self.barcode = self.barcode[:4] + month + self.barcode[6:]

        year = input(f"Year\t{self.barcode[:4]}:\t".expandtabs(20))
        if year != "":
            self.barcode = year + self.barcode[4:]


class Electronics(Products):
    category = "Electronics"
    category_code = "E"

    def __init__(self, name, cost_price, mrp, quantity, power_option):
        super().__init__(name, cost_price, mrp, quantity)
        self.power_option = power_option
        self.__offers = 5

    def show_details(self):
        print(f"------------- Details of {self.name} -------------")
        print("Category:", self.category)
        print("Cost price:", self._Products__cost_price)
        print("MRP:", self._mrp)
        print("Stock:", self.quantity)
        print("Barcode:", self.barcode)
        print("Power:", self.power_option)
        print("-" * 55)
        print()

    @property
    def schemes(self):
        return self._Electronics__offers

    @schemes.setter
    def schemes(self, newValue):
        self._Electronics__offers = newValue

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        power_option = input("Power option: ")
        return cls(name, cost_price, mrp, quantity, power_option)

    def editDetails(self):
        super().editDetails()
        power = input(f"Power\t{self.power_option}:\t")
        if power != "":
            self.power_option = power


class Furniture(Products):
    category = "Furniture"
    category_code = "F"

    def __init__(self, name, cost_price, mrp, quantity, material):
        super().__init__(name, cost_price, mrp, quantity)
        self.material = material

    def show_details(self):
        super().show_details()
        print("Material:", self.material)
        print("-" * 55)
        print()

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        material = input("Material: ")
        return cls(name, cost_price, mrp, quantity, material)


class Grocery(Products):
    category = "Grocery"
    category_code = "G"

    def __init__(self, name, cost_price, mrp, quantity, exp_date):
        super().__init__(name, cost_price, mrp, quantity)
        self.exp_date = exp_date

    def show_details(self):
        super().show_details()
        print("Expiry Date:", self.exp_date)
        print("-" * 55)
        print()

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        exp_date = input("Expiry date: ")
        return cls(name, cost_price, mrp, quantity, exp_date)


class Toys(Products):
    category = "Toy"
    category_code = "T"

    def __init__(self, name, cost_price, mrp, quantity, age_group):
        super().__init__(name, cost_price, mrp, quantity)
        self.age_group = age_group

    def show_details(self):
        super().show_details()
        print("Age group:", self.age_group)
        print("-" * 55)
        print()

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        age_group = input("Age group: ")
        return cls(name, cost_price, mrp, quantity, age_group)


class Cloths(Products):
    category = "Cloths"
    category_code = "C"

    def __init__(self, name, cost_price, mrp, quantity, size):
        super().__init__(name, cost_price, mrp, quantity)
        self.size = size

    def show_details(self):
        super().show_details()
        print("Size:", self.size)
        print("-" * 55)
        print()

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        size = input("Size: ")
        return cls(name, cost_price, mrp, quantity, size)

if __name__ == '__main__':
    pass
