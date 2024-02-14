# class person
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"{self.name} has deposit: {self.deposit} and loan: {self.loan}"


# House
class House:
    def __init__(self, ID, price, owner=None, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status
