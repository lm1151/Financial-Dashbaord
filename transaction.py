# This file defines a Transaction class used to model each financial entry

class Transaction:
    # Initializes the transaction with its details
    def __init__(self, date, description, category, amount):
        self.date = date
        self.description = description
        self.category = category
        self.amount = float(amount)  # Convert string to float for calculations
