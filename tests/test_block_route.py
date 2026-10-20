import allure
from page_object.locators.main_page_locators import MainPageLocators
from page_object.data import adress_one, adress_two, assert_free, assert_zero_minutes
from page_object.urls import URL_MAIN_PAGE


@allure.epic('Отрисовка блока с выбором маршрута')
class TestBlockRoutePage:
    @allure.title('Проверка отображения блока с выбором маршрута')
    def test_block_route(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)

        check = main_page.wait_and_find_element(MainPageLocators.LOCATOR_BLOCK_ROUTE)
        assert check.is_displayed()

    @allure.title('Проверка отображения блока с выбором маршрута, при указании одного и того же адреса')
    def test_block_route_one_adress(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_one)
    
        check_free = main_page.get_text_to_element(MainPageLocators.LOCATOR_BLOCK_AUTO_FREE)
        assert assert_free == check_free

        check_zero = main_page.get_text_to_element(MainPageLocators.LOCATOR_BLOCK_ZERO_MINUTES)
        assert assert_zero_minutes == check_zero