from .base_page import BasePage
from .locators import ProductPageLocators
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage): 
    def add_to_cart(self):
        button_to_add = self.browser.find_element(*ProductPageLocators.BUTTON_TO_ADD)
        button_to_add.click()        
                           
    def should_be_product_page(self):
       # self.should_be_product_url()
        self.should_be_button_to_add_to_cart()   
    
    def should_be_message(self):
        self.should_be_item_added_to_cart()
        self.should_be_price_to_cart()

    #def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        #assert "?promo=newYear" in self.browser.current_url, 'Страница по данному url-адресу не найдена'

    def should_be_button_to_add_to_cart(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.BUTTON_TO_ADD), 'Кнопка добавления отсутствует'
    
    def should_be_item_added_to_cart(self):
        # реализуйте проверку добавления товара в корзину       
        name_item = self.browser.find_element(*ProductPageLocators.NAME_ITEM).text        
        message_name_item = self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_THE_CART).text   
        assert name_item == message_name_item, 'Товар не добавлен в корзину!' 

    def should_be_price_to_cart(self):
        # реализуйте проверку добавления товара в корзину       
        price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
        message_price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM_IN_THE_CART).text
        assert price_item == message_price_item, 'Цена товара не совпадает!'        
        
    

