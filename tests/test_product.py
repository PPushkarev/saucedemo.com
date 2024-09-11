from conftest import driver
from pages.cartpage import CartPage
from pages.productpage import ProductPage
from setup import login_user


class TestProductPage:

    def test_choose_product(self, driver, login_user):
        product_page = ProductPage(driver, 'https://www.saucedemo.com/inventory.html')
        cart_page = CartPage(driver, 'https://www.saucedemo.com/cart.html')
        product_page.open_page()
        product_page.product_choice()
        assert cart_page.checked_product_in_cart(), 'Product did not been chosen'
