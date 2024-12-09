from pycoingecko import CoinGeckoAPI

def get_top_100_tokens_by_volume():
    cg = CoinGeckoAPI()
    try:
        return cg.get_coins_markets(vs_currency="usd", order="volume_desc", per_page=100, page=1)
    except Exception as e:
        print(f"Error fetching top tokens: {e}")
        return []
