"""
In this scenario, we are building an e-commerce system where products can be classified as Physical or Digital products. Both types of products share some common attributes (like name, price, and product_id), but each type also has its own unique properties.

We will create a base class Product to hold common attributes and methods, and then create two derived classes: PhysicalProduct and DigitalProduct. Finally, we'll create a class SpecialProduct that inherits from both PhysicalProduct and DigitalProduct, demonstrating multiple inheritance.
"""

# Base class : Product
class Product:
    """ Base class """
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Product ID: {self.product_id}")

# Derived class : inherit from Product
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, weight, shipping_cost):
        super().__init__(product_id, name, price)
        self.weight = weight
        self.shipping_cost = shipping_cost

    def display_product_info(self):
        super().display_product_info()
        print(f"Weight: {self.weight}kg")
        print(f"Shipping Cost: ${self.shipping_cost}")

    def calculate_shipping(self):
        print(f"Shipping Cost for {self.name}: ${self.shipping_cost}")

# Derived class : inherit from Product
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, download_size, download_link):
        super().__init__(product_id, name, price)
        self.download_size = download_size
        self.download_link = download_link

    def display_product_info(self):
        super().display_product_info()
        print(f"Download Size: {self.download_size}MB")
        print(f"Download Link: {self.download_link}")

    def provide_download_link(self):
        print(f"Download Link for {self.name}: {self.download_link}")
    
# Derived class: SpecialProduct (inherits from both PhysicalProduct and DigitalProduct)
class SpecialProduct(PhysicalProduct, DigitalProduct):
    def __init__(self, product_id, name, price, weight, shipping_cost, download_size, download_link, special_offer):
        PhysicalProduct.__init__(product_id, name, price, weight, shipping_cost)
        DigitalProduct.__init__(product_id, name, price, download_size, download_link)
        self.special_offer = special_offer

    def display_product_info(self):
        print(f"Special Offer: {self.special_offer}")
        PhysicalProduct.display_product_info(self)
        DigitalProduct.display_product_info(self)

    def apply_special_offer(self):
        print(f"Applying special offer: {self.special_offer} to {self.name}")
        self.price = self.price * 0.9  # 10% discount for the special offer
        print(f"New price after offer: ${self.price}")


# Create objects of each product type
physical_product = PhysicalProduct("Laptop", 1000, "P123", 2.5, 50)
digital_product = DigitalProduct("E-book", 30, "D456", 5, "http://downloadlink.com")
special_product = SpecialProduct("Smartphone with E-book", 800, "SP789", 0.5, 15, 50, "http://downloadlink.com", "10% Off")

# Display details and apply special offer
print("\nPhysical Product Details:")
physical_product.display_product_info()
physical_product.calculate_shipping()

print("\nDigital Product Details:")
digital_product.display_product_info()
digital_product.provide_download_link()

print("\nSpecial Product Details (Physical + Digital):")
special_product.display_product_info()
special_product.apply_special_offer()




