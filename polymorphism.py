class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def printInfo(self):
        print("My name is", self.name, "and i am", self.age, "years old")


    def soundCat(self):
        print("I go meoww")


class Dog:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def printInfo2(self):
        print("My name is", self.name, "and i am", self.age, "years old")


    def soundDog(self):
        print("I go rof rof")


cat1 = Cat("Aria", 5)
cat1.printInfo()
cat1.soundCat()

dog1 = Dog("muddy", 6)
dog1.printInfo2()
dog1.soundDog()

