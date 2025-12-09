from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items_in_basket(self): #проверяем что корзина пустая
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
        "There are items in the cart"

    def should_be_empty_basket_message(self): #ожидаем, что есть текст о том что корзина пуста
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "The text is missing"



