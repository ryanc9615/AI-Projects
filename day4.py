import csv
from collections import deque
from datetime import datetime

# Open and read the CSV file
def read_sales_data(filename):
    sales_records = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_records.append({
                'date': datetime.strptime(row['date'], '%Y-%m-%d'),
                'product_id': row['product_id'],
                'quantity': int(row['quantity']),
            })
    return sales_records

# Creating the Product Sales History Dictionary

def initialise_product_history():
    # Create an empty dictionary that will store deques
    product_history = {}
    return product_history

def update_product_history(product_history, product_id, quantity):
    # If this is the first time we've seen this product, create its deque
    if product_id not in product_history:
        product_history[product_id] = deque(maxlen=7)

    # Add the new quanitity to the product's history
    product_history[product_id].append(quantity)

def process_sales_records(sales_records):
    # Initialise the product history dictionary
    product_history = initialise_product_history()

    # Sort records by date to ensure chronological processing
    sales_records.sort(key=lambda x:x['date'])

    # Will store our results
    results = []

    # Process each record
    for record in sales_records:
        product_id = record['product_id']
        quantiy = record['quantity']
        date = record['date']

        
