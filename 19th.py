import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("sales_data.csv")

# Task a: Get total profit of all months and show line plot
total_profit = data["Profit"].sum()
months = data["Month"]
plt.plot(months, data["Sold units"], linestyle="--",
         color="blue", linewidth=4, label="Sold units")
plt.title(f"Total Profit: ${total_profit:.2f}")
plt.xlabel("Months")
plt.ylabel("Sold units")
plt.legend(loc="lower right")
plt.show()

# Task b: Display the number of units sold per month for each product using multiline plots
products = ["Product A", "Product B", "Product C"]
for product in products:
    plt.plot(data["Month"], data[product], label=product)
plt.title("Units Sold per Month by Product")
plt.xlabel("Months")
plt.ylabel("Units Sold")
plt.legend()
plt.show()

# Task c: Read chair and table product sales data and show it using the bar chart
chair_data = data[["Month", "Chair"]]
table_data = data[["Month", "Table"]]
plt.bar(chair_data["Month"], chair_data["Chair"], label="Chair")
plt.bar(table_data["Month"], table_data["Table"], label="Table")
plt.title("Units Sold per Month for Chairs and Tables")
plt.xlabel("Months")
plt.ylabel("Units Sold")
plt.legend()
plt.show()

# Task d: Read all product sales data and show it using the stack plot
products = ["Product A", "Product B", "Product C", "Chair", "Table"]
data_to_plot = [data[product] for product in products]
plt.stackplot(data["Month"], data_to_plot, labels=products)
plt.title("Units Sold per Month by Product")
plt.xlabel("Months")
plt.ylabel("Units Sold")
plt.legend(loc="upper left")
plt.show()
