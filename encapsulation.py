class Book():
    def __init__(self, name, pages, author):
        self.pages = pages
        self.author = author
        self.name = name
        self.__worth = 10000
        self.__color = "gold"

    def printInfo(self):
        print("This book which its name is:", self.name, "has " , self.pages, "pages", "It was written by", self.author)

    def worth(self):
        print(self.__worth)

    def worth2(self, updated):
        self.__worth = updated

    def color(self):
        print(self.__color)

    def changeColor(self, newpaint):
        self.__color = newpaint

book1 = Book("Stigma", 57, "Aguro")
book1.printInfo()
book1.worth()
book1.worth2(19000)
book1.worth()
book1.color()
book1.changeColor("blue")
book1.color()

