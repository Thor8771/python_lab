import random
import csv

# Generate sales data for 12 months
months = range(1, 13)
product_names = ["Product A", "Product B", "Product C", "Chair", "Table"]
sales_data = []

for month in months:
    row = {"Month": month}
    for product in product_names:
        row[product] = random.randint(10, 100)
    sales_data.append(row)

# Calculate profit as a random percentage of total revenue
for row in sales_data:
    revenue = sum(row[product] for product in product_names)
    profit = revenue * random.uniform(0.05, 0.20)
    row["Profit"] = profit

# Write the data to a CSV file
with open("sales_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f, fieldnames=["Month"] + product_names + ["Profit"])
    writer.writeheader()
    writer.writerows(sales_data)
