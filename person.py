class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def greeting(self):
		print('Hi, my name is ' + self.name + '!')
