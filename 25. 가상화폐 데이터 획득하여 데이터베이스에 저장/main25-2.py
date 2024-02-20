import pyupbit
import sqlite3

ticker = "KRW-BTC"
interval = "minute1"
to = "2023-12-31 23:59"
count = 200
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

db_path = r"coin.db"

con = sqlite3.connect(db_path, isolation_level=None)
price_now.to_sql('BTC', con, if_exists='append')

con.close()
