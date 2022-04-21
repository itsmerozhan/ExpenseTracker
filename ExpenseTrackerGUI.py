# import modules
import datetime
import sqlite3
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

# initializing the GUI Window for Expense Tracker
root = Tk()  # create an object
root.title("Expense Tracker App")
root.geometry("1500x880")
root.iconbitmap("expenses.ico")
root.resizable(False, False)

# Connecting to the database
dbConnection = sqlite3.connect('ExpensesDetails.db')
dbcursor = dbConnection.cursor()

# Creating a table
dbcursor.execute(""" CREATE TABLE IF NOT EXISTS ExpensesDetails (
                        Id                  INTEGER PRIMARY KEY,
                        Date                DATETIME,
                        Category            TEXT,
                        PayMode             TEXT,
                        Payee               TEXT,
                        Description         TEXT,
                        IncomeAmount        FLOAT,
                        ExpenseAmount       FLOAT,
                        RemainingAmount     FLOAT)
                    """)

dbConnection.commit()
dbConnection.close()


def query_database():
    # Create a database or connect to one that exists
    dbConnection = sqlite3.connect('ExpensesDetails.db')
    # Create a cursor instance
    dbcursor = dbConnection.cursor()
    dbcursor.execute("SELECT * FROM ExpensesDetails")
    records = dbcursor.fetchall()

    # Add our data to the screen
    global count
    count = 0

    # for record in records:
    #     print(record)
    for record in records:
        if count % 2 == 0:
            treeView_data.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                                 tags=('evenRows',))
        else:
            treeView_data.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                                 tags=('oddRows',))
        # increment counter
        count += 1
    dbConnection.commit()


# adding some style in the app
styleApp = ttk.Style()
styleApp.theme_use("default")  # can use theme like clam, classic, default etc.
# color combination code -- #2193b0, #6dd5ed, #1F2F98 # treeview Back ground = blue, foreground -- text,
styleApp.configure("Treeview",
                   foreground="#000000", rowheight=30, fieldbackground="#FFFFFF")
styleApp.map("Treeview", background=[('selected', "#2193b0")])

# declaring some variables for category, paymode, payee, description, income and expense amount
category = StringVar(value='Select an option')
payMode = StringVar(value='Select an option')
payee = StringVar()
description = StringVar()
incomeAmount = DoubleVar()
expenseAmount = DoubleVar()

# SideView Frame for Add Expense Menus
sideView_frame = LabelFrame(root, text="Welcome to Expense Tracker")
sideView_frame.place(x=10, y=10, relwidth=0.2, relheight=0.55)

# image of Expense Tracker

img_expense = Image.open("expenses_tracker.png")
img_expense = img_expense.resize((260, 120), Image.ANTIALIAS)  # removes structural padding around images
img_photoImage = ImageTk.PhotoImage(img_expense)
img_label = Label(sideView_frame, image=img_photoImage)
img_label.grid(row=0, column=0, padx=15)

# adding new frame inside sideViewFrame
addExpense_frame = LabelFrame(sideView_frame, text="Fill Up Form to Add Your Expenses")
addExpense_frame.place(x=5, y=130, relwidth=0.97, relheight=0.68)

# Labels
expense_number_label = Label(addExpense_frame, text="Enter Serial Number:")
expense_number_label.place(x=10, y=10)
expense_number_entry = Entry(addExpense_frame)
expense_number_entry.place(x=130, y=10)

date_label = Label(addExpense_frame, text="Enter Date :")
date_label.place(x=10, y=34)
# date_entry = Entry(addExpense_frame)
date_entry = DateEntry(addExpense_frame, date_entry=datetime.datetime.now().date())
date_entry.place(x=130, y=34)

category_label = Label(addExpense_frame, text="Enter Category :")
category_label.place(x=10, y=58)
category_entry = Entry(addExpense_frame)
# category_entry = OptionMenu(addExpense_frame, category, *['Housing', 'Food', 'Transportation', 'Utilities',
#                                                           'Insurance', 'Medical and Healthcare'])
category_entry.place(x=130, y=58)

payMode_label = Label(addExpense_frame, text="Enter Payment Mode:")
payMode_label.place(x=10, y=82)
# payMode_entry = OptionMenu(addExpense_frame, payMode,
#                            *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Online Banking'])
payMode_entry = Entry(addExpense_frame)
payMode_entry.place(x=130, y=82)

payee_label = Label(addExpense_frame, text="Enter Payee Name :")
payee_label.place(x=10, y=106)
payee_entry = Entry(addExpense_frame)
payee_entry.place(x=130, y=106)

desc_label = Label(addExpense_frame, text="Enter Description :")
desc_label.place(x=10, y=130)
desc_entry = Entry(addExpense_frame)
desc_entry.place(x=130, y=130)

income_label = Label(addExpense_frame, text="Income Amount :")
income_label.place(x=10, y=155)
income_entry = Entry(addExpense_frame)
income_entry.place(x=130, y=155)

expense_label = Label(addExpense_frame, text="Expense Amount :")
expense_label.place(x=10, y=180)
expense_entry = Entry(addExpense_frame)
expense_entry.place(x=130, y=180)

remaining_amount_label = Label(addExpense_frame, text="Remaining Amount :")
remaining_amount_label.place(x=10, y=205)
remaining_amount_entry = Entry(addExpense_frame)
remaining_amount_entry.place(x=130, y=205)

# Treeview Frame
treeView_frame = LabelFrame(root, text="Expense Lists")
treeView_frame.place(relx=0.215, rely=0.013, relwidth=0.78, relheight=0.4)

# treeView Scroll Bar
treeView_scrollData = Scrollbar(treeView_frame)
treeView_scrollData.pack(side=RIGHT, fill=Y)  # setting scroll bar to right side

# creating a tree treeview for data display
treeView_data = ttk.Treeview(treeView_frame,
                             yscrollcommand=treeView_scrollData.set, selectmode="extended")
treeView_data.pack()
# configuration of scroll bar
treeView_scrollData.config(command=treeView_data.yview)  # vertical showcase of data

# columns name for the database
# S.No, Date, Category,Mode of Payment, Payee, Description, IncomeAmount, ExpenseAmount, RemainingAmount
treeView_data['columns'] = ("Id", "Date", "Category", "Mode of Payment", "Payee",
                            "Description", "Income Amount", "Expense Amount", "Remaining Amount")

# Formatting the columns for tree view
treeView_data.column("#0", width=0, minwidth=0, stretch=NO)
treeView_data.column("Id", anchor=CENTER, width=40, minwidth=0, stretch=NO)
treeView_data.column("Date", anchor=CENTER, width=80, minwidth=0, stretch=NO)
treeView_data.column("Category", anchor=CENTER, width=100, minwidth=0, stretch=NO)
treeView_data.column("Mode of Payment", anchor=CENTER, width=120, minwidth=0, stretch=NO)
treeView_data.column("Payee", anchor=CENTER, width=140, minwidth=0, stretch=NO)
treeView_data.column("Description", anchor=CENTER, width=240, minwidth=0, stretch=NO)
treeView_data.column("Income Amount", anchor=CENTER, width=140, minwidth=0, stretch=NO)
treeView_data.column("Expense Amount", anchor=CENTER, width=140, minwidth=0, stretch=NO)
treeView_data.column("Remaining Amount", anchor=CENTER, width=140, minwidth=0, stretch=NO)

# Creating Headings for displaying data in tree view
treeView_data.heading("#0", text="", anchor=CENTER)
treeView_data.heading("Id", text="S.No", anchor=CENTER)
treeView_data.heading("Date", text="Date", anchor=CENTER)
treeView_data.heading("Category", text="Category", anchor=CENTER)
treeView_data.heading("Mode of Payment", text="Mode of Payment", anchor=CENTER)
treeView_data.heading("Payee", text="Payee", anchor=CENTER)
treeView_data.heading("Description", text="Description", anchor=CENTER)
treeView_data.heading("Income Amount", text="Income Amount", anchor=CENTER)
treeView_data.heading("Expense Amount", text="Expense Amount", anchor=CENTER)
treeView_data.heading("Remaining Amount", text="Remaining Amount", anchor=CENTER)

# Coloring even and odd row in treeview
treeView_data.tag_configure('oddRows', background="#FFFFFF")
treeView_data.tag_configure('evenRows', background="#6dd5ed")


# functions for button to operate CRUD operation
def clear_expenses():
    # global category, payMode, payee, description, incomeAmount, expenseAmount
    # # Setting today date when data is clear
    # today_date = datetime.datetime.now().date()
    # date_entry.set_date(today_date)
    # category.set('Select an option')
    # payMode.set('Select an option')

    # clear the entry boxes
    expense_number_entry.delete(0, END)
    date_entry.delete(0, END)
    category_entry.delete(0, END)
    payMode_entry.delete(0, END)
    payee_entry.delete(0, END)
    desc_entry.delete(0, END)
    income_entry.delete(0, END)
    expense_entry.delete(0, END)
    remaining_amount_entry.delete(0, END)


# pop values in the boxes
def view_expenses(e):  # e is the event for button release

    # clear the entry boxes
    expense_number_entry.delete(0, END)
    date_entry.delete(0, END)
    category_entry.delete(0, END)
    payMode_entry.delete(0, END)
    payee_entry.delete(0, END)
    desc_entry.delete(0, END)
    income_entry.delete(0, END)
    expense_entry.delete(0, END)
    remaining_amount_entry.delete(0, END)

    # select the expense for view
    selected_expense = treeView_data.focus()
    expense_values = treeView_data.item(selected_expense, 'values')

    # show selected data in the entry boxes
    expense_number_entry.insert(0, expense_values[0])
    date_entry.insert(0, expense_values[1])
    category_entry.insert(0, expense_values[2])
    payMode_entry.insert(0, expense_values[3])
    payee_entry.insert(0, expense_values[4])
    desc_entry.insert(0, expense_values[5])
    income_entry.insert(0, expense_values[6])
    expense_entry.insert(0, expense_values[7])
    remaining_amount_entry.insert(0, expense_values[8])


# moving the expenses up and down
def expense_move_up():
    rows = treeView_data.selection()
    for row in rows:
        treeView_data.move(row, treeView_data.parent(row), treeView_data.index(row) - 1)


def expense_move_down():
    rows = treeView_data.selection()
    for row in reversed(rows):
        treeView_data.move(row, treeView_data.parent(row), treeView_data.index(row) + 1)


# Remove only one expenses
def remove_only_one():
    expense_remove = treeView_data.selection()[0]
    treeView_data.delete(expense_remove)

    # delete the only one data in database
    # Create a database or connect to one that exists
    dbConnection = sqlite3.connect('ExpensesDetails.db')
    # Create a cursor instance
    dbcursor = dbConnection.cursor()
    # Deleting the data from database
    dbcursor.execute("DELETE FROM ExpensesDetails WHERE id =" + expense_number_entry.get())

    # Delete from Database
    dbConnection.commit()
    dbConnection.close()
    clear_expenses()

    # Confirmation of deleting data
    messagebox.showinfo("Expenses Deleted", "Your Record is deleted successfully")


# Remove multiple expenses
def remove_multiple():
    # Confirmation of deleting data
    delete_multiple_data = messagebox.askyesno("Are Your Sure?", "Are you sure you want to delete selected expenses "
                                                                 "from the table")
    if delete_multiple_data == 1:
        expense_multiple_remove = treeView_data.selection()
        for expenses_multiple in expense_multiple_remove:
            treeView_data.delete(expenses_multiple)

        dbConnection = sqlite3.connect('ExpensesDetails.db')
        # Create a cursor instance
        dbcursor = dbConnection.cursor()
        # Deleting all the data from database
        dbcursor.execute("DROP TABLE ExpensesDetails")

        # Delete from Database
        dbConnection.commit()
        dbConnection.close()
        clear_expenses()


# Remove all the expenses
def remove_all():
    # Confirmation of deleting data
    delete_data = messagebox.askyesno("Are Your Sure?", "Are you sure you want to delete all the data from the table")
    if delete_data == 1:
        record_delete = treeView_data.selection()
        id_delete = []
        for records in record_delete:
            id_delete.append(treeView_data.item(records, 'values')[2])
        for record in record_delete:
            treeView_data.delete(record)
        # Create a database or connect to one that exists
        dbConnection = sqlite3.connect('ExpensesDetails.db')
        # Create a cursor instance
        dbcursor = dbConnection.cursor()
        # Deleting all the data from database
        dbcursor.execute("DELETE FROM customers WHERE id = ?", [(a,) for a in id_delete])

        id_delete = []
        # Delete from Database
        dbConnection.commit()
        dbConnection.close()
        clear_expenses()


# Update the expenses details
def update_expenses():
    # Grab the record number
    selected = treeView_data.focus()
    # Update expenses
    treeView_data.item(selected, text="", values=(
        expense_number_entry.get(), date_entry.get(), category_entry.get(), payMode_entry.get(), payee_entry.get(),
        desc_entry.get(),
        income_entry.get(), expense_entry.get(), remaining_amount_entry.get(),))

    # update the data in database
    # Create a database or connect to one that exists
    dbConnection = sqlite3.connect('ExpensesDetails.db')
    # Create a cursor instance
    dbcursor = dbConnection.cursor()
    # Updating the data
    dbcursor.execute(""" UPDATE ExpensesDetails SET
                            Date = :Date,
                            Category = :Category,
                            PayMode = :PayMode,
                            Payee = :Payee,
                            Description = :Description,
                            IncomeAmount = :IncomeAmount,
                            ExpenseAmount = :ExpenseAmount,
                            RemainingAmount = :RemainingAmount
                            WHERE Id = :Id""",
                     {
                         'Date': date_entry.get(),
                         'Category': category_entry.get(),
                         'PayMode': payMode_entry.get(),
                         'Payee': payee_entry.get(),
                         'Description': desc_entry.get(),
                         'IncomeAmount': income_entry.get(),
                         'ExpenseAmount': expense_entry.get(),
                         'RemainingAmount': remaining_amount_entry.get(),
                         'Id': expense_number_entry.get()
                     }
                     )
    dbConnection.commit()
    dbConnection.close()

    # Clear entry boxes
    expense_number_entry.delete(0, END)
    date_entry.delete(0, END)
    category_entry.delete(0, END)
    payMode_entry.delete(0, END)
    payee_entry.delete(0, END)
    desc_entry.delete(0, END)
    income_entry.delete(0, END)
    expense_entry.delete(0, END)
    remaining_amount_entry.delete(0, END)

    if not treeView_data.selection():
        messagebox.showerror('No expense selected!', 'Please Select the Expenses to edit')
        return

    # Confirmation of updating data
    messagebox.showinfo("Expenses Updated", "Your Expenses is Updated successfully")


# Adding a new expenses in the database
def add_expenses():
    # add the data in database
    # Create a database or connect to one that exists
    dbConnection = sqlite3.connect('ExpensesDetails.db')
    # Create a cursor instance
    dbcursor = dbConnection.cursor()

    # adding new expenses
    dbcursor.execute("INSERT INTO ExpensesDetails VALUES (:Id, :Date, :Category, :PayMode, :Payee, :Description, "
                     ":IncomeAmount, :ExpenseAmount, :RemainingAmount)",
                     {
                         'Id': expense_number_entry.get(),
                         'Date': date_entry.get(),
                         'Category': category_entry.get(),
                         'PayMode': payMode_entry.get(),
                         'Payee': payee_entry.get(),
                         'Description': desc_entry.get(),
                         'IncomeAmount': income_entry.get(),
                         'ExpenseAmount': expense_entry.get(),
                         'RemainingAmount': remaining_amount_entry.get()
                     }
                     )
    dbConnection.commit()
    dbConnection.close()

    # Clear entry boxes
    expense_number_entry.delete(0, END)
    date_entry.delete(0, END)
    category_entry.delete(0, END)
    payMode_entry.delete(0, END)
    payee_entry.delete(0, END)
    desc_entry.delete(0, END)
    income_entry.delete(0, END)
    expense_entry.delete(0, END)
    remaining_amount_entry.delete(0, END)

    # Refresh treeviewData
    # Clearing the treeview data
    treeView_data.delete(*treeView_data.get_children())
    query_database()

    # Confirmation of added data
    messagebox.showinfo("Expenses Added", "Your Expenses is Added successfully")


# Create a database if database is dropped
def create_database():
    dbConnection = sqlite3.connect('ExpensesDetails.db')
    dbcursor = dbConnection.cursor()

    # Creating a table
    dbcursor.execute(""" CREATE TABLE IF NOT EXISTS ExpensesDetails (
                            Id                  INTEGER PRIMARY KEY,
                            Date                DATETIME,
                            Category            TEXT,
                            PayMode             TEXT,
                            Payee               TEXT,
                            Description         TEXT,
                            IncomeAmount        FLOAT,
                            ExpenseAmount       FLOAT,
                            RemainingAmount     FLOAT)
                    """)
    dbConnection.commit()
    dbConnection.close()


# add Expenses Button in addExpense_frame
add_button = Button(addExpense_frame, text="Add Expenses", command=add_expenses)
add_button.place(x=10, y=255, width=100)

clear_button = Button(addExpense_frame, text="Clear Fields", command=clear_expenses)
clear_button.place(x=138, y=255, width=100)

# Buttons with button_frame
button_frame = LabelFrame(root, text="Other Operations")
button_frame.place(relx=0.215, rely=0.43, relwidth=0.78, relheight=0.08)

update_button = Button(button_frame, text="Update Expenses", command=update_expenses)
update_button.grid(row=0, column=0, padx=10, pady=10)

remove_only_one = Button(button_frame, text="Remove Only One Selected Expense", command=remove_only_one)
remove_only_one.grid(row=0, column=1, padx=10, pady=10)

remove_multiple = Button(button_frame, text="Remove Multiple Selected Expenses", command=remove_multiple)
remove_multiple.grid(row=0, column=2, padx=10, pady=10)

remove_all_expenses = Button(button_frame, text="Remove All Expenses", command=remove_all)
remove_all_expenses.grid(row=0, column=3, padx=10, pady=10)

move_upButton = Button(button_frame, text="Move Up", command=expense_move_up)
move_upButton.grid(row=0, column=6, padx=10, pady=10)

move_downButton = Button(button_frame, text="Move Down", command=expense_move_down)
move_downButton.grid(row=0, column=7, padx=10, pady=10)

# Bind the tree view
treeView_data.bind("<ButtonRelease-1>", view_expenses)

# Graph frame
graph_frame = LabelFrame(root, text="Graphical Representation of the Expenses")
graph_frame.place(x=10, y=500, relwidth=0.989, relheight=0.42)


# matplotlib graph
def graph_demonstration():

    dbConnection = sqlite3.connect('ExpensesDetails.db')
    dbcursor = dbConnection.cursor()
    dbcursor.execute("SELECT IncomeAmount, ExpenseAmount, RemainingAmount FROM ExpensesDetails")
    expenses_data_fetch = dbcursor.fetchall()
    incomeAmount = []
    expenseAmount = []
    remainingAmount = []
    # dbConnection.commit()
    # dbConnection.close()

    for row in expenses_data_fetch:
        incomeAmount.append(row[0])
        expenseAmount.append(row[1])
        remainingAmount.append(row[2])

    plt.plot(incomeAmount, label="Income")
    plt.plot(expenseAmount, label="Expense")
    plt.plot(remainingAmount, label="Remaining Amount")
    plt.legend()
    plt.xlabel("Expenditure")
    plt.ylabel("Income")
    plt.title("Income and Expenditure")
    plt.show()


show_graphButton = Button(button_frame, text="Expenses Graph", command=graph_demonstration)
show_graphButton.grid(row=0, column=5, padx=10, pady=10)

# execute the data in the database
query_database()
root.mainloop()
