import json

with open("bazaar.json", "r") as file:
    data = json.load(file)
    if input("Type 'y' if you want to enter your own item: ") == "y":
        item = input("Enter item: ").upper().replace(" ", "_")
    else:
        item = "summoning_eye".upper().replace(" ", "_")
    if item in data["products"]:
        inst_buy_price = int(data['products'][item]['quick_status']['buyPrice'])
        inst_sell_price = int(data['products'][item]['quick_status']['sellPrice'])
        order_buy_price = int(data['products'][item]['sell_summary'][0]['pricePerUnit'])
        order_sell_price = int(data['products'][item]['buy_summary'][0]['pricePerUnit'])
        order_buy_amount = 0
        order_sell_amount = 0
        try:

            for i in range(10):
                order_buy_amount += int(data['products'][item]['buy_summary'][i]['amount'])
                order_sell_amount += int(data['products'][item]['sell_summary'][i]['amount'])
        except IndexError:
            pass
        estim_profit = int(data['products'][item]['buy_summary'][0]['pricePerUnit']) - int(
            data['products'][item]['sell_summary'][0]['pricePerUnit'])
        print(f"Insta buy price: {inst_buy_price:,d}")
        print(f"Insta sell price: {inst_sell_price:,d}")
        print("-" * 30)
        print(f"Order buy price: {order_buy_price:,d}")
        print(f"Order sell price: {order_sell_price:,d}")
        print("-" * 30)
        print("Last 10 orders")
        try:
            print(f"Order buy amount: {order_buy_amount:,d}")
            print(f"Order sell amount: {order_sell_amount:,d}")
        except ValueError:
            print("Order buy amount: Less than 10 orders")
            print("Order sell amount: Less than 10 orders")
        print("-" * 30)
        print(f"Estimated profit: {estim_profit:,d} coins")
    else:
        print("Item not found")
