import allure
from page_object.locators.main_page_locators import MainPageLocators
from page_object.urls import URL_MAIN_PAGE
from page_object.data import adress_one, adress_two, seconds
import re

@allure.epic('Сценарии')
class TestScenarios:
    @allure.title('Проверка окна ожидания')
    def test_waiting_window(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_button_order_taxi()
        main_page.click_order_requirements()
        main_page.click_enter_number_and_order()

        check_machine_search = main_page.wait_and_find_element(MainPageLocators.LOCATOR_MACHINE_SEARCH)
        assert check_machine_search.is_displayed()

        check_timer = main_page.wait_and_find_element(MainPageLocators.LOCATOR_TIMER)
        assert check_timer.is_displayed()

        check_cancel = main_page.wait_and_find_element(MainPageLocators.LOCATOR_BUTTON_CANCEL)
        assert check_cancel.is_displayed()

        check_details = main_page.wait_and_find_element(MainPageLocators.LOCATOR_BUTTON_DETAILS)
        assert check_details.is_displayed()

    @allure.title('Проверка окна совершенного заказа')
    def test_window_completed_order(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_button_order_taxi()
        main_page.click_enter_number_and_order()
        main_page.wait_timer_and_open_details(seconds)

        check_time_n = main_page.wait_and_find_element(MainPageLocators.LOCATOR_TIME_N)
        assert check_time_n.is_displayed()

        check_number_car_image = main_page.wait_and_find_element(MainPageLocators.LOCATOR_NUMBER_CAR_IMAGE)
        assert check_number_car_image.is_displayed()

        check_driver = main_page.wait_and_find_element(MainPageLocators.LOCATOR_BLOCK_DRIVER)
        assert check_driver.is_displayed()

        check_cancel = main_page.wait_and_find_element(MainPageLocators.LOCATOR_BUTTON_CANCEL)
        assert check_cancel.is_displayed()

        check_details = main_page.wait_and_find_element(MainPageLocators.LOCATOR_BUTTON_DETAILS)
        assert check_details.is_displayed()

    @allure.title('Проверка, что в деталях заказа указана стоимость тарифа')
    def test_tariff_cost(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_button_order_taxi()
        taxi_fare = main_page.take_taxi_fare()
        taxi_price = re.search(r'\d+', taxi_fare).group()
        main_page.click_enter_number_and_order()
        main_page.wait_timer_and_open_details(seconds)
        main_page.click_details()

        details = main_page.get_text_to_element(MainPageLocators.LOCATOR_TAXI_FARE_DETAILS)
        details_price = re.search(r'\d+', details).group()
        
        assert taxi_price == details_price

    @allure.title('Проверка закрытия окна заказа')
    def test_close_order_window(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_button_order_taxi()
        main_page.click_enter_number_and_order()
        main_page.wait_timer_and_open_details(seconds)
        main_page.click_cancel()
        
        assert main_page.wait_element_invisible(MainPageLocators.LOCATOR_ORDER_WINDOW)



        
