#TO get prices of all the cryptos from all exchanges

import requests
import collections
import time


#********************Tickers**********************#

COINDELTA = r'https://coindelta.com/api/v1/public/getticker/'
COINSECURE = r'https://api.coinsecure.in/v1/exchange/ticker'
KOINEX = r'https://koinex.in/api/ticker'
ZEBPAY = 'https://www.zebapi.com/api/v1/market/ticker-new/{}/inr'   #zebpay has individual API for each currency,need to use format to construct API
UNOCOIN = r'https://www.unocoin.com/trade?all'
BUYUCOIN = r'https://www.buyucoin.com/api/v1/crypto'#ETH,XRP ind of extension
ETHEXINDIA = r'https://ethexindia.com/api/ticker'
POCKETBITS = 'https://pocketbits.in/api/ticker'
COINOME = r'https://www.coinome.com/api/v1/ticker.json'
#**************TIcker ends**********************#

class Extractprice:
    def __init__(self):
        self.coindelta = self.get_coindelta_prices()
        # self.zebpay = self.get_zebpay_prices()

        self.all_coins = []

    def get_ethexindia_prices(self):
        req1 = requests.get(ETHEXINDIA)
        data = req1.json()
        ethexindiadict = {}
        ethexindiadict['ETH'] = data['last_traded_price']
        return ethexindiadict

    def get_coinome_prices(self):
        req1 = requests.get(COINOME)
        data = req1.json()
        coinomedict = {}
        print(data)

    def get_buyucoin_prices(self):
        req1 = requests.get(BUYUCOIN)
        data = req1.json()
        print(data)
		#
        # buyucoindict = {}
        # data = data['BuyUcoin_data']
        # print(data)
        # buyucoindict['BTC'] = data[0]['btc_sell_price']
        # return buyucoindict

    def get_coindelta_prices(self):
        '''
        This should have ask/bid pattern
        returns dictionary of coin and current price
        dictionary format :{COIN_NAME_IN_CAP : price in INR}
        '''
        # req1 = requests.get(COINDELTA)
        # data = req1.json()
        # coindeltadict = {}
        # for fields in data:
        #     coindeltadict[(fields['MarketName'].split('-')[0]).upper()] = {'Last':fields['Last'],'Ask':fields['Ask'],'Bid':fields['Bid']}
		#
        # return coindeltadict
        temp_list={}
        temp_list = {'BTC': {'Last': 733990.0, 'Ask': 716009.0, 'Bid': 716300.0}, 'ETH': {'Last': 0.09100009, 'Ask': 0.09999999, 'Bid': 0.06960001}, 'LTC': {'Last': 0.02999796, 'Ask': 0.02699999, 'Bid': 0.01}, 'OMG': {'Last': 0.00171, 'Ask': 0.00237, 'Bid': 0.0012}, 'QTUM': {'Last': 0.0037, 'Ask': 0.0036, 'Bid': 0.00206}, 'XRP': {'Last': 0.00010006, 'Ask': 0.00011099, 'Bid': 9.1e-05}, 'BCH': {'Last': 100000.0, 'Ask': 100900.0, 'Bid': 99500.0}}
        return temp_list

    def get_zebpay_prices(self):
        # zebpaydict = {}
        # coins = ['btc','ltc','xrp','bch']
        # for coin in coins:
        #     zebpayreq = ZEBPAY.format(coin)
        #     req1 = requests.get(zebpayreq)
        #     data = req1.json()
        #     zebpaydict[data['virtualCurrency'].upper()]={'Sell':data['sell'],'Buy':data['buy']}
        # return zebpaydict
        temp_testing = {
                        'BTC':{'Sell':'900000','Buy':'899999'},\
                        'LTC':{'Sell':'14500','Buy':'17000'},\
                        'XRP':{'Sell':'30','Buy':'33'}
                       }
        return temp_testing

    def get_koinex_prices(self):
        '''
        returns dictionary of coin and current price
        dictionary format :{COIN_NAME_IN_CAP : price in INR
        '''
        req1 = requests.get(KOINEX)
        data = req1.json()
        koinexdict = data['prices']
        return koinexdict

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

    def price_manipulation(self):
        pass

    def get_all_coins(self):
        '''
        :return:list of all coins
        '''
        self.all_coins=self.merge_all_dicts(self.coindelta,self.zebpay).keys()
        return self.all_coins

    def merge_all_dicts(self,*args):
        '''
        accepts all the dictionaries as argument and returns a universal dictionary
        '''
        univ_dict = {}
        for i in args:
            univ_dict.update(i)
        return univ_dict

# priceobj = Extractprice()
# print(priceobj.get_coindelta_prices())    #working fine
# # # print(priceobj.get_coinsecure_prices())   #working fine
# # # print (priceobj.get_koinex_prices())      #working fine
# # print(priceobj.get_zebpay_prices()  )            #working fine
# # # print(priceobj.get_buyucoin_prices())     #working fine,need to saggrigate all coins
# # # print(priceobj.get_ethexindia_prices())
# # # priceobj.get_coinome_prices()               #working fine, need to saggrigate all coins
# #
# # print(priceobj.coindelta)
# # print(priceobj.zebpay)
# print(priceobj.get_all_coins())