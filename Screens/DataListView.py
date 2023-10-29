from kivy.uix.screenmanager import Screen
from kivy.utils import platform
from kivymd.uix.filemanager import MDFileManager
import os 

class DataViewScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)