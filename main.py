from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
"""
main.py
This would be the home interface of intended app
"""
kv = """
<Row@BoxLayout>:
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            size: self.size
            pos: self.pos
    value1:''
    value2:''
    value3:''
    value4:''
    BoxLayout:
    	orientation:'vertical'
    	BoxLayout:
    		orientation:'horizontal'
    		Label:
    			font_size:'18sp'
    			text:root.value1
    		Label:
    			text:root.value2
		BoxLayout:
    		orientation:'horizontal'
    		Label:
    			text:root.value3
    		Label:
    			text:root.value4
    			


<Best>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
	viewclass: 'Row'
	RecycleBoxLayout:
		default_size: None, dp(56)
		default_size_hint: 1, None
		size_hint_y: None
		height: self.minimum_height
		orientation: 'vertical'
		spacing: dp(1)
"""

Builder.load_string(kv)


class Best(RecycleView):
	def __init__(self,*args,**kwargs):
		datval1=['ALFA','BETA','GAMA','BETA']
		datval2=['100','200','300','400']
		datval3=['sell']*4
		datval4=['30%']*4
		self.data = []
		super(Best,self).__init__(*args,**kwargs)
		for i in range(len(datval1)):
			self.data.append({'value1':datval1[i],'value2':datval2[i],'value3':datval3[i],'value4':datval4[i]})
			#data to recycleview should be given in as a dictionary, define label name in KV and create the
			#layout, the same layoout will be shown in in view of recycleview

class BestApp(App):
    def build(self):
        return Best()


if __name__ == '__main__':
    BestApp().run()
