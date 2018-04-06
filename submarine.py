import matplotlib.pyplot as plt
import csv

brand = []
price = []

with open(r"submarine.csv",newline="") as f:
    data = csv.reader(f)
    for row in data:
        brand.append(row[0])
        price.append(int(row[1]))

print(brand)
print(price)

total = len(brand)

x = range(total)
avg = sum(price) / total
avg_text = ("{:.1f}".format(avg))

print("average of sales: ",avg)
    
plt.bar(x,price, label="Price (Bilion)")
plt.xticks(x, brand)
    
plt.axhline(avg, label="Average", color="red", linestyle="--" )
plt.title("Price by Brand of Submarine", color="red", fontsize = 17)

plt.ylabel("Price", fontsize = 16, color="blue")
plt.xlabel("Submarine Brand by Uncle Engineer 555", fontsize = 16, color="blue")

for a,b in zip(x, price):
    plt.text(a, b+0.5, str(b))
plt.text(-0.5, avg+(avg/15), 'Average: ' + avg_text)
plt.legend()
plt.show()
