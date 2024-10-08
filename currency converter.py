import tkinter as tk
from tkinter import ttk

# Static exchange rates (hardcoded for simplicity)
# Rates are based on 1 unit of 'from_currency' to 'to_currency'
exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'INR': 74.50, 'JPY': 110.12, 'CAD': 1.25},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'INR': 87.60, 'JPY': 129.53, 'CAD': 1.47},
    'GBP': {'USD': 1.33, 'EUR': 1.13, 'INR': 99.32, 'JPY': 147.00, 'CAD': 1.66},
    'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.010, 'JPY': 1.48, 'CAD': 0.017},
    'JPY': {'USD': 0.009, 'EUR': 0.007, 'GBP': 0.006, 'INR': 0.68, 'CAD': 0.011},
    'CAD': {'USD': 0.80, 'EUR': 0.68, 'GBP': 0.60, 'INR': 59.50, 'JPY': 88.24}
}

# Function to perform the currency conversion
def convert_currency():
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    amount = float(amount_entry.get())

    # Fetch the exchange rate from the static dictionary
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        exchange_rate = exchange_rates[from_currency][to_currency]
        converted_amount = round(amount * exchange_rate, 2)
        result_label.config(text=f"Converted Amount: {converted_amount} {to_currency}")
    else:
        result_label.config(text="Conversion not available for these currencies.")

# Create the GUI application
root = tk.Tk()
root.title("Simple Currency Converter")

# Create the input fields and dropdowns
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(column=0, row=0)

amount_entry = tk.Entry(root)
amount_entry.grid(column=1, row=0)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(column=0, row=1)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(column=0, row=2)

# Create dropdowns for currency selection
currencies = ["USD", "EUR", "GBP", "INR", "JPY", "CAD"]  # Add more currencies as needed

from_currency_combobox = ttk.Combobox(root, values=currencies, state="readonly")
from_currency_combobox.grid(column=1, row=1)
from_currency_combobox.current(0)  # Default selection

to_currency_combobox = ttk.Combobox(root, values=currencies, state="readonly")
to_currency_combobox.grid(column=1, row=2)
to_currency_combobox.current(1)  # Default selection

# Create a button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=1, row=3)

# Label to show conversion result
result_label = tk.Label(root, text="")
result_label.grid(column=1, row=4)

# Start the GUI event loop
root.mainloop()
