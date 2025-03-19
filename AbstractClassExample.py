from abc import ABC, abstractclassmethod

class AbstractDemo1(ABC):
    @abstractclassmethod
    def display(self):
        pass

class AbstractDemo2(AbstractDemo1):

    def display(self):
        print("Abstract Demo 2 () display ")

obj = AbstractDemo2()
obj.display()