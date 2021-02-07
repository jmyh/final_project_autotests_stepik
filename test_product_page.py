import pytest
import time

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

main_link = "http://selenium1py.pythonanywhere.com/"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
product_link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
promo_link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

password = "Melon1234"


@pytest.mark.setup
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link1)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, promo_link)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        product_name = page.get_product_name()
        page.should_be_message_added_to_basket(product_name)
        product_cost = page.get_product_cost()
        page.should_be_cost_message(product_cost)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_name = page.get_product_name()
    page.should_be_message_added_to_basket(product_name)
    product_cost = page.get_product_cost()
    page.should_be_cost_message(product_cost)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.should_not_be_basket_items()
    page.should_be_empty_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link2)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link1)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link1)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link2)
    page.open()
    page.should_be_login_link()
