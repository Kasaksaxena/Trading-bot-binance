from binance.client import Client

api_key="a3aad9edbe5a1f6b1a79e4f47bfb92e7883799f1eb3e082c56b19efd3d96f2c3"
api_secret="04232b8db31410e07095fff4a90a01921c129f422a44cfd6bb852cff21a9c812"
client=Client(api_key,api_secret)
client.FUTURES_URL="http://testnet.binancefuture.com/fapi"

try:
    balance=client.futures_account_balance()
    print("Connected to Binance Futures Testnet")
    for b in balance:
        if float(b["balance"])>0:
            print(f"{b["asset"]}:{b["balance"]}")
except Exception as e:
    print("Error",e)
    
        