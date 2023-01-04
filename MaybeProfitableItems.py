import json

from tabulate import tabulate

with open("bazaar.json", "r") as file:
    data = json.load(file)

items = []

for item in data["products"]:

    if item.startswith("ENCHANTMENT_"):
        continue
    # print(item)
    try:
        estim_profit = int(data['products'][item]['buy_summary'][0]['pricePerUnit']) - int(
            data['products'][item]['sell_summary'][0]['pricePerUnit'])
        cost = int(data['products'][item]['sell_summary'][0]['pricePerUnit'])

        if estim_profit > 0 and cost > 0:
            weight = estim_profit / cost
        else:
            weight = 0

        order_buy_amount = 0
        order_sell_amount = 0
        try:
            for i in range(10):
                order_buy_amount += int(data['products'][item]['buy_summary'][i]['amount'])
                order_sell_amount += int(data['products'][item]['sell_summary'][i]['amount'])
        except IndexError:
            pass

        if estim_profit > 20 and cost > 0 and order_buy_amount > 100_000 and order_sell_amount > 100_000:
            items.append([item, estim_profit, cost, order_buy_amount, order_sell_amount, weight])
    except IndexError:
        continue

data2 = sorted(items, key=lambda x: x[1]/x[2], reverse=False)

print(tabulate(data2, headers=["Item", "Estimated profit", "Cost", "Order Buy Amount", "Order Sell Amount", "Weight"],
               tablefmt="github", intfmt=","))
