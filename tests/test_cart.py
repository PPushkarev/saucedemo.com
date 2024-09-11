from pages.cartpage import CartPage
from setup import login_user
from setup import choose_product


class TestCartPage:

    def test_of_buying(self, driver, login_user, choose_product):
        cart_page = CartPage(driver, 'https://www.saucedemo.com/cart.html')
        cart_page.open_page()
        first_name = 'Paul'
        last_name = 'Saint'
        zip_code = '54646'
        cart_page.shopping(first_name, last_name, zip_code)
        assert cart_page.checked_shopping_complete(), 'Shopping did not been completed'
