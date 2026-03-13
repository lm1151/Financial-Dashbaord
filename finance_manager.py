# This module handles the processing and summarizing of transactions

import pandas as pd
from transaction import Transaction

class FinanceManager:
    def __init__(self):
        self.transactions = []

    # Load transactions from a CSV and store as Transaction objects
    def load_csv(self, file_path):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            txn = Transaction(row['Date'], row['Description'], row['Category'], row['Amount'])
            self.transactions.append(txn)

    # Calculate total income, total expenses, and balance
    def get_summary(self):
        income = sum(txn.amount for txn in self.transactions if txn.amount > 0)
        expense = sum(txn.amount for txn in self.transactions if txn.amount < 0)
        balance = income + expense  # expense is negative, so this gives net
        return income, expense, balance
