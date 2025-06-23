from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key,api_secret,testnet=True):
        self.client=Client(api_key,api_secret)
        if testnet:
            self.client.FUTURES_URL='http://testnet.binancefuture.com/fapi'
            # Configure logging
            logging.basicConfig( filename="trade_logs.txt",
                                level=logging.INFO, 
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
    
    def place_market_order(self,symbol,side,quantity):
        try:
            order=self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower()=="buy" 
                else SIDE_SELL,
                type=ORDER_TYPE_MARKET,quantity=quantity)
            logging.info("Market order:{order}")
            print("Market order executed" ,order)
        except Exception as e:
            logging.error(f"Market order failed:{e}")
            print("Error",e)
            
    def place_limit_order(self,symbol,side,quantity,price):
        try:
            order=self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower()=="buy" 
                else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                 quantity=quantity,
                 price=price ,
                 timeForce=TIME_IN_FORCE_GTC
                )
            logging.info("Limit order:{order}")
            print("Limit order placed",order)
        except Exception as e:
            logging.error(f"Limit order failed:{e}")
            print("Error",e)
            