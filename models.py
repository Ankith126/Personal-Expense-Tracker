#we need to create the class  and each expense has id,date,amount,category,description.
#after this we need to display the data as the user readable format by using __str__ method.
#converting the expense attributes into string using to_csv_line()
#next we parse the input raw data to the meaning input data by using from_csv_line() and using decorator because we are not using object data or class data.
class Expense:
    def __init__(self, id: int, date: str, amount: float, category: str, description: str):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
    def to_csv_line(self) -> str:
        return f"{self.id}, {self.date}, {self.amount}, {self.category}, {self.description}"
    @staticmethod
    def from_csv_line(line: str) -> "Expense":
        parts = line.strip().split(",")
        if len(parts) != 5:
            raise ValueError("Invalid data")
        id = int(parts[0])
        date = parts[1]
        amount = float(parts[2])
        category = parts[3]
        description = parts[4]
        return Expense(id, date, amount, category, description)
    def __str__(self) ->str:
        return f"{self.id} | {self.date} | {self.amount:.2f} | {self.category} | {self.description}"

