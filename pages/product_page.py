from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_btn.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    def should_be_message_added_to_basket(self, true_message):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Message about adding product is not presented"
        text = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).text
        assert true_message == text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is not disappeared, but should be"

    def should_be_cost_message(self, true_cost):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST), \
            "Message about cost of product is not presented"
        text = self.browser.find_element(*ProductPageLocators.MESSAGE_COST).text
        assert true_cost == text

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def get_product_name(self):
        self.should_be_product_name()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), "Product cost is not presented"

    def get_product_cost(self):
        self.should_be_product_cost()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
