from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class CartPage(BasePage):
    CHECKED_PRODUCT_IN_CART_CONFIRM = (
        By.XPATH, "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
    CHECK_OUT_BUTTON = (By.CSS_SELECTOR, "button[id='checkout']")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='first-name']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='last-name']")
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, "input[id='postal-code']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[id='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "button[id='finish']")
    COMPLETE_SHOPPING_CONFIRM = (By.XPATH, "//span[@data-test='title' and text()='Checkout: Complete!']")

    def checked_product_in_cart(self):
        return self.visable_one_element(self.CHECKED_PRODUCT_IN_CART_CONFIRM).is_displayed()

    def shopping(self, first_name, last_name, zip_code):
        self.visable_one_element(self.CHECK_OUT_BUTTON).click()
        self.visable_one_element(self.FIRST_NAME_FIELD).clear()
        self.visable_one_element(self.FIRST_NAME_FIELD).send_keys(first_name)
        self.visable_one_element(self.LAST_NAME_FIELD).clear()
        self.visable_one_element(self.LAST_NAME_FIELD).send_keys(last_name)
        self.visable_one_element(self.ZIP_CODE_FIELD).clear()
        self.visable_one_element(self.ZIP_CODE_FIELD).send_keys(zip_code)
        self.visable_one_element(self.CONTINUE_BUTTON).click()
        self.visable_one_element(self.FINISH_BUTTON).click()

    def checked_shopping_complete(self):
        return self.visable_one_element(self.COMPLETE_SHOPPING_CONFIRM).is_displayed()
