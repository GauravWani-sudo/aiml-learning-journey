class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def bark(self):
        print("dog barks")

dog = Dog()

dog.sound()
dog.bark()