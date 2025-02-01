class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"The item {item_name} is added at price {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"The item {item_name} is deleted from {self.name}.")
        else:
            print(f"The item {item_name} isn't found in {self.name}.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"The item's price {item_name} is updated {new_price}.")
        else:
            print(f"The item {item_name} isn't found in {self.name}.")

store1 = Store("Fruit paradise", "Lenina Str, 10")
store2 = Store("Meet store", "Kirova,8")

store1.add_item("Apples", 1.2)
store1.add_item("Bananas", 0.9)

print(store1.get_price("Apples"))
store1.update_price("Apples", 1.5)
print(store1.get_price("Apples"))
store1.remove_item("Bananas")
print(store1.get_price("Bananas"))

