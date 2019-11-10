import allure
import pytest

from Tests.TestBase import TestBase


@allure.testcase('https://yandex.ru/')
@allure.feature('Web')
@allure.story('Проверка авторизации пользователя')
class Test_Login_smoke(TestBase):

    @allure.title('Тест 1 - Валидный вход')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.Login
    def test_1_Login_smoke(self):
        self.APP.login.set_Login(self.GroupData.Users['User1']['Login'])
        self.APP.login.set_password(self.GroupData.Users['User1']['password'])
        self.APP.login.set_username(self.GroupData.Users['User1']['Name'])
        self.APP.login.click_button_login()
        assert 'Home' == self.APP.register.get_text_Home()
        assert "You're logged in!!" == self.APP.register.get_text_logged_in()

    @allure.title('Тест 2 - Не коректный логин')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.Login
    def test_2_Login_smoke(self):
        self.APP.login.set_Login('Fail')
        self.APP.login.set_password('Fail')
        self.APP.login.set_username('Fail')
        self.APP.login.click_button_login()

        assert 'Username or password is incorrect' in self.APP.login.get_text_danger()

    @allure.title('Тест 3 - Проверка активации кнопки Login')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.Login
    @pytest.mark.parametrize("Login, password, username, expected",
                             [
                                 ('angular', '', '', 'False'),
                                 ('angular', 'password', '', 'False'),
                                 ('angular', 'password', 'test', 'True')
                             ])
    def test_3_Login_smoke(self, Login, password, username, expected):
        self.APP.login.set_Login(Login)
        self.APP.login.set_password(password)
        self.APP.login.set_username(username)
        assert str(expected) == str(self.APP.login.get_button_login_is_enabled())

