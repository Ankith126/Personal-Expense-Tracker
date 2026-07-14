#create Expense Tracker
#it can store the expenses internally
#we can add or delte the expense and also we need to search for the expense
#we need to generate the summaries for the expense
from models import Expense
class ExpenseTracker:
    def __init__(self):
        self.expenses: list = []
        self.next_id: int = 1
    def add(self, date: str, amount: float, category: str, description: str) -> Expense:
        expense = Expense(self.next_id, date, amount, category, description )
        self.expenses.append(expense)
        self.next_id += 1
        return expense
    def delete(self, expense_id: int) -> bool:
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                return True
            return False
    def get_all(self) -> list:
        return self.expenses
    def get_by_category(self, category: str) -> list:
        matched_expenses = []
        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                matched_expenses.append(expense)
        return matched_expenses
    def search(self, keyword: str) -> list:
        matched_expenses = filter(lambda expense: keyword.lower() in expense.description.lower(), self.expenses)
        return list(matched_expenses)
    def monthly_summary(self, year: int, month: int) -> dict:
        summary = {}
        for expense in self.expenses:
            parts = expense.date.split("-")
            expense_year = int(parts[0])
            expense_month = int(parts[1])
            if expense_year == year and expense_month == month:
                if expense.category not in summary:
                    summary[expense] = 0
                summary[expense.category] += expense.amount
        return summary
