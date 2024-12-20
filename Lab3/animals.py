class Animal():
	def makeSound(self):
		return 'default'
	
class Dog(Animal):
	def makeSound(self):
		return 'bark'
	
class Cat(Animal):
	def makeSound(self):
		return 'meow'

def learnSkill(petName: Animal):
	return petName.makeSound()

dog = Dog()

print(learnSkill(dog))

