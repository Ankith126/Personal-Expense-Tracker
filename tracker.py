#creating the main() for the outputs of all tabs
from manager import ExpenseTracker
from file_handler import save_expenses, load_expenses
from utils import validate_amount, validate_date,format_table, get_menu_choice
DATA_FILE = "data/expenses.csv"
def main() -> None:
    tracker = ExpenseTracker()

    loaded_expenses = load_expenses(DATA_FILE)
    for expense in loaded_expenses:
        tracker.add(expense.date, expense.amount, expense.category, expense.description)
        print("personal Expense Tracker")
        print("loaded expenses from file")
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Monthly Summary")
        print("5. Search")
        print("6. Delete Expense")
        print("7. Save & Quit")

        choice = get_menu_choice("Choose an option (1-7): ", ["1", "2", "3", "4", "5", "6", "7"])

        if choice == "1":
            print("Add Expense")
            date = input("Enter the date: ").strip()
            if not validate_date(date):
                print("Date must be in YYYY-MM-DD format.")
                continue
            amount_input = input("Enter the amount:").strip()
            try:
                amount = validate_amount(amount_input)
            except ValueError:
                print("Amount must be a positive number.")
                continue

            category = input("Category: ").strip()
            description = input("Description: ").strip()

            expense = tracker.add(date, amount, category, description)
            print(f"Expense #{expense.id} added.")

        elif choice == "2":
            print(" All Expenses ")
            expenses = tracker.get_all()
            if len(expenses) == 0:
                print("No expenses found.")
            else:
                print(format_table(expenses))

        elif choice == "3":
            print(" View by Category ")
            category = input("Category: ").strip()
            expenses = tracker.get_by_category(category)
            if len(expenses) == 0:
                print(f"No expenses found in category '{category}'.")
            else:
                print(format_table(expenses))
                total = 0
                for expense in expenses:
                    total += expense.amount
                    print(f"Total: {total:.2f}")

        elif choice == "4":
            print(" Monthly Summary")
            try:
                year = int(input("Year: ").strip())
                month = int(input("Month: ").strip())
            except ValueError:
                print("Year and month must be numbers.")
                continue
            summary = tracker.monthly_summary(year, month)
            if len(summary) == 0:
                print("No expenses found for this month.")
            else:
                print(f"Monthly Summary: {year}-{month:02d}")
                total = 0
                for category in summary:
                    print(f"{category}: {summary[category]:.2f}")
                    total += summary[category]
                    print(f"Total: {total:.2f}")

        elif choice == "5":
            print(" Search")
            keyword = input("Keyword: ").strip()
            expenses = tracker.search(keyword)
            if len(expenses) == 0:
                print("No matching expenses found.")
            else:
                print(format_table(expenses))

        elif choice == "6":
            print(" Delete Expense")
            try:
                expense_id = int(input("Expense ID: ").strip())
            except ValueError:
                print("Expense ID must be a number.")
                continue

            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == "yes":
                deleted = tracker.delete(expense_id)
                if deleted:
                    print(f"Expense {expense_id} deleted.")
                else:
                    print(f"No expense with ID {expense_id}.")

        elif choice == "7":
             print("Saving")
             save_expenses(DATA_FILE, tracker.get_all())
             print(f"Done. {len(tracker.get_all())} expenses saved.")
             break
main()