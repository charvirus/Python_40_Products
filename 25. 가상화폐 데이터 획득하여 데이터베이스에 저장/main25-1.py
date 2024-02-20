import pyupbit

coin_list = pyupbit.get_tickers(fiat='KRW')
print(coin_list)

price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(price_now)
