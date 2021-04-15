import csv

with open("ACB.csv") as file:
    acb_csv = csv.reader(file)
#'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'
    date = []
    open_price = []
    high_price = []
    low_price = []
    close_price = []
    adj_close_price = []
    volume = []

    for row in acb_csv:

        for value in row:

            if row.index(value) == 0:
                date.append(value)
            if row.index(value) == 1:
                open_price.append(value)
            if row.index(value) == 2:
                high_price.append(value)
            if row.index(value) == 3:
                low_price.append(value)
            if row.index(value) == 4:
                close_price.append(value)
            if row.index(value) == 5:
                adj_close_price.append(value)
            if row.index(value) == 6:
                volume.append(value)

    def return_price_list():
        return date, open_price, high_price, low_price, close_price, adj_close_price, volume
