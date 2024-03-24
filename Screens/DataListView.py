from kivy.uix.screenmanager import Screen
from kivy.utils import platform
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivy.metrics import dp
import pandas as pd
import os 

class DataViewScreen(Screen):
    dataTable = None

    dataViewLayout = AnchorLayout()
    
            

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def load_data_table(self):
          columnData=list(MDApp.get_running_app().data.columns)
          columnData = [(x, dp(30)) for x in columnData]
          rowData = MDApp.get_running_app().data.to_records(index=False)     



          self.dataTable = MDDataTable(
               column_data= columnData,
               row_data= rowData,
               rows_num= 10,
               use_pagination=True               
          )
          self.add_widget(self.dataTable)
          print("added") #remove after testing
            
        