import allure
import pytest
from page_object.locators.main_page_locators import MainPageLocators
from page_object.urls import URL_MAIN_PAGE
from page_object.data import adress_one, adress_two


@allure.epic('Подготовка к заказу такси')
class TestPreparingOrderTaxi:

    @pytest.mark.xfail(reason="Баг AAA-002: время не пересчитывается")
    @allure.title('Проверка переключения между видами маршрута Оптимальный и Быстрый')
    def test_switching_optimal_and_fast(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        take_cost = main_page.take_cost()
        take_time = main_page.take_time()
        main_page.click_optimal()
       
        assert main_page.change_active_tobacco()

        assert take_cost != main_page.get_text_to_element(MainPageLocators.LOCATOR_COST)

        assert take_time != main_page.get_text_to_element(MainPageLocators.LOCATOR_TIME)

    @allure.title('Проверка переключения на вид Свой')
    def test_switch_mine(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_designer_button()

        assert main_page.change_active_type_mine()
        assert main_page.are_all_types_active()

    @allure.title('Проверка активности кнопки "Вызвать такси"')
    def test_button_active_order_taxi(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)

        assert main_page.wait_and_find_clickable_element(MainPageLocators.LOCATOR_BUTTON_ORDER_TAXI)

    @allure.title('Проверка активности кнопки "Забронировать"')
    def test_button_active_to_book(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_designer_button()
        main_page.click_drive_button()

        assert main_page.wait_and_find_clickable_element(MainPageLocators.LOCATOR_BUTTON_TO_BOOK)


        





