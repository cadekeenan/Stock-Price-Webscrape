import Utilities

#NASDAQ ticker
ticker = str(input('NASDAQ Ticker: '))
Utilities.get_desc(ticker)
Utilities.get_day_range(ticker)
Utilities.get_volume(ticker)
Utilities.get_market_cap(ticker)
