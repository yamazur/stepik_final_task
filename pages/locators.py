from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class RegisterPageLocators:
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, "a.btn.btn-default[href*='basket']")
    BASKET_NOT_EMPTY = (By.ID, "basket_formset")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")