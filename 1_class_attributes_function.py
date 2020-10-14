class Person:
    # этот метод будет вызван после создания экземпляра класса
    def __init__(self, name):
        self.name = name 

    def display(self):
        print(self.name)
