from kivy.uix.screenmanager import Screen
from kivy.utils import platform
from kivymd.uix.filemanager import MDFileManager
import os 

if platform =="android":
        from android.storage import primary_external_storage_path
        primary_ext_storage = primary_external_storage_path()

class FileManager(Screen):

    


    
    fileManager = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path = os.path.expanduser("~") or os.path.expanduser("/")
        self.fileManager = MDFileManager(
            select_path= self.select_path,
            exit_manager=self.close_fileManager,
            ext=['.csv']

        )
    def open_filemanager(self):
        print("button pressed")
        if platform =="android":
              self.fileManager.show(primary_ext_storage)
              print(f"{primary_ext_storage}")
        else:
              self.fileManager.show(self.path)

    def select_path(self,path: str):
        self.close_fileManager()
        self.ids.selected_file.text = f"{path}"

    def close_fileManager(self,*args):
        self.fileManager.close()