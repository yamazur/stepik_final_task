from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BTN)
        add_product.click()
        self.solve_quiz_and_get_code()

    def should_be_product_in_basket(self):
        # Получаем название товара на странице
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Получаем название из сообщения
        product_name_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert product_name == product_name_alert, 'Product name does not match'

        # Получаем цену товара на странице
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Получаем цену из сообщения
        product_price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text
        assert product_price == product_price_alert, 'Product price does not match'

        print("Товар успешно добавлен в корзину!")

    def should_not_be_success_message(self):
        """Проверяет, что нет сообщения об успехе"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        """Проверяет, что сообщение об успехе исчезает"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it didn't"