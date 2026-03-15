import csv
from datetime import datetime

file_name = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    note = input("Enter note: ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])

    print("Expense saved successfully!")

def view_expense():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)

            print("\nDate | Amount | Category | Note")
            print("----------------------------------")

            for row in reader:
                print(" | ".join(row))

    except:
        print("No expense records found.")

while True:

    print("\nDaily Expense Tracker")
    print("1 Add Expense")
    print("2 View Expense")
    print("3 Exit")

    choice = input("Select option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        break

    else:
        print("Invalid choice")