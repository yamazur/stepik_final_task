import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

# @pytest.mark.parametrize('link',[
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     pytest.param(
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Product name does not match")
#     ),
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#     ])

# def test_guest_can_add_product_to_basket(browser, link): #добавляем товар в корзину
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.should_be_product_in_basket()

# def test_guest_should_see_login_link_on_product_page(browser): #нахолдим страницу логина
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page(browser): #переходим на страницу логина
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser): #переход на страницу корзины и проверки на то, что она пустая
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket()
    basket_page.should_be_empty_basket_message()

# @pytest.mark.xfail(reason="Success message is present")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): #проверка на то, что сообщение об успехе отсутсвует после добавления товара в корзину
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser): #проверка на то, что сообщение об успехе в целом отсутсвует на странице товара
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail(reason="The success message does not disappear") #проверка на то, что сообщение об успехе исчезает через время
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.success_message_should_disappear()







