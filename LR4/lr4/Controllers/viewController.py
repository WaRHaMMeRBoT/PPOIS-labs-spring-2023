from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDSlideTransition

from lr4.Controllers.baseController import BaseController
from lr4.view.view import View


class ViewController(MDScreenManager):
    def __init__(self, **kwargs):
        super(ViewController, self).__init__(**kwargs)
        self.transition = MDSlideTransition()
        self.dialog: MDDialog = NotImplemented
        self.baseController = BaseController()
        self.view = View(self)

    def get_info_of_plant(self, obj):
        print(obj.id)
