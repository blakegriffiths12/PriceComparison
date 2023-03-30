import tkinter as tk

def int_check_answer(question,error):
    valid = False 
    while not valid:
        try:
            response = float(entry.get())
            return(response)
        except ValueError:
            error_label.config(text=error)

# function to calculate price per gram
def price_per_gram(price, weight):
    return price / weight
  
def compare_prices():
    """Compare prices of products and recommend the best value for money"""
    budget = float(budget_entry.get())
    products = []
    for i in range(len(product_entries)):
        name = product_entries[i][0].get()
        price = float(product_entries[i][1].get())
        quantity = float(product_entries[i][2].get())
        products.append((name, price, quantity))
    unit_prices = []
    for product in products:
        name, price, quantity = product
        unit_price = price / quantity
        unit_prices.append((name, unit_price))
    # Sort the list of products by unit price
    unit_prices.sort(key=lambda x: x[1])
    # Find the product that fits within the budget and has the lowest unit price
    affordable_products = [p for p in unit_prices if p[1] <= budget]
    if not affordable_products:
        result_label.config(text="Sorry, you can't afford any of these products.")
    else:
        best_value = affordable_products[0][0]
        result_label.config(text=f"The best value for money is {best_value}.")

def add_product():
    product_frame = tk.Frame(root)
    name_label = tk.Label(product_frame, text="Product name:")
    name_entry = tk.Entry(product_frame)
    name_label.pack(side=tk.LEFT)
    name_entry.pack(side=tk.LEFT)
    price_label = tk.Label(product_frame, text="Product price:")
    price_entry = tk.Entry(product_frame)
    price_label.pack(side=tk.LEFT)
    price_entry.pack(side=tk.LEFT)
    quantity_label = tk.Label(product_frame, text="Product quantity:")
    quantity_entry = tk.Entry(product_frame)
    quantity_label.pack(side=tk.LEFT)
    quantity_entry.pack(side=tk.LEFT)
    product_frame.pack()
    product_entries.append((name_entry, price_entry, quantity_entry))

# Create the main window
root = tk.Tk()
root.title("Price Comparison Tool")

# Create the budget entry field and label
budget_label = tk.Label(root, text="Enter a Budget:")
budget_label.pack()
budget_entry = tk.Entry(root)
budget_entry.pack()

# Create the add product button
add_button = tk.Button(root, text="Add Product", command=add_product)
add_button.pack()

# Create a list to hold the product entries
product_entries = []

# Create the compare button
compare_button = tk.Button(root, text="Compare Prices", command=compare_prices)
compare_button.pack()

# Create the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
