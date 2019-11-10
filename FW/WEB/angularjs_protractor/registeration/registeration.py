import allure
from FW.WEB.MainPage import MainPage


class Registeration(MainPage):

    _logout = '//div[@class="ng-scope"]/p[2]/a[@href="#/login"]'
    _text_Home = '//div[@class="ng-scope"]/h1'
    _text_logged_in = '//div[@class="ng-scope"]/p[1]'

    def click_logout(self):
        self.click_by_xpath(self._logout)
        self.refresh_the_page()
        self.manager.waiting.waiting_for_the_element(self._Chat)
        return self.manager.login

    @allure.step('Получение текста Home')
    def get_text_Home(self):
        return self.get_tag_text(self._text_Home)

    @allure.step('Получение текста You\'re logged in!!')
    def get_text_logged_in(self):
        return self.get_tag_text(self._text_logged_in)



