from coin_getter import getCryptos

print ("How many criptocurrencies you want to get(They are filtered by market capitalization)?")
n = input()

coins = getCryptos(n)

iteration = 1
for i in coins:
    print(str(iteration) + ") " + i['name'] + ", market capitalization = " + f"{i['market_cap']:,}" + "$")
    iteration += 1