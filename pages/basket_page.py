from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BASKET), "Success message is presented, but should not be"    

    def should_not_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Success message is presented, but should not be"