from kivy.app import App
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.adapters.dictadapter import ListAdapter


class MainView(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(MainView, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.list_adapter = ListAdapter(data=["Drug Name #{0}".format(i) for i in range(10)], cls=ListItemButton, sorted_keys=[])
        self.list_adapter.bind(on_selection_change=self.selection_change)
        list_view = ListView(adapter=self.list_adapter)
        self.add_widget(list_view)
        
        
        
    def selection_change(self, adapter, *args):
        popup_content = GridLayout(cols=1)
        popup_content_dismiss = Button(text='Close', size_hint_y=None, height=40)
        popup_content.add_widget(Label(text='Drug Details here'))
        popup_content.add_widget(popup_content_dismiss)
        
        drug_popup = Popup(title='Drug Details', content=popup_content, 
                           size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        
        popup_content_dismiss.bind(on_press=drug_popup.dismiss)
        
        drug_popup.open()
        


class ATX_MDGApp(App):
    def build(self):
        self.title = "ATX - Medic Drug Guide"
        return MainView()


if __name__ == '__main__':
    ATX_MDGApp().run()