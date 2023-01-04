# read file bazzar.json

import json

with open("bazaar.json", "r") as file:
    data = json.load(file)
    l = []
    for product in data["products"]:
        if product.startswith("ENCHANTMENT_"):
            continue
        else:
            print(product)
        try:
            profit = data["products"][product]["sell_summary"][0]["pricePerUnit"] - \
                     data["products"][product]["quick_status"]["sellPrice"]

            profit = round(profit)

            if profit > 1000:
                if data["products"][product]["sell_summary"][0]["amount"] > 100:
                    l.append((product, profit))

            print(f"Profit: {profit}")
        except IndexError:
            print("No data")

        print("")
print(f'{"=" * 20} Profitable Items {"=" * 20}')
for item in l:
    print(f"{item[0]}: {item[1]}")
