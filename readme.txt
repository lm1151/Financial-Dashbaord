Personal Finance Dashboard

This Python project is a personal finance management tool developed as a final assignment for my programming course. It demonstrates the integration of object-oriented programming (OOP), data transformation, third-party library usage, file I/O, and basic data visualization in Python.

The dashboard allows users to upload and process a CSV file of financial transactions. It calculates total income, expenses, and net balance, visualizes spending across categories, provides budget alerts, and exports a summary report. The program is designed to be lightweight, modular, and user-friendly, serving as a foundational tool for anyone looking to gain insights into their personal finances.

Core Objectives:
- Reinforce core Python programming concepts including class creation, data encapsulation, file manipulation, and control flow.
- Demonstrate real-world utility by solving a problem many users face: managing and analyzing spending data.
- Encourage clean, modular design using multiple `.py` files for separation of concerns.
- Introduce external libraries (`pandas`, `matplotlib`) and show how they simplify data tasks and visualization.

Key Features:
Read and parse structured data from a CSV file  
Create `Transaction` objects for each row in the CSV  
Categorize transactions as income or expenses  
Calculate and display:
   - Total income  
   - Total expenses  
   - Net balance  
Automatically generate and open a bar chart visualizing expense breakdown  
Export the financial summary to a `summary.txt` file  
Display budget warnings when spending exceeds certain category thresholds  
Apply object-oriented design principles for code organization and reuse

File & Folder Structure:

- main.py
  - The core execution script. It initializes the finance manager, loads data, triggers summary generation, calls the visualization module, and handles budget alerts and file output.

- transaction.py
  - Defines the `Transaction` class, which holds individual record data: `date`, `description`, `category`, and `amount`. It’s used throughout the app for consistent data structure and logic clarity.

- finance_manager.py
  - Handles the logic of loading and transforming data. The `FinanceManager` class parses the CSV using `pandas`, creates `Transaction` objects, and calculates totals for income, expenses, and balance.

- visualizer.py
  - Generates a bar chart using `matplotlib`, grouping expenses by category. This helps users see where their money goes visually.

- transactions.csv
  - Input data file. Must include the columns:  
    `Date, Description, Category, Amount`  
    Example:  
    `2025-04-01,Paycheck,Income,2500.00`

- summary.txt
  - Automatically generated after each run. Contains total income, total expenses, and net balance in a plain text format. Useful for saving a historical snapshot.

- requirements.txt
  - Lists third-party packages required to run the program:
    - `pandas`: for data manipulation and CSV parsing
    - `matplotlib`: for creating bar chart visualizations

- readme.txt
  - (This file) Provides detailed instructions, program overview, and design structure for instructors or future users.

How to Run This Program:

1. Create a virtual environment (optional but recommended):
   python3 -m venv venv
   source venv/bin/activate       # On Mac/Linux
   venv\Scripts\activate        # On Windows

2. Install dependencies:
   pip install -r requirements.txt

3. Ensure `transactions.csv` is properly formatted and located in the same directory as `main.py`.  
   The first line must contain headers: `Date,Description,Category,Amount`

4. Run the program:
   python3 main.py

5. Expected Output:
   - A summary report printed in the terminal
   - A `summary.txt` file created in your project folder
   - A popup window with a bar chart of expenses by category
   - Console warnings if spending exceeded preset category limits (e.g., Food > $200)


Budget Threshold Logic:
The program provides warning messages for overspending in the following categories:
- Food: if total spending exceeds $200
- Entertainment: if total spending exceeds $100

This can be easily extended in `main.py` to add more categories or customize limits.


Design Choices and Rationale:
- Object-Oriented Design: The use of classes (`Transaction`, `FinanceManager`) allows for cleaner, more scalable architecture.
- Separation of Concerns: Each `.py` file handles a specific piece of functionality, keeping the code organized and easier to debug or extend.
- Pandas for CSV Parsing: Chosen for its efficiency in loading and transforming tabular data.
- Matplotlib for Visualization: Allows users to visually understand their spending, which adds value beyond raw numbers.
- Plain Text Summary Output: Useful for saving results or sharing them with others.

--------------------------
Ideas for Future Expansion:
--------------------------
- Add support for filtering by date/month/year
- Add more advanced analytics (spending trends over time)
- Allow custom budget thresholds per user
- Export chart as PNG or PDF
- Add a GUI with Tkinter or Streamlit
- Connect to APIs like Plaid for real-time transaction imports