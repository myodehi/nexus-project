# Modeling Mest
#Mest is a school that contains Eits and Fellows

class Person:


	def __init__(self, name, nationalities):

		self.name = name
		self.country = nationalities

class Eit(Person):


	def __init__(self, name, nationalities, funfacts = True):

		super().__init__(name, nationalities)
		self.funfacts = funfacts

class Fellow(Person):

	def __init__(self, name, nationalities):
		super().__init__(name, nationalities)

	def teached(self, teach):
		self.teach = teach





eit1 = Eit('Agnes', 'kenya', True)

print(eit1.funfacts)