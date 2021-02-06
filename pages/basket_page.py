from .base_page import BasePage
from .locators import BasketPageLocators

EMPTY_MESSAGE = "Your basket is empty. Continue shopping"


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket contains items"

    def should_be_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket does not contain empty message"
        text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert text == EMPTY_MESSAGE, "Wrong 'basket empty message'"
