from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView, ListItemButton, ListItemLabel
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.lang import Builder

Builder.load_string("""
#:import label kivy.uix.label
#:import lv kivy.uix.listview
#:import la kivy.adapters.listadapter

<DrugListView>:
    list_view: dlv
    deselected_color: (0.188, 0.281, 0375, 1)
    selected_color: (0, 0.062, 0.125, 1)
    ListView:
        id: dlv
        size_hint: .9,.9
        
        adapter:
            la.ListAdapter(
            data = ["Drug Name #{0}".format(i) for i in range(33)],
            selection_mode = 'single',
            allow_empty_selection = True,
            cls = lv.ListItemButton)
            
    
""")


class MainView(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        super(MainView, self).__init__(**kwargs)
        
        list_view = DrugListView()#ListView(adapter=self.list_adapter)
        self.add_widget(list_view)
        
class DrugListView(ModalView):     
    def __init__(self, **kwargs):
        super(DrugListView, self).__init__(**kwargs)
        self.list_view.adapter.bind(on_selection_change=self.selection_changed)

        
    def selection_changed(self, adapter, *args):
        curr_drug = adapter.selection[0].text
        
        popup_content = GridLayout(cols=1)
        popup_content_text = "Drug info for " + str(curr_drug)
        popup_content_dismiss = Button(text ='Close', size_hint_y=None, height=40)
        popup_content.add_widget(Label(text = popup_content_text))
        popup_content.add_widget(popup_content_dismiss)
        
        drug_popup = Popup(title='Drug Details', content = popup_content, 
                           size_hint = (.7, .7), auto_dismiss=False)
        
        popup_content_dismiss.bind(on_press = drug_popup.dismiss)
        
        drug_popup.open()
        


class ATX_MDGApp(App):
    def build(self):
        self.title = "ATX - Medic Drug Guide"
        return MainView()


if __name__ == '__main__':
    ATX_MDGApp().run()