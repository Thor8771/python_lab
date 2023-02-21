from matplotlib import pyplot as plt
import pandas as pd
import csv


def common():
	plt.xticks(data["Months"])
	plt.xlabel("Months")
	plt.ylabel("Sold Units")
	plt.legend()


data = pd.read_csv("data.csv")

plt.figure()
plt.title("a. Get total profit of all months with blue dotted line & width of 4 &\n label x,y, as Months and Sold Units & show legend at lower right")
plt.plot(data["Months"], data["Total profit"], color='blue',
         linestyle='dotted', linewidth=4, label="units")
common()
plt.legend(loc="lower right")

# (ii)
plt.figure()
plt.title(
	"b. Display the number of units sold per month for each product using\nmultiline plots")
for product in data.columns[1:7]:
	plt.plot(data["Months"], data[product], label=product)
common()

# (iii)
plt.figure()
plt.title(
	"c. Read chair and table product sales data and show it using the bar chart")
plt.bar(data["Months"] - 0.2, data["Chair"], 0.4, label="Chair")
plt.bar(data["Months"] + 0.2, data["Table"], 0.4, label="Table")
common()

# (iv)
d = plt.figure()
plt.title("d. Read all product sales data and show it using the stack plot")
clmn = data.columns[:7]
plt.stackplot(data["Months"], data[clmn].T, labels=data.keys())
common()

plt.show()

# print(dir(d))
# d.show()
# input()
