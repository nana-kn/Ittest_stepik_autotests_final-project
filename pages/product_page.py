from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    def add_to_cart(self):
        button_to_add = self.browser.find_element(*ProductPageLocators.BUTTON_TO_ADD)
        button_to_add.click()        
                           
    def should_be_product_page(self):
        self.should_be_button_to_add_to_cart()
        self.should_not_be_success_message()        
    
    def should_be_message(self):
        self.should_be_item_added_to_cart()
        self.should_be_price_to_cart()
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_ITEM_IN_THE_CART), "Success message is presented, but should not be"    

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_ITEM_IN_THE_CART), "Success message is not disappeared, but should be"
    

    def should_be_button_to_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_TO_ADD), 'Кнопка добавления отсутствует'
    
    def should_be_item_added_to_cart(self):      
        name_item = self.browser.find_element(*ProductPageLocators.NAME_ITEM).text        
        message_name_item = self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_THE_CART).text   
        assert name_item == message_name_item, 'Товар не добавлен в корзину!' 

    def should_be_price_to_cart(self):      
        price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
        message_price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM_IN_THE_CART).text
        assert price_item == message_price_item, 'Цена товара не совпадает!'        


