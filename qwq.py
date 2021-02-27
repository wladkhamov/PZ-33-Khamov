from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):

        Fl = FloatLayout() 

        btn = Button(text ='Это кнопка',
            font_size=20,
            on_press=self.btn_press,
            background_color=[0.1,0.2,0.4,1],
            background_normal='',
            pos_hint ={"x":0.425, "y":0.6},
            size_hint = (.15, .1))

        Fl.add_widget(btn)

        btn1 = Button(text ='Это не кнопка',
            font_size=20,
            on_press=self.btn_press,
            background_color=[0.5,0.5,1,1],
            background_normal='',
            pos_hint ={"x":0.425, "y":0.4},
            size_hint = (.15, .1))

        Fl.add_widget(btn1) 

        return Fl 
    def btn_press(self, instance):
        instance.text='Я нажата'


if __name__=="__main__":
    myApp().run()

