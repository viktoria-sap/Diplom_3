from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import allure
from data.locators import OrderLinePageLocators, MainPageLocators


class OrderLinePage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы Ленты Заказов')
    def wait_for_orders_line_header_loaded(self):
        self.wait_for_element_loaded(OrderLinePageLocators.ORDER_LINE_HEADER)

    @allure.step('Получаем ID первого заказа')
    def get_first_order_id(self):
        return self.find_element_text(OrderLinePageLocators.FIRST_ORDER[1])

    @allure.step('Кликаем заказ Ленты Заказов по номеру {order_id}')
    def click_order_by_id(self, order_id):
        locator = OrderLinePageLocators.BUTTON_BY_ORDER_ID.format(order_id)
        selector = (By.XPATH, locator)
        self.click_element_located(selector)

    @allure.step('Проверяем видимость модального окна')
    def check_order_details_modal_opened(self):
        try:
            self.find_element(OrderLinePageLocators.ORDER_DETAILS_MODAL)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Получаем ID заказа из заголовка модального окна')
    def get_order_id_from_modal(self):
        return self.find_element_text(OrderLinePageLocators.ORDER_DETAILS_MODAL_ORDER_ID_XPATH)

    @allure.step('Проверяем наличие ID {order_id} заказа в Ленте заказов')
    def check_order_id_in_orders_line(self, order_id):
        locator = OrderLinePageLocators.ORDER_ID_P.format(order_id)
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Нажимаем Конструктор')
    def click_constructor(self):
        return self.click_element_located(MainPageLocators.MENU_CONSTRUCTOR)

    @allure.step('Получаем значение счетчика Выполнено за все время')
    def get_total_count(self):
        return self.find_element_text(OrderLinePageLocators.TOTAL_COUNT_XPATH)

    @allure.step('Получаем значение счетчика Выполнено за сегодня')
    def get_today_count(self):
        return self.find_element_text(OrderLinePageLocators.TODAY_COUNT_XPATH)

    @allure.step('Проверяем наличие ID {order_id} заказа среди заказов в работе')
    def check_order_id_in_processing_orders(self, order_id):
        locator = OrderLinePageLocators.ORDER_ID_LI.format(order_id)
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True


