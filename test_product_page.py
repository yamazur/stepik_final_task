import pytest
import time
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


class TestGuestGoToLoginPageFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser): #нахолдим страницу логина
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser): #переходим на страницу логина
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

@pytest.mark.need_review
class TestGuestAddToBasketFromProductPage:
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser): #переход на страницу корзины и проверки на то, что она пустая
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_no_items_in_basket()
        basket_page.should_be_empty_basket_message()

    def test_guest_can_add_product_to_basket(self, browser): #добавляем товар в корзину
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_product_in_basket()


class TestGuestSuccessMessageFromProductPage:
    @pytest.mark.xfail(reason="Success message is present")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser): #проверка на то, что сообщение об успехе отсутсвует после добавления товара в корзину
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser): #проверка на то, что сообщение об успехе в целом отсутсвует на странице товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="The success message does not disappear") #проверка на то, что сообщение об успехе исчезает через время
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.success_message_should_disappear()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открываем страницу регистрации
        self.login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        self.login_page.open()

        #генерируем уникальные данные для почты и пароля
        self.email = f"test{int(time.time())}@example.com"
        self.password = f"{int(time.time())}"

        #регистрируем нового пользователя
        self.login_page.register_new_user(self.email, self.password)

        #проверяем, что пользователь залогинен
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser): #проверка на то, что сообщение об успехе в целом отсутсвует на странице товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): #добавляем товар в корзину
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_product_in_basket()