class Groceries:
    def __init__(self) -> None:
        self.items       = dict()
        self.itemPrice   = list()
        self.time        = 0
        self.amount      = 0
        self.total_price = 0


    def addItem(self, item, amount):
        self.items[item] = amount
        self.itemPrice.append(self.getPrice(amount))  
        self.amount = len(self.itemPrice)
        self.total_price = self.getTotalPrice()
        return

    def getPrice(self, amount):
        return 5 * amount

    def getTotalPrice(self):
        return sum(self.itemPrice)


