from conftest import driver
from pages.loginpage import LoginPage


class TestLoginPage:

    def test_login_user(self, driver):
        login_page = LoginPage(driver, 'https://www.saucedemo.com/')
        login_page.open_page()
        user_name = 'standard_user'
        user_password = 'secret_sauce'
        login_page.login_to_account(user_name, user_password)
        assert login_page.check_account_enter(), 'Login process did not been completed'
