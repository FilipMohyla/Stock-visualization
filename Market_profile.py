import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import import_from_csv

float_close_price = []
string_prices = []
counters = []
days_list = []

date, open_price, high_price, low_price, close_price, adj_close_price, volume = import_from_csv.return_price_list()

del close_price[0]
del date[0]

for number in close_price:
  
    number = float(number)
    number = round(number, 0)
    
    float_close_price.append(number)
    counters.append(float_close_price.count(number))
    
    number = str(number)
    string_prices.append(number)


for i in range(1, len(float_close_price)+1):
    days_list.append(float(i))


plt.plot(date, float_close_price, color="green")


market_profile_subplot = plt.subplot()
market_profile_subplot.twiny()
plt.scatter(counters, float_close_price, s=2, color="red")

plt.xlabel("Number of occurred prices in time")
plt.ylabel("Price in $")
plt.title("Aurora Cannabis")
plt.legend()

plt.show()
