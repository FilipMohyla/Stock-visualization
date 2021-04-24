from mpl_finance import candlestick_ohlc
import mplfinance as mpf
import pandas as pd

data = pd.read_csv("ACB.csv", index_col = 0, parse_dates = True)
data.index.name = "Date"
data.shape
data.head(3)
data.tail(3)

mpf.plot(data,
type="candle",
mav = (5, 20, 200),
volume = True,
show_nontrading = True,
style = "charles",
)
