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

    def sell_house(self, buyer, loan_amount=None):
        if loan_amount is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდულია"
            print(f"სახლი N{self.ID} {self.status} {buyer.name}-ზე.")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდულია სესხით"
            buyer.loan += loan_amount
            print(f"სახლი N{self.ID} {self.status} {buyer.name}-ზე. {buyer.name} აქს სესხი {loan_amount} ლარი")


# buy house without loan
# Person
person1 = Person("Giorgi")
person2 = Person("Oto")
print(person1)
print(person2)

house1 = House("001", 10000, owner=person1)

print("House status:", house1.status)
print("House owner:", house1.owner.name)

# sell house
house1.sell_house(person2)

# print status
print("House status:", house1.status)
print("House owner:", house1.owner.name)
print(person1)
print(person2)


# buy house with loan and buyer has deposit and loan
# Person
person3 = Person("Irakli")
person4 = Person("Tamo", 27000, 5000)
print(person3)
print(person4)

house2 = House("002", 15000, owner=person3)

print("House status:", house2.status)
print("House owner:", house2.owner.name)

# sell house_2
house1.sell_house(person4, 15000)

# print status
print("House status:", house2.status)
print("House owner:", house2.owner.name)
print(person3)
print(person4)
