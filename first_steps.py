import matplotlib.pyplot as plt
import numpy as np
import import_from_csv

date, open_price, high_price, low_price, close_price, adj_close_price, volume = import_from_csv.return_price_list()

close_price.remove("Close")
close_price = [0] + close_price
float_close_price = []

for number in close_price:
    number = float(number)
    float_close_price.append(number)

days_list = []

for i in range(1, len(float_close_price)+1):
    days_list.append(i)

x = days_list
y = float_close_price
#print(days_list)

plt.xlabel("Time")
plt.ylabel("Price")

plt.title("Aurora Cannabis")


plt.plot(x, y)

plt.legend()
plt.show()
