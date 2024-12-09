from .top_tokens import get_top_100_tokens_by_volume
from .cex_integration import fetch_cex_prices
from .dex_integration import fetch_dex_prices

def fetch_prices(limit=100):
    top_tokens = get_top_100_tokens_by_volume()
    symbols = {token['symbol'].upper() for token in top_tokens}

    cex_prices = fetch_cex_prices(symbols)
    dex_prices = fetch_dex_prices(symbols)

    comparisons = []
    for token in symbols:
        for dex, dex_price in dex_prices.get(token, {}).items():
            for cex, cex_price in cex_prices.get(token, {}).items():
                if dex_price and cex_price:
                    difference = round((cex_price - dex_price) / dex_price * 100, 2)
                    comparisons.append({
                        "token": token,
                        "cex": cex,
                        "dex": dex,
                        "cex_price": cex_price,
                        "dex_price": dex_price,
                        "difference": difference
                    })

    return comparisons
