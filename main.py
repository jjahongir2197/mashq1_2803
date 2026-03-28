class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name} | {self.price}"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_cart(self):
        for i, item in enumerate(self.items):
            print(i+1, item.info())
        print("Total:", self.total_price())


class Shop:
    def __init__(self):
        self.products = []
        self.cart = Cart()

    def add_product(self, name, price):
        self.products.append(Product(name, price))

    def show_products(self):
        for i, p in enumerate(self.products):
            print(i+1, p.info())

    def add_to_cart(self, index):
        if 0 <= index < len(self.products):
            self.cart.add_product(self.products[index])


def run():
    shop = Shop()

    shop.add_product("Phone", 3000000)
    shop.add_product("Laptop", 7000000)
    shop.add_product("Mouse", 150000)

    while True:
        print("\n1 Products")
        print("2 Add to Cart")
        print("3 Show Cart")
        print("4 Exit")

        c = input()

        if c == "1":
            shop.show_products()

        elif c == "2":
            shop.show_products()
            i = int(input("Product: ")) - 1
            shop.add_to_cart(i)

        elif c == "3":
            shop.cart.show_cart()

        else:
            break


run()
