# 💸 Smart Expense Tracker with Insights

A Python-based CLI application that helps users track daily expenses, categorize spending, and gain meaningful financial insights through summaries and visualizations.

---

## 📌 Features

* Add daily expenses (date, category, amount, description)
* Store data using CSV file
* Monthly expense summary
* Category-wise breakdown (for selected month)
* Pie chart visualization using matplotlib
* Identify highest spending category
* Simple CLI interface

---

## 🛠️ Tech Stack

* Python 3
* CSV (data storage)
* Matplotlib (visualization)

---

## 📁 Project Structure

Smart-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── README.md

---

## ⚙️ Setup & Execution (Virtual Environment)

### 1. Clone Repository

git clone <your-repo-link>
cd Smart-Expense-Tracker

---

### 2. Create Virtual Environment

python -m venv venv

---

### 3. Activate Virtual Environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 4. Install Dependencies

pip install matplotlib

---

### 5. Run Application

python expense_tracker.py

---

## 🧠 How It Works

### Expense Entry

User enters:

* Date (YYYY-MM-DD)
* Category (Food, Travel, Bills, etc.)
* Amount
* Description

Data is stored in expenses.csv.

---

### Monthly Summary

* Calculates total expense for selected month
* Shows category-wise spending for that month
* Displays pie chart visualization

---

### Highest Spending Category

* Finds category with maximum expense

---

## 📊 Sample Output

Enter month (YYYY-MM): 2026-04

Total expense for 2026-04: ₹8500

Category-wise Breakdown:
Food: ₹3000
Travel: ₹2000
Bills: ₹3500

---

## 📈 Visualization

* Pie chart shows percentage distribution of expenses by category for the selected month

---

## 🚀 Future Enhancements

* GUI using Tkinter
* Web app using Flask
* Export reports as PDF
* AI-based spending suggestions
* Multi-user login system
* Database integration (MySQL)

---

## 🎯 Objective

To help users understand spending patterns and manage finances effectively.

---

## 📌 Notes

* expenses.csv is created automatically on first run
* Date format must be YYYY-MM-DD
* matplotlib must be installed for charts

---

## 👨‍💻 Author

Developed as a mini project for expense tracking and analysis.
