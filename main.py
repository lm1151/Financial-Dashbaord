# This script coordinates the entire workflow of the personal finance dashboard

from finance_manager import FinanceManager
import visualizer

# Export the financial summary to a text file
def export_summary(income, expense, balance):
    with open("summary.txt", "w") as f:
        f.write("Personal Finance Summary\n")
        f.write("------------------------\n")
        f.write(f"Total Income: ${income:.2f}\n")
        f.write(f"Total Expenses: ${abs(expense):.2f}\n")
        f.write(f"Net Balance: ${balance:.2f}\n")

# Display warnings if spending exceeds certain category thresholds
def check_budget_warnings(transactions):
    from collections import defaultdict
    category_totals = defaultdict(float)

    for txn in transactions:
        if txn.amount < 0:  # only count expenses
            category_totals[txn.category] += abs(txn.amount)

    # Threshold warnings
    if category_totals["Food"] > 200:
        print("⚠️ Warning: You've spent over $200 on Food.")
    if category_totals["Entertainment"] > 100:
        print("⚠️ Warning: Entertainment expenses are high this month.")

# Main function that runs the entire program
def main():
    manager = FinanceManager()
    manager.load_csv('transactions.csv')  # Load transaction data

    income, expense, balance = manager.get_summary()  # Get calculated summary
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${abs(expense):.2f}")
    print(f"Net Balance: ${balance:.2f}")

    visualizer.plot_expense_by_category(manager.transactions)  # Show bar chart
    check_budget_warnings(manager.transactions)               # Check for overspending
    export_summary(income, expense, balance)                 # Save summary to file
    print("Summary exported to summary.txt")

if __name__ == "__main__":
    main()
