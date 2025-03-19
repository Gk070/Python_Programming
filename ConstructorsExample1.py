# Paramatrized Constructors

class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("ID : ", self.id)
        print("Name : ", self.name)

emp1 = Employee(1, "John")
emp1.display()