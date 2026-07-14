#we need to write all expenses into a csv file.
#and then read the csv file and skip the corrupt lines with a warning.
#return empty list if file missing.
from models import Expense
def save_expenses(filepath: str, expenses: list) -> None:
    try:
        with open(filepath, "w") as f:
            for expense in expenses:
                f.write(expense.to_csv_line())
            f.close()
    except ValueError:
        print("Error for save expenses")
def load_expenses(filepath: str) -> list:
    expenses = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                try:
                    expense = Expense.from_csv_line(line)
                    expenses.append(expense)
                except ValueError:
                    print("Warning: skip corrupt lines")
            f.close()
    except FileNotFoundError:
        return []
    return expenses

