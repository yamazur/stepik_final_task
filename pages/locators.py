from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_ALERT = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")