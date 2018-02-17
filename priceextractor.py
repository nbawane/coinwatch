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
        self.zebpay = self.get_zebpay_prices()
        self.buyucoin = self.get_buyucoin_prices()
        self.all_coins = self.get_all_coins()   #list containing all the coins avalable across all the exchanges
        self.universal_dict = {}    #this would contain avg of all the buy/sells of coins

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
        for coin in data:
            cdata=data[coin]
            coinomedict[coin.split('-')[0].upper()]={'Last':cdata['last'], 'Sell':cdata['lowest_ask'], 'Buy':cdata['highest_bid']}

        return coinomedict

    def get_buyucoin_prices(self):
        # req1 = requests.get(BUYUCOIN)
        # buyudata = req1.json()
        # buyucoinprice={}
        # data = buyudata['BuyUcoin_data'][0]
        # coin = None
        # for key in data:
        #     coin = key.split('_')[0].upper()
        #     if coin is None or coin not in buyucoinprice.keys():
        #         temp_coin = coin
        #         buyucoinprice[coin] = {}
		#
        #     if 'sell' in key:
        #         buyucoinprice[coin].update({'Sell': data[key]})
		#
        #     if 'buy' in key:
        #         buyucoinprice[coin].update({'Buy': data[key]})
		#
        # return buyucoinprice

        return {'ARK': {'Buy': '380', 'Sell': '286'}, 'BAT': {'Buy': '37.71', 'Sell': '27.47'}, 'BCC': {'Buy': '110923', 'Sell': '90673'}, 'BTC': {'Buy': '788551', 'Sell': '670152'}, 'BTS': {'Buy': '24.89', 'Sell': '13.23'}, 'CLOAK': {'Buy': '812', 'Sell': '598'}, 'CVC': {'Buy': '36.19', 'Sell': '28.27'}, 'DASH': {'Buy': '53677', 'Sell': '44489'}, 'DGB': {'Buy': '3.85', 'Sell': '2.8'}, 'DOGE': {'Buy': '0.58', 'Sell': '0.4'}, 'ETC': {'Buy': '2589', 'Sell': '1967'}, 'ETH': {'Buy': '71763', 'Sell': '57643'}, 'FCT': {'Buy': '2694', 'Sell': '2101'}, 'GNT': {'Buy': '37.06', 'Sell': '28.18'}, 'LSK': {'Buy': '2529', 'Sell': '1980'}, 'LTC': {'Buy': '16873', 'Sell': '13575'}, 'NEO': {'Buy': '10000', 'Sell': '7711'}, 'NXT': {'Buy': '21.02', 'Sell': '14.96'}, 'OMG': {'Buy': '1369', 'Sell': '1058'}, 'PAY': {'Buy': '164', 'Sell': '123'}, 'PIVX': {'Buy': '486', 'Sell': '379'}, 'QTUM': {'Buy': '2435', 'Sell': '1907'}, 'REP': {'Buy': '4079', 'Sell': '3201'}, 'SC': {'Buy': '2.47', 'Sell': '1.78'}, 'STEEM': {'Buy': '333', 'Sell': '257'}, 'STRAT': {'Buy': '717', 'Sell': '548'}, 'XEM': {'Buy': '43.9', 'Sell': '33.66'}, 'XMR': {'Buy': '23742', 'Sell': '19178'}, 'XRP': {'Buy': '87.28', 'Sell': '69.89'}, 'ZEC': {'Buy': '35810', 'Sell': '29553'}}

    def get_coindelta_prices(self):
        '''
        This should have ask/bid pattern
        returns dictionary of coin and current price
        dictionary format :{COIN_NAME_IN_CAP : price in INR}
        '''
        # req1 = requests.get(COINDELTA)
        # data = req1.json()
        # coindeltadict = {}
        # for fields in data :
        #     if 'inr' in (fields['MarketName']):
        #         coindeltadict[(fields['MarketName'].split('-')[0]).upper()] = {'Last':fields['Last'],'Sell':fields['Ask'],'Buy':fields['Bid']}
		#
        # return coindeltadict
        # temp_list={}
        temp_list = {'BTC': {'Last': 708004.02, 'Sell': 712396.9, 'Buy': 708501.0}, 'ETH': {'Last': 62898.0, 'Sell': 62898.0, 'Buy': 62640.0}, 'LTC': {'Last': 14898.0, 'Sell': 14850.0, 'Buy': 14800.0}, 'OMG': {'Last': 1175.0, 'Sell': 1175.0, 'Buy': 1174.0}, 'QTUM': {'Last': 2123.99, 'Sell': 2123.99, 'Buy': 2110.1}, 'XRP': {'Last': 75.72, 'Sell': 75.8, 'Buy': 75.79}, 'BCH': {'Last': 99697.99, 'Sell': 99697.99, 'Buy': 99202.0}}
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
        stats doesnot have all the coins hence sell and buy prices are kept same
        '''
        req1 = requests.get(KOINEX)
        data = req1.json()
        koinexdict = data['prices']

        for coin in koinexdict:
            try:
                koinexstat = data['stats'][coin]
                koinexdict[coin]=({'Last':koinexdict[coin],'Sell':koinexstat['lowest_ask'],'Buy':koinexstat['highest_bid']})
            except KeyError:
                koinexdict[coin] = (
                {'Last': koinexdict[coin], 'Sell': koinexdict[coin], 'Buy':koinexdict[coin]})
        return koinexdict
        # return {'BTC': '691001.0', 'ETH': '62300.0', 'XRP': '75.05', 'BCH': '99500.0', 'LTC': '14550.0', 'MIOTA': 139.44, 'OMG': 1151.39, 'GNT': 30.62}
    def get_coinsecure_prices(self):
        '''
        returns dictionary of coin and current price
        dictionary format :{COIN_NAME_IN_CAP : price in INR}
        '''
        req1 = requests.get(COINSECURE)
        data = req1.json()        
        coinsecuredict = {}

        coinsecuredict['BTC'] = {'Last':data['message']['lastPrice']/100, 'Sell':data['message']['ask']/100, 'Buy':data['message']['bid']/100}
        return coinsecuredict

    def price_manipulation(self):
        pass

    def get_all_coins(self,*args):
        '''
        :return:list of all coins
        '''
        coindata = {}
        for coindict in args:
            coindata.update(coindict)
        return coindata.keys()

    def merge_all_dicts(self,*args):
        '''
        accepts all the dictionaries as argument and returns a universal dictionary
        '''
        univ_dict = {}
        for i in args:
            univ_dict.update(i)
        return univ_dict

    def get_avg_prices(self,*coin_dicts):
        '''
        :param coin_dicts: dict of all exchanges
        :return: average price of a particular coin accross the exchange
        '''

        self.all_coins = self.get_all_coins(*coin_dicts)
        for coin in self.all_coins:
            sell = 0
            buy = 0
            coin_count = 0
            for coindata in coin_dicts:
                try:
                    #to catch if a coin is present in particular exchange
                    sell += float(coindata[coin]['Sell'])
                    buy += float(coindata[coin]['Buy'])
                    coin_count+=1   #number of exchanges in which the coin is available
                except (KeyError):
                    pass
            try:
                self.universal_dict[coin]={'Sell':str(float(sell)/coin_count),'Buy':str(float(buy)/coin_count)}
            except ZeroDivisionError:
                pass
        return self.universal_dict


priceobj = Extractprice()
# print (priceobj.get_avg_prices(priceobj.buyucoin,priceobj.coindelta,priceobj.zebpay))

# print(priceobj.get_coindelta_prices())    #working fine
# print(priceobj.get_coinsecure_prices())     #working fine
# print (priceobj.get_koinex_prices())      #working fine
# print(priceobj.get_zebpay_prices()  )     #working fine
# print(priceobj.get_buyucoin_prices())     #working fine
# print(priceobj.get_ethexindia_prices())
priceobj.get_coinome_prices()
# print(priceobj.coindelta)
# print(priceobj.zebpay)
# print(priceobj.get_all_coins())