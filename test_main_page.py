from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser): #переходим на страницу логина и проверяем, что мы на правильной странице
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser): #нахолдим страницу логина
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser): #переход на страницу корзины и проверки на то, что она пустая
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page() #переходим в корзину по кнопке в шапке профиля
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket() #проверяем, что корзина пустая
    basket_page.should_be_empty_basket_message() #проверяем, что есть сообщение о пустой корзине