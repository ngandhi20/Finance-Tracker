# class for transactions for sql database

class Transactions:
    """A practice transactions class"""

    def __init__(self, date, amount, category):
        self.date = date
        self.amount = amount
        self.category = category