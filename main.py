#import kivy
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.utils import platform
from kivy.properties import StringProperty
from jnius import autoclass
#from android.permissions import request_permissions, Permission
import os
# Define the permission constants
#Environment = autoclass('android.os.Environment')

#from jnius import autoclass, cast
#PythonActivity = autoclass('org.kivy.android.PythonActivity')
#Environment = autoclass('android.os.Environment')
#context = cast('android.content.Context', PythonActivity.mActivity)



class LayoutVars(FloatLayout):
                 label_text = StringProperty("tbd")
    

class CSV_Art(MDApp):

    fileManager = None
    #label_text = StringProperty("to be defined")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.path = os.path.expanduser("~") or os.path.expanduser("/")

        self.fileManager = MDFileManager(
            select_path= self.select_path,
            exit_manager=self.close_fileManager,
            ext=['.csv']
            
        )

    def open_filemanager(self):
        self.fileManager.show(self.path)
        

    def select_path(self,path: str):
        self.close_fileManager()
        self.root.ids.selected_file.text = f"{path}"
        

    def close_fileManager(self,*args):
        self.fileManager.close()
        
    
    def build(self):

      

        if 'android' in platform:
            LayoutVars.label_text = "Running on Android"
        else:
                LayoutVars.label_text = "Running on a different platform"
        return Builder.load_file("app.kv")


    
if __name__ == "__main__":
    app = CSV_Art()
    app.run()