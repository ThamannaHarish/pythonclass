# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):  
        print("The dog barks.")

# Child class
class Cat(Animal):
    def speak(self): 
        print("The cat meows.")


animal = Animal()
dog = Dog()
cat = Cat()


animal.speak()  
dog.speak()     
cat.speak()     
