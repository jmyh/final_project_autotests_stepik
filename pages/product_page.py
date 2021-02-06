from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        login_link.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    def should_be_message_added_to_basket(self, true_message):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Message about adding product is not presented"
        text = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).text
        assert true_message in text

    def should_be_cost_message(self, true_cost):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST), \
            "Message about cost of product is not presented"
        text = self.browser.find_element(*ProductPageLocators.MESSAGE_COST).text
        assert true_cost in text

