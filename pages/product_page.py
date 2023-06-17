from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button doesn't exist"
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def should_be_alert(self):
        self.should_be_name()
        self.should_be_price()

    def should_be_name(self):
        assert self.browser.find_element(*ProductPageLocators.NAME).text == self.browser.find_element(*ProductPageLocators.ALERT_NAME).text, "Name doesn't match"

    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text, "Price doesn't match"

    def should_not_be_success_message_1(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_not_be_success_message_2(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_not_be_success_message_3(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"