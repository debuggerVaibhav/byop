Pocket Expense Tracker
📌 Overview
The Pocket Expense Tracker is a Python-based utility designed to solve the common problem of "invisible spending." In a world of digital micro-transactions, it’s easy to lose track of small daily costs. This tool provides a centralized, terminal-based interface to log, categorize, and analyze expenditures in real-time.

🛠 The Problem & Solution
The Problem: Many existing expense apps are over-complicated, require account sign-ups, or lack privacy. Users often need a "no-friction" way to quickly log a cost without leaving their desktop environment.

The Solution: A lightweight, local Python application that prioritizes speed and data integrity through robust error handling and a clean Command Line Interface (CLI).

✨ Features
Dynamic Logging: Add expenses with descriptions and timestamps.

Data Validation: Built-in safeguards to prevent crashes from invalid inputs (e.g., entering text where a price is expected).

Instant Analytics: Live calculation of total spending to help users stay within budget.

Formatted Output: Clean, tabular view of historical data for easy review.

💻 Technologies Used
Language: Python 3.x

Core Modules: * datetime: For automated entry logging.

sys/os: For terminal navigation and clean exit handling.

Version Control: Git/GitHub (Reflecting an iterative development process).

🚀 Installation & Setup
Clone the Repository:

Bash
git clone https://github.com/your-username/Vityarthi-Project.git
Navigate to Directory:

Bash
cd Vityarthi-Project
Run the Application:

Bash
python expense_tracker.py
🧪 Testing the Program
To ensure the application is running correctly, follow these test cases:

Standard Entry: Choose 1, enter "Coffee" and 5.50. Verify it appears in the list.

Input Resilience: Try entering "Free" as an amount. The program should catch the error and prompt for a number.

Calculation Check: Add three items and select 3 to ensure the sum matches your manual calculation.

Empty State: View the list before adding any items to see the "No expenses recorded" handling.

📈 Development Roadmap (Key Decisions)
Decision 1: Chose a List-of-Dictionaries structure to allow for easy expansion (e.g., adding "Category" tags later).

Decision 2: Implemented a while True loop for the menu to ensure a seamless user experience until an explicit exit command is given.
