# 🐍 Python Mini Projects

This repository contains three beginner-level Python console projects: a Password Generator, a To-Do List app, and an Expense Tracker. Each project is in its own folder with its own code file.

---

## 🔐 1. Password Generator

A simple program that generates a random password of a length chosen by the user, using a mix of uppercase letters, lowercase letters, and digits.

**Features:**
- Takes password length as input from the user
- Generates a random password using letters (A-Z, a-z) and digits (0-9)
- Displays the generated password instantly

**How to Run:**
```
python password_generator.py
```

---

## ✅ 2. To-Do List (Console App)

A menu-driven command-line To-Do list application. Users can add tasks, view their task list, and exit the program.

**Features:**
- Add new tasks to the list
- View all added tasks with numbering
- Simple menu-driven interface
- Handles invalid menu choices gracefully

**How to Run:**
```
python to_do_list.py
```

---

## 💰 3. Expense Tracker (Console App)

A program that lets users enter multiple expenses one by one and then displays the total amount spent.

**Features:**
- Enter expenses one at a time
- Type "done" to stop entering expenses
- Automatically calculates and displays the total spent

**How to Run:**
```
python expense_tracker.py
```

---

## 🛠️ Technologies Used
- Python 3
- Built-in libraries only: `random`, `string`

## 🚀 Future Improvements
- Add file storage so data is saved between runs (To-Do List, Expense Tracker)
- Add categories for expenses
- Add option for special characters in password generator
- Build graphical user interfaces (GUI) using Tkinter for all three projects

## 👩‍💻 Author
Created as part of Python practice projects.

---

## 📷 Outputs

### Password Generator
```
Enter password length: 12
Generated Password: chCvNfFlYN5u
```

### To-Do List
```
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 1
Enter Task: learn python
Task Added Successfully!

===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 1
Enter Task: complete python  assignments
Task Added Successfully!

===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 2

Your Tasks:
1. learn python
2. complete python  assignments

===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit
Enter your choice: 3
Thank You!
```

### Expense Tracker
```
===== Expense Tracker =====
Enter expense amount (or type 'done' to finish): 100
Enter expense amount (or type 'done' to finish): 50
Enter expense amount (or type 'done' to finish): 20
Enter expense amount (or type 'done' to finish): done

===== Summary =====
Total Spent: 170.0
```
