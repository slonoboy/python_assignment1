# Cyptocurrency filter by market capitalization
### Installation 
Download coin_getter.py file from src/ to your project folder
###  Usage
``` python

from coin_getter import getCryptos
coins = getCryptos(n)      # n is the number of coins, ordered by capitalizatoin, you want to get
# the function returns a list of dictionaries related to each coin

```

The format of the list is 
``` python
[{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 
'current_price': 44858, 'market_cap': 845031768160, 'market_cap_rank': 1, 'fully_diluted_valuation': 942701226548, 'total_volume': 35638690994, 
'high_24h': 45058, 'low_24h': 43179, 'price_change_24h': 1494.22, 'price_change_percentage_24h': 3.4458, 'market_cap_change_24h': 25219149564, 
'market_cap_change_percentage_24h': 3.07621, 'circulating_supply': 18824275.0,'total_supply': 21000000.0, 'max_supply': 21000000.0, 
'ath': 64805, 'ath_change_percentage': -30.72742, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81,
'atl_change_percentage': 66103.45746, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None,
'last_updated': '2021-09-23T20:11:15.553Z'}, {...}, ...]

```

### Examples
Remember that the function has only one parameter which requires for a number of coins. There are a couple of examples here:

``` python

>>> getCryptos(1)
[{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 44765, 'market_cap': 842136575448, 'market_cap_rank': 1, 'fully_diluted_valuation': 939470157424, 'total_volume': 35510404215, 'high_24h': 45058, 'low_24h': 43179, 'price_change_24h': 1283.99, 'price_change_percentage_24h': 2.953, 'market_cap_change_24h': 20968795806, 'market_cap_change_percentage_24h': 2.55353, 'circulating_supply': 18824300.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 64805, 'ath_change_percentage': -30.96695, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81, 'atl_change_percentage': 65874.53754, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-23T20:59:45.595Z'}]

>>> getCryptos(10)[0]['id']   
'bitcoin'

>>> getCryptos(10)[1]['id']             
'ethereum'

>>> coins = getCryptos(3)
>>> for i in coins:
...     i["symbol"]
... 
'btc'
'eth'
'ada'

``` 
