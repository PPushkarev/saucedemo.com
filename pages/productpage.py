from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class ProductPage(BasePage):
    SAUCE_LABS_BACKPACK_PRODUCT = (By.XPATH, "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[id = 'add-to-cart']")
    CART_BUTTON = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")

    def product_choice(self):
        self.visable_one_element(self.SAUCE_LABS_BACKPACK_PRODUCT).click()
        self.visable_one_element(self.ADD_TO_CART_BUTTON).click()
        self.visable_one_element(self.CART_BUTTON).click()
