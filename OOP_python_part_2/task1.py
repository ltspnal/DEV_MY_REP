class Product:
    def __init__(self, name, store, price):
        self.name = name
        self.store = store
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.store}): {self.price} PLN"

    def __add__(self, other):
        return self.price + other.price if isinstance(other, Product) else NotImplemented


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product_by_index(self, index):
        return self.products[index] if 0 <= index < len(self.products) else None

    def get_product_by_name(self, name):
        return next((p for p in self.products if p.name == name), None)

    def sort_products(self, key):
        self.products.sort(key=key)

    def __add__(self, other):
        return sum(p.price for p in self.products + other.products)

    def display_products(self):
        for product in self.products:
            print(product)


if __name__ == "__main__":
    warehouse1 = Warehouse()
    warehouse2 = Warehouse()

    warehouse1.add_product(Product("Ноутбук - Apple MacBook Pro 16 M4 Max 16-core CPU", "TechStore", 29249))
    warehouse1.add_product(Product("Телефон - iPhone 16 Pro Max 256 GB", "MobileShop", 6299))
    warehouse2.add_product(Product("Монитор - Monitor XIAOMI A27i 27 1920x1080px IPS 100Hz", "PCStore", 499))

    print("\nProducts:")
    warehouse1.display_products()

    print("\nSorted by price:")
    warehouse1.sort_products(lambda p: p.price)
    warehouse1.display_products()


print("\nTotal price:", warehouse1 + warehouse2)
