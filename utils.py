#we need to convert the amount from string to float.
#we need to validate the date in the format and also checking or validating the month ad day
#we need to convert list of expenses into formatted table string.
#also checking the menu choice by using while loop because we do not know the users choice.
def validate_date(date_str: str) -> bool:
    parts = date_str.split("-")
    if len(parts) != 3:
        return False
    year = parts[0]
    month = parts[1]
    day = parts[2]
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    month_num = int(month)
    day_num = int(day)
    if month_num < 1 or month_num > 12:
        return False
    if day_num < 1 or day_num > 31:
        return False
    return True

def validate_amount(amount_str: str) -> float:
    amount = float(amount_str)
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return amount
def format_table(expenses: list) -> str:
    result = ""
    result += "ID | Date | Amount| Category | Description"
    result += "-" * 60
    for expense in expenses:
        result += str(expense)
    return result
def get_menu_choice(prompt: str, valid_choices: list) -> str:
    while True:
        choice = input("Enter the prompt:").strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice")
