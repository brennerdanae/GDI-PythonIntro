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

def receipt_total(**groceries):
	for item in groceries:
		total += item['price']
	return total


