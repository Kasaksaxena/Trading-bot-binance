from tradingbot import BasicBot

api_key=input("Enter your API Key: ")
api_secret=input("Enter your API secret: ")

bot=BasicBot(api_key,api_secret)

symbol=input("Enter symbol (e.g BTCUSDT):").upper()
side=input("Buy or Sell?").lower()
order_type=input("Order Type (market/limit):").lower()
quantity=float(input("Enter quantity:"))

if order_type=="market":
 bot.place_market_order(symbol,side,quantity)
elif order_type=="limit":
    price=float(input("Enter price:"))
    bot.place_limit_order(symbol,side,quantity,price)
else:
    print("INVALID ORDER TYPE")

