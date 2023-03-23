'''
  Name: Jack Seeler & Blake Griffiths 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
#---------------------------------imports---------------------------------------------



#---------------------------------functions-------------------------------------------
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




def compare_prices(budget, products):
    """Compare prices of products and recommend the best value for money"""
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
        return "Sorry, you can't afford any of these products."
    else:
        best_value = affordable_products[0][0]
        return f"The best value for money is {best_value}."


def get_product_info():
    """Get product information from user input"""
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = float(input("Enter product quantity : "))
    return (name, price, quantity)


#------------------------------------------main---------------------------------------
# Ask the user for their budget
while True:
    user_input = input("Enter a Budget: ")
    if user_input.isdigit():
        number = int(user_input)
        break
    else:
        print("Invalid input. Please enter a number.")

print("The entered number is:", number)

products = []
while True:
    add_product = input("Add a product? (y/n) ")
    if add_product.lower() == "n":
        break
    else:
        product_info = get_product_info()
        products.append(product_info)

# Call the compare_prices function and print the result
result = compare_prices(budget, products)
print(result)
  
