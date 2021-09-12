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

    row_count = 0

    for row in acb_csv:

        date.append(row[0])
        open_price.append(row[1])
        high_price.append(row[2])
        low_price.append(row[3])
        close_price.append(row[4])
        adj_close_price.append(row[5])
        volume.append(row[6])


def return_price_list():
    return date, open_price, high_price, low_price, close_price, adj_close_price, volume
