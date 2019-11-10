from FW.WEB.AnyPage import AnyPage
from FW.WEB.MainPage import MainPage
from FW.WEB.angularjs_protractor.registeration.login.login import Login
from FW.WEB.angularjs_protractor.registeration.registeration import Registeration
from FW.WEB.waitingFW import waitingFW
from FW.ExternalApp.work_with_time import work_with_time
from FW.ExternalApp.DriverInstance import DriverInstance
from Data.GroupData import group_data


class Application_Manager:

    def __init__(self):
        self.group_data = group_data
        self.time = work_with_time()
        self.driver_instance = DriverInstance()
        self.waiting = waitingFW(self)

        self.any_page = AnyPage(self)
        self.main_page = MainPage(self)
        self.login = Login(self)
        self.register = Registeration(self)
