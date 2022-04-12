# import modules
import datetime
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import *

# initializing the GUI Window for Expense Tracker
root = Tk()  # create an object
root.title("Expense Tracker App")
root.geometry("1500x880")
root.iconbitmap("expenses.ico")
root.resizable(False, False)

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
sideView_frame.place(x=10, y=10, relwidth=0.2, relheight=0.5)

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
date_label = Label(addExpense_frame, text="Select Date :")
date_label.place(x=10, y=10)
date_label = DateEntry(addExpense_frame, date_label=datetime.datetime.now().date())
date_label.place(x=130, y=10)

category_label = Label(addExpense_frame, text="Category :")
category_label.place(x=10, y=34)
category_label = OptionMenu(addExpense_frame, category, *['Housing', 'Food', 'Transportation', 'Utilities',
                                                          'Insurance', 'Medical and Healthcare'])
category_label.place(x=126, y=34)

payMode_label = Label(addExpense_frame, text="Mode of Payment :")
payMode_label.place(x=10, y=68)
payMode_label = OptionMenu(addExpense_frame, payMode,
                           *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Online Banking'])
payMode_label.place(x=126, y=68)

payee_label = Label(addExpense_frame, text="Name of Payee :")
payee_label.place(x=10, y=106)
payee_label = Entry(addExpense_frame)
payee_label.place(x=130, y=106)

desc_label = Label(addExpense_frame, text="Description :")
desc_label.place(x=10, y=135)
desc_label = Entry(addExpense_frame)
desc_label.place(x=130, y=135)

income_label = Label(addExpense_frame, text="Income Amount :")
income_label.place(x=10, y=165)
income_label = Entry(addExpense_frame)
income_label.place(x=130, y=165)

expense_label = Label(addExpense_frame, text="Expense Amount :")
expense_label.place(x=10, y=195)
expense_label = Entry(addExpense_frame)
expense_label.place(x=130, y=195)

# add Expenses Button
add_button = Button(addExpense_frame, text="Add Expenses")
add_button.place(x=10, y=225, width=100)

clear_button = Button(addExpense_frame, text="Clear Fields")
clear_button.place(x=138, y=225, width=100)

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
treeView_data['columns'] = ("Row Id", "Date", "Category", "Mode of Payment", "Payee",
                            "Description", "Income Amount", "Expense Amount", "Remaining Amount")

# Formatting the columns for tree view
treeView_data.column("#0", width=0, minwidth=0, stretch=NO)
treeView_data.column("Row Id", anchor=CENTER, width=40, minwidth=0, stretch=NO)
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
treeView_data.heading("Row Id", text="S.No", anchor=CENTER)
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

# Buttons with button_frame
button_frame = LabelFrame(root, text="Other Operations")
button_frame.place(relx=0.215, rely=0.43, relwidth=0.78, relheight=0.08)

update_button = Button(button_frame, text="Update Record")
update_button.grid(row=0, column=0, padx=10, pady=10)

remove_only_one = Button(button_frame, text="Remove Only One Selected Expense")
remove_only_one.grid(row=0, column=1, padx=10, pady=10)

remove_multiple = Button(button_frame, text="Remove Multiple Selected Expenses")
remove_multiple.grid(row=0, column=2, padx=10, pady=10)

remove_all_expenses = Button(button_frame, text="Remove All Expenses")
remove_all_expenses.grid(row=0, column=3, padx=10, pady=10)

select_record_button = Button(button_frame, text="Select Record")
select_record_button.grid(row=0, column=4, padx=10, pady=10)

show_graphButton = Button(button_frame, text="Show Graph")
show_graphButton.grid(row=0, column=5, padx=10, pady=10)

move_upButton = Button(button_frame, text="Move Up")
move_upButton.grid(row=0, column=6, padx=10, pady=10)

move_downButton = Button(button_frame, text="Move Down")
move_downButton.grid(row=0, column=7, padx=10, pady=10)

# Graph frame
graph_frame = LabelFrame(root, text="Graphical Representation of the Expenses")
graph_frame.place(x=10, y=460, relwidth=0.989, relheight=0.46)


root.mainloop()
