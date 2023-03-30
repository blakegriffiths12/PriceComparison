# import necessary modules
import tkinter as tk
from tkinter import messagebox

# function to check if the input is an integer
def int_check_answer(question,error):
    valid=False 
    while not valid:
        try:
          response=int(input(question))
          return(response)
        except ValueError:
            print (error)

# function to calculate price per gram
def price_per_gram(price, weight):
    return price / weight

# function to compare prices and recommend the best value for money
def compare_prices(budget, products):
    unit_prices = []
    for product in products:
        name, price, quantity = product
        unit_price = price / quantity
        unit_prices.append((name, unit_price))
    # sort the list of products by unit price
    unit_prices.sort(key=lambda x: x[1])
    # find the product that fits within the budget and has the lowest unit price
    affordable_products = [p for p in unit_prices if p[1] <= budget]
    if not affordable_products:
        return "Sorry, you can't afford any of these products."
    else:
        best_value = affordable_products[0][0]
        return f"The best value for money is {best_value}."

# function to get product information from user input
def get_product_info():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = float(input("Enter product quantity: "))
    return (name, price, quantity)

# function to add a product
def add_product():
    product_info = get_product_info()
    products.append(product_info)
    update_display()

# function to update the display
def update_display():
    # clear the listbox
    listbox.delete(0, END)
    # add the products to the listbox
    for product in products:
        name, price, quantity = product
        listbox.insert(END, f"{name} - ${price:.2f} ({quantity:.2f} units)")

# function to handle the compare button click event
def compare_button_click():
    # get the budget from the entry widget
    budget = budget_entry.get()
    # check if the budget is a number
    if budget.isdigit():
        budget = int(budget)
        # call the compare_prices function and show the result in a messagebox
        result = compare_prices(budget, products)
        messagebox.showinfo("Result", result)
    else:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")

def exit_gui():
  root.destroy()
# create the main window
root = tk.Tk()
root.title("Price Comparison Tool")
root.geometry("500x500")

# create the widgets
title_label = tk.Label(root, text="Price Comparison Tool", font=("Arial", 20))
budget_label = tk.Label(root, text="Enter your budget:")
budget_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add a product", command=add_product)
compare_button = tk.Button(root, text="Compare prices", command=compare_button_click)
listbox_label = tk.Label(root, text="Your products:")
listbox = tk.Listbox(root)

exit_button = tk.Button(root, text="Exit", command=exit_gui)

# configure the widgets
title_label.pack(pady=10)
budget_label.pack(pady=10)
budget_entry.pack(pady=10)
add_button.pack(pady=10)
listbox_label.pack(pady=10)
listbox.pack(pady=10)
compare_button.pack(pady=10)
exit_button.pack()

# initialize the products list
products = []

# update the display
update_display()

# run the main loop
root.mainloop()