#import kivy
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
import os

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
         return Builder.load_file("app.kv")


    
if __name__ == "__main__":
    app = CSV_Art()
    app.run()