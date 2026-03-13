# This module creates a bar chart showing expense totals by category

import matplotlib.pyplot as plt
from collections import defaultdict

# Plot a bar chart of expense totals grouped by category
def plot_expense_by_category(transactions):
    category_totals = defaultdict(float)

    # Group expenses by category
    for txn in transactions:
        if txn.amount < 0:  # Only count expenses
            category_totals[txn.category] += abs(txn.amount)

    # Prepare data for plotting
    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    # Generate bar chart
    plt.bar(categories, totals)
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
