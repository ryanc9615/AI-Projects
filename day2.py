import pandas as pd
import numpy as np

# Create a list on monthly revenue
monthly_revenue = [1000, 1200, 1100, 1300, 1400, 1250, 1350, 1450, 1550, 1600, 1700, 1800]

# convert the list into a 3x4 matrix 
revenue_matrix = np.array(monthly_revenue).reshape(3,4)
print("Revenue Matrix:")
print(revenue_matrix)

# Calculate total revenue per quarter (sum columns)
quarterly_totals = revenue_matrix.sum(axis=1)
print("Quarterly Totals:")
print(quarterly_totals)

# Slice into the third quarter (months 7-9)
third_quarter = revenue_matrix[2, :]
print("Third Quarter Revenue:")
print(third_quarter)


# Read the monthly revenue data from a CSV file
df = pd.read_csv("monthly_revenue.csv")

# Extract revenue column and convert it to a numpy array
revenue_array = df['Revenue'].to_numpy()

# Reshape the revenue array into a 3x4 matrix
revenue_matrix = revenue_array.reshape(3,4)
print("Revenue Matrix:")
print(revenue_matrix)

# Calculate the total revenue for each quarter 
quarterly_revenue = revenue_matrix.sum(axis=1)
print("Quarterly Revenue:")
print(quarterly_revenue)

# Slice the second quarter
second_quarter = revenue_matrix[1, :]
print("Second Quarter Revenue:")
print(second_quarter)

