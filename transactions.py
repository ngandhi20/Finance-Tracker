# class for transactions for sql database
# this is the first showing of this class just as practice

class Transactions:
    """A practice transactions class"""

    def __init__(self, id, date, amount, category):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category