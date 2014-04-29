from kivy.app import App
from kivy.uix.widget import Widget


class DrugList(Widget):
    pass


class ATX_MDGApp(App):
    def build(self):
        self.title = "ATX - Medic Drug Guide"
        return DrugList()


if __name__ == '__main__':
    ATX_MDGApp().run()