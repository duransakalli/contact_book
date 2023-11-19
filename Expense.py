# Expense Tracker Application

def add_expense(expenses):
    amount = float(input("Enter the amount of expense: $"))
    category = input("Enter the category: ")
    expense = {"amount": amount, "category": category}
    expenses.append(expense)
    print("Expense added \n")


def view_expenses(expenses):
    print("Expenses: ")
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}")
    print()


def add_income(incomes):
    amount = float(input("Enter the amount of income: $"))
    category = input("Enter the category: ")
    income = {"amount": amount, "category": category}
    incomes.append(income)
    print("Income added \n")


def view_incomes(incomes):
    print("Incomes: ")
    for income in incomes:
        print(f"Category: {income['category']}, Amount: {income['amount']}")
    print()


def view_balance(expenses, incomes):
    total_expenses = sum(item['amount'] for item in expenses)
    total_income = sum(item['amount'] for item in incomes)
    balance = total_income - total_expenses
    print(f"Total income: ${total_income}, Total expenses: ${total_expenses}")
    print(f"Total Balance: ${balance} \n")


def main():
    expenses = []
    incomes = []

    while True:
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expenses")
        print("4. View Incomes")
        print("5. View Balance")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            add_income(incomes)
        elif choice == '3':
            view_expenses(expenses)
        elif choice == '4':
            view_incomes(incomes)
        elif choice == '5':
            view_balance(expenses, incomes)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
