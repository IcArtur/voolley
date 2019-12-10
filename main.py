from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup



grey = [1,1,1,1]
black = [0,0,0,0]
players_list = ["Arianna", "Elena", "Valentina", "Francesca", "Beatrice", "Martina", "Nicolle"]

class VolleyApp(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')

        for player in players_list:
            btn = Button(text=player, background_color=grey)
            btn.bind(on_press=self.on_press_button)
            layout.add_widget(btn)
        return layout

    def on_press_button(self, instance):
        ppup = Popup(title='Test popup', size_hint=(1, .5))
        layout2 = BoxLayout(padding=10)
        lbl = Label(text="Cazzo")
        btn1 = Button(text="+")
        btn2 = Button(text="-")
        layout2.add_widget(btn2)
        layout2.add_widget(lbl)
        layout2.add_widget(btn1)
        ppup.content = layout2
        ppup.open()


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()