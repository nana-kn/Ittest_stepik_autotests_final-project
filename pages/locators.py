from selenium.webdriver.common.by import By

class MainPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    
class ProductPageLocators():
    BUTTON_TO_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_ITEM = (By.CSS_SELECTOR, ".product_main h1")
    NAME_ITEM_IN_THE_CART = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_ITEM = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_ITEM_IN_THE_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    ITEMS_IN_THE_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
 

class LoginPageLocators():
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1") 
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    BUTTON_REGISTER =(By.NAME, "registration_submit")   
