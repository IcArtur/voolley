from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.accordion import Accordion, AccordionItem



grey = [1,1,1,1]
black = [0,0,0,0]
players_list = ["Arianna", "Elena", "Valentina", "Francesca", "Beatrice", "Martina", "Nicolle"]
fields = ["Punti \n battuta", "Errori \n battuta", "Punti \n attacco", "Errori \n attacco", "Muri \n punto",
          "Ricezioni \n buone", "Ricezioni \n subite", "Tocchi \n a muro", "Appoggi/Difese #"]


class VolleyApp(App):
    def build(self):
        root_acc = Accordion(orientation='vertical')

        for player in players_list:
            item = AccordionItem(title=player)
            btn = Button(text=player, background_color=grey)
            item.add_widget(btn)
            item = self.create_layout(player)
            root_acc.add_widget(item)
        return root_acc

    def create_count_buttons(self, field):
        layout2 = BoxLayout(padding=10)
        lbl = Label(text=field)
        btn1 = Button(text="+")
        btn2 = Button(text="-")
        layout2.add_widget(btn2)
        layout2.add_widget(lbl)
        layout2.add_widget(btn1)
        return layout2

    def create_layout(self, player):
        item = AccordionItem(title=player)
        for field in fields:
            layy = self.create_count_buttons(field)
            item.add_widget(layy)
        return item

    # def on_press_button(self, instance):
    #     ppup = Popup(title='Test popup', size_hint=(1, .5))
    #     layout2 = BoxLayout(padding=10)
    #     lbl = Label(text="Cazzo", size=self.texture_size)
    #     btn1 = Button(text="+")
    #     btn2 = Button(text="-")
    #     layout2.add_widget(btn2)
    #     layout2.add_widget(lbl)
    #     layout2.add_widget(btn1)
    #     ppup.content = layout2
    #     ppup.open()

if __name__ == "__main__":
    app = VolleyApp()
    app.run()