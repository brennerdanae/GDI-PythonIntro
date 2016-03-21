groceries = [
{'name': 'Cupcake', 'price': 3.99},
{'name': 'Pretzels', 'price': 1.49},
{'name': 'Beer', 'price': 7.99},
{'name': 'Havarti', 'price': 4.99},
{'name': 'Cheddar', 'price': 3.99},
{'name': 'Triscuits', 'price': 2.00},
{'name': 'Apothic Red', 'price': 12.99},
{'name': 'Bananas', 'price': .99},
{'name': 'Lucky Charms', 'price': 2.99}
]

def receipt_total(groceries):
	total = 0
	for item in groceries:
		total += item['price']

	return total

class ShoppingCart(object):
	def __init__(self, customer_name):
		self.customer_name = customer_name
		self.items = []

	def add_item(self, item):
		self.item.append(item)	

	def receipt_total(self, groceries):
		total = 0
		for item in groceries:
			total += item['price']
		return total	

# {
# 	'Item name': 'Leeks', 
# 	'Category':	 'Produce', 
# 	'Original Price': 2.50, 
# 	'Sale Price': 1.99, 
# 	'Taxable': True,
# 	'UPC': 123456789
# 	'weight': 12.5,
# }	


