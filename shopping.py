groceries = [
{'name': 'Cupcake', 'price': 3.99, 'taxable': True},
{'name': 'Pretzels', 'price': 1.49, 'taxable': False},
{'name': 'Beer', 'price': 7.99, 'taxable': True},
{'name': 'Havarti', 'price': 4.99, 'taxable': False},
{'name': 'Cheddar', 'price': 3.99, 'taxable': True},
{'name': 'Triscuits', 'price': 2.00, 'taxable': False},
{'name': 'Apothic Red', 'price': 12.99, 'taxable': True},
{'name': 'Bananas', 'price': .99, 'taxable': False},
{'name': 'Lucky Charms', 'price': 2.99, 'taxable': True},
]

def get_total(groceries):
	total = 0
	for item in groceries:
		total += item['price']

	return total

class ShoppingCart(object):
	def __init__(self, name, tax_rate=.065):
		self.name = name
		self.items = []
		self.tax_rate = tax_rate

	def add_item(self, item):
		self.items.append(item)	

	def get_total(self):
		total = 0
		for item in self.items:
			total += item['price']

		tax_amount = self.get_taxable_total() * self.tax_rate	
		
		return total + tax_amount

	def get_taxable_total(self):
		taxable_total = 0
		for item in self.items:
			if item['taxable'] is True:
				taxable_total += item['price']

		return taxable_total

	def get_grand_total(self):
		grand_total = 0

# {
# 	'Item name': 'Leeks', 
# 	'Category':	 'Produce', 
# 	'Original Price': 2.50, 
# 	'Sale Price': 1.99, 
# 	'Taxable': True,
# 	'UPC': 123456789
# 	'weight': 12.5,
# }	