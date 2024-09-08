import csv
from datetime import datetime

# File to store expenses
FILE_NAME = 'expenses.csv'


# Function to add a new expense
def add_expense(amount, category, description=''):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description, datetime.now().strftime('%Y-%m-%d')])


# Function to read and display all expenses
def show_expenses():
    try:
        with open(FILE_NAME, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f'Amount: {row[0]}, Category: {row[1]}, Description: {row[2]}, Date: {row[3]}')
    except FileNotFoundError:
        print("No expenses recorded yet!")


# Function to show total expenses by category
def summary_by_category():
    expenses_by_category = {}
    try:
        with open(FILE_NAME, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[0])
                if category in expenses_by_category:
                    expenses_by_category[category] += amount
                else:
                    expenses_by_category[category] = amount
    except FileNotFoundError:
        print("No expenses recorded yet!")

    print("Expenses by category:")
    for category, total in expenses_by_category.items():
        print(f'{category}: ${total:.2f}')


# Main Menu
def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add new expense")
        print("2. Show all expenses")
        print("3. Show summary by category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            add_expense(amount, category, description)
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()