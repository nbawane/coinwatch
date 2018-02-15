#TO get prices of all the cryptos from all exchanges

import requests
import collections
import time


#********************Tickers**********************#

COINDELTA = r'https://coindelta.com/api/v1/public/getticker/'
COINSECURE = r'https://api.coinsecure.in/v1/exchange/ticker'
KOINEX = r'https://koinex.in/api/ticker'
ZEBPAY = r'' #No API as of now
UNOCOIN = r'https://www.unocoin.com/trade?all'
BUYUCOIN = r'https://www.buyucoin.com/api/v1/btc/'#ETH,XRP ind of extension

#**************TIcker ends**********************#

class Extractprice:
    def __init__(self):
        pass
    
    # def convert(self,data):
    #     '''
    #     convert unocode data to string, taken from
    #     stackoverflow
    #     '''
    #     if isinstance(data, str):
    #         return str(data)
    #     elif isinstance(data, collections.Mapping):
    #         return dict(map(self.convert, data.iteritems()))
    #     elif isinstance(data, collections.Iterable):
    #         return type(data)(map(self.convert, data))
    #     else:
    #         return data
        
    def get_coindelta_prices(self):
        '''
        returns dictionary of coin and current price
        dictionary format :{COIN_NAME_IN_CAP : price in INR}
        '''
        req1 = requests.get(COINDELTA)
        data = req1.json()        
        coindeltadict = {}
        for fields in data:
            coindeltadict[(fields['MarketName'].split('-')[0]).upper()] = fields['Last']

        return coindeltadict

    def get_koinex_prices(self):
        '''
        returns dictionary of coin and current price
        dictionary format :{COIN_NAME_IN_CAP : price in INR
        '''
        req1 = requests.get(KOINEX)
        data = req1.json()
        koinexdict = data['prices']
        return koinexdict

    def get
    def get_coinsecure_prices(self):
        '''
        returns dictionary of coin and current price
        dictionary format :{COIN_NAME_IN_CAP : price in INR}
        '''
        req1 = requests.get(COINSECURE)
        data = req1.json()        
        coinsecuredict = {}

        coinsecuredict['BTC'] = data['message']['lastPrice']/100
        return coinsecuredict


priceobj = Extractprice()
# print(priceobj.get_coindelta_prices())    #working fine
# print(priceobj.get_coinsecure_prices())   #working fine
# print (priceobj.get_koinex_prices())      #working fine



