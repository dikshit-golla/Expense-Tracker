import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# -------------------------------
# Initialize CSV file
# -------------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

  
# -------------------------------
# Add Expense
# -------------------------------
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Bills/etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")


# -------------------------------
# Read Expenses
# -------------------------------
def read_expenses():
    expenses = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)
    return expenses


# -------------------------------
# Monthly Summary
# -------------------------------
def monthly_summary():
    expenses = read_expenses()
    month = input("Enter month (YYYY-MM): ")

    total = 0
    category_data = {}

    for exp in expenses:
        if exp["Date"].startswith(month):
            amount = exp["Amount"]
            category = exp["Category"]

            total += amount
            category_data[category] = category_data.get(category, 0) + amount


    print(f"\n Total expense for {month}: ₹{total}\n")


    print("Category-wise Breakdown:")
    for cat, amt in category_data.items():
        print(f"{cat}: ₹{amt}")


    if category_data:
        plt.pie(category_data.values(), labels=category_data.keys(), autopct='%1.1f%%')
        plt.title(f"Expense Distribution for {month}")
        plt.show()
    else:
        print("No expenses found for this month.\n")


# -------------------------------
# Category-wise Breakdown
# -------------------------------
def category_breakdown():
    expenses = read_expenses()

    category_data = {}

    for exp in expenses:
        category = exp["Category"]
        category_data[category] = category_data.get(category, 0) + exp["Amount"]

    print("\n Category-wise Spending:")
    for cat, amt in category_data.items():
        print(f"{cat}: ₹{amt}")

    plt.pie(category_data.values(), labels=category_data.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()


# -------------------------------
# Highest Spending Category
# -------------------------------
def highest_spending_category():
    expenses = read_expenses()

    category_data = {}

    for exp in expenses:
        category = exp["Category"]
        category_data[category] = category_data.get(category, 0) + exp["Amount"]

    if category_data:
        max_category = max(category_data, key=category_data.get)
        print(f"\n Highest spending category: {max_category} (₹{category_data[max_category]})\n")
    else:
        print("No data available.\n")


# -------------------------------
# Main Menu
# -------------------------------
def main():
    initialize_file()

    while True:
        print("====== Smart Expense Tracker ======")
        print("1. Add Expense")
        print("2. Monthly Summary")
        print("3. Category Breakdown")
        print("4. Highest Spending Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            monthly_summary()
        elif choice == '3':
            category_breakdown()
        elif choice == '4':
            highest_spending_category()
        elif choice == '5':
            print("Thank you for using Smart Expense Tracker! Looking forward to serving you again!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()