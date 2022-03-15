from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    
class ProductPageLocators():
    BUTTON_TO_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_ITEM = (By.CSS_SELECTOR, ".product_main h1")
    NAME_ITEM_IN_THE_CART = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_ITEM = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_ITEM_IN_THE_CART = (By.CSS_SELECTOR, ".alertinner p strong")
