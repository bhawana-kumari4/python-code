# Expense Tracker

total = 0

print("===== Expense Tracker =====")

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total = total + float(expense)

print("\n===== Summary =====")
print("Total Spent:", total)