from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.core.window import Window


grey = [1,1,1,1]
black = [0,0,0,0]
players_list = ["Arianna", "Elena", "Valentina", "Francesca", "Beatrice", "Martina", "Nicolle", "Mirka", "Genoveffa", "Denise"]
fields = ["Punti battuta", "Errori battuta", "Punti attacco", "Errori attacco", "Muri punto",
          "Ricezioni buone", "Ricezioni subite", "Tocchi a muro", "Appoggi/Difese #"]
Window.size = (768, 1024)
# Config.set('graphics', 'width', '1080')
# Config.set('graphics', 'height', '1920')
# Config.write()

view = Builder.load_file("main.kv")


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

    def create_label(self):
        pass

    def create_count_buttons(self, field):
        layx = GridLayout(cols=3)
        lbl = Label(text=field, size_hint= (None,None), size=(125,50))
        btn1 = Button(text="+", size_hint= (None,None), size=(50,50))
        btn2 = Button(text="-", size_hint= (None,None), size=(50,50))
        layx.add_widget(btn2)
        layx.add_widget(lbl)
        layx.add_widget(btn1)
        return layx

    def create_layout(self, player):
        item = AccordionItem(title=player)
        layout3 = GridLayout(cols=3)
        for field in fields:
            layy = self.create_count_buttons(field)
            layout3.add_widget(layy)
        item.add_widget(layout3)
        return item

    # def on_press_button(self, instance):
    #     ppup = Popup(title='Test popup', size_hint=(1, .5))
    #     layout2 = BoxLayout(padding=10)
    #     lbl = Label(text="xxx", size=self.texture_size)
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