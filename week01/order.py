
class Order:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display(self):
        print("Order:" + self.name + " amount:" + str(self.amount))

    def add_amount(self, amount: int) -> None:
        if amount < 0:
            return
        self.amount += amount


orders = []
orders.append(Order("john", 24.7))
orders.append(Order("mary", 12.3))

for order in orders:
    order.display()

x = 98347598345734985795837598437543985798759483754398573495347593457439853475
print(x)




