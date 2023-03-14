'''
  Name: Jack Seeler & Blake Griffiths 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''

# Exchange rates
usd_rate = 1.0
eur_rate = 1.2
gbp_rate = 1.4

# List of prices in USD
prices_usd = [10.0, 20.0, 30.0, 40.0]

# Function to convert prices to another currency
def convert_prices(prices, rate):
    return [price * rate for price in prices]

# Convert prices to EUR and GBP
prices_eur = convert_prices(prices_usd, eur_rate)
prices_gbp = convert_prices(prices_usd, gbp_rate)

# Print original and converted prices
print("Original prices (USD):", prices_usd)
print("Prices converted to EUR:", prices_eur)
print("Prices converted to GBP:", prices_gbp)
