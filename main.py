from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
import priceextractor as price
"""
main.py
This would be the home interface of intended app
"""
kv = """
<Row@BoxLayout>:
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1,0.91
        Rectangle:
            size: self.size
            pos: self.pos
    icon:''
    coin:''
    buybid:''
    bbvalue:''
    sellask:''
    savalue:''

    BoxLayout:
    	orientation:'horizontal'
		BoxLayout:
    		orientation:'vertical'
			Image:
				pos_hint: {'center_x': 0.5}
				size_hint: None,None
				size:25,25
				source:root.icon

    		Label:
    			font_size:'16sp'
    			bold:True
    			text:root.coin

    	BoxLayout:
    		orientation:'vertical'
    		Label:
    			text:root.sellask
    		Label:
    			color:1,0,0,1
    			text:root.savalue
    			
		BoxLayout:
    		orientation:'vertical'
    		Label:
    			text:root.buybid
    		Label:
    			color:0,1,0,1
    			text:root.bbvalue
    			

<Best>:
    canvas:
        Color:
            rgba: 0.1, 0.1, 0.1, 0.1
        Rectangle:
            size: self.size
            pos: self.pos
	viewclass: 'Row'
	RecycleBoxLayout:
		default_size: None, dp(60)
		default_size_hint: 1, None
		size_hint_y: None
		height: self.minimum_height
		orientation: 'vertical'
		spacing: dp(1)
"""

Builder.load_string(kv)


class Best(RecycleView):
	def __init__(self,*args,**kwargs):

		currency_details = price.Extractprice()

		# zebpay = currency_details.zebpay
		# coindelta = currency_details.coindelta
		buyucoin = currency_details.get_buyucoin_prices()
		coindelta = buyucoin
		self.data = []
		super(Best,self).__init__(*args,**kwargs)
		for coin in coindelta.keys():
			icon_path = 'icon/{}.png'.format(coin)
			self.data.append({'icon':icon_path,'coin':coin,'sellask':'Sell', 'savalue':str(coindelta[coin]['Sell']),\
							  'buybid':'Buy', 'bbvalue':str(coindelta[coin]['Buy'])})
			# self.icon = '{}.png'.format(coin)
			#data to recycleview should be given in as a dictionary, define label name in KV and create the
			#layout, the same layoout will be shown in in view of recycleview


class BestApp(App):
    def build(self):
        return Best()


if __name__ == '__main__':
    BestApp().run()
