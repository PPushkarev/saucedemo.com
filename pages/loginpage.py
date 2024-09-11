from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class LoginPage(BasePage):
    USER_NAME_INPUT = (By.CSS_SELECTOR, "input[id='user-name']")
    USER_PASWWORD_INPUT = (By.CSS_SELECTOR, "input[id='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[id='login-button']")
    PRODUCT_PAGE = (By.CSS_SELECTOR, "span[data-test='title']")

    def login_to_account(self, user_name, user_password):
        self.visable_one_element(self.USER_NAME_INPUT).clear()
        self.visable_one_element(self.USER_NAME_INPUT).send_keys(user_name)
        self.visable_one_element(self.USER_PASWWORD_INPUT).clear()
        self.visable_one_element(self.USER_PASWWORD_INPUT).send_keys(user_password)
        self.visable_one_element(self.LOGIN_BUTTON).click()

    def check_account_enter(self):
        return self.visable_one_element(self.PRODUCT_PAGE).is_displayed()
