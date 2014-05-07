from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from drugs import drug_data


class MainView(BoxLayout):
    #list_view = ObjectProperty(None)
    def __init__(self, **kwargs):
        #kwargs['orientation'] = "vertical"
        super(MainView, self).__init__(**kwargs)
        
        druglist_view = DrugListView()
        self.add_widget(druglist_view)
        
        
class DrugListView(ModalView): 
    list_view = ObjectProperty(None)   
    curr_sel = StringProperty("")
    def __init__(self, **kwargs):
        super(DrugListView, self).__init__(**kwargs)
        
        self.list_view.adapter.bind(on_selection_change = self.selection_changed)
        
    def selection_changed(self, adapter, *args):
        
        #dd = drug_data
         
        # get the current selection
        curr_sel = adapter.selection[0].text
        print self.curr_sel
        drugdetail_view = DrugListViewDetail(curr_drug=curr_sel)
        drugdetail_view.open()
        
        # display drug details based on the current selection  
#         popup_content = BoxLayout(orientation="vertical")
#         popup_content_text = dd[curr_sel.text]["name"] + "\n\n" \
#                                 + "[b]Adult Dosage:[/b]\n" + dd[curr_sel.text]["adult dosage"]    
#         popup_content.add_widget(Label(text = popup_content_text, size_hint_x=0.9, text_size=(400,None), markup=True))
#         popup_dismiss = Button(text ='Close', size_hint_y=None, height=40)
#         popup_content.add_widget(popup_dismiss)
#         
#         drug_popup = Popup(title='Drug Details', content = popup_content, 
#                            size_hint = (.7, .7), auto_dismiss=False)
#         
#         popup_dismiss.bind(on_press = drug_popup.dismiss)
#         
#         drug_popup.open()
        
class DrugListViewDetail(Popup):
    detail_view = ObjectProperty(None)
    curr_drug = StringProperty("")
    
    
    def __init__(self, **kwargs):
        super(DrugListViewDetail, self).__init__(**kwargs)
        

    
#print drug_detail
#print drug_data["Adenosine"]["adult dosage"]    
    
class ATX_MDGApp(App):
    def build(self):
        self.title = "ATX Medic Drug Guide"
        
        return MainView()


if __name__ == '__main__':
    ATX_MDGApp().run()