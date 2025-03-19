class Fruit:

    def __init__(self, name):
        self.name = name

    def setFruitName(self, name):
        self.name = name
    
    def getFruitName(self):
        return self.name

f1 = Fruit("Grapes")
print("Fruit Name is : ", f1.getFruitName())

f1.setFruitName("Apple")
print("Fruit Name is : ", f1.getFruitName())