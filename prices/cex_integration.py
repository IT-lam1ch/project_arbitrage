import requests

def fetch_cex_prices(symbols):
    cex_prices = {}

    # Binance
    binance_url = "https://api.binance.com/api/v3/ticker/price"
    try:
        response = requests.get(binance_url).json()
        for item in response:
            symbol = item['symbol']
            price = float(item['price'])
            if symbol in symbols:
                cex_prices.setdefault(symbol, {})['Binance'] = price
    except Exception as e:
        print(f"Error fetching Binance prices: {e}")

    # Bybit
    bybit_url = "https://api.bybit.com/v2/public/tickers"
    try:
        response = requests.get(bybit_url).json()
        for item in response['result']:
            symbol = item['symbol'].replace("/", "")
            price = float(item['last_price'])
            if symbol in symbols:
                cex_prices.setdefault(symbol, {})['Bybit'] = price
    except Exception as e:
        print(f"Error fetching Bybit prices: {e}")

    # MEXC
    mexc_url = "https://api.mexc.com/api/v3/ticker/price"
    try:
        response = requests.get(mexc_url).json()
        for item in response:
            symbol = item['symbol']
            price = float(item['price'])
            if symbol in symbols:
                cex_prices.setdefault(symbol, {})['MEXC'] = price
    except Exception as e:
        print(f"Error fetching MEXC prices: {e}")

    # BitGet
    bitget_url = "https://api.bitget.com/api/spot/v1/market/tickers"
    try:
        response = requests.get(bitget_url).json()
        for item in response['data']:
            symbol = item['symbol']
            price = float(item['last'])
            if symbol in symbols:
                cex_prices.setdefault(symbol, {})['BitGet'] = price
    except Exception as e:
        print(f"Error fetching BitGet prices: {e}")

    return cex_prices
