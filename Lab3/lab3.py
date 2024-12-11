class Order:
	ordersQty = 0

	def __init__(self):
		self.items = {}
		Order.ordersQty += 1
	
	def addItem(self, item, price):
		if price <= 0:
			raise ValueError("Enter valid price (it should be higher than 0)")
		
		self.items[item] = price
		return self.items
	
	def removeItem(self, item):
		if item not in self.items:
			raise KeyError(f"There is no item with name as {item}")

		confirmation = input("Do you really wanna remove this item? (yes/no)").strip().lower()

		if confirmation == 'yes': 
			del self.items[item]
		else: 
			print('Deletion was cancelled')
		
		return self.items

	def getTotal(self):
		return sum(self.items.values())
	

if __name__ == "__main__":
    order1 = Order()

    print("Adding items:")
    print(order1.addItem("Apple", 50))
    print(order1.addItem("Milk", 100))

    print("Deleting Items:")
    print(order1.removeItem("Apple"))

    print("Overall price:")
    print(order1.getTotal())

    print("Orders qty:")
    print(Order.ordersQty)

