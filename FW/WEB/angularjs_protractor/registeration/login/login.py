import time

import allure
from FW.WEB.MainPage import MainPage


class Login(MainPage):

    _login = '//*[@id="username"]'
    _password = '//*[@id="password"]'
    _username = '//label[@ng-if="to.label"]/../input'
    _username_description = '//*[@id="formly_1_input_username_0"]'
    _Login = '//form[@name="form"]/div/button'
    _text_danger = '//div[@ng-if="Auth.error"]'
    _Auth_dataLoading = '//div[@class="form-actions"]/img'

    @allure.step('Вводим Login (Вводим в поле Username данные не Username О_о)')
    def set_Login(self, Login):
        self.send_keys_by_xpath(self._login, Login)
        return self

    @allure.step('Вводим Пароль')
    def set_password(self, password):
        self.send_keys_by_xpath(self._password, password)
        return self

    @allure.step('Вводим username')
    def set_username(self, username):
        self.send_keys_by_xpath(self._username, username)
        return self

    @allure.step('Нажимаем кнопку Вход')
    def click_button_login(self):
        self.click_by_xpath(self._Login)
        self.manager.waiting.waiting_for_item_not_display(self._Auth_dataLoading)
        return self.manager.register

    def get_button_login_is_enabled(self):
        return self.GetDriver().find_element_by_xpath(self._Login).is_enabled()

    @allure.step('Получение текста предупреждения')
    def get_text_danger(self):
        return self.get_tag_text(self._text_danger)
