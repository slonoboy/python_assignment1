from pycoingecko import CoinGeckoAPI

def getCryptos(n):
    cg = CoinGeckoAPI()
    return cg.get_coins_markets(vs_currency='usd', order="market_cap_desc", page="1",per_page= n)
    

