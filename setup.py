import pytest
from pages.cartpage import CartPage
from pages.loginpage import LoginPage
from pages.productpage import ProductPage


# fixture for login into account
@pytest.fixture(scope='function')
def login_user(driver):
    login_page = LoginPage(driver, 'https://www.saucedemo.com/')
    login_page.open_page()
    user_name = 'standard_user'
    user_password = 'secret_sauce'
    login_page.login_to_account(user_name, user_password)
    return login_page


# fixture for product buying
@pytest.fixture(scope='function')
def choose_product(driver):
    product_page = ProductPage(driver, 'https://www.saucedemo.com/inventory.html')
    cart_page = CartPage(driver, 'https://www.saucedemo.com/cart.html')
    product_page.open_page()
    product_page.product_choice()
    assert cart_page.checked_product_in_cart()
    return cart_page
